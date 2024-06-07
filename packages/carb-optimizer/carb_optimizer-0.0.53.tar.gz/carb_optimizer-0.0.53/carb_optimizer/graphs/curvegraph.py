"""
a graph encoding directed trading curves, based on a ``CurveContainer`` object

---
(c) Copyright Bprotocol foundation 2023. 
Licensed under MIT
"""
__VERSION__ = "1.0-rc3" # TODO-RELEASE
__DATE__ = "01/Jun/2024+"


from .base import GraphBase, nx
#from ..curves import CurveContainer      
    # fails in Python 3.8 due to circular imports
    # works in 3.11; TODO-RELEASE: move tests to 3.11?
from dataclasses import dataclass, field


@dataclass
class CurveGraph(GraphBase):
    """
    create, manage and analyze a directed graph of trading curves
    """
    __VERSION__ = __VERSION__
    __DATE__ = __DATE__
    
    #CC: CurveContainer
    _CC: any = field(init=True, repr=False, default=None) # CurveContainer 
    _G: nx.DiGraph = field(init=False, default=None, repr=False)
    
    def __post_init__(self):
        #assert isinstance(self.CC, CurveContainer), "CC not provided"
        assert not self.CC is None, "CC not provided"
        self._G = nx.DiGraph()
        self._build_graph()
        assert not self.G is None, "graph not built"
        
    @property
    def CC(self):
        """the associated curve container object (``CurveContainer``)"""
        return self._CC
        
    @classmethod
    def _create_curve_edges(self, curve):
        """
        creates the edges corresponding to a curve
        
        :curve:     curve object (``ConstantProductCurve``)
        :returns:   list of 0-2 edges
        
        NOTE. A curve that can be traded in both directions will create two edges,
        one each way. A curve that can be traded in only one direction will create
        only one edge, going from the token that the AMM receives to the token that
        leaves the AMM.
        
        In other words, an AMM the allows trading USDC to ETH has an edge ``USDC -> ETH``
        
        IMPORTANT NOTE: the convention up to release #42 included was the opposite, 
        ie the graph edges went the other way
        """
        edges = []
        if curve.x_act > 0:
            edges += [(curve.tkny, curve.tknx)]  # x>0 ==> allows trading y -> x
        if curve.y_act > 0:
            edges += [(curve.tknx, curve.tkny)]  # y>0 ==> allows trading x -> y
        return edges
        
    def _create_edges(self):
        """creates and returns the directed edges of the graph (trading curves)"""
        edges = [self._create_curve_edges(curve) for curve in self.CC]
        edges = [e for sublist in edges for e in sublist]
        return edges
    
    def converts(self, *, frm, to, raiseonerror=True):
        """
        returns True iff the Graph allows converting ``frm`` to ``to``
        """
        G = self.G
        if not frm in G or not to in G:
            if raiseonerror:
                raise ValueError(f"Both tokens [{frm}, {to}] must be nodes of G [{G.nodes}]")
            return False
        return G.has_edge(frm, to)
    
