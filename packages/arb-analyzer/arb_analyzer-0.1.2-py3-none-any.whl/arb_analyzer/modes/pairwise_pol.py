"""
Defines the pairwise-pol arbitrage finder class

[DOC-TODO-OPTIONAL-longer description in rst format]

---
(c) Copyright Bprotocol foundation 2023-24.
All rights reserved.
Licensed under MIT.
"""
from typing import Any, List
from itertools import product

from arb_analyzer.constants import ExchangeType
from .base_pairwise import ArbitrageFinderBasePairwise


class ArbitrageFinderPairwisePol(ArbitrageFinderBasePairwise):
    def get_combos(self) -> List[Any]:
        bancor_pol_tkns = self.CCm.by_params(exchange="bancor_pol").tokens()
        bancor_pol_tkns = set([tkn for tkn in bancor_pol_tkns if tkn != self.context.wrapped_gas_token.id])
        return [(tkn0, tkn1) for tkn0, tkn1 in product(bancor_pol_tkns, [self.context.wrapped_gas_token.id]) if tkn0 != tkn1]

    def get_curve_combos(self, curves: List[Any]) -> List[Any]:
        pol_curves = [curve for curve in curves if ExchangeType(curve.params.exchange_type) == ExchangeType.CARBON_POL]
        carbon_curves = [curve for curve in curves if ExchangeType(curve.params.exchange_type) == ExchangeType.CARBON_V1]
        other_curves = [curve for curve in curves if ExchangeType(curve.params.exchange_type) not in [ExchangeType.CARBON_POL, ExchangeType.CARBON_V1]]
        curve_combos = [[curve] + pol_curves for curve in other_curves]

        if len(carbon_curves) > 0:
            base_dir_one = [curve for curve in carbon_curves if curve.pair == carbon_curves[0].pair]
            base_dir_two = [curve for curve in carbon_curves if curve.pair != carbon_curves[0].pair]

            if len(base_dir_one) > 0:
                curve_combos += [[curve] + base_dir_one for curve in pol_curves]

            if len(base_dir_two) > 0:
                curve_combos += [[curve] + base_dir_two for curve in pol_curves]

        return curve_combos
