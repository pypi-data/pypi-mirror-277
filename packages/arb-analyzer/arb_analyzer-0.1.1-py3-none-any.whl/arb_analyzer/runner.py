import logging
import time
from decimal import Decimal
from typing import Any, List, Tuple

from click.utils import LazyFile

from carb_optimizer import CurveContainer

from .config import logs
from .constants import ExchangeType
from .context import Context
from .interfaces.input import Input, TokenId
from .interfaces.output import CarbonExtras, CarbonTradeAction, FlashLoan, Opportunity, Output, Step, UniswapV3Extras
from .helpers.tradeinstruction import TradeInstruction, TradeMovement
from .helpers.routehandler import TxRouteHandler, maximize_last_trade_per_tkn
from .helpers.carbon_trade_splitter import split_carbon_trades
from .helpers.wrap_unwrap_processor import add_wrap_or_unwrap_trades_to_route
from .modes import ArbitrageFinderFactory, ArbitrageFinderBase
from . import exchanges


logger = logging.getLogger(__name__)


class Runner:
    SCALING_FACTOR = 0.999

    def __init__(self, input: Input, dump_curves_fp: LazyFile | None, tax_tokens=list[TokenId]):
        self._mode = input.mode
        self._event_info = input.event_info
        self._funding = input.funding
        self._tokens = {t.id: t for t in input.tokens}
        self._dump_curves_fp = dump_curves_fp
        self._tax_tokens = tax_tokens
        self._ts = time.perf_counter()

        Context(
            gas_token=self._tokens[input.context.gas_token],
            wrapped_gas_token=self._tokens[input.context.wrapped_gas_token],
            stablecoin=self._tokens[input.context.stablecoin],
            min_native_profit=input.context.min_native_profit,
        )

        self._pools = {}
        for curve in input.curves:
            self._pools[curve.id] = exchanges.PoolFactory(curve, self._tokens)

    def run(self):
        curve_container = self._get_curves()
        if self._dump_curves_fp is not None:
            self._dump_curves_fp.write(curve_container.as_json())

        logger.info("Timing - preprocessing %f", time.perf_counter() - self._ts)
        self._ts = time.perf_counter()

        arb_finder = ArbitrageFinderFactory(
            arb_mode=self._mode,
            flashloan_tokens=[t for t in self._funding.tokens.keys()],
            curve_container=curve_container,
            dump_curves_fp=self._dump_curves_fp,
        )
        arb_opportunities = arb_finder.find_arb_opps()

        logger.info("Timing - optimizer %f", time.perf_counter() - self._ts)
        self._ts = time.perf_counter()

        opportunities = []
        for arb_opp in arb_opportunities:
            instructions = self._handle_trade_instructions(arb_finder, self._mode, arb_opp)
            steps = []
            for route in instructions["route"]:
                exchange_type = ExchangeType(route.exchange_type)
                if route.extras is not None:
                    if exchange_type == ExchangeType.CARBON_V1:
                        extras = CarbonExtras(trade_actions=[
                            CarbonTradeAction(strategy_id=ta["strategy_id"], amount=ta["amount"])
                            for ta in route.extras
                        ])
                    elif exchange_type == ExchangeType.UNISWAP_V3:
                        extras = UniswapV3Extras(
                            fee=route.extras
                        )
                else:
                    extras = None

                steps.append(Step(
                    cid=route.cid,
                    exchange_type=ExchangeType(route.exchange_type),
                    exchange_name=route.exchange_name,
                    source_token=route.source_token,
                    target_token=route.target_token,
                    source_amount=route.source_amount,
                    min_target_amount=route.min_target_amount,
                    extras=extras,
                ))

            opportunities.append(Opportunity(
                profit_gas_token=Decimal(instructions["profit_gas_token"]),
                flashloans=[
                    FlashLoan(token=token_id, amount=amount)
                    for fl
                    in instructions["flashloans"]
                    for token_id, amount
                    in zip(fl["source_tokens"], fl["source_amounts"])
                ],
                route=steps,
            ))

        logger.info("Timing - postprocessing %f", time.perf_counter() - self._ts)

        return Output(
            opportunities=opportunities,
            logs=logs,
        )

    def _get_curves(self) -> CurveContainer:
        """
        Gets the curves from the database.

        Returns
        -------
        CurveContainer
            The container of curves.
        """
        curves = []
        for pool in self._pools.values():
            for curve in pool.constant_product_curves:
                if all(curve.params[tkn] not in self._tax_tokens for tkn in ['tknx_addr', 'tkny_addr']):
                    curves.append(curve)

        return CurveContainer(curves)

    def _handle_trade_instructions(
        self,
        arb_finder: ArbitrageFinderBase,
        arb_mode: str,
        arb_opp: dict,
    ) -> tuple[str | None, dict | None]:
        """
        Creates and executes the trade instructions
        
        This is the workhorse function that chains all the different actions that
        are necessary to create trade instructions and to ultimately execute them.
        
        Parameters
        ----------
        arb_finder: ArbitrageFinderBase
            The arbitrage finder.
        arb_mode: str
            The arbitrage mode.
        arb_opp: dictionary
            The dictionary containing an arbitrage opportunity found by the Optimizer
        replay_from_block: int
            the block number to start replaying from (default: None)

        Returns
        -------
        - The hash of the transaction if submitted, None otherwise.
        - The receipt of the transaction if completed, None otherwise.
        """
        src_token = arb_opp["src_token"]
        trade_instructions_dic = arb_opp["trade_instructions_dic"]

        # Order the trade instructions
        ordered_trade_instructions_dct = self._simple_ordering_by_src_token(
            trade_instructions_dic, src_token
        )

        # Scale the trade instructions
        ordered_scaled_dcts = self._basic_scaling(
            ordered_trade_instructions_dct, src_token
        )

        # Convert the trade instructions
        ordered_trade_instructions_objects = self._convert_trade_instructions(
            ordered_scaled_dcts
        )

        # Create the tx route handler
        tx_route_handler = TxRouteHandler(
            tokens=self._tokens,
            pools=self._pools,
            trade_instructions=ordered_trade_instructions_objects
        )

        # Aggregate the carbon trades
        agg_trade_instructions = (
            tx_route_handler.aggregate_carbon_trades(ordered_trade_instructions_objects)
            if any(trade.is_carbon for trade in ordered_trade_instructions_objects)
            else ordered_trade_instructions_objects
        )

        # Calculate the trade instructions
        calculated_trade_instructions = tx_route_handler.calculate_trade_outputs(
            agg_trade_instructions
        )

        # Aggregate multiple Bancor V3 trades into a single trade
        calculated_trade_instructions = tx_route_handler.aggregate_bancor_v3_trades(
            calculated_trade_instructions
        )

        flashloan_struct = tx_route_handler.generate_flashloan_struct(
            trade_instructions_objects=calculated_trade_instructions
        )

        # Get the flashloan token
        fl_token = calculated_trade_instructions[0].input.token
        flashloan_amount_wei = calculated_trade_instructions[0].input.wei_amount
        flashloan_fee = float(self._funding.fee)
        flashloan_fee_amt = flashloan_fee * (flashloan_amount_wei / 10**int(fl_token.decimals))

        flashloan_tkn_profit = tx_route_handler.calculate_trade_profit(
            calculated_trade_instructions
        )

        # Calculate the best profit
        best_profit_gastkn, best_profit_usd = self.calculate_profit(
            arb_finder, flashloan_tkn_profit, fl_token.id, flashloan_fee_amt
        )

        # Check if the best profit is greater than the minimum profit
        if best_profit_gastkn < Context.instance.min_native_profit:
            logger.info(
                f"[bot._handle_trade_instructions]:\n"
                f"- Expected profit: {best_profit_gastkn}\n"
                f"- Minimum profit:  {Context.instance.min_native_profit}\n"
            )
            return {
                "profit_gas_token": best_profit_gastkn,
                "flashloans": flashloan_struct,
                "arb_details": "",
                "route": []
            }

        # Log the arbitrage details
        arb_info = [
            f"arb mode = {arb_mode}",
            f"gas profit = {best_profit_gastkn}",
            f"usd profit = {best_profit_usd}",
            f"flashloan token = {fl_token.symbol}",
            f"flashloan amount = {calculated_trade_instructions[0].input.amount}",
            f"flashloan profit = {flashloan_tkn_profit}"
        ]
        arb_ti_info = [
            {
                "exchange": trade.pool.exchange_name,
                "tkn_in": {trade.input.token.symbol: trade.input.token.id} if trade.input.token.symbol != trade.input.token.id else trade.input.token.id,
                "amt_in": trade.input.amount,
                "tkn_out": {trade.output.token.symbol: trade.output.token.id} if trade.output.token.symbol != trade.output.token.id else trade.output.token.id,
                "amt_out": trade.output.amount
            }
            for trade in calculated_trade_instructions
        ]
        arb_details = "\n".join(
            [
                "arbitrage details:",
                *[f"- {line}" for line in arb_info],
                "- trade instructions:",
                *[f"  {index + 1}. {line}" for index, line in enumerate(arb_ti_info)]
            ]
        )
        logger.info(f"[bot._handle_trade_instructions] {arb_details}")

        # Split Carbon Orders
        split_calculated_trade_instructions = split_carbon_trades(trade_instructions=calculated_trade_instructions)

        # # Encode the trade instructions
        # encoded_trade_instructions = tx_route_handler.custom_data_encoder(
        #     split_calculated_trade_instructions
        # )

        # # Get the deadline
        # deadline = self._get_deadline(replay_from_block)

        # Get the route struct
        route_struct = tx_route_handler.get_route_structs(trade_instructions=split_calculated_trade_instructions)

        route_struct_processed = add_wrap_or_unwrap_trades_to_route(
            flashloans=flashloan_struct,
            routes=route_struct,
            trade_instructions=split_calculated_trade_instructions,
        )

        maximize_last_trade_per_tkn(route_struct=route_struct_processed)

        # Log the flashloan details
        logger.debug(f"[bot._handle_trade_instructions] Flashloan of {fl_token.symbol}, amount: {flashloan_amount_wei}")
        logger.debug(f"[bot._handle_trade_instructions] Flashloan token address: {fl_token.id}")
        logger.debug(f"[bot._handle_trade_instructions] Route Struct: \n {route_struct_processed}")
        logger.debug(f"[bot._handle_trade_instructions] Trade Instructions: \n {trade_instructions_dic}")

        return {
            "profit_gas_token": best_profit_gastkn,
            "flashloans": flashloan_struct,
            "arb_details": arb_details,
            "route": route_struct_processed
        }

    def _simple_ordering_by_src_token(
        self, best_trade_instructions_dic, best_src_token
    ):
        """
        Reorders a trade_instructions_dct so that all items where the best_src_token is the tknin are before others
        """
        src_token_instr = [
            x for x in best_trade_instructions_dic if x["tknin"] == best_src_token
        ]
        non_src_token_instr = [
            x
            for x in best_trade_instructions_dic
            if (x["tknin"] != best_src_token and x["tknout"] != best_src_token)
        ]
        src_token_end = [
            x for x in best_trade_instructions_dic if x["tknout"] == best_src_token
        ]
        ordered_trade_instructions_dct = (
            src_token_instr + non_src_token_instr + src_token_end
        )

        return ordered_trade_instructions_dct

    def _basic_scaling(self, best_trade_instructions_dic, best_src_token):
        """
        For items in the trade_instruction_dic scale the amtin by 0.999 if its the src_token
        """
        scaled_best_trade_instructions_dic = [
            dict(x.items()) for x in best_trade_instructions_dic
        ]
        for item in scaled_best_trade_instructions_dic:
            if item["tknin"] == best_src_token:
                item["amtin"] *= self.SCALING_FACTOR

        return scaled_best_trade_instructions_dic

    def _convert_trade_instructions(
        self, trade_instructions_dicts: List[dict[str, Any]]
    ) -> List[TradeInstruction]:
        """
        Converts the trade instructions dictionaries into `TradeInstruction` objects.

        Parameters
        ----------
        trade_instructions_dic: List[Dict[str, Any]]
            The trade instructions dictionaries.

        Returns
        -------
        List[Dict[str, Any]]
            The trade instructions.
        """
        return [
            TradeInstruction(
                pool=self._pools[ti["cid"]],
                input=TradeMovement(token=self._tokens[ti["tknin"]], amount=Decimal(str(ti["amtin"]))),
                output=TradeMovement(token=self._tokens[ti["tknout"]], amount=Decimal(str(ti["amtout"]))),
            )
            for ti in trade_instructions_dicts
        ]

    def calculate_profit(
        self,
        arb_finder: ArbitrageFinderBase,
        best_profit: Decimal,
        fl_token: str,
        flashloan_fee_amt: int = 0,
    ) -> Tuple[Decimal, Decimal]:
        """
        Calculate the best profit in GAS token and in USD.

        Parameters
        ----------
        arb_finder: ArbitrageFinderBase
            The arbitrage finder.
        best_profit: Decimal
            The best profit.
        fl_token: str
            The flashloan token.
        flashloan_fee_amt: int
            The flashloan fee amount.

        Returns
        -------
        Tuple[Decimal, Decimal]
            best_profit_gastkn, best_profit_usd.
        """
        src_profit = Decimal(str(best_profit)) - Decimal(str(flashloan_fee_amt))
        best_profit_gastkn = arb_finder.calculate_profit(fl_token, src_profit)

        try:
            best_profit_usd = 1 / arb_finder.calculate_profit(Context.instance.stablecoin.id, 1 / best_profit_gastkn)
        except Exception as e:
            best_profit_usd = Decimal("NaN")
            logger.info(f"[bot.calculate_profit] error: {e}")

        logger.debug(f"[bot.calculate_profit] input: {best_profit, fl_token, flashloan_fee_amt}")
        logger.debug(f"[bot.calculate_profit] output: {best_profit_gastkn, best_profit_usd}")

        return best_profit_gastkn, best_profit_usd
