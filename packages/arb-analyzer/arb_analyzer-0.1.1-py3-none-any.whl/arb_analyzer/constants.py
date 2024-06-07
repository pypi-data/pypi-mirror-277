from decimal import Decimal
from enum import Enum


Q96 = Decimal("2") ** Decimal("96")


class ArbitrageMode(Enum):
    PAIRWISE_ALL = "pairwise_all"
    PAIRWISE_POL = "pairwise_pol"
    TRIANGLE_ALL = "triangle_all"
    TRIANGLE_B3 = "triangle_b3"
    TRIANGLE_MULTI = "triangle_multi"


class TriggerEventType(Enum):
    TRADE = "trade"
    LIQUIDITY = "liq"
    TIMER = "timer"
    CARBON = "carbon"


class ExchangeType(Enum):
    BANCOR_V2 = 1
    BANCOR_V3 = 2
    UNISWAP_V2 = 3
    UNISWAP_V3 = 4
    SUSHISWAP = 5
    CARBON_V1 = 6
    BALANCER = 7
    CARBON_POL = 8
    CURVE = 9
    WRAPPER = 10
    SOLIDLY_V2 = 11
    VELODROME_V2 = 12
    XFAI_V0 = 13


class FundingMode(Enum):
    FLASHLOAN = "flashloan"
    WALLET = "wallet"
    MIXED = "mixed"
