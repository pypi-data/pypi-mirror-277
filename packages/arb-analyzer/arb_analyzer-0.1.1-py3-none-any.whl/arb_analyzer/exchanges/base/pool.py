from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from carb_optimizer import ConstantProductCurve

from arb_analyzer.constants import ExchangeType
from arb_analyzer.interfaces.input import Curve, Token, TokenId


@dataclass
class Pool(ABC):
    id: str
    descr: str  # TODO: is this needed? why?
    exchange_name: str  # TODO: consider removing or pointing to parent Exchange object
    exchange_type: ExchangeType
    fee: int  # TODO: should we store this in Decimal and get rid of fee_float?
    tkn0: Token
    tkn1: Token

    # @property
    # @abstractmethod
    # def tokens(self):
    #     ...

    # # TODO: remove, should be obtainable from Token object
    # @property
    # @abstractmethod
    # def token_addresses(self):
    #     ...

    @classmethod
    @abstractmethod
    def from_input(cls, curve: Curve, tokens: dict[TokenId, Token]) -> "Pool":
        ...

    @property
    @abstractmethod
    def constant_product_curves(self) -> List[ConstantProductCurve]:
        ...
