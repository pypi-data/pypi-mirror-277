"""
finding optimal arbitrage opportunities by looking at the market graph


---
This module is still subject to active research, and
comments and suggestions are welcome. The corresponding
author is Stefan Loesch <stefan@bancor.network>

(c) Copyright Bprotocol foundation 2023. 
Licensed under MIT
"""
__VERSION__ = "1.0-rc3" # TODO-RELEASE
__DATE__ = "01/Jun/2024+"

import numpy as np
import matplotlib.pyplot as plt
import math as m
from enum import Enum
from dataclasses import dataclass, field
import itertools as it

from ..helpers.attrdict import AttrDict
from ..helpers.timer import Timer
from .arboptimizerbase import ArbOptimizerBase, ArbOptimizerResult
from ..curves.curvecontainer import CurveContainer
from ..curves.edgecontainer import EdgeContainer
from ..graphs.curvegraph import CurveGraph

@dataclass
class TTResult:
    """
    result of ``token_transport`` (to come) and ``token_transport_exploded``
    
    :amt_in:    the amount pushed into the path (``>0``)
    :amt_out:   the amount coming out on the other side of the path (``<0``)
    :tkn_in:    the token pushed in
    :tkn_out:   the token coming out
    """
    amt_in: float
    amt_out: float
    tkn_in: str
    tkn_out: str  
    
    def __float__(self):
        return float(self.amt_out)
    
    def __int__(self):
        return int(float(self))
                
@dataclass
class TTPath():
    """
    result object when detailed path information is request in `token_transport`` (to come) and ``token_transport_exploded``
    
    :edge:      the edge of this step (as ``tuple`` token in, token out)
    :curves:    the curves used for this step, as ``list`` of curves (1)
    :amt_in:    the amounts going into those curve, as ``list`` of ``floats``
    :amt_out:   the amount going out, ditto
    :O:         the optimizer object
    
    NOTE 1. Currently only one curve per edge is supported
    """
    edge:    tuple = field(repr=True)
    curves:  list = field(repr=False)
    amt_in:  list[float] = field(repr=True)
    amt_out: list[float] = field(repr=True)
    _O:      any = field(repr=False)
    
    def __post_init__(self):
        assert len(self.curves) == 1, f"currently only one curve per edge is supported [{len(self.curves)}]"
        for c in self.curves:
            assert c.token_s == set(self.edge), f"curve tokens not consistent with edge {self.curve.cid} {self.edge}"
                    
        if not isinstance(self.amt_in, list) or not isinstance(self.amt_out, list):
            raise ValueError("amt_in and amt_out must be lists", self.amt_in, self.amt_out)
        # for _ in self.amt_in: assert _ > 0, f"all amt_in must be >0, {_}"
        # for _ in self.amt_out: assert _ < 0, f"all amt_out must be <0, {_}"
            # TODO: The above can fail on CapacityExceeded objects
        assert len(self.curves) == len(self.amt_in) == len(self.amt_out), f"lengths must match [{len(self.curves)} != {len(self.amt_in)} != {len(self.amt_out)}]"
    
    @property
    def O(self):
        """returns the optimizer object"""
        return self._O
    
    @property
    def tkn_in(self):
        """returns the token pushed in"""
        return self.edge[0]
    
    @property
    def tkn_out(self):
        """returns the token coming out"""
        return self.edge[1]
    
    @property
    def ec(self):
        """returns the edge container object"""
        return self.O.EC(self.edge)
    
    @property
    def p(self):
        """returns the ``max_price`` of ``edge``"""
        return self.ec.max_price()
    
    @classmethod
    def result(cls, cycles):
        """
        create a ``TTResult`` object from a list of ``TTPath`` objects
        
        NOTE: the amount / token pushed in (out) is taken from the first (last)
        element in the list
        """
        return TTResult(
            amt_in      = sum(cycles[0].amt_in),
            tkn_in      = cycles[0].edge[0],
            amt_out     = sum(cycles[-1].amt_out),
            tkn_out     = cycles[-1].edge[1],
        )

class CERESULT(Enum):
    """possible values for ``CapacityExceeded.result`` (``enum``)"""
    RAISE = 0
    ZERO = 1
    MAX_IN = 2
    MAX_OUT = 3
    
