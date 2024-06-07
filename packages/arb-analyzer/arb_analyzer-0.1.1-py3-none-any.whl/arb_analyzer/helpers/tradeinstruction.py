from dataclasses import dataclass, field
from typing import List
from decimal import Decimal, ROUND_DOWN

from arb_analyzer.constants import ExchangeType
from arb_analyzer.context import Context
from arb_analyzer.interfaces.input import Token
from arb_analyzer.exchanges.base.pool import Pool


@dataclass
class TradeMovement:
    token: Token
    amount: Decimal

    def __post_init__(self):
        self.quantize()

    @property
    def wei_amount(self) -> int:
        return int(self.amount * 10 ** self.token.decimals)

    def quantize(self):
        self.amount = self.amount.quantize(Decimal("1") / 10 ** self.token.decimals, rounding=ROUND_DOWN)

@dataclass
class TradeInstruction:
    pool: Pool
    input: TradeMovement
    output: TradeMovement
    aggregated_from: List["TradeInstruction"] = field(default_factory=lambda : [])

    def __repr__(self):
        return f"{self.pool.exchange_type.name}"
    
    @property
    def pair(self):
        return f"{self.input.token.symbol}/{self.output.token.symbol}"

    def __post_init__(self):
        """
        Use the database session to get the token addresses and decimals based on the Pool.cid and Token.key
        """
        context = Context.instance

        if context.gas_token in [self.pool.tkn0, self.pool.tkn1]:
            if self.input.token == context.wrapped_gas_token:
                self.input.token = context.gas_token
            if self.output.token == context.wrapped_gas_token:
                self.output.token = context.gas_token

        self.custom_int = self.get_custom_int()

    def get_custom_int(self) -> int:
        """
        Gets the custom int field for the pool

        Uni V3 & forks: the fee
        Balancer: the pool ID
        Solidly V2 & forks: 0 for volatile, 1 for stable
        """
        custom_int = 0
        if self.pool.exchange_type == ExchangeType.UNISWAP_V3:
            custom_int = int(Decimal(self.pool.fee) * Decimal("1000000"))
        # elif self.exchange_name in self.ConfigObj.SOLIDLY_V2_FORKS:
        #     custom_int = 0 if pool.pool_type != self.ConfigObj.network.POOL_TYPE_STABLE else 1
        # elif self.exchange_name in self.ConfigObj.BALANCER_NAME:
        #     custom_int = int(pool.anchor, 16)
        return custom_int

    @property
    def is_carbon(self) -> bool:
        return self.pool.exchange_type == ExchangeType.CARBON_V1
