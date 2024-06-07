from arb_analyzer.constants import ExchangeType
from arb_analyzer.interfaces.input import Curve, Token, TokenId
from .base.pool import Pool
from .carbon_v1.pool import Pool as CarbonV1Pool
from .uniswap_v3.pool import Pool as UniswapV3Pool


def PoolFactory(curve: Curve, tokens: dict[TokenId, Token]) -> Pool:
    return {
        ExchangeType.CARBON_V1: CarbonV1Pool,
        ExchangeType.UNISWAP_V3: UniswapV3Pool,
    }[curve.exchange_type].from_input(curve, tokens)