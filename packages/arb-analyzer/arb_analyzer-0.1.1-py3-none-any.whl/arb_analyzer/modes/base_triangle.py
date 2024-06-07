"""
Defines the base class for triangle arbitrage finder modes

[DOC-TODO-OPTIONAL-longer description in rst format]

---
(c) Copyright Bprotocol foundation 2023-24.
All rights reserved.
Licensed under MIT.
"""
import json
import logging
from typing import Any, List, Dict

from carb_optimizer import CurveContainer, MargPOptimizer
from carb_optimizer.optimizer.base import TIF

from .base import ArbitrageFinderBase


logger = logging.getLogger(__name__)


class ArbitrageFinderBaseTriangle(ArbitrageFinderBase):
    def find_arbitrage(self) -> Dict[List[Any], List[Any]]:
        arb_opps = []
        call_info = {"optimizer": "MargPOptimizer", "calls": []}
        combos = self.get_combos()

        for src_token, miniverse in combos:
            try:
                container = CurveContainer(miniverse)
                optimizer = MargPOptimizer(container)
                params = self.get_params(container, container.tokens(), src_token)
                optimization = optimizer.optimize(src_token, params=params)
                trade_instructions_dic = optimization.trade_instructions(TIF.DICTS)
                trade_instructions_df = optimization.trade_instructions(TIF.DFAGGR)
            except Exception as e:
                logger.debug(f"[ArbitrageFinderBaseTriangle] {e}")
                continue
            if trade_instructions_dic is None or len(trade_instructions_dic) < 3:
                # Failed to converge
                continue

            profit = self.get_profit(src_token, optimization, trade_instructions_df)
            if profit is not None:
                arb_opps.append({"profit": profit, "src_token": src_token, "trade_instructions_dic": trade_instructions_dic})

                call_info["calls"].append({
                    "curves": optimizer.curves.as_dicts(),
                    "src_token": src_token,
                    "params": params,
                    "profit": str(profit),
                    "trade_instructions": trade_instructions_dic,
                })
            
        if self._dump_curves_fp is not None:
            json.dump(call_info, self._dump_curves_fp, indent=2)

        return {"combos": combos, "arb_opps": sorted(arb_opps, key=lambda arb_opp: arb_opp["profit"], reverse=True)}
