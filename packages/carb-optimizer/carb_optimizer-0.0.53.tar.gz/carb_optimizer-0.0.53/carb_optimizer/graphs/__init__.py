"""
graph analysis related functions

NOTE. This module is a lightweight graphs library that supplements -- and may be in time
may replace the ``arbgraphs`` module. The latter has accumulated a lot of functionality,
and it is not practical to integrate the current code into it.

---
(c) Copyright Bprotocol foundation 2023. 
Licensed under MIT
"""
from .base import GraphBase
from .pairgraph import PairGraph
from .curvegraph import CurveGraph