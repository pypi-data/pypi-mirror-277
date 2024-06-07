"""
CArbOptimizer: a library for optimizing arbitrage opportunities in AMM pools.

---
(c) Copyright Bprotocol foundation 2023-24. 
Licensed under MIT
"""
import importlib.metadata


__VERSION_POETRY__ = importlib.metadata.version('carb-optimizer')
from .releaseinfo.release_number import __RELEASE_NUMBER__ as __VERSION__, __RELEASE_DATE__ as __DATE__
__AUTHOR__ = 'Stefan K Loesch'
__COPYRIGHT__ = 'Bprotocol foundation 2023-24'
__LICENSE__ = 'MIT'

# VERSION THAT UPDATES DIRECTLY IN THIS FILE
# __VERSION__ = 30
# __RELEASE_DATE__ = '2024-05-28T22:52:44Z'
# - name: Set release date and increase version (init)
# run: |
#     DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
#     sed -i -e "s/__DATE__ = '.*'/__DATE__ = '$DATE'"/g ./carb_optimizer/__init__.py
#     sed -i -E 's/(__VERSION__ = )([0-9]+)/echo "\1$((\2 + 1))"/e' ./carb_optimizer/__init__.py


from .curves import SimplePair

from .curves import CurveBase
from .curves import ConstantProductCurve
from .curves import CurveContainer

from .optimizer import MargPFullOptimizer
from .optimizer import MargPPairOptimizer
from .optimizer import GraphOptimizer

from .run_mode import RunMode
