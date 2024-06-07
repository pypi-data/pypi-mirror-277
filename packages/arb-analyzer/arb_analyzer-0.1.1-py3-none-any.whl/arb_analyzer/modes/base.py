"""
Defines the base class for arbitrage finder modes

[DOC-TODO-OPTIONAL-longer description in rst format]

---
(c) Copyright Bprotocol foundation 2023-24.
All rights reserved.
Licensed under MIT.
"""
import abc
from decimal import Decimal
from typing import Any, List, Dict

from click.utils import LazyFile

from arb_analyzer.constants import ExchangeType
from arb_analyzer.context import Context
from arb_analyzer.interfaces.input import Token, TokenId


class ArbitrageFinderBase:
    """
    Base class for all arbitrage finder modes
    """

    def __init__(self, flashloan_tokens, curve_container, context: Context, dump_curves_fp=LazyFile | None):
        self.flashloan_tokens = flashloan_tokens
        self.CCm = curve_container
        self.context = context
        self._dump_curves_fp = dump_curves_fp

    def find_combos(self) -> List[Any]:
        return self.find_arbitrage()["combos"]

    def find_arb_opps(self) -> List[Any]:
        return self.find_arbitrage()["arb_opps"]

    @abc.abstractmethod
    def find_arbitrage(self) -> Dict[List[Any], List[Any]]:
        """
        See subclasses for details

        Returns
        -------
        A dictionary with:
        - A list of combinations
        - A list of arbitrage opportunities
        """
        ...

    def get_profit(self, src_token: TokenId, optimization, trade_instructions_df):
        if is_net_change_small(trade_instructions_df):
            profit = self.calculate_profit(src_token, -optimization.result)
            if profit.is_finite() and profit > self.context.min_native_profit:
                return profit
        return None

    def calculate_profit(self, src_token: TokenId, src_profit: float) -> Decimal:
        if src_token not in [self.context.gas_token.id, self.context.wrapped_gas_token.id]:
            price = self.find_reliable_price(self.CCm, self.context.wrapped_gas_token.id, src_token)
            assert price is not None, f"No conversion rate for {self.context.gas_token.id} and {src_token}"
            return Decimal(str(src_profit)) / Decimal(str(price))
        return Decimal(str(src_profit))

    def get_params(self, container, dst_tokens: List[TokenId], src_token: TokenId):
        pstart = {src_token: 1}
        for dst_token in dst_tokens:
            if dst_token != src_token:
                pstart[dst_token] = self.find_reliable_price(container, dst_token, src_token)
                if pstart[dst_token] is None:
                    return None
        return {"pstart": pstart}

    def find_reliable_price(self, container, dst_token: TokenId, src_token: TokenId):
        container1 = container.by_tknx(dst_token).by_tkny(src_token)
        container2 = container.by_tknx(src_token).by_tkny(dst_token)
        for exchange_type in [ExchangeType.BANCOR_V2, ExchangeType.BANCOR_V3, ExchangeType.UNISWAP_V2, ExchangeType.UNISWAP_V3]:
            list1 = [curve.p / 1 for curve in container1.by_params(exchange_type=exchange_type).curves]
            list2 = [1 / curve.p for curve in container2.by_params(exchange_type=exchange_type).curves]
            price = (list1 + list2 + [None])[0]
            if price is not None:
                return price
        list1 = [curve.p / 1 for curve in container1.curves]
        list2 = [1 / curve.p for curve in container2.curves]
        return (list1 + list2 + [None])[0]

def is_net_change_small(trade_instructions_df) -> bool:
    try:
        return max(trade_instructions_df.iloc[-1]) < 1e-4
    except Exception:
        return False
