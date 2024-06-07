"""
Defines the base class for pairwise arbitrage finder modes

[DOC-TODO-OPTIONAL-longer description in rst format]

---
(c) Copyright Bprotocol foundation 2023-24.
All rights reserved.
Licensed under MIT.
"""
import json
import logging
from typing import Any, Dict, List

from carb_optimizer import CurveContainer, PairOptimizer
from carb_optimizer.optimizer.base import TIF

from .base import ArbitrageFinderBase


logger = logging.getLogger(__name__)


class ArbitrageFinderBasePairwise(ArbitrageFinderBase):
    def find_arbitrage(self) -> Dict[str, List[Any]]:
        arb_opps = []
        call_info = {"optimizer": "PairOptimizer", "calls": []}
        combos = self.get_combos()

        for dst_token, src_token in combos:
            curves = self.CCm.by_pairs(f"{dst_token}/{src_token}").curves
            if len(curves) < 2:
                continue

            for curve_combos in self.get_curve_combos(curves):
                if len(curve_combos) < 2:
                    continue
                try:
                    container = CurveContainer(curve_combos)
                    optimizer = PairOptimizer(container)
                    params = self.get_params(container, [dst_token], src_token)
                    optimization = optimizer.optimize(src_token, params=params)
                    trade_instructions_dic = optimization.trade_instructions(TIF.DICTS)
                    trade_instructions_df = optimization.trade_instructions(TIF.DFAGGR)
                except Exception as e:
                    logger.debug(f"[ArbitrageFinderBasePairwise] {e}")
                    continue
                if trade_instructions_dic is None or len(trade_instructions_dic) < 2:
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