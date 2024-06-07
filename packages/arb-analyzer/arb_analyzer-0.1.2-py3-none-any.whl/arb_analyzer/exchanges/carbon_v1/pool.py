import logging
from decimal import Decimal
from dataclasses import dataclass
from typing import List

from carb_optimizer import ConstantProductCurve

from arb_analyzer.context import Context
from arb_analyzer.interfaces.input import Curve, Token, TokenId
from ..base.pool import Pool as BasePool
from ..carbon_v1.trade.impl import encodeOrder, decodeOrder


logger = logging.getLogger(__name__)


@dataclass
class Pool(BasePool):
    y_0: int
    y_1: int
    z_0: int
    z_1: int
    A_0: int
    A_1: int
    B_0: int
    B_1: int

    # @property
    # def tokens(self):
    #     ...

    # # TODO: remove, should be obtainable from Token object
    # @property
    # def token_addresses(self):
    #     ...

    @classmethod
    def from_input(cls, curve: Curve, tokens: dict[TokenId, Token]) -> "Pool":
        return cls(
            id=curve.id,
            descr=f"CarbonV1 {curve.fee}%",
            exchange_name=curve.exchange_name,  # TODO: use actual exchange name
            exchange_type=curve.exchange_type,
            fee=float(curve.fee) / 1e6,
            tkn0=tokens[curve.pair[0]],
            tkn1=tokens[curve.pair[1]],
            y_0=curve.native.y_0,
            y_1=curve.native.y_1,
            z_0=curve.native.z_0,
            z_1=curve.native.z_1,
            A_0=curve.native.A_0,
            A_1=curve.native.A_1,
            B_0=curve.native.B_0,
            B_1=curve.native.B_1,
        )

    @property
    def constant_product_curves(self) -> List[ConstantProductCurve]:
        cpc_list = []
        for order in self._to_cpc_dict()["strategy_orders"]:
            try:
                cpc_list.extend(
                    ConstantProductCurve.from_carbonv1(
                        **{
                            k: float(v) if isinstance(v, Decimal) else v
                            for k, v in order.items()
                        }
                    )
                )
            except Exception as e:
                logger.error(f"carbon curve {order} error {e}")
        return cpc_list

    @property
    def _params(self):
        """
        creates the parameter dict for the ConstantProductCurve class
        """
        return {
            "exchange": str(self.exchange_name),
            "exchange_type": self.exchange_type.value,
            "tknx_dec": int(self.tkn0.decimals),
            "tkny_dec": int(self.tkn1.decimals),
            "tknx_addr": str(self.tkn0.id),
            "tkny_addr": str(self.tkn1.id),
            # "blocklud": int(self.last_updated_block),
        }

    def _to_cpc_dict(self) -> dict:
        encoded_orders = [
            {
                "y": self.y_1,
                "z": self.z_1,
                "A": self.A_1,
                "B": self.B_1,
            },
            {
                "y": self.y_0,
                "z": self.z_0,
                "A": self.A_0,
                "B": self.B_0,
            },
        ]

        decoded_orders = [decodeOrder(encoded_order) for encoded_order in encoded_orders]

        decimals = [
            10 ** self.tkn1.decimals,
            10 ** self.tkn0.decimals,
        ]

        converters = [
            Decimal(10) ** (self.tkn0.decimals - self.tkn1.decimals),
            Decimal(10) ** (self.tkn1.decimals - self.tkn0.decimals),
        ]

        tokens_ids = [
            Context.instance.wrapped_gas_token.id if token.id == Context.instance.gas_token.id else token.id
            for token in (self.tkn0, self.tkn1)
        ]

        strategy_orders = [
            {
                "cid": self.id,
                "yint": Decimal(encoded_orders[i]["z"]) / decimals[i],
                "y": Decimal(encoded_orders[i]["y"]) / decimals[i],
                "pb": decoded_orders[i]["lowestRate"] * converters[i],
                "pa": decoded_orders[i]["highestRate"] * converters[i],
                "tkny": tokens_ids[1 - i],
                "pair": "/".join(tokens_ids),
                "fee": self.fee,
                "descr": self.descr,
                "params": self._params,
            }
            for i in [0, 1] if encoded_orders[i]["y"] > 0 and encoded_orders[i]["B"] > 0
        ]

        pm_within_range = False
        no_limit_orders = False
        prices_overlap = False

        # Only overlapping strategies are selected for modification
        if len(strategy_orders) == 2:
            p_marg_0 = (decoded_orders[0]["marginalRate"] * converters[0]) ** -1
            p_marg_1 = (decoded_orders[1]["marginalRate"] * converters[1]) ** +1

            # check if the marginal prices are within a 1% threshold (may included stable/stable pairs)
            pm_within_range = abs(p_marg_0 - p_marg_1) <= max(p_marg_0, p_marg_1) / 100

            # verify that the strategy does not consist of any limit orders
            no_limit_orders = not any(encoded_order["A"] == 0 for encoded_order in encoded_orders)

            # check if the price boundaries pa/pb overlap at one end
            min0, max0 = sorted([strategy_orders[0]["pa"] ** +1, strategy_orders[0]["pb"] ** +1])
            min1, max1 = sorted([strategy_orders[1]["pa"] ** -1, strategy_orders[1]["pb"] ** -1])
            prices_overlap = max(min0, min1) < min(max0, max1)

            # if all conditions are met then this is likely an overlapping strategy
            if pm_within_range and no_limit_orders and prices_overlap:
                # calculate the geometric mean
                pm = 1 / (p_marg_0 * p_marg_1).sqrt()
                # modify the y_int based on the new geomean to the limit of y
                for order in strategy_orders:
                    yint = encodeOrder({
                        "liquidity": order["y"],
                        "lowestRate": order["pb"],
                        "highestRate": order["pa"],
                        "marginalRate": pm,
                    })["z"]
                    if order["yint"] < yint:
                        order["yint"] = yint

        return {
            "strategy_orders": strategy_orders,
            "pm_within_range": pm_within_range,
            "no_limit_orders": no_limit_orders,
            "prices_overlap": prices_overlap,
        }
