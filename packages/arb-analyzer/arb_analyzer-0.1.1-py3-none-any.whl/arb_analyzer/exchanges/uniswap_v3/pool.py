import logging
from dataclasses import dataclass
from typing import List

from carb_optimizer import ConstantProductCurve

from arb_analyzer.interfaces.input import Curve, Token, TokenId
from ..base.pool import Pool as BasePool
from .univ3calc import Univ3Calculator


logger = logging.getLogger(__name__)


FEE_LOOKUP = {
    0.00008: Univ3Calculator.FEE80,
    0.0001: Univ3Calculator.FEE100,
    0.00025: Univ3Calculator.FEE250,
    0.00045: Univ3Calculator.FEE450,
    0.0005: Univ3Calculator.FEE500,
    0.0025: Univ3Calculator.FEE2500,
    0.0030: Univ3Calculator.FEE3000,
    0.01: Univ3Calculator.FEE10000,
}


@dataclass
class Pool(BasePool):
    liquidity: int
    sqrt_price_q96: int
    tick: int
    tick_spacing: int

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
            descr=f"UniV3 {curve.fee}%",
            exchange_name=curve.exchange_name,
            exchange_type=curve.exchange_type,
            fee=float(curve.fee) / 1e6,
            tkn0=tokens[curve.pair[0]],
            tkn1=tokens[curve.pair[1]],
            liquidity=curve.native.liquidity,
            sqrt_price_q96=curve.native.sqrt_price_q96,
            tick=curve.native.tick,
            tick_spacing=curve.native.tick_spacing,
        )

    @property
    def constant_product_curves(self) -> List[ConstantProductCurve]:
        """
        Preprocesses a Uniswap V3 pool params in order to create a ConstantProductCurve instance for optimization.

        :return: ConstantProductCurve
            :k:        pool constant k = xy [x=k/y, y=k/x]
            :x:        (virtual) pool state x (virtual number of base tokens for sale)
            :x_act:    actual pool state x (actual number of base tokens for sale)
            :y_act:    actual pool state y (actual number of quote tokens for sale)
            :pair:     tkn_address pair in slash notation ("TKNB/TKNQ"); TKNB is on the x-axis, TKNQ on the y-axis
            :cid:      unique id (optional)
            :fee:      fee (optional); eg 0.01 for 1%
            :descr:    description (optional; eg. "UniV3 0.1%")
            :params:   additional parameters (optional)

        """
        args = {
            "token0": self.tkn0,
            "token1": self.tkn1,
            "sqrt_price_q96": self.sqrt_price_q96,
            "tick": self.tick,
            "liquidity": self.liquidity,
        }
        feeconst = FEE_LOOKUP.get(self.fee)
        if feeconst is None:
            raise ValueError(
                f"Illegal fee for Uniswap v3 pool: {self.fee} [{FEE_LOOKUP}]]"
            )
        uni3 = Univ3Calculator.from_dict(args, feeconst)
        params = uni3.cpc_params()
        if params["uniL"] == 0:
            logger.debug(f"empty univ3 pool [{self.cid}]")
            return []
        params["cid"] = self.id
        params["descr"] = self.descr
        params["params"] = self._params
        return ConstantProductCurve.from_univ3(**params)
    
    @property
    def _params(self):
        """
        creates the parameter dict for the ConstantProductCurve class
        """
        return {
            "exchange": str(self.exchange_name),
            "exchange_type": self.exchange_type,
            "tknx_dec": int(self.tkn0.decimals),
            "tkny_dec": int(self.tkn1.decimals),
            "tknx_addr": str(self.tkn0.id),
            "tkny_addr": str(self.tkn1.id),
            # "blocklud": int(self.last_updated_block),
        }