@dataclass
class CapacityExceeded():
    """
    sentinel and info class for when the capacity of a trading curve or path is exceeded
    
    :amt_in:        the amount that was pushed in when it failed (``>0``)
    :max_in:        the amount that could maximally have been pushed in (``>0``)
    :tkn_in:        the token that was pushed in
    :max_out:       the amount that could have maximally been released (``<0``)
    :tkn_out:       the token that was released
    :curves:        the curve ``set`` that did not have sufficient capacity
    :result:        what ``float(self)`` returns (``ZERO``, ``MAX_IN``, ``MAX_OUT``)
    """
    amt_in: float = None
    max_in: float = None
    tkn_in: str = None
    max_out: float = None
    tkn_out: float = None
    curves: set = field(init=True, default=None, repr=False) 
    result: CERESULT = CERESULT.ZERO
    
    def __post_init__(self):
        self.tkn_in  = self.tkn_in or "TKN_IN"
        self.tkn_out = self.tkn_out or "TKN_OUT"
        
        if not self.amt_in is None:
            assert self.amt_in > 0, f"amt_in must be >0, {self.amt_in}"
        if not self.max_in is None:
            assert self.max_in >= 0, f"max_in must be >=0, {self.max_in}"
        if not self.max_out is None:
            assert self.max_out <= 0, f"max_out must be >=0, {self.max_out}"
        
    def __float__(self):
        if self.result == CERESULT.ZERO:
            return 0.
        elif self.result == CERESULT.MAX_IN:
            return float(self.max_in)
        elif self.result == CERESULT.MAX_OUT:
            return float(self.max_out)
        raise NotImplementedError(f"Unknown / not implemented result {self.result}")
    
    def __int__(self):
        return int(float(self))
    
    def __add__(self, other):
        return (float(self)+other)
    
    def __sub__(self, other):
        return (float(self)-other)
    
    def __mul__(self, other):
        return (float(self)*other)
    
    def __truediv__(self, other):
        return (float(self)/other)
    
    def __floordiv__(self, other):
        return (float(self)//other)
    
    def __radd__(self, other):
        return (other+float(self))
    
    def __rsub__(self, other):
        return (other-float(self))
    
    def __rmul__(self, other):
        return (other*float(self))
    
    def __rtruediv__(self, other):
        return (other/float(self))
    
    def __rfloordiv__(self, other):
        return (other//float(self))
    
@dataclass
class ExplodedPath():
    """
    represents a path exploded into its curves, ie a path with exactly one curve per edge
    
    :_path:    path to be analyzed, as sequence of nodes; see ``token_transport``
    :_curves:  curves to be used, exactly one per edge
    :_ix:      the index of this exploded path (can be ``int`` or ``str``; not used)
    :_O:       the optimizer object
    """
    _path: list = field(init=True, repr=True)
    _curves: list = field(init=True, repr=False)
    _ix: any = field(init=True, repr=True)
    _O: any = field(init=True, repr=False)
    _edges: list = field(init=False, repr=False)
    
    def __post_init__(self):
        self._edges = self.O.CG.path2edges(self._path)
        assert len(self._curves) == len(self._edges), f"number of curves must match number of edges [{len(self._curves)} != {len(self._edges)}]"
        for ix in range(len(self._curves)):
            assert self._curves[ix] in self.O.EC(self._edges[ix]).curves, f"curve {self._curves[ix]} not in edge {self._edges[ix]}"
        
    @property
    def path(self):
        """returns the path (as list of nodes)"""
        return self._path
    
    @property
    def edges(self):
        """returns the edges of the path (as list of tuples of adjacent nodes)"""
        return self._edges
    
    def __len__(self):
        """length is the number of edges"""
        return len(self.edges)
    
    @property
    def ix(self):
        """returns the index of the current curve"""
        return self._ix
    
    @property
    def curves(self):
        """returns the curves of the path (as list of curves)"""
        return self._curves
    
    @property
    def O(self):
        """returns the optimizer object"""
        return self._O


@dataclass
class GraphOptimizerResult(ArbOptimizerResult):
    """
    result of the ``GraphOptimizer`` class
    
    :tt_paths:      the token transport paths calculated by the GraphOptimizer
    :edge_curves:   a ``dict`` edge -> [curves], associating curves with the
                    respective edges
    """
    tt_paths: list[TTPath] = field(repr=False, default=None)
    edge_curves: dict = field(repr=False, default=None)
    
    def __post_init__(self, *args, **kwargs):
        super().__post_init__(*args, **kwargs)
        assert self.curves is None, "do not provide curves explicitly; they are filled automatically"
        
        if not self.is_error:
            # data validation and enrichment, only if not an error result
            assert not self.tt_paths is None, "tt_paths must be provided"
            assert not self.edge_curves is None, "edge_curves must be provided"
            edges = [ttp.edge for ttp in self.tt_paths]
            if not set(edges) == set(self.edge_curves.keys()):
                raise ValueError("Inconsistent edge sets", edges, self.edge_curves.keys())
            for e,cc in self.edge_curves.items():
                if not len(cc) == 1:
                    raise ValueError("Currently must have exactly one curve per edge", e, cc)
                c = cc[0]
                if not c.token_s == set(e):
                    raise ValueError("Curve tokens not consistent with edge", c.token_s, e, c.cid, c)
            self.curves = CurveContainer(self.edge_curves.values())
            if not len(self.curves) == len(edges):
                raise ValueError(f"inconsistent number of curves [{len(self.curves)} != {len(edges)}]", self.curves, edges)
        
    def trade_instructions(self, ti_format=None):
        """ 
        returns list of ``TradeInstruction`` objects [API]

        :ti_format:     use the ``TIF`` enum constants to determine format; 
                        see ``TradeInstruction.to_format`` for details; 
                        default is ``to_format`` default (1)
                        
        NOTE 1. Not all formats are currently supported by this function, notably the 
        data frame formats that also display prices; we do not consider a priority as
        data frame formats are only meant for human consumption. All production code
        must use ``TIF.OBJECTS`` or ``TIF.DICTS``.
        """
        try:
            assert (self.is_error is False), "cannot get this data from an error result"
            for ttp in self.tt_paths:
                assert len(ttp.curves) == 1, f"currently only one curve per edge is supported [{len(ttp.curves)}, {ttp}]"
                # TODO: iterate over all curves in ttp.curves and remove above assertion
            result = (
                ArbOptimizerBase.TradeInstruction.new(
                    curve_or_cid=self.edge_curves[ttp.edge][0], 
                    tkn1=ttp.tkn_in,    amt1=ttp.amt_in[0], 
                    tkn2=ttp.tkn_out,   amt2=ttp.amt_out[0],
                )
                for ttp in self.tt_paths
            )
            return ArbOptimizerBase.TradeInstruction.to_format(
                result, robj=self, ti_format=ti_format
            )
        except AssertionError:
            if self.raiseonerror:
                raise
            return None
    

@dataclass
class GraphOptimizer(ArbOptimizerBase):
    """
    implements the graph based arbitrage finding algorithm
    """
    __VERSION__ = __VERSION__
    __DATE__ = __DATE__
    
    @property
    def kind(self):
        return "graph"
    
    _CC: CurveContainer = field(init=True, repr=False)
    _ECC: dict[EdgeContainer] = field(init=False, repr=False)
    _G: CurveGraph = field(init=False, repr=False)
    
    def __post_init__(self):
        super().__post_init__()
        self._CG = CurveGraph(_CC=self.CC)
        self._ECC = EdgeContainer.from_CC(self.CC)
        for ec in self._ECC.values():
            ec.freeze()
        

    # enums and dataclasses
    CERESULT = CERESULT                     # result type for "capacity exceeded"
    TTResult = TTResult                     # result class for token transport
    TTPath = TTPath                         # result class for path in token transport
    CapacityExceeded = CapacityExceeded     # result class for "capacity exceeded"
    ExplodedPath = ExplodedPath
    
    Result = GraphOptimizerResult
    
    def EC(self, edge=None, *, tkn_source=None, tkn_target=None, raiseonerror=False):
        """
        returns the edge container object for the given edge
        
        :edge:              ``tuple`` of ``(tkn_source, tkn_source)``
        :raiseonerror:      if ``True``, raises a key error if the edge is not present
                            otherwise it returns ``None``
        """
        if edge is None:
            assert not tkn_source is None, "``tkn_source`` must be provided if ``edge`` is not provided"
            assert not tkn_target is None, "``tkn_target`` must be provided if ``edge`` is not provided"
            edge = (tkn_source, tkn_target)
        else:
            assert tkn_source is None, "``tkn_source`` must not be provided if ``edge`` is provided"
            assert tkn_target is None, "``tkn_target`` must not be provided if ``edge`` is provided"
        
        try:
            return self._ECC[edge]
        except KeyError:
            if raiseonerror: raise
            return None
    
    @property
    def CG(self):
        """
        provide direct access to the CurveGraph object
        """
        return self._CG
    
    @property
    def G(self):
        """
        shortcut to the graph object ``self.CG.G``
        """
        return self.CG.G
    
    def price_transport_exploded(self, exploded_path, *, details=False):
        """
        returns the "price transport" (1) for the given exploded path (2)
        
        NOTE 1. see ``price_transport`` for parameters and explanations
        
        NOTE 2. An *exploded* path is a path where every edge is represented by a single curve
        (it is called "exploded" because we explode the parallel path into all possible 
        single-curve fragments)
        """
        curves = exploded_path.curves
        pairs = [f"{e[0]}/{e[1]}" for e in exploded_path.edges]
        prices = (c.price(pair=pair) for c,pair in zip(curves, pairs))
        if details:
            return list(prices)
        return m.prod(prices)
    ptx = price_transport_exploded
    
    
    def price_transport(self, path, *, details=False):
        """
        returns the "price transport" (1) for the given path
        
        :path:      a (often but not necessarily circular) path on the graph of trading 
                    curves, represented as a list of nodes (1)
        :details:   if ``True``, the list of prices along the edges instead of its product
        :returns:   the price transport for the given path
        
        NOTE 1. The ``path`` is a list of nodes :math:`(n_1, n_2, \ldots, n_k)`
        where each of the nodes corresponds to a token, and the edges between the nodes
        correspond to trading curves that exist in this direction. In practical applications
        we often look at circuits where the first and last note coincide :math:`n_1=n_k`
        
        We furthermore are given :math:`p_{ij}` which corresponds to the best price for
        trading token :math:`i` for token :math:`j` along the curve connecting the two
        nodes. We choose to express the prices in units of the target token per source
        token, therefore when multiple trading curves are on the same edge then we are
        looking at the highest (marginal) price. We entirely ignore trade volumes here,
        so the analysis is only valid _"for the first cent traded"_.

        It is easy to see that the price trading the entire path :math:`p_{11}` is
        the product of the prices along the edges, ie
        
        .. math::
            
                p_{11} = p_{12} \cdot p_{23} \cdot \ldots \cdot p_{k1}
                
        Depending on the ``details`` parameter, this function either return the left
        hand side of the equation, or the list of prices on the right hand side.
        """
        path_e = CurveGraph._path_format(path, path_format=CurveGraph.PF.EDGES)
        prices = (self.EC(e).max_price() for e in path_e)
        if details:
            return list(prices)
        return m.prod(prices)
    pt = price_transport
    
    def token_transport_exploded(self, exploded_path, amt_in, *,  details=False, verbosity=0):
        """
        transports tokens along the given exploded path (1)
        
        :exploded_path:     a (typically circular) path on the graph of trading curves, represented as 
                            an ``ExplodedPath`` object
        :amt_in:            the amt_in of source tokens to be pushed into the first node; note: the amt_in 
                            is always positive, and it will be converted into the right convention (curve 
                            outflows are negative) in the function
        :details:           whether to only return the result (default) or the details of the transport
        :verbosity:         verbosity level, info (``1``) or debug (``10,20,...``)
        :returns:           the token transport for the given exploded path (or details)
        
        NOTE 1. An "exploded path" is a path that has been *exploded* into all different combinations
        of pathways through constituent curves, so de facto it is a combination of curves that can
        all be chained together. In practice, it is represented as an ``ExplodedPath`` object.
        """
        assert amt_in >= 0, f"amt_in must not be negative [{amt_in}]"
        current_dx = amt_in 
        if details: cycle_info = []
        curves, edges = exploded_path.curves, exploded_path.edges
        if verbosity >= 10:
            print(f"[ttx] amt_in={amt_in} path={exploded_path.path}")
        for ix, (c, e) in enumerate(zip(curves, edges)):
            tkn_in, tkn_out = e
            current_dy = c.dtknfromdtkn_f(e[0], current_dx, ignorebounds=False)
            if verbosity >= 10:
                print(f"[ttx:{ix}] in={current_dx} {tkn_in} out={current_dy} {tkn_out}")
            if current_dy is None:
                # too much pushed ==> capacity exceeded
                max_in  = c.dtkn_max(tkn_in)
                max_out = c.dtkn_min(tkn_out)
                current_dy = self.CapacityExceeded(amt_in=amt_in, max_in=max_in, tkn_in=tkn_in, max_out=max_out, tkn_out=tkn_out, curves={c})
                if verbosity >= 10:
                    print(f"[ttx] capacity exceeded: max_in={max_in} {tkn_in} max_out={max_out} {tkn_out}")
                    print(f"[ttx] capacity exceeded: => {current_dy}")
            if details: 
                # store the info of the current cycle if so desired
                cycle_info.append(self.TTPath(
                    edge=e, 
                    curves=[c], 
                    amt_in=[current_dx], 
                    amt_out=[current_dy], 
                    _O=self
                ))
            
            # if we have capacity exceeded, no need to continue
            if type(current_dy) == self.CapacityExceeded:
                break
            
            # now prepare for the next step
            current_dx = -current_dy
        
        # finally return the result
        if details: return cycle_info
        return TTResult(
            amt_in  =       amt_in,
            tkn_in  =       edges[0][0],
            amt_out =       current_dy,
            tkn_out =       edges[-1][1],
        )
    ttx = token_transport_exploded


    def ttx_max_amt(self, exploded_path, *, verbosity=0):
        """
        maximum amount that can be transported over an "exploded" path (1)
        
        :exploded_path:     a (typically circular) path on the graph of trading curves, represented as 
                            an ``ExplodedPath`` object; see ``token_transport_exploded``
        :verbosity:         verbosity level, info (``1``) or debug (``10,20,...``)
        :returns:           a ``SimpleResult`` (2) of ``amt_in`` (error result if all unlevered curves)              
        
        NOTE 1. This function estimates the maximum amount that can be passed as ``amt_in`` 
        into ``token_transport_exploded`` and returns it as a ``SimpleResult``. You can then
        call ``token_transport_exploded`` to get the actual cycle results. If all curves
        are unlevered the maximum amount calculation does not make sense as you will be able to 
        push everything through, but at ultimately infinite prices which will kill the numerics
        later if not dealt with here. Therefore all-unlevered simply returns an error result.
        
        NOTE 2. Currently the function can return a ``SimpleNumericResult`` which is a derived class
        from ``SimpleResult`` but the calling code should not rely on this remaining the case.
        """
        timer = Timer()
        curves, edges = exploded_path.curves, exploded_path.edges
        
        # first check if all curves are unlevered ==> return None
        unlevered = [c.is_unlevered for c in curves]
        if all(unlevered):
            return self.SimpleNumericResult(name="amt_max", error="all curves are unlevered")
        first_levered_ix = unlevered.index(False)
        fl_curve  = curves[first_levered_ix]
        fl_edge   = edges[first_levered_ix]
        fl_tkn_in = fl_edge[0]
            # fl_curve, fl_edge, fl_tkn_in now contain the respective values
            # for the first levered curve etc
        
        prices = self.price_transport_exploded(exploded_path, details=True)
            # `prices`` now contains the prices quoted in `amt_out` per `amt_in`
        fl_price = m.prod(prices[:first_levered_ix])
            # `fl_price` now is the price transport to the first levered curve
        fl_max_amt_in_fl_tkn_in = fl_curve.dtkn_max(fl_tkn_in)
            # the maximum amount that can be pushed through, in units of fl_tkn_in
        max_amt_in = fl_max_amt_in_fl_tkn_in/fl_price
            # ditto, but in units of the first token to be pushed into the chain
            
        if verbosity >= 10:
            print(f"[ttxm] first levered curve: ix = {first_levered_ix} of {len(curves)}, max_amt_in = {fl_max_amt_in_fl_tkn_in} {fl_tkn_in}")
            print(f"[ttxm] price transport: p = {fl_price} {edges[0][0]} per {fl_tkn_in}")
            print(f"[ttxm] price transport details: prices={prices[:first_levered_ix]} edges={edges[:first_levered_ix]}")
            print(f"[ttxm] result: max_amt_in = {max_amt_in} {edges[0][0]}")
        
        context = dict(max_amt_in=max_amt_in, tkn_in=edges[0][0], 
                    fl_ix=first_levered_ix, fl_max_amt_in=fl_max_amt_in_fl_tkn_in, fl_tkn_in=fl_tkn_in, fl_price=fl_price)
        
        bracket_hi, bracket_lo = max_amt_in, 1e-100
        for counter in range(1000):
            bracket_mid = 0.5*(bracket_hi+bracket_lo)
            if verbosity >= 10:
                print(f"[ttxm:{counter}] brackets = {bracket_lo} -> {bracket_mid} <- {bracket_hi} ")
            if bracket_hi/bracket_lo - 1 < 0.01:
                break
            r = self.token_transport_exploded(exploded_path, amt_in=bracket_mid)
            if verbosity >= 20:
                print(f"[ttxm] r.amt_out={r.amt_out} r={r} ")
            if isinstance(r.amt_out, CapacityExceeded):
                # transport fails ==> high boundary comes down
                if verbosity >= 10:
                    print(f"[ttxm] fails @ {bracket_mid} => high boundary down")
                bracket_hi = bracket_mid
            else:
                # transport succeeds ==> low boundary comes up
                if verbosity >= 10:
                    print(f"[ttxm] success @ {bracket_mid} => low boundary up")
                bracket_lo = bracket_mid
        return self.SimpleNumericResult(bracket_mid, name="amt_max", N=counter, time=float(timer.end()), context=context)
        
    
    TTX_EPS = 1e-2
    
    def ttx_opt_amt(self, exploded_path, *, verbosity=0):
        """
        optimal amount that can be transported over an "exploded" path 1)
        
        :exploded_path:     a (typically circular) path on the graph of trading curves, represented as 
                            an ``ExplodedPath`` object; see ``token_transport_exploded``
        :verbosity:         verbosity level, info (``1``) or debug (``10,20,...``)
        :returns:           a ``SimpleResult`` (2) of ``amt_in``             
        
        NOTE 1. When pushing tokens through a curve -- or a set of curves, as is the
        generic case here -- then results gets the worse (for the user) the more is
        pushed through. This is by design of all AMM curves, or all order book like
        structures for that matter, where they offers the "better prices in the book"
        first, and the worse rices later on.

        When looking at arbitrages we look at circular paths, eg pushing from USDC to
        USDC via a set of two or more curves. The ``price_transport`` function firstly
        allows checking whether this makes sense at all: if the first dollar circular
        pushed yields less than a dollar there is no point of going further. We
        therefore deal with situations where the first dollar pushed yields more than a
        dollar. Now we have a number of effects

        1. the profit on the *marginal* dollar push decreases because the AMM shows
        worse and worse prices

        2. the cumulative profits increase when we push more as long as the marginal
        profit on the  last dollar pushed is still positive

        3. levered curves may run out of capacity before the point of negative marginal
        profit is reached

        Taking those three together, when we plot dollar profit versus dollars pushed
        the graph always starts out upwards sloping (initial marginal profit positive).
        It then either reaches a maximum (zero marginal profit, point A) or simply stops
        (capacity reached, point B). Those scenarios are mutually exclusive, and the
        optimal amount is either point A or point B.

        NOTE 2. Currently the function can return a ``SimpleNumericResult`` which is a derived class
        from ``SimpleResult`` but the calling code should not rely on this remaining the case.
        """
        timer = Timer()
        curves, edges = exploded_path.curves, exploded_path.edges
        
        # first we determine the max amount we can push through the path
        # which gives us an upper boundary for where we can look for 
        # the optimal price
        max_amt = self.ttx_max_amt(exploded_path).result
        if verbosity >= 10:
            print(f"[ttx_opt_amt] max_amt={max_amt}")
        if max_amt is None:
            # max_amt None ==> all unlevered curves; now need to find suitable starting point
            if verbosity >= 10:
                print(f"[ttx_opt_amt] unlevered curves only")
            amt_start = 0.1 * curves[0].tkn_act(edges[0][0])
                # start value for optimization: set at 10pc of first curve holdings
        else:
            # max_amt given ==> check whether we are in Scenario A or Scenario B
            # Scenario A: interior maximum      ==> downward sloping at boundary
            # Scenario B: maximum at boundary   ==> upward sloping at boundary
            max_amt_eps = max_amt*(1-self.TTX_EPS)
            gain_at_max_amt     = -max_amt     - self.token_transport_exploded(exploded_path, max_amt).amt_out
            gain_at_max_amt_eps = -max_amt_eps - self.token_transport_exploded(exploded_path, max_amt_eps).amt_out
                # note: amt_out is negative so this is actually a difference
            if gain_at_max_amt_eps < gain_at_max_amt:
                # upwards sloping ==> Scenario B ==> return result
                if verbosity >= 10:
                    print(f"[ttx_opt_amt] includes levered curves, upwards {gain_at_max_amt_eps} < {gain_at_max_amt}")
                context = dict(max_amt=max_amt)
                return self.SimpleNumericResult(max_amt, name="amt_opt", time=float(timer.end()), context=context)
            else:
                # downwards sloping at boundary ==> run a goalseek
                if verbosity >= 10:
                    print(f"[ttx_opt_amt] levered curves only, downwards {gain_at_max_amt_eps} > {gain_at_max_amt}")
                amt_start = max_amt/3
                    # start value for optimization set at a third of max
        
        if verbosity >= 10:
            print(f"[ttx_opt_amt] amt_start = {amt_start}")
                            
        context = dict(max_amt=max_amt, amt_start=amt_start)
        func = lambda x: -x - self.token_transport_exploded(exploded_path, x).amt_out
        # if debug == "func":
        #     print(f"[ttx_opt_amt] returning func [verbosity = {verbosity}]")
        #     return func
        r = self._findminmax_nr(func, amt_start, verbosity=verbosity)
        return self.SimpleNumericResult(r.result, r.error, N=r.N, time=float(timer.end()), name="amt_opt", context=context)
        
        
    def transport_curves(self, path):
        """
        the curves used in the transport along a given path
        
        :path:      the path to be analyzed, as sequence of nodes; see ``token_transport``
        :returns:   a ``dict`` of curves used in the transport ``{edge: [curves]}``
        """
        path_e = self.CG.path2edges(path)
        
        def curves(ec):
            try:
                return ec.curves
            except AttributeError: # None
                return []
        return {e: curves(self.EC(e)) for e in path_e}
    

    def explode(self, path):
        """
        explodes a path into subpaths following exactly one curve per edge, returning a list of ``ExplodedPath`` objects
        
        :path:      path to be analyzed, as sequence of nodes; see ``token_transport``
        :returns:   list of ``ExplodedPath`` objects
        """
        edges = self.CG.path2edges(path)
        curves = [self.EC(e).curves for e in edges]
        exploded = it.product(*curves)
        exploded = [
            self.ExplodedPath(_path=path, _curves=c, _ix=ix, _O=self) 
            for ix, c in enumerate(exploded)
        ]
        return exploded


    NON_PLOT_PARAMS = AttrDict(
        show = False,
        npoints = 100,
        grid = True,
        xlabel = "amount in",
        ylabel = "amount out",
        title=None,
    )
    PLOT_PARAMS = AttrDict(
    )
    def plot_transport(self, path, amount_max, amount_min=None, **plot_params):
        """
        calculates and plots the transport along a path
        
        :path:          the transport path to be analyzed, see ``token_transport``
        :amount_max:    the maximum amount to be pushed into the first node (default:``x_act*1.01``)
        :amount_min:    the minimum amount to be pushed into the first node (default: 0)
        :plot_params:   additional parameters for plotting (1)
                        
        NOTE 1. The parameters that are passed to ``plt.plot`` by default are in ``PLOT_PARAMS``,
        and they are augmented / modified the ``plot_params``. Additionally there are params in 
        ``NON_PLOT_PARAMS`` that are used outside of ``plt.plot``. Those will also be modified
        by the respective entry in ``plot_params``.
        """
        PP =  AttrDict({**self.PLOT_PARAMS})
        NPP = AttrDict({**self.NON_PLOT_PARAMS})
        for k in plot_params:
            if k in NPP:
                # if they are in NPP ==> update NPP
                NPP[k] = plot_params[k]
            else:
                # otherwise update or add to
                PP[k] = plot_params[k]
        amount_min = amount_min or 0
        #print("NPP", NPP)
        xv = np.linspace(amount_min, amount_max, NPP.npoints)
        yv = np.array([float(self.token_transport(path, x)) for x in xv])
        plt.plot(xv, yv, **PP)
        plt.grid(NPP.grid)
        if NPP.title:   plt.title(NPP.title)
        if NPP.xlabel:  plt.xlabel(NPP.xlabel)
        if NPP.ylabel:  plt.ylabel(NPP.ylabel)
        if NPP.show:    plt.show()
    
    
    def optimize(self, *args, **kwargs):
        """ 
        not implemented; use ``multi_optimize`` instead (1)
        
        NOTE 1. The other optimizers have an ``optimize`` method that *optimizes* the entire
        market provided, ie that provides one global set of trade instructions to extract 
        maximal value. For methodological reasons, it is not possible to do this with the
        ``GraphOptimizer``. Instead, it produces a set of, often mutually exclusive, trading
        instructions that extract value from the market, but without attaining the global 
        minimum.
        
        It is not possible to fit the multi-optimization into the same API as the optimization.
        Most importantly, 
        
        -   **optimization** returns a ``list`` (logically, a ``set`` because the order does not 
            matter and there is no repetition) of trade instructions, all of which need to be 
            implemented in order to executed the trade
        
        -   **multi-optimization** returns a ``list of lists`` (again, logically ``sets of sets``)
            of trade instructions, where the sets contained in the first list typically compete and
            therefore cannot be implemented together.
        
        In other words: The result of ``optimize`` is a list of trade instructions and should 
        be implemented as is. The result of ``multi_optimizer`` is a list of list of trade
        instructions, and the caller needs to choose one to implement.
        """
        raise NotImplementedError(f"{self.__class__.__name__} does not implement `optimize`; use `multi_optimize` instead. ")

    MO_LENGTH = [2,3]
    MO_THRESHOLD = 0
    
    class MORESULT(Enum):
        OBJECTS = 1
        TTPATHS = 11
        XPATHS = 12

    def multi_optimize(self, target_token=None, *, length=None, threshold=None, exploded_paths=None, result=None, params=None):
        """
        runs the optimization process [API]
        
        :target_token:      the flashloan token that will be the beginning and end of every arbitrage cycle
                            can be omitted only if ``exploded_paths`` is provided
        :length:            the cycle lenght to consider, either as a single ``int`` value, or as a list of 
                            ``int``. Note that only cycles of the exact length given are considered, so eg
                            ``length=4`` only looks at cycles of length 4. To look at everything up to 4 
                            use ``length==[2,3,4]``; default: ``MO_LENGTH``
        :threshold:         the initial threshold for the price transport: only paths meeting this threshold
                            will be considered (eg, 0.05 = 5% gain; default: ``MO_THRESHOLD``)
        :exploded_paths:    alternative invocation on a pre-computed iterable of ``ExplodedPath`` objects 
                            that are then considered as-is; if this option is chosen, all parameters above
                            must be ``None``
        :result:            how to return the result (1)
        :params:            ``dict`` of optional params to influence the optimization algo; should not be 
                            provide in production except for debug purposes (2)
        :returns:           a list of TBC
        
        NOTE 1.The following ``result`` values (enum ``MORESULT``) are recognized
        
        ===================     ================================================
        ``OBJECTS``             ``list`` of ``ArbOptimizerResult`` objects
                                (default)
        ``TTPATHS``             ``list`` of ``list`` of ``TTPath`` objects
        ``XPATHS``              intermediary result: return the explosed paths
                                as list of ``ExplodedPath`` objects
        ===================     ================================================
        
        
        NOTE 2. The following parameters can be provided in ``params``
        
        ===================     ================================================
        ``info``                print info output if true'ish
        ``debug``               print debug output (levels ``1``, ``2``, ...)
        ===================     ================================================            
        """
        timer = Timer()
        result = result or self.MORESULT.OBJECTS
        P = lambda item: params.get(item, None) if params is not None else None
        
        verbosity = self._verbosity(params)
        if verbosity >= 10:
            print("[multi_optimize] params", params)
            print("[multi_optimize] ==> verbosity", verbosity)
        
        if not exploded_paths is None:
            if verbosity>=10:
                print(f"[multi_optimize] using exploded paths (len={len(exploded_paths)})")
            try:
                assert target_token is None
                assert length is None
                assert threshold is None
            except Exception as e:
                raise ValueError("If `exploded_paths` is provided the other parameters must not be", e)
        else:
            assert not target_token is None, "`target_token` must be provided"
            if isinstance(target_token,str):
                target_token = [t.strip() for t in target_token.split(",")]
            length = length or self.MO_LENGTH
            if isinstance(length, int):
                length = [length]
            threshold = threshold or self.MO_THRESHOLD
            
        if exploded_paths is None:
            exploded_paths = []
            for tkn in target_token:
                if verbosity>=10:
                    print(f"[multi_optimize] evaluating token {tkn}")
                for l in length:
                    circuits = self.CG.circuits(tkn, l) 
                    if verbosity>=10:
                        print(f"[multi_optimize] found {len(circuits)} circuits of length {l}")
                    for circ in circuits:
                        xpaths = self.explode(circ)
                        if verbosity>=20:
                            print(f"[multi_optimize] found {len(xpaths)} paths in circuit {circ}")
                        exploded_paths += xpaths
        
        if result == self.MORESULT.XPATHS:
            # XPATHS ==> RETURN EXPLODED PATHS
            if verbosity>=10:
                print(f"[multi_optimize] returning {len(exploded_paths)} exploded circuits as requested")
            return exploded_paths
        
        if verbosity>=10:
            print(f"[multi_optimize] evaluating {len(exploded_paths)} exploded circuits")
        
        circ_profits = [
            (ep, self.price_transport_exploded(ep)) for ep in exploded_paths
        ]
        if verbosity>=20:
            profits = [x[1] for x in circ_profits]
            print(f"[multi_optimize] circuit profits {profits}")
        
        one_plus_threshold = 1+threshold
        above_threshold_circs = [x for x in circ_profits if x[1] > one_plus_threshold]
        if verbosity>=1:
            print(f"[multi_optimize] found {len(above_threshold_circs)} out of {len(exploded_paths)} circuits above threshold={threshold}")
            if verbosity>=20:
                for p in above_threshold_circs:
                    print(f"[multi_optimize] profit {p[1]-1} for path {p[0].path}")
        
        if verbosity>=10:
            print(f"[multi_optimize] evaluating token transport for {len(above_threshold_circs)} circuits")
        
        result_circs = []    
        for ix, circ in enumerate(above_threshold_circs):
            r = self.ttx_opt_amt(circ[0], verbosity=verbosity)
            if verbosity>=10:
                r_or_err = r.result or f"error: {r.error}"
                print(f"[multi_optimize] circuit #{ix:3}: amount = {r_or_err} [price transport = {circ[1]:0.2f}]")
            if not r.is_error:
                r2 = self.token_transport_exploded(circ[0], r.result, details=1)
                result_circs += [r2]
                if verbosity>=20:
                    print(f"[multi_optimize] circuit #{ix:3}: result = {r2}")
        if verbosity>=10:
            print(f"[multi_optimize] obtained {len(result_circs)} result circuits")
            if verbosity>=20:
                for ix, rc in enumerate(result_circs):
                    print(f"[multi_optimize] circ #{ix:3}: {rc}")
        
        if result == self.MORESULT.TTPATHS:
            # TTPATHS ==> RETURN TOKEN TRANSPORT PATHS
            if verbosity>=10:
                print(f"[multi_optimize] returning paths [len={len(result_circs)}]")
            return result_circs
        
        elif result == self.MORESULT.OBJECTS:
            # OBJECTS (DEFAULT) ==> RETURN RESULT OBJECTS
            if len(result_circs) == 0:
                return [self.Result(
                    O = self,
                    targettkn = target_token[0],
                    error = "no profitable circuits found",
                    method = self.kind,
                    time = float(timer.end()),
                )]
                
            result_objs = [
                self.Result(
                    O = self,
                    error = None,
                    #info = None,
                    method = self.kind,
                    result = sum(tt_path[0].amt_in)-sum(tt_path[-1].amt_out),
                    targettkn = target_token[0],
                    time = float(timer.end()),
                    tt_paths=tt_path, 
                    edge_curves={
                        p.edge: CurveContainer(p.curves) 
                        for p in tt_path
                    }
                )
                for tt_path in result_circs # the `rc` are `TTPath` objects
            ]
            return result_objs
        else:
            raise ValueError(f"Unknown result {result}")



