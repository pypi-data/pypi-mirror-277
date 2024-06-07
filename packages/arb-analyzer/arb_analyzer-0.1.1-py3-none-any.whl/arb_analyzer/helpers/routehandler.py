"""
Route handler for the Fastlane project.

Main classes defined here are

- ``RouteStruct``: represents a single trade route
- ``TxRouteHandler``: converts trade instructions from the optimizer into routes

It also defines a few helper function that should not be relied upon by external modules,
even if they happen to be exported.
---
(c) Copyright Bprotocol foundation 2023-24.
All rights reserved.
Licensed under MIT.
"""
__VERSION__ = "1.1.1"
__DATE__ = "02/May/2023"

import logging
from decimal import Decimal
from decimal import InvalidOperation
from dataclasses import dataclass
from typing import List, Any, Dict, Tuple

from arb_analyzer.constants import ExchangeType, Q96
from arb_analyzer.context import Context
from arb_analyzer.interfaces.input import Token, TokenId
from arb_analyzer.exchanges.base.pool import Pool
from arb_analyzer.exchanges.carbon_v1.trade.impl import tradeBySourceAmount, tradeByTargetAmount
from .tradeinstruction import TradeInstruction, TradeMovement


logger = logging.getLogger(__name__)


@dataclass
class RouteStruct:
    """
    A class that represents a single trade route in the format required by the arbitrage contract Route struct.

    Parameters
    ----------
    platformId: int
        The exchange ID. (0 = Bancor V2, 1 = Bancor V3, 2 = Uniswap V2, 3 = Uniswap V3, 4 = Sushiswap V2, 5 = Sushiswap, 6 = Carbon)
    targetToken: str
        The target token address.
    minTargetAmount: int
        The minimum target amount. (in wei)
    deadline: int
        The deadline for the trade.
    customAddress: str
        The custom address. Typically used for the Bancor V2 anchor address.
    customInt: int
        The custom integer. Typically used for the fee.
    _customData: dict
        The custom data. Required for trades on Carbon. (unencoded)
    customData: bytes
        The custom data abi-encoded. Required for trades on Carbon. (abi-encoded)
    """

    cid: str
    exchange_type: str
    exchange_name: str
    source_token: str
    target_token: str
    source_amount: int
    min_target_amount: int
    deadline: int
    # customAddress: str
    # customInt: int
    # customData: bytes
    extras: Any


def maximize_last_trade_per_tkn(route_struct: List[RouteStruct]):
    """
    Sets the source amount of the last trade to 0 per-token, ensuring that all tokens held will be used in the last trade.
    :param route_struct: the route struct object
    """

    tkns_traded = [route_struct[0].source_token]
    for j, trade in enumerate(reversed(route_struct)):
        idx = len(route_struct) - 1 - j
        if trade.source_token in tkns_traded:
            continue
        else:
            route_struct[idx].source_amount = 0
            tkns_traded.append(trade.source_token)


