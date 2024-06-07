"""
Finds the arbitrage opportunities once the data has been read

Whilst the Optimizer can work with any number of curves, the arbitrages found
are not _linear_ in the sense that they may require significant initial token 
balances in multiple tokens to execute, and those balances are only certain to
be repaid at the end.

What we generally want is _linear_ transaction where we start with one token
that we can obtain in a flashloan, that we then pass through a series of
exchanges without having to borrow additional tokens, and that are repaid at
the end.

Creating such linear transaction in the generic case is complex, and the longer
the transaction the more likely is that by the time that it has been submitted
on part of the chain has gone and the entire transaction fails.

The way we deal with this issue is that we are looking specifically for _pairwise_ 
and _triangle_ arbitrages, the former only operating on a single pair, and the
latter operating on all pairs that are based on a fixed set of three tokens. 

In order to find and evaluate those arbitrages there is a hierarchy of classes
that are defined in this module

- ``ArbitrageFinderBase`` (``base``): fundamental base class
    - ``ArbitrageFinderPairwiseBase`` (``base_pairwise``): base class for pairwise arbitrages
        - ``ArbitrageFinderMultiPairwiseAll`` (``pairwise_multi_all``)
        - ``ArbitrageFinderMultiPairwisePol`` (``pairwise_multi_pol``)
    - ``ArbitrageFinderTriangleBase`` (``base_triangle``): base class for triangle arbitrages    
        - ``ArbitrageFinderTriangleMulti`` (``triangle_multi``)
        - ``ArbitrageFinderTriangleMultiComplete`` (``triangle_multi_complete``)
        - ``ArbitrageFinderTriangleBancor3TwoHop`` (``triangle_bancor_v3_two_hop``)


---
(c) Copyright Bprotocol foundation 2023-24.
All rights reserved.
Licensed under MIT.
"""
from typing import List

from click.utils import LazyFile

from carb_optimizer import CurveContainer

from arb_analyzer.constants import ArbitrageMode
from arb_analyzer.context import Context
from arb_analyzer.modes.base import ArbitrageFinderBase
from arb_analyzer.modes.pairwise_all import ArbitrageFinderPairwiseAll
from arb_analyzer.modes.pairwise_pol import ArbitrageFinderPairwisePol
from arb_analyzer.modes.triangle_all import ArbitrageFinderTriangleAll
from arb_analyzer.modes.triangle_b3 import ArbitrageFinderTriangleB3
from arb_analyzer.modes.triangle_multi import ArbitrageFinderTriangleMulti

def ArbitrageFinderFactory(
    arb_mode: ArbitrageMode,
    flashloan_tokens: List[str],
    curve_container: CurveContainer,
    dump_curves_fp: LazyFile | None,
) -> ArbitrageFinderBase:
    cls = {
        ArbitrageMode.PAIRWISE_ALL: ArbitrageFinderPairwiseAll,
        ArbitrageMode.PAIRWISE_POL: ArbitrageFinderPairwisePol,
        ArbitrageMode.TRIANGLE_ALL: ArbitrageFinderTriangleAll,
        ArbitrageMode.TRIANGLE_B3: ArbitrageFinderTriangleB3,
        ArbitrageMode.TRIANGLE_MULTI: ArbitrageFinderTriangleMulti,
    }[arb_mode]
    return cls(
        flashloan_tokens=flashloan_tokens,
        curve_container=curve_container,
        context=Context.instance,
        dump_curves_fp=dump_curves_fp,
    )
