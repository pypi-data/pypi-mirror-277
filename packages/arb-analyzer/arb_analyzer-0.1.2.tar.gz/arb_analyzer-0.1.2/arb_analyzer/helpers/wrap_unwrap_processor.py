"""
Deals with wrap and unwrap trades (eg WETH <-> ETH) in the route.

Defines the ``add_wrap_or_unwrap_trades_to_route`` method.

TODO: see whether to consolidate this with other objects

---
(c) Copyright Bprotocol foundation 2023-24.
All rights reserved.
Licensed under MIT.
"""
from typing import List

from arb_analyzer.constants import ExchangeType
from arb_analyzer.context import Context
from arb_analyzer.helpers.tradeinstruction import TradeInstruction
from arb_analyzer.helpers.routehandler import RouteStruct


class FlashloanTokenException(Exception):
    """
    Exception raised due to an incompatible Flashloan token combination.
    """
    pass


def add_wrap_or_unwrap_trades_to_route(
    flashloans: List[dict],
    routes: List[RouteStruct],
    trade_instructions: List[TradeInstruction]
) -> List[dict]:
    """
    This method adds wrap and/or unwrap routes.

    Args:
        cfg: the configuration object.
        flashloans: A list of flashloans.
        routes: A list of routes.
        trade_instructions: A list of trade instructions.

    Returns:
        new_routes: A new list of routes.
    """
    context = Context.instance

    balance_tracker = {}
    for flashloan in flashloans:
        for token, amount in zip(flashloan["source_tokens"], flashloan["source_amounts"]):
            balance_tracker[token] = amount

    flashloan_native_gas_token = context.gas_token.id in balance_tracker
    flashloan_wrapped_gas_token = context.wrapped_gas_token.id in balance_tracker

    if flashloan_native_gas_token and flashloan_wrapped_gas_token:
        raise FlashloanTokenException("[add_wrap_or_unwrap_trades_to_route] Cannot flashloan both wrapped & native gas tokens!")

    segmented_routes = {}
    for idx in range(len(routes)):
        pair = f"{trade_instructions[idx].input.token.id}/{trade_instructions[idx].output.token.id}"
        if pair not in segmented_routes:
            segmented_routes[pair] = {
                "amt_out": 0,
                "amt_in": 0,
                "trades": {},
            }

        segmented_routes[pair]["amt_out"] += trade_instructions[idx].output.wei_amount
        segmented_routes[pair]["amt_in"] += trade_instructions[idx].input.wei_amount
        segmented_routes[pair]["trades"][idx] = trade_instructions[idx].is_carbon

    new_routes = []
    deadline = routes[0].deadline

    for pair, segment in segmented_routes.items():
        token_in, token_out = pair.split("/")
        amount_in = segment["amt_in"]

        if token_in in [context.gas_token.id, context.wrapped_gas_token.id] and amount_in > balance_tracker.get(token_in, 0):
            token_in_inv = context.gas_token.id if token_in == context.wrapped_gas_token.id else context.wrapped_gas_token.id
            new_routes.append(
                _get_wrap_or_unwrap_native_gas_tkn_struct(
                    source_token=token_in_inv,
                    target_token=token_in,
                    amount=amount_in,
                    deadline=deadline
                )
            )
            balance_tracker[token_in_inv] = balance_tracker.get(token_in_inv, 0) - amount_in
            balance_tracker[token_in] = balance_tracker.get(token_in, 0) + amount_in

        balance_tracker[token_in] = balance_tracker.get(token_in, 0) - segment["amt_in"]
        balance_tracker[token_out] = balance_tracker.get(token_out, 0) + segment["amt_out"]

        new_routes.extend([routes[trade_idx] for trade_idx in segment["trades"] if segment["trades"][trade_idx] == True])
        new_routes.extend([routes[trade_idx] for trade_idx in segment["trades"] if segment["trades"][trade_idx] == False])

    should_wrap = flashloan_wrapped_gas_token and balance_tracker.get(context.gas_token.id, 0) > 0
    should_unwrap = flashloan_native_gas_token and balance_tracker.get(context.wrapped_gas_token.id, 0) > 0

    if should_wrap or should_unwrap:
        new_routes.append(
            _get_wrap_or_unwrap_native_gas_tkn_struct(
                source_token=context.gas_token.id if should_wrap else context.wrapped_gas_token.id,
                target_token=context.wrapped_gas_token.id if should_wrap else context.gas_token.id,
                amount=0,
                deadline=deadline
            )
        )

    return new_routes

def _get_wrap_or_unwrap_native_gas_tkn_struct(
    source_token: str,
    target_token: str,
    amount: int,
    deadline: int
) -> dict:
    return RouteStruct(
        cid=None,
        exchange_type=ExchangeType.WRAPPER,
        exchange_name="",
        source_token=source_token,
        target_token=target_token,
        source_amount=amount,
        min_target_amount=amount,
        deadline=deadline,
        extras=None,
    )