@dataclass
class TxRouteHandler:
    """
    A class that handles the routing of the bot by converting trade instructions into routes.

    Parameters
    ----------
    trade_instructions_dic: List[Dict[str, Any]]
        The trade instructions. Formatted output from the `CPCOptimizer` class.
    trade_instructions_df: pd.DataFrame
        The trade instructions as a dataframe. Formatted output from the `CPCOptimizer` class.
    """
    __VERSION__ = __VERSION__
    __DATE__ = __DATE__

    tokens: dict[TokenId, Token]
    pools: dict[str, Pool]
    trade_instructions: List[TradeInstruction]

    def __post_init__(self):
        self.contains_carbon = True
        # self.ConfigObj = self.trade_instructions[0].ConfigObj
        if not self.trade_instructions:
            raise ValueError("No trade instructions found.")
        if len(self.trade_instructions) < 2:
            raise ValueError("Length of trade instructions must be greater than 1.")
        if sum([1 if self.trade_instructions[i].is_carbon else 0 for i in range(len(self.trade_instructions))]) == 0:
            self.contains_carbon = False

    @staticmethod
    def custom_data_encoder(
            agg_trade_instructions: List[TradeInstruction],
    ) -> List[TradeInstruction]:
        for i in range(len(agg_trade_instructions)):
            instr = agg_trade_instructions[i]
            if instr.raw_txs == "[]":
                instr.custom_data = "0x"
                agg_trade_instructions[i] = instr
            else:
                tradeInfo = eval(instr.raw_txs)
                tradeActions = []
                for trade in tradeInfo:
                    tradeActions += [
                        {
                            "strategyId": int(trade["cid"]),
                            "amount": int(
                                trade["_amtin_wei"]
                            ),
                        }
                    ]

                # Define the types of the keys in the dictionaries
                types = ["uint256", "uint128"]

                # Extract the values from each dictionary and append them to a list
                values = [32, len(tradeActions)] + [
                    value
                    for data in tradeActions
                    for value in (data["strategyId"], data["amount"])
                ]

                # Create a list of ABI types based on the number of dictionaries
                all_types = ["uint32", "uint32"] + types * len(tradeActions)

                # Encode the extracted values using the ABI types
                encoded_data = eth_abi.encode(all_types, values)
                instr.custom_data = '0x' + str(encoded_data.hex())
                agg_trade_instructions[i] = instr
        return agg_trade_instructions

    def _to_route_struct(
            self,
            pool: Pool,
            min_target_amount: int,
            deadline: int,
            target_address: str,
            # custom_address: str,
            # customData: Any,
            # customInt: int,
            source_token: str,
            source_amount:int,
            aggregated_from: list[TradeInstruction],
    ) -> RouteStruct:
        """
        Converts trade instructions into routes.

        Parameters
        ----------
        min_target_amount: int
            The minimum target amount.
        deadline: int
            The deadline.
        target_address: str
            The target address.
        platform_id: int
            The exchange id.
        custom_address: str
            The custom address.
        customData: Any
            The custom data.
        override_min_target_amount: bool
            Whether to override the minimum target amount.
        sourceToken: str
            The source token of the trade. V2 routes only.
        sourceAmount: float,
            The source token amount for the trade. V2 routes only.
        exchange_name: str
            The name of the exchange. This is specifically for toggling router overrides.

        Returns
        -------
        RouteStruct
            The route struct.
        """
        # target_address = self.ConfigObj.w3.to_checksum_address(target_address)
        # source_token = self.ConfigObj.w3.to_checksum_address(source_token)
        # customData = self._handle_custom_data_extras(
        #     platform_id=platform_id,
        #     custom_data=customData,
        #     exchange_name=exchange_name
        # )

        if pool.exchange_type == ExchangeType.CARBON_V1:
            extras = []
            for ti in aggregated_from:
                extras += [
                    {
                        "strategy_id": ti.pool.id,
                        "amount": ti.input.wei_amount,
                    }
                ]
        elif pool.exchange_type == ExchangeType.UNISWAP_V3:
            extras = int(pool.fee * 1000000)

        return RouteStruct(
            cid=pool.id,
            exchange_type=pool.exchange_type.value,
            exchange_name=pool.exchange_name,
            target_token=target_address,
            source_token=source_token,
            source_amount=source_amount,
            min_target_amount=min_target_amount,
            deadline=deadline,
            # customAddress=custom_address,
            # customInt=customInt,
            # customData=customData,
            extras=extras,
        )

    def _handle_custom_data_extras(self, platform_id: int, custom_data: bytes, exchange_name: str):
        """
        This function toggles between Uniswap V3 routers used by the Fast Lane contract. This is input in the customData field.

        :param platform_id: int
        :param custom_data: bytes
        :param exchange_name: str

        returns:
            custom_data: bytes
        """

        if platform_id == self.ConfigObj.network.EXCHANGE_IDS.get(self.ConfigObj.network.UNISWAP_V3_NAME):
            assert custom_data == "0x", f"[routehandler.py _handle_custom_data_extras] attempt to override input custom_data {custom_data}"
            if self.ConfigObj.network.NETWORK == ETHEREUM or exchange_name in [PANCAKESWAP_V3_NAME, BUTTER_V3_NAME, AGNI_V3_NAME, CLEOPATRA_V3_NAME, METAVAULT_V3_NAME]:
                return '0x0000000000000000000000000000000000000000000000000000000000000000'
            else:
                return '0x0100000000000000000000000000000000000000000000000000000000000000'

        if platform_id == self.ConfigObj.network.EXCHANGE_IDS.get(self.ConfigObj.network.AERODROME_V2_NAME):
            assert custom_data == "0x", f"[routehandler.py _handle_custom_data_extras] attempt to override input custom_data {custom_data}"
            return '0x' + eth_abi.encode(['address'], [self.ConfigObj.network.FACTORY_MAPPING[exchange_name]]).hex()

        return custom_data

    def get_route_structs(self, trade_instructions: List[TradeInstruction]) -> List[RouteStruct]:
        result = []
        for ti in trade_instructions:
            result.append(self._to_route_struct(
                pool=ti.pool,
                min_target_amount=ti.output.wei_amount,
                deadline=None,
                target_address=ti.output.token.id,
                # custom_address=self.get_custom_address(pool),
                # customInt=trade_instruction.custom_int,
                # customData=trade_instruction.custom_data,
                source_token=ti.input.token.id,
                source_amount=ti.input.wei_amount,
                aggregated_from=ti.aggregated_from
            ))

        return result

    # def get_custom_address(
    #         self,
    #         pool: Pool
    # ):
    #     """
    #     This function gets the custom address field. For Bancor V2 this is the anchor. For Uniswap V2/V3 forks, this is the router address.
    #     :param pool: Pool

    #     returns: str
    #     """
    #     if pool.exchange_name == self.ConfigObj.BANCOR_V2_NAME:
    #         return pool.anchor
    #     elif pool.exchange_name in self.ConfigObj.CARBON_V1_FORKS:
    #         return self.ConfigObj.CARBON_CONTROLLER_MAPPING[pool.exchange_name]
    #     elif pool.exchange_name in self.ConfigObj.UNI_V2_FORKS:
    #         return self.ConfigObj.UNI_V2_ROUTER_MAPPING[pool.exchange_name]
    #     elif pool.exchange_name in self.ConfigObj.SOLIDLY_V2_FORKS:
    #         return self.ConfigObj.SOLIDLY_V2_ROUTER_MAPPING[pool.exchange_name]
    #     elif pool.exchange_name in self.ConfigObj.CARBON_V1_FORKS:
    #         return self.ConfigObj.CARBON_CONTROLLER_ADDRESS
    #     elif pool.exchange_name in self.ConfigObj.UNI_V3_FORKS:
    #         return self.ConfigObj.UNI_V3_ROUTER_MAPPING[pool.exchange_name]
    #     else:
    #         return pool.tkn0_address

    def generate_flashloan_struct(self, trade_instructions_objects: List[TradeInstruction]) -> list:
        """
        Generates the flashloan struct for submitting FlashLoanAndArbV2 transactions
        :param trade_instructions_objects: a list of TradeInstruction objects

        :return:
            list
        """
        return self._get_flashloan_struct(trade_instructions_objects=trade_instructions_objects)

    def _get_flashloan_platform_id(self, tkn: str) -> int:
        """
        Returns the platform ID to take the flashloan from
        :param tkn: str

        :return:
            int
        """

        if self.ConfigObj.NETWORK not in ["ethereum", "tenderly"]:
            return 7

        # Using Bancor V3 to flashloan BNT, ETH, WBTC, LINK, USDC, USDT
        if tkn in [self.ConfigObj.BNT_ADDRESS, self.ConfigObj.ETH_ADDRESS, self.ConfigObj.WBTC_ADDRESS,
                   self.ConfigObj.LINK_ADDRESS, self.ConfigObj.BNT_ADDRESS, self.ConfigObj.ETH_ADDRESS,
                   self.ConfigObj.WBTC_ADDRESS, self.ConfigObj.LINK_ADDRESS]:
            return 2
        else:
            return 7

    def _get_flashloan_struct(self, trade_instructions_objects: List[TradeInstruction]) -> list:
        """
        Turns an object containing trade instructions into a struct with flashloan tokens and amounts ready to send to the smart contract.
        :param flash_tokens: an object containing flashloan tokens in the format {tkn: {"tkn": tkn_address, "flash_amt": tkn_amt}}
        """
        flash_tokens = self._extract_single_flashloan_token(trade_instructions=trade_instructions_objects)
        flashloans = []
        balancer = {"platformId": 7, "source_tokens": [], "source_amounts": []}
        has_balancer = False

        for tkn in flash_tokens.keys():
            # platform_id = self._get_flashloan_platform_id(tkn)
            source_token = flash_tokens[tkn]["tkn"]
            source_amounts = abs(flash_tokens[tkn]["flash_amt"])
            source_token = self.wrapped_gas_token_to_native(source_token)
            flashloans.append({
                "source_tokens": [source_token],
                "source_amounts": [source_amounts]
            })
        #     if platform_id == 7:
        #         has_balancer = True
        #         balancer["sourceTokens"].append(source_token)
        #         balancer["sourceAmounts"].append(source_amounts)
        #     else:
        #         source_token = self.wrapped_gas_token_to_native(source_token)
        #         flashloans.append(
        #             {"platformId": platform_id, "sourceTokens": [source_token], "sourceAmounts": [source_amounts]})
        # if has_balancer:
        #     flashloans.append(balancer)

        return flashloans

    def wrapped_gas_token_to_native(self, tkn: str):
        """
        Checks if a Token is a wrapped gas token and converts it to the native gas token.

        This is only relevant on the Ethereum network

        :param tkn: the token address

        returns:
        the token address
        """

        # if self.ConfigObj.NETWORK not in ["ethereum", "tenderly"]:
        #     return tkn

        if tkn in [Context.instance.wrapped_gas_token.id, Context.instance.wrapped_gas_token.id]:
            return Context.instance.gas_token.id if tkn == Context.instance.wrapped_gas_token.id else Context.instance.gas_token.id
        else:
            return tkn

    def _extract_single_flashloan_token(self, trade_instructions: List[TradeInstruction]) -> Dict:
        """
        Generate a flashloan tokens and amounts.
        :param trade_instructions: A list of trade instruction objects
        """

        # is_FL_NATIVE_permitted = False
        # if self.ConfigObj.NETWORK in [self.ConfigObj.NETWORK_ETHEREUM]:
        #     is_FL_NATIVE_permitted = True

        # if trade_instructions[0].tknin_is_native and not is_FL_NATIVE_permitted:
        #     tknin_address = Context.instance.wrapped_gas_token
        #     self.ConfigObj.logger.info(
        #         f"[routehandler._extract_single_flashloan_token] Not permitted to flashloan NATIVE - Switching to WRAPPED")
        # elif trade_instructions[0].tknin_is_native and is_FL_NATIVE_permitted:
        tknin_address = trade_instructions[0].input.token.id
        flash_tokens = {
            tknin_address:
                {
                    "tkn": tknin_address,
                    "flash_amt": trade_instructions[0].input.wei_amount,
                    "decimals": trade_instructions[0].input.token.decimals}
        }

        return flash_tokens

    @staticmethod
    def aggregate_bancor_v3_trades(calculated_trade_instructions: List[TradeInstruction]):
        """
        This function aggregates Bancor V3 trades into a single multi-hop when possible

        Parameters
        ----------
        calculated_trade_instructions: List[TradeInstruction]
            Trade instructions that have already had trades calculated


        Returns
        -------
        calculated_trade_instructions
            The trade instructions now with Bancor V3 trades combined into single trades when possible.
        """

        for idx, trade in enumerate(calculated_trade_instructions):
            if idx > 0:
                if trade.pool.exchange_name == "bancor_v3" and calculated_trade_instructions[
                    idx - 1].pool.exchange_name == "bancor_v3":
                    trade_before = calculated_trade_instructions[idx - 1]
                    # This checks for a two-hop trade through BNT and combines them
                    if trade_before.output.token.id == trade.input.token.id == "0x1F573D6Fb3F13d689FF844B4cE37794d79a7FF1C":
                        new_trade_instruction = TradeInstruction(ConfigObj=trade.ConfigObj, cid=trade_before.cid,
                                                                 amtin=trade_before.amtin, amtout=trade.amtout,
                                                                 tknin=trade_before.tknin_address,
                                                                 tknout=trade.tknout_address,
                                                                 pair_sorting="", raw_txs="[]", db=trade.db)
                        new_trade_instruction.tknout_is_native = trade.tknout_is_native
                        new_trade_instruction.tknout_is_wrapped = trade.tknout_is_wrapped
                        calculated_trade_instructions[idx - 1] = new_trade_instruction
                        calculated_trade_instructions.pop(idx)

        return calculated_trade_instructions

    def aggregate_carbon_trades(self, trade_instructions_objects: List[TradeInstruction]) -> List[TradeInstruction]:
        """
        Aggregate carbon independent IDs and create trade instructions.

        This function takes a list of dictionaries containing trade instructions,
        aggregates the instructions with carbon independent IDs, and creates
        a list of TradeInstruction objects.

        Parameters
        ----------
        trade_instructions_objects: List[TradeInstruction]
            The trade instructions objects.

        Returns
        -------
        List[TradeInstruction]
            The trade instructions objects.

        """
        aggregated = []
        for i, ti in enumerate(trade_instructions_objects):
            if ti.is_carbon:
                if len(aggregated) > 0:
                    previous_ti = aggregated[-1][-1]
                    if previous_ti.is_carbon and previous_ti.pair == ti.pair:  # TODO: can we compare cids?
                        aggregated[-1].append(ti)
                        continue
            aggregated.append([ti])

        return [
            TradeInstruction(
                pool=ti_group[0].pool,
                input=TradeMovement(
                    token=ti_group[0].input.token,
                    amount=sum([ti.input.amount for ti in ti_group]),
                ),
                output=TradeMovement(
                    token=ti_group[0].output.token,
                    amount=sum([ti.output.amount for ti in ti_group]),
                ),
                aggregated_from=ti_group if ti_group[0].is_carbon else [],
            )
            for ti_group in aggregated
        ]

    def _calc_amount1(
            self,
            liquidity: Decimal,
            sqrt_price_times_q96_lower_bound: Decimal,
            sqrt_price_times_q96_upper_bound: Decimal,
    ) -> Decimal:
        """
        Refactored calc amount1.

        Parameters
        ----------
        liquidity: Decimal
            The liquidity.
        sqrt_price_times_q96_lower_bound: Decimal
            The sqrt price times q96 lower bound.
        sqrt_price_times_q96_upper_bound: Decimal
            The sqrt price times q96 upper bound.

        Returns
        -------
        Decimal
            The amount1.
        """
        if sqrt_price_times_q96_lower_bound > sqrt_price_times_q96_upper_bound:
            sqrt_price_times_q96_lower_bound = sqrt_price_times_q96_upper_bound
            sqrt_price_times_q96_upper_bound = sqrt_price_times_q96_lower_bound
        return liquidity * (sqrt_price_times_q96_upper_bound - sqrt_price_times_q96_lower_bound)

    def _swap_token0_in(
            self,
            amount_in: Decimal,
            fee: Decimal,
            liquidity: Decimal,
            sqrt_price: Decimal,
            decimal_tkn0_modifier: Decimal,
            decimal_tkn1_modifier: Decimal,
    ) -> Decimal:
        """
        Refactored swap token0 in.

        Parameters
        ----------
        amount_in: Decimal
            The amount in.
        fee: Decimal
            The fee.
        liquidity: Decimal
            The liquidity.
        sqrt_price: Decimal
            The sqrt price.
        decimal_tkn0_modifier: Decimal
            The decimal tkn0 modifier.
        decimal_tkn1_modifier: Decimal
            The decimal tkn1 modifier.

        Returns
        -------
        Decimal
            The amount out.
        """
        price_next_n = int(liquidity * Q96 * sqrt_price)
        price_next_d = int(liquidity * Q96 + amount_in * (1 - fee) * decimal_tkn0_modifier * sqrt_price)
        amount_out = self._calc_amount1(liquidity, sqrt_price, Decimal(price_next_n // price_next_d)) / Q96

        return amount_out / decimal_tkn1_modifier

    def _swap_token1_in(
            self,
            amount_in: Decimal,
            fee: Decimal,
            liquidity: Decimal,
            sqrt_price: Decimal,
            decimal_tkn0_modifier: Decimal,
            decimal_tkn1_modifier: Decimal,
    ) -> Decimal:
        """
        Refactored swap token1 in.

        Parameters
        ----------
        amount_in: Decimal
            The amount in.
        fee: Decimal
            The fee.
        liquidity: Decimal
            The liquidity.
        sqrt_price: Decimal
            The sqrt price.
        decimal_tkn0_modifier: Decimal
            The decimal tkn0 modifier.
        decimal_tkn1_modifier: Decimal
            The decimal tkn1 modifier.

        Returns
        -------
        Decimal
            The amount out.
        """

        amount_in = amount_in * (Decimal(str(1)) - fee)
        result = (((liquidity * Q96 * ((((
                                                                amount_in * decimal_tkn1_modifier * Q96) / liquidity) + sqrt_price) - sqrt_price) / (
                        (((amount_in * decimal_tkn1_modifier * Q96) / liquidity) + sqrt_price)) / (
                        sqrt_price)) / decimal_tkn0_modifier))

        return result

    def _calc_uniswap_v3_output(
            self,
            amount_in: Decimal,
            fee: Decimal,
            liquidity: Decimal,
            sqrt_price: Decimal,
            decimal_tkn0_modifier: Decimal,
            decimal_tkn1_modifier: Decimal,
            tkn_in: str,
            tkn_out: str,
            tkn_0_address: str,
            tkn_1_address: str
    ) -> Decimal:
        """
        Refactored calc uniswap v3 output.

        Parameters
        ----------
        amount_in: Decimal
            The amount in.
        fee: Decimal
            The fee.
        liquidity: Decimal
            The liquidity.
        sqrt_price: Decimal
            The sqrt price.
        decimal_tkn0_modifier: Decimal
            The decimal tkn0 modifier.
        decimal_tkn1_modifier: Decimal
            The decimal tkn1 modifier.
        tkn_in: str
            The token in.
        tkn_0_address: str
            The token 0 key.

        Returns
        -------
        Decimal
            The amount out.
        """
        assert tkn_in == tkn_0_address or tkn_out == tkn_0_address, f"Uniswap V3 swap token mismatch, tkn_in: {tkn_in}, tkn_0_address: {tkn_0_address}, tkn_1_address: {tkn_1_address}"
        assert tkn_in == tkn_1_address or tkn_out == tkn_1_address, f"Uniswap V3 swap token mismatch, tkn_in: {tkn_in}, tkn_0_address: {tkn_0_address}, tkn_1_address: {tkn_1_address}"

        liquidity = Decimal(str(liquidity))
        fee = Decimal(str(fee))
        sqrt_price = Decimal(str(sqrt_price))
        decimal_tkn0_modifier = Decimal(str(decimal_tkn0_modifier))
        decimal_tkn1_modifier = Decimal(str(decimal_tkn1_modifier))

        return (
            self._swap_token0_in(
                amount_in=amount_in,
                fee=fee,
                liquidity=liquidity,
                sqrt_price=sqrt_price,
                decimal_tkn0_modifier=decimal_tkn0_modifier,
                decimal_tkn1_modifier=decimal_tkn1_modifier,
            )
            if tkn_in == tkn_0_address
            else self._swap_token1_in(
                amount_in=amount_in,
                fee=fee,
                liquidity=liquidity,
                sqrt_price=sqrt_price,
                decimal_tkn0_modifier=decimal_tkn0_modifier,
                decimal_tkn1_modifier=decimal_tkn1_modifier,
            )
        )

    def _calc_carbon_output(
            self, curve: Pool, tkn_in: str, tkn_in_decimals: int, tkn_out_decimals: int, amount_in: Decimal
    ):
        """
        calc fastlane_bot output.

        Parameters
        ----------
        curve: Pool
            The pool.
        tkn_in: str
            The token in.
        amount_in: Decimal
            The amount in.

        Returns
        -------
        Decimal
            The amount in.
            The amount out.
        """
        assert tkn_in in [curve.tkn0.id, curve.tkn1.id], f"Token in: {tkn_in} does not match tokens in Carbon Curve: {curve.tkn0.id} & {curve.tkn1.id}"

        encoded_order = {
            curve.tkn0.id: {
                'y': int(curve.y_1),
                'z': int(curve.z_1),
                'A': int(curve.A_1),
                'B': int(curve.B_1),
            },
            curve.tkn1.id: {
                'y': int(curve.y_0),
                'z': int(curve.z_0),
                'A': int(curve.A_0),
                'B': int(curve.B_0),
            },
        }[tkn_in]

        target_liquidity = encoded_order['y']
        assert target_liquidity > 0, f"Trade incoming to empty carbon curve: {curve}"

        fee = 1 - Decimal(curve.fee)

        source_scale = 10 ** tkn_in_decimals
        target_scale = 10 ** tkn_out_decimals

        source_amount = int(amount_in * source_scale)
        target_amount = tradeBySourceAmount(source_amount, encoded_order)

        if target_amount > target_liquidity:
            target_amount = target_liquidity
            source_amount = tradeByTargetAmount(target_amount, encoded_order)

        real_source_amount = Decimal(source_amount) / source_scale
        real_target_amount = Decimal(target_amount) / target_scale * fee

        return real_source_amount, real_target_amount

    def _calc_balancer_output(self, curve: Pool, tkn_in: str, tkn_out: str, amount_in: Decimal):
        """
        This is a wrapper function that extracts the necessary pool values to pass into the Balancer swap equation and passes them into the low-level function.
        curve: Pool
            The pool.
        tkn_in: str
            The token in.
        tkn_out: str
            The token out.
        amount_in: Decimal
            The amount in.

        returns:
            The number of tokens expected to be received by the trade.
        """
        tkn_in_weight = Decimal(str(curve.get_token_weight(tkn=tkn_in)))
        tkn_in_balance = Decimal(str(curve.get_token_balance(tkn=tkn_in))) / 10 ** Decimal(
            str(curve.get_token_decimals(tkn=tkn_in)))
        tkn_out_weight = Decimal(str(curve.get_token_weight(tkn=tkn_out)))
        tkn_out_balance = Decimal(str(curve.get_token_balance(tkn=tkn_out))) / 10 ** Decimal(
            str(curve.get_token_decimals(tkn=tkn_out)))
        self.ConfigObj.logger.debug(
            f"[routehandler.py _calc_balancer_output] tknin {tkn_in} weight: {tkn_in_weight}, tknout {tkn_out} tknout weight: {tkn_out_weight}")

        # Extract trade fee from amount in
        fee = Decimal(str(amount_in)) * Decimal(str(curve.fee_float))
        amount_in = amount_in - fee

        if amount_in > (tkn_in_balance * Decimal("0.3")):
            raise BalancerInputTooLargeError(
                "Balancer has a hard constraint that amount in must be less than 30% of the pool balance of tkn in, making this trade invalid.")

        amount_out = self._calc_balancer_out_given_in(balance_in=tkn_in_balance, weight_in=tkn_in_weight,
                                                      balance_out=tkn_out_balance, weight_out=tkn_out_weight,
                                                      amount_in=amount_in)
        if amount_out > (tkn_out_balance * Decimal("0.3")):
            raise BalancerOutputTooLargeError(
                "Balancer has a hard constraint that the amount out must be less than 30% of the pool balance of tkn out, making this trade invalid.")

        # amount_in = (1 - Decimal(str(curve.fee_float))) * Decimal(str(amount_in))
        return amount_out

    @staticmethod
    def _calc_balancer_out_given_in(balance_in: Decimal,
                                    weight_in: Decimal,
                                    balance_out: Decimal,
                                    weight_out: Decimal,
                                    amount_in: Decimal) -> Decimal:
        """
        This function uses the Balancer swap equation to calculate the token output, given an input.

        :param balance_in: the pool balance of the source token
        :param weight_in: the pool weight of the source token
        :param balance_out: the pool balance of the target token
        :param weight_out: the pool weight of the target token
        :param amount_in: the number of source tokens trading into the pool

        returns:
        The number of tokens expected to be received by the trade.

        """

        denominator = balance_in + amount_in
        base = balance_in / denominator if denominator > 0 else 0
        exponent = weight_in / weight_out
        power = base ** exponent
        return balance_out * (1 - power)

    def _solve_trade_output(
            self, curve: Pool, trade: TradeInstruction, amount_in: Decimal = None
    ) -> Tuple[Decimal, Decimal, int, int]:
        if not isinstance(trade, TradeInstruction):
            raise Exception("trade in must be a TradeInstruction object.")

        if curve.exchange_name != "balancer":
            tkn0 = Context.instance.wrapped_gas_token if curve.tkn0 == Context.instance.gas_token and (
                   trade.input.token == Context.instance.wrapped_gas_token or trade.output.token == Context.instance.wrapped_gas_token) else curve.tkn0
            tkn1 = Context.instance.wrapped_gas_token if curve.tkn1 == Context.instance.gas_token and (
                   trade.input.token == Context.instance.wrapped_gas_token or trade.output.token == Context.instance.wrapped_gas_token) else curve.tkn1

            assert tkn0 in [trade.input.token, trade.output.token], f"[_solve_trade_output] tkn0 {tkn0.id} not in [{trade.input.token.id}, {trade.output.token.id}]"
            assert tkn1 in [trade.input.token, trade.output.token], f"[_solve_trade_output] tkn0 {tkn1.id} not in [{trade.input.token.id}, {trade.output.token.id}]"
            assert tkn0 != tkn1, f"[_solve_trade_output] tkn0 == tkn1 {tkn0.id}, {tkn1.id}"

        else:
            # TODO: fix
            tokens = [curve.tkn0.id, curve.tkn1.id]
            assert trade.input.token.id in tokens, f"[_solve_trade_output] trade.tknin_address {trade.input_token.id} not in Balancer curve tokens: {tokens}"
            assert trade.output.token.id in tokens, f"[_solve_trade_output] trade.tknout_address {trade.output_token.id} not in Balancer curve tokens: {tokens}"

        if curve.exchange_type == ExchangeType.UNISWAP_V3:
            amount_out = self._calc_uniswap_v3_output(
                tkn_in=trade.input.token.id,
                tkn_out=trade.output.token.id,
                amount_in=amount_in,
                fee=Decimal(curve.fee),
                liquidity=curve.liquidity,
                sqrt_price=curve.sqrt_price_q96,
                decimal_tkn0_modifier=Decimal(10 ** curve.tkn0.decimals),
                decimal_tkn1_modifier=Decimal(10 ** curve.tkn1.decimals),
                tkn_0_address=curve.tkn0.id,
                tkn_1_address=curve.tkn1.id
            )
        elif curve.exchange_type == ExchangeType.CARBON_V1:# or curve.exchange_name == self.ConfigObj.BANCOR_POL_NAME:
            amount_in, amount_out = self._calc_carbon_output(
                curve=curve, tkn_in=trade.input.token.id, tkn_in_decimals=trade.input.token.decimals,
                tkn_out_decimals=trade.output.token.decimals, amount_in=amount_in
            )
        # elif curve.exchange_name == self.ConfigObj.BALANCER_NAME:
        #     amount_out = self._calc_balancer_output(curve=curve, tkn_in=trade.tknin_address,
        #                                             tkn_out=trade.tknout_address, amount_in=amount_in)

        # elif curve.exchange_name in self.ConfigObj.SOLIDLY_V2_FORKS and curve.pool_type in "stable":
        #     raise ExchangeNotSupportedError(
        #         f"[routerhandler.py _solve_trade_output] Solidly V2 stable pools are not yet supported")
        # else:
        #     tkn0_amt, tkn1_amt = (
        #         (curve.tkn0_balance, curve.tkn1_balance)
        #         if trade.tknin_address == tkn0_address
        #         else (curve.tkn1_balance, curve.tkn0_balance)
        #     )
        #     tkn0_dec = tkn0_decimals if trade.tknin_address == tkn0_address else tkn1_decimals
        #     tkn1_dec = tkn1_decimals if trade.tknout_address == tkn1_address else tkn0_decimals

        #     tkn0_amt = self._from_wei_to_decimals(tkn0_amt, tkn0_dec)
        #     tkn1_amt = self._from_wei_to_decimals(tkn1_amt, tkn1_dec)

        #     amount_out = self._single_trade_result_constant_product(
        #         tokens_in=amount_in,
        #         token0_amt=tkn0_amt,
        #         token1_amt=tkn1_amt,
        #         fee=curve.fee_float,
        #     )

        amount_out = amount_out * Decimal("0.9999")
        amount_out = amount_out.quantize(Decimal("1") / 10 ** trade.output.token.decimals)
        amount_in_wei = int(amount_in * 10 ** trade.input.token.decimals)
        amount_out_wei = int(amount_out * 10 ** trade.output.token.decimals)
        return amount_in, amount_out, amount_in_wei, amount_out_wei

    def calculate_trade_profit(self, trade_instructions: List[TradeInstruction]) -> Decimal:
        """
        Calculates the profit of the trade in the Flashloan token by calculating the sum in vs sum out
        """
        sum_in = Decimal(0)
        sum_out = Decimal(0)
        flt = trade_instructions[0].input.token.id

        for trade in trade_instructions:
            if trade.input.token.id == flt:
                sum_in += abs(trade.input.amount)
            elif trade.output.token.id == flt:
                sum_out += abs(trade.output.amount)
        sum_profit = sum_out - sum_in
        return sum_profit

    def calculate_trade_outputs(self, trade_instructions: List[TradeInstruction]) -> List[TradeInstruction]:
        """
        Refactored calculate trade outputs.

        Parameters
        ----------
        trade_instructions: List[Dict[str, Any]]
            The trade instructions.

        Returns
        -------
        List[Dict[str, Any]]
            The trade outputs.
        """
        next_amount_in = trade_instructions[0].input.amount
        for idx, trade in enumerate(trade_instructions):
            raw_txs_lst = []
            # total_percent = 0
            if trade.input.amount <= 0:
                trade_instructions.pop(idx)
                continue
            if trade.aggregated_from != []:
                data = trade.aggregated_from
                expected_in = trade_instructions[idx].input.amount

                remaining_tkn_in = Decimal(str(next_amount_in))

                percents = []
                for tx in data:
                    try:
                        percents.append(tx.input.amount / Decimal(str(expected_in)))
                    except InvalidOperation:
                        percents.append(Decimal(0))
                        # total_percent += tx["amtin"]/expected_in
                        logger.warning(
                            f"[calculate_trade_outputs] Invalid operation: {tx.input.amount}/{expected_in}")

                last_tx = len(data) - 1

                for _idx, (tx, percent) in enumerate(zip(data, percents)):
                    curve = tx.pool

                    _next_amt_in = Decimal(str(next_amount_in)) * percent
                    if _next_amt_in > remaining_tkn_in:
                        _next_amt_in = remaining_tkn_in

                    if _idx == last_tx:
                        if _next_amt_in < remaining_tkn_in:
                            _next_amt_in = remaining_tkn_in

                    (
                        amount_in,
                        amount_out,
                        amount_in_wei,
                        amount_out_wei,
                    ) = self._solve_trade_output(
                        curve=curve, trade=trade, amount_in=_next_amt_in
                    )

                    remaining_tkn_in -= amount_in

                    if amount_in_wei <= 0:
                        continue

                    raw_txs_lst.append(TradeInstruction(
                        pool=tx.pool,
                        input=TradeMovement(
                            token=tx.input.token,
                            amount=amount_in
                        ),
                        output=TradeMovement(
                            token=tx.output.token,
                            amount=amount_out
                        ),
                    ))

                    remaining_tkn_in = remaining_tkn_in.quantize(Decimal("1") / 10 ** trade.input.token.decimals)
                    if _idx == last_tx and remaining_tkn_in > 0:

                        for __idx, _tx in enumerate(raw_txs_lst):
                            adjusted_next_amt_in = _tx.input.amount + remaining_tkn_in
                            _curve = _tx.pool
                            (
                                _amount_in,
                                _amount_out,
                                _amount_in_wei,
                                _amount_out_wei,
                            ) = self._solve_trade_output(
                                curve=_curve, trade=trade, amount_in=adjusted_next_amt_in
                            )

                            test_remaining = remaining_tkn_in - _amount_in + _tx.input.amount
                            remaining_tkn_in = remaining_tkn_in.quantize(Decimal("1") / 10 ** trade.input.token.decimals)
                            if test_remaining < 0:
                                continue

                            remaining_tkn_in = remaining_tkn_in + _tx.input.amount - _amount_in

                            _ti = TradeInstruction(
                                pool=_tx.pool,
                                input=TradeMovement(
                                    token=_tx.input.token,
                                    amount=_amount_in
                                ),
                                output=TradeMovement(
                                    token=_tx.output.token,
                                    amount=_amount_out
                                ),
                            )

                            raw_txs_lst[__idx] = _ti

                            if remaining_tkn_in == 0:
                                break

                _total_in = 0
                _total_in_wei = 0
                _total_out = 0
                _total_out_wei = 0
                for raw_tx in raw_txs_lst:
                    _total_in += raw_tx.input.amount
                    _total_in_wei += raw_tx.input.wei_amount
                    _total_out += raw_tx.output.amount
                    _total_out_wei += raw_tx.output.wei_amount

                trade_instructions[idx].input.amount = _total_in
                trade_instructions[idx].output.amount = _total_out
                trade_instructions[idx].aggregated_from = raw_txs_lst
                amount_out = _total_out

            else:
                curve = trade.pool
                (
                    amount_in,
                    amount_out,
                    amount_in_wei,
                    amount_out_wei,
                ) = self._solve_trade_output(
                    curve=curve, trade=trade, amount_in=next_amount_in
                )
                trade_instructions[idx].input.amount = amount_in
                trade_instructions[idx].output.amount = amount_out

            next_amount_in = amount_out

        return trade_instructions

    def _from_wei_to_decimals(self, tkn0_amt: Decimal, tkn0_decimals: int) -> Decimal:
        return Decimal(str(tkn0_amt)) / Decimal("10") ** Decimal(str(tkn0_decimals))


class BalancerInputTooLargeError(AssertionError):
    pass


class BalancerOutputTooLargeError(AssertionError):
    pass


class ExchangeNotSupportedError(AssertionError):
    pass
