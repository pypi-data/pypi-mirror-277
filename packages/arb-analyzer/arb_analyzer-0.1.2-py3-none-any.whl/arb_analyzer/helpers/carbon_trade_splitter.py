"""
Helper function to split Carbon trades into multiple trades, eg if ETH and WETH is involved

Defines the ``split_carbon_trades`` function 

TODO: maybe this should be moved into a slightly bigger context

---
(c) Copyright Bprotocol foundation 2023-24.
All rights reserved.
Licensed under MIT.
"""
from typing import List

from arb_analyzer.constants import ExchangeType
from arb_analyzer.context import Context
from arb_analyzer.interfaces.input import Token
from .tradeinstruction import TradeInstruction, TradeMovement


def split_carbon_trades(trade_instructions: List[TradeInstruction]) -> List[TradeInstruction]:
    """
    This method splits every trade instruction which includes a mix of gas tokens and/or a mix of Carbon deployments,
    into several trade instructions. For example, `NATIVE/WRAPPED -> TKN` is split into `NATIVE -> TKN` and `WRAPPED -> TKN`.

    Args:
        context: the configuration object.
        trade_instructions: A list of trade instructions.

    Returns:
        new_trade_instructions: A new list of trade instructions.
    """
    context = Context.instance

    new_trade_instructions = []
    for trade_instruction in trade_instructions:
        pool = trade_instruction.pool
        if pool.exchange_type != ExchangeType.CARBON_V1:
            new_trade_instructions.append(trade_instruction)
            continue

        carbon_exchanges = {}

        for tx in trade_instruction.aggregated_from:
            pool_tokens = [pool.tkn0, pool.tkn1]
            if context.gas_token in pool_tokens:
                pool_type = context.gas_token.id
            elif context.wrapped_gas_token in pool_tokens:
                pool_type = context.wrapped_gas_token.id
            else:
                pool_type = ''

            exchange_id = pool.exchange_name + pool_type
            if exchange_id in carbon_exchanges:
                carbon_exchanges[exchange_id].append(tx)
            else:
                carbon_exchanges[exchange_id] = [tx]

        for txs in carbon_exchanges.values():
            new_trade_instructions.append(
                TradeInstruction(
                    pool=txs[0].pool,
                    input=TradeMovement(
                        token=txs[0].input.token,
                        amount=sum([tx.input.amount for tx in txs]),
                    ),
                    output=TradeMovement(
                        token=txs[0].output.token,
                        amount=sum([tx.output.amount for tx in txs]),
                    ),
                    aggregated_from=txs,
                )
            )

    return new_trade_instructions
