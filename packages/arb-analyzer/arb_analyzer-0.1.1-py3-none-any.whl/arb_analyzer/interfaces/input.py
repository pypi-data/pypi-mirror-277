from decimal import Decimal

from pydantic import BaseModel, Field

from arb_analyzer.constants import ArbitrageMode, ExchangeType, FundingMode, TriggerEventType


type TokenId = str


class Context(BaseModel):
    gas_token: TokenId
    wrapped_gas_token: TokenId
    stablecoin: TokenId
    min_native_profit: Decimal


class EventInfo(BaseModel):
    type: TriggerEventType


class Funding(BaseModel):
    mode: FundingMode
    fee: Decimal | None
    tokens: dict[TokenId, int | None | str]


class CarbonV1Order(BaseModel):
    y_0: int
    y_1: int
    z_0: int
    z_1: int
    A_0: int
    A_1: int
    B_0: int
    B_1: int


class UniswapV3Pool(BaseModel):
    liquidity: int
    sqrt_price_q96: int
    tick: int
    tick_spacing: int


class Curve(BaseModel):
    id: str
    exchange_name: str
    exchange_type: ExchangeType = Field(alias="platform_id")
    fee: Decimal
    pair: tuple[TokenId, TokenId]
    native: CarbonV1Order | UniswapV3Pool


class Token(BaseModel):
    id: TokenId
    decimals: int
    symbol: str
    usd_price: Decimal | None


class Input(BaseModel):
    version: str
    job_id: str
    context: Context
    mode: ArbitrageMode
    event_info: EventInfo
    funding: Funding
    curves: list[Curve]
    tokens: list[Token]
