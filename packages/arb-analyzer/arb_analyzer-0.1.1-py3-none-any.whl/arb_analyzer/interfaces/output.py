from decimal import Decimal

from pydantic import BaseModel, Field, field_serializer

from arb_analyzer.constants import ExchangeType


type TokenId = str


class FlashLoan(BaseModel):
    token: TokenId
    amount: int

    @field_serializer("amount")
    def serialize_amount(self, amount: int, _info):
        return str(amount)


class CarbonTradeAction(BaseModel):
    strategy_id: int
    amount: int

    @field_serializer("strategy_id")
    def serialize_strategy_id(self, strategy_id: int, _info):
        return str(strategy_id)

    @field_serializer("amount")
    def serialize_amount(self, amount: int, _info):
        return str(amount)


class CarbonExtras(BaseModel):
    trade_actions: list[CarbonTradeAction]


class UniswapV3Extras(BaseModel):
    fee: int


class Step(BaseModel):
    cid: str | None = None
    platform_id: ExchangeType = Field(alias="exchange_type")
    exchange_name: str
    source_token: TokenId
    target_token: TokenId
    source_amount: int
    min_target_amount: int
    extras: CarbonExtras | UniswapV3Extras | None = None

    class Config:
        populate_by_name = True

    @field_serializer("source_amount")
    def serialize_source_amount(self, source_amount: int, _info):
        return str(source_amount)

    @field_serializer("min_target_amount")
    def serialize_min_target_amount(self, min_target_amount: int, _info):
        return str(min_target_amount)


class Opportunity(BaseModel):
    profit_gas_token: Decimal
    flashloans: list[FlashLoan]
    route: list[Step]


class Output(BaseModel):
    opportunities: list[Opportunity]
    logs: list[str]
