"""
a graph encoding undirected trading pairs, based on a ``CurveContainer`` object

---
(c) Copyright Bprotocol foundation 2023. 
Licensed under MIT
"""
__VERSION__ = "1.0-rc3" # TODO-RELEASE
__DATE__ = "01/Jun/2024+"


from .base import GraphBase, nx
from dataclasses import dataclass,field


@dataclass
class PairGraph(GraphBase):
    """
    create, manage and analyze an undirected graph of trading pairs
    """
    __VERSION__ = __VERSION__
    __DATE__ = __DATE__
    
    pairs: list = None
    tokens: list = None
    
    
    def __post_init__(self):
        assert not self.pairs is None, "pairs not provided"
        assert not self.tokens is None, "tokens not provided"
        self._G = nx.Graph()
        self._build_graph()
        assert not self.G is None, "graph not built"
    
    @classmethod
    def from_CC(cls, CC):
        """
        alternative constructor from a ``CurveContainer`` object (1)
        
        NOTE 1. Technically, every object with a ``pairs()`` and a ``tokens()`` 
        method can be provided as input
        """
        pairs = CC.pairs()
        tokens = CC.tokens()
        return cls(pairs=pairs, tokens=tokens)
    
    def _create_edges(self, pairs=None):
        """creates and returns the undirected edges of the graph (trading pairs)"""
        edges = [tuple(p.split("/")) for p in self.pairs]
        return edges
    
