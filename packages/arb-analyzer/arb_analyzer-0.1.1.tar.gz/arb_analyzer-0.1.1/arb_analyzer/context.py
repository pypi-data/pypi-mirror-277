from dataclasses import dataclass
from decimal import Decimal

from .interfaces.input import Token


@dataclass
class Context:
    def __new__(cls, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
            for field, value in kwargs.items():
                setattr(cls.instance, field, value)
        return cls.instance

    gas_token: Token
    wrapped_gas_token: Token
    stablecoin: Token
    min_native_profit: Decimal
