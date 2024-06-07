"""
a CurveContainer object that is restricted to curves being able to trade in a single pair, in single direction.

---
(c) Copyright Bprotocol foundation 2023. 
Licensed under MIT
"""
__VERSION__ = "1.0-rc3" # TODO-RELEASE
__DATE__ = "01/Jun/2024+"


from .cpc import ConstantProductCurve
from .curvecontainer import CurveContainer
from .curvebase import CurveBase

from dataclasses import dataclass, field
from enum import Enum


@dataclass
class EdgeContainer(CurveContainer, CurveBase):
    """
    a ``CurveContainer`` restricted to a single pair an a single direction of trade
    
    
    A ``CurveContainer`` object can hold many different curves, covering many different pairs, 
    making aggregation between objects difficult. However, once we restrict the curves to a 
    single pair then we can consider the aggregation of those curves as the new, bigger curve.
    
    We furthermore restrict the direction of trading, in line with the way Carbon curves work.
    In other words, any Carbon curve will appear in exactly one EdgeContainer, whilst conventional
    AMMs like Uniswap will appear in two -- one for each direction.
    
    The ``EdgeContainer`` is closely related to the objects in the ``graphs`` module, notably
    the ``EdgeGraph`` object. In fact, there is a one-to-one correspondence between the edges
    in an ``EdgeGraph`` and ``EdgeContainer`` objects.
    
    :tkn_out:   the source token of the curves in this container, ie the one that 
                can be traded out by the curves (1)
    :tkn_in:    the target token, ie the one that is being traded in (1)
    
    
    NOTE 1. The price convention of the container is that the base token is ``tkn_out`` and 
    the quote token is ``tkn_in``, and therefore the pair is ``tkn_out/tkn_in``.
    Note that this is consistent with Carbon conventions ``dy/dx`` where ``y`` is the token
    that is available for trading on the curve.
    """
    __VERSION__ = __VERSION__
    __DATE__ = __DATE__
    
    curves: list = field(default_factory=list, repr=False) # redefined to avoid repr
    tkn_out: str = field(default=None, repr=True)
    tkn_in: str = field(default=None, repr=True)
    _max_price: float = field(default=None, repr=False, init=False)
    
    def __post_init__(self):
        
        if isinstance(self.curves, str):
            raise ValueError("curves must not be a string; did you put tokens as positional arguments?")
        super().__post_init__()
        
        if self.tkn_out is None and self.tkn_in is None:
            if len(self.curves) == 0:
                raise ValueError("must provide either tokens, or a list of curves")
            self.tkn_out = self.curves[0].tknb
            self.tkn_in = self.curves[0].tknq
        
        try:
            assert isinstance(self.tkn_out, str)
            assert isinstance(self.tkn_in, str)
        except AssertionError:
            raise ValueError("parameters must be of right type and not None", self.__dict__)
        
        self._is_inverse = dict()
        for c in self.curves:
            self._is_inverse[c] = self._assert_validity_get_direction(c)

    
    @classmethod
    def from_pair(cls, pair, *, curves=None, tkn_in=None):
        """
        alternative constructor: from a pair ``tkn_out/tkn_in``
        
        :curves:    a list of curves to add to the container (must be consistent 
                    with the pair and direction)
        :tkn_in:    to freeze the in-token if the quote direction of the pair 
                    is in the wrong direction or not known
        
        """
        curves = curves or []
        tknb, tknq = pair.split("/") # default: pair = "tkn_out/tkn_in"
        if not tkn_in is None:
            assert tkn_in in [tknb, tknq], f"if in-token [{tkn_in}] is provided, it must be in {pair}"
            if tkn_in == tknb:
                # tkn_in should be tknq; if not ==> reverse
                tknb, tknq = tknq, tknb
        return cls(tkn_out=tknb, tkn_in=tknq, curves=curves)

    @classmethod
    def from_curves(cls, curves, *, tkn_out=None):
        """
        alternative constructor: from a list of curves
        
        :curve:     the list of curves; they must all be of the same pair
        :tkn_out:   to freeze the source token if the quote direction of the first pair in the
                    list is in the wrong direction or not known
        """
        if len(curves) == 0:
            raise ValueError("curves must not be empty")
        c = curves[0]
        if tkn_out is None:
            pair = c.pair
        else:
            pair = c.pair if c.tknb == tkn_out else c.pair_r
        return cls.from_pair(pair, curves=curves)
    
    class TYPE(Enum):
        """
        Enum for the type of the curve
        """
        DICT = 1
        LIST = 2
        GENERATOR = 3
        
    @classmethod
    def from_CC(cls, CC, *, result_type=None):
        """
        alternative constructor: create multiple EdgeContainers from a CurveContainer
        
        :CC:            the CurveContainer to split into EdgeContainers (1)
        :result_type:   the ``TYPE`` of the return value (``DICT``, ``LIST``, ``GENERATOR``) (2)
        :returns:       the ``EdgeContainer`` object embedded into a structure as described below (2)
        
        NOTE 1. There is no filtering applied to the curve container object, the entire container
        is split into multiple EdgeContainers. This is not a real restriction however as the
        CurveContainer object can be filtered before calling this method.
        
        NOTE 2. The return value of this methods is as described in the table below. The pair
        is always in the form ``(tkn_out, tkn_in)``.
        
        =============   ===========================================================
        ``TYPE``        return value
        =============   ===========================================================
        ``DICT``        ``dict`` of ``{pair: EdgeContainer}``
        ``LIST``        ``generator`` of ``(key, EdgeContainer)`` pairs
        ``GENERATOR``   ``list`` of ``(key, EdgeContainer)`` pairs
        =============   ===========================================================
        """
        # that's all pairs, including some(!) reverse ones
        pairs = {tuple(p.split("/"))for p in CC.pairs()}
        
        # now we make sure we have all pairs, including all reverse ones
        pairs_r = {(a, b) for a, b in pairs} | {(b, a) for a, b in pairs}
        #print("pairs =>", len(pairs), len(pairs_r))
        
        # convert pair tuples to pair strings
        pair = lambda pt: f"{pt[0]}/{pt[1]}"
        
        # for each pair in each direction -> (pair_t, CC)
        result = ((pair_t, CC.by_pairs(pair(pair_t))) for pair_t in pairs_r)
        
        # convert CC to curves and remove invalid ones -> (pair_t, [valid curves])
        result = ( (r[0], [c for c in r[1] if cls.is_edge_curve(c, r[0])]) for r in result)    
        
        # remove lines with no curves -> (pair_t, [valid curves])                                        
        result = ( r for r in result if len(r[1]) > 0) 

        # convert curves to EdgeContainer -> (pair_t, EdgeContainer)
        result = ( (r[0], cls(tkn_out=r[0][1], tkn_in=r[0][0], curves=r[1])) for r in result)
        
        result_type = result_type or cls.TYPE.DICT
        if result_type == cls.TYPE.GENERATOR:
            return result
        if result_type == cls.TYPE.LIST:
            return list(result)
        if result_type == cls.TYPE.DICT:
            return {r[0]: r[1] for r in result}
        raise ValueError("invalid result_type", result_type)
    
    
    def add(self, item):
        """
        adds a curve to the container
        
        :curve:     the curve to add
        """
        # unwrap iterables...
        try:
            for c in item:
                self.add(c)
            return self
        except TypeError:
            pass

        # at this point, item must be a ConstantProductCurve object
        assert isinstance(item, ConstantProductCurve), f"item must be a ConstantProductCurve object {item}"
        is_inverse = self._assert_validity_get_direction(item)
        super().add(item)
        self._is_inverse[item] = is_inverse
    
    def _assert_validity_get_direction(self, curve):
        """
        validates the curve to be added
        
        :curve:     the curve to validate
        :returns:   True if the curves is inverted (1), False otherwise
        :raises:    ValueError if the curve does not match the pair
        
        NOTE 1. Inverted refers to the direction of the pair
        ===============  =====================================================================
        regular curve    curve ``tknb/x`` is ``tkn_out``, curve ``tknq/y`` is ``tkn_in``    
        inverted curve   curve ``tknb/x`` is ``tkn_in``, curve ``tknq/y`` is ``tkn_out``    
        ===============  =====================================================================
        """
        try:
            assert curve.tknb == self.tkn_out
            assert curve.tknq == self.tkn_in
            assert curve.tknx == self.tkn_out
            if curve.x_act == 0:
                raise ValueError(f"curve (cid={curve.cid}, {curve.pair}) has no balance in tkn_out {self.tkn_out}")
            is_inverse = False
        except AssertionError:
            try:
                assert curve.tknq == self.tkn_out
                assert curve.tknb == self.tkn_in
                assert curve.tkny == self.tkn_out
                if curve.y_act == 0:
                    raise ValueError(f"curve (cid={curve.cid}, {curve.pair}) has no balance in tkn_out {self.tkn_out}")
                is_inverse = True
            except AssertionError:
                raise ValueError(f"curve (cid={curve.cid}, {curve.pair}) does not match EdgeContainer pair {self.pair}", curve)
        return is_inverse
    
    @classmethod
    def is_edge_curve(cls, curve, edge):
        """
        checks if a curve is an edge curve for a given edge
        
        :curve:     the curve to check
        :edge:      the edge to check against, as tuple ``(tkn_out, tkn_in)``
        :returns:   ``True`` if the curve is an edge curve 
        """
        #print("[is_edge_curve] curve", curve)
        if set(edge) != {curve.tknb, curve.tknq}:
            #print("[is_edge_curve] wrong tokens", set(edge), {curve.tknb, curve.tknq})
            return False
        if edge[1] == curve.tknx:
            #print("[is_edge_curve] x_act", curve.x_act, "x_act>0", curve.x_act > 0)
            return curve.x_act > 0
        elif edge[1] == curve.tkny:
            #print("[is_edge_curve] y_act", curve.y_act, "y_act>0", curve.y_act > 0)
            return curve.y_act > 0
        else:
            raise ValueError("unexpected error", edge, curve)
    
    @property
    def tknb(self):
        """
        base token, equal to ``tkn_out`` (can be traded out of the curves)
        """
        return self.tkn_out
    tknx = tknb
    
    @property
    def tknq(self):
        """
        quote token, equal to ``tkn_in`` (can be traded into the curves)
        """
        return self.tkn_in
    tkny = tknq
    
    @property
    def pair(self):
        """
        the trading pair, also providing its price convention ``tkn_in`` per ``tkn_out``
        """
        return f"{self.tknb}/{self.tknq}"
    
    def max_price(self, *, incl_pair=False):
        """
        returns the maximum price of the pair within all curves, in the unit of ``tkn_in`` per ``tkn_out``
        
        :returns:   the maximum price, ie the price of the curve with the largest ``tknq`` balance
        
        NOTE: This value is frozen when the object is frozen.
        """
        if (not self.is_frozen) or (self._max_price is None):
            if len(self.curves) == 0:
                raise ValueError("no curves in container")
            max_price = max([c.price(pair=self.pair) for c in self.curves])
            if self.is_frozen:
                self._max_price = max_price
        else:
            max_price = self._max_price
        if not incl_pair:
            return max_price
        return (max_price, self[0].price(pair=self.pair, incl_pair=True)[1])
    
    class RESULT(Enum):
        """
        Enum for the result of the dxvecfrompvec_f
        """
        AGGR = 0
        DETAILED = 1
        
    def dxvecfrompvec_f(self, pvec, *, ignorebounds=False, result=None):
        """
        Returns token holding vector ``xvec`` at price vector ``pvec`` [API]
        
        :pvec:      a dict containing all prices; the dict must contain the keys
                    for ``tknx`` and for ``tkny`` and the associated value must be the respective
                    price in any numeraire (only the ratio is used)
        :returns:   token difference amounts as dict ``{tknx: dx, tkny: dy}`` (or constituent 
                    dicts if ``result`` is ``RESULT.DETAILED``)
        
        EXAMPLE
        
        .. code-block:: python
        
            pvec = {"USDC": 1, "ETH": 2000, "WBTC": 40000}
            dxvec = curve.dxvecfrompvec_f(pvec) 
                # --> {"ETH": -20, "WBTC": 1.01}
        """
        if len(self) == 0:
            return {self.tkn_out: 0, self.tkn_in: 0}
        
        ib = ignorebounds
        constituents = (
            (c, c.dxvecfrompvec_f(pvec, ignorebounds=ib))
            #if not self._is_inverse[c] else (c, c.dxvecfrompvec_f(pvec, ignorebounds=ib))
            for c in self.curves
        )
        if result == self.RESULT.DETAILED:
            return list(((x[0].cid, x[0].subcid), x[1]) for x in constituents)
        constituents = list(x[1] for x in constituents)
        keys = list(constituents[0].keys())
        return {key: sum(d[key] for d in constituents) for key in keys}
    
    def xvecfrompvec_f(self, pvec, *, ignorebounds=False, result=None):
        """
        Returns change in token holding vector ``xvec``, ``dxvec``, at price vector ``pvec`` [API]
        
        :pvec:      a dict containing all prices; the dict must contain the keys
                    for ``tknx`` and for ``tkny`` and the associated value must be the respective
                    price in any numeraire (only the ratio is used)
        :returns:   token amounts as dict ``{tknx: x, tkny: y}``
        
        EXAMPLE
        
        .. code-block:: python
        
            pvec = {"USDC": 1, "ETH": 2000, "WBTC": 40000}
            xvec = curve.xvecfrompvec_f(pvec) 
                # --> {"ETH": 200, "WBTC": 10}
        """
        if len(self) == 0:
            return {self.tkn_out: 0, self.tkn_in: 0}
        
        ib = ignorebounds
        constituents = (
            (c, c.xvecfrompvec_f(pvec, ignorebounds=ib))
            #if not self._is_inverse[c] else (c, c.xvecfrompvec_f(pvec, ignorebounds=ib))
            for c in self.curves
        )
        if result == self.RESULT.DETAILED:
            return list(((x[0].cid, x[0].subcid), x[1]) for x in constituents)
        constituents = list(x[1] for x in constituents)
        keys = list(constituents[0].keys())
        return {key: sum(d[key] for d in constituents) for key in keys}


    @staticmethod 
    def _dxfromdy_h(c, dy, *, reverse=False, ignorebounds=False):
        """
        helper function for extract ``dxfromdy_f`` or ``dyfromdx_f`` from a curve
        
        :c:             the curve to extract the function from
        :dy:            the input value ``dy`` (or ``dx`` if ``reverse`` is True)
        :reverse:       if ``True``, all ``x``, ``y`` will be swapped
        :ignorebounds:  passed to the curve function
        :returns:       ``c.dxfromdy_f(dy)`` (or ``c.x_act`` if out of bounds) or the reverse
        """
        if reverse == False:
            result = c.dxfromdy_f(dy, ignorebounds=ignorebounds)
            if result is None: result = c.dx_max
        else:
            result = c.dyfromdx_f(dy, ignorebounds=ignorebounds)
            if result is None: result = c.dy_max
        return result

    def _is_inverse_h(self, c, _reverse):
        """helper function to known when to inverse"""
        reverse = not self._is_inverse[c]
        reverse = reverse if not _reverse else not reverse
        return reverse

    def dyfromdx_f(self, dx, *, ignorebounds=False, result=None, _reverse=False):
        """
        ``dy`` value for given ``dx`` value, if in range; ``None`` otherwise (1)
        
        NOTE 1. ``x`` here is ``tkn_out`` and ``y`` is ``tkn_in``
        
        """
        assert len(self) > 0, "no curves in container"
        assert len(self) < 2, "cannot currently deal with more than one curve"
        reverse = lambda c: self._is_inverse[c] if _reverse else not self._is_inverse[c]

        # NOTE: the below code pushes the amount dx through each and every curve; this is
        # obviously wrong as it pushes the same tokens through multiple curves, which
        # leads to double counting. We have to implement a more sophisticated algorithm
        # that routes between the curves on the age such that marginal prices coincide.
        # This will almost certainly require a goal seek.
        
        # This however may not be the right approach, because we do not particularly care
        # about starting this process by pushing ``dx``. Instead we could ask _what happens
        # at a price ``p``_ in which case our live may become much easier.
        constituents = (
            (c, self._dxfromdy_h(c, dx, reverse = reverse(c), ignorebounds=ignorebounds))
            for c in self.curves
        )            
        if result == self.RESULT.DETAILED:
            return list(((c.cid, c.subcid), y) for c,y  in constituents)
        return sum(y[1] for y in constituents) 
        
    def dxfromdy_f(self, dy, *, ignorebounds=False, result=None):
        """
        ``dx`` value for given ``dy`` value, if in range; ``None`` otherwise (1)
        
        NOTE 1. ``x`` here is ``tkn_out`` and ``y`` is ``tkn_in``
        
        """
        return self.dyfromdx_f(dy, ignorebounds=ignorebounds, result=result, _reverse=True)

        
    def invariant(self, include_target=False):
        """
        Returns the current invariant of the curve (1)
        
        :include_target:    if True, the target invariant returned in addition to the actual invariant
        :returns:           invariant, or (invariant, target) (1)
        
        NOTE 1: eg for constant product the invariant is :math:`k(x,y)=xy`
        """
        raise NotImplementedError("invariant not implemented here")
    
    
    
