"""
representing a collection of bonding curves

---
(c) Copyright Bprotocol foundation 2023. 
Licensed under MIT
"""
__VERSION__ = "4.0-rc3" # TODO-RELEASE
__DATE__ = "01/Jun/2024+"

from .simplepair import SimplePair as Pair
from . import tokenscale as ts
from .params import Params
from .curvebase import DAttrDict
from .cpc import ConstantProductCurve, AF
from .cpcinverter import CPCInverter
from ..graphs import PairGraph
from ..helpers.timer import Timer
from ..enums import ExchangeType

from dataclasses import dataclass, field
import random
from math import sqrt
import numpy as np
import pandas as pd
import json
from matplotlib import pyplot as plt
import itertools as it
import collections as cl
import time
from enum import Enum


AD = DAttrDict

def _safe(func):
    """
    safe execution wrapper: returns ``False`` if exception other than ``KeyError`` occurs
    """
    def func_safe(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            #print(f"[_safe] KeyError")
            raise
        except Exception as e:
            #print(f"[_safe] exception {e}")
            return False
    return func_safe

@dataclass
class CurveContainer:
    """
    container for curve (derived from ``CurveBase``) objects (1) [API]

    :curves:        an iterable of CPC curves, possibly wrapped in CPCInverter objects
                    CPCInverter objects are unwrapped automatically, the resulting
                    list will ALWAYS be curves, possibly with inverted=True; items can
                    also be added using the ``+=`` operator
    :tokenscale:    a TokenScaleBase object (or None, in which case the default)
                    this object contains indicative prices for the tokens which are
                    sometimes useful for numerical stability reasons; the default token
                    scale is unity across all tokens [DEPRECATED]
    
    The following operations are supported (2)
    
    ==================  ================================================
    ``+=``              adds a curve to the container
    ``for __ in``       iterates over the curves in the container
    ``len``             number of curves in the container
    ``[i]``             returns the curve at index ``i``
    ``in``              checks if a curve is in the container
    ==================  ================================================
                    
    NOTE 1: Whilst technically it should be possible to add
    generic ``CurveBase`` objects to ``CurveContainer`` objects,
    a lot of the functionality will break if it is anything
    other than a ``ConstantProductCurve``. However, importantly,
    the optimizer functionality should still work with generic
    curve objects.
    
    NOTE 2. Container operations including `+=` and the constructor do
    not copy the curves provided, but simply rearrange them into a new
    list. Therefore, changes to curve objects will propagate to all 
    container in which this same curve is contained. This should not be
    a problem because curve information is mostly semantically immutable.
    However, there can be certain variable state attached to some curves.
    If this is used care must be taken when rearranging curves in new 
    containers.
    """

    __VERSION__ = __VERSION__
    __DATE__ = __DATE__
    Pair = Pair

    curves: list = field(default_factory=list)
    tokenscale: ts.TokenScaleBase = field(default=None, repr=False)
    _is_frozen: bool = field(default=False, repr=True, init=False)
    
    def __post_init__(self):

        if self.tokenscale is None:
            self.tokenscale = self.TOKENSCALE
        
        # ensure that the curves are in a list (they can be provided as any
        # iterable, e.g. a generator); also unwraps CPCInverter objects
        # if need be, and it flattens nested curves (as obtained by the 
        # exchange bound generators like `from_carbonv1`)
        self.curves = _flatten(self.curves)
        self.curves = [c for c in CPCInverter.unwrap(self.curves)]

        for i, c in enumerate(self.curves):
            if c.cid is None:
                # print("[__post_init__] setting cid", i)
                c.set_cid(i)
            else:
                # print("[__post_init__] cid already set", c.cid)
                pass
            c.set_tokenscale(self.tokenscale)

        self.curves_by_cid = {c.cid: c for c in self.curves}
        self.curveix_by_curve = {c: i for i, c in enumerate(self.curves)}
        # self.curves_by_primary_pair = {c.pairo.primary: c for c in self.curves}
        self.curves_by_primary_pair = {}
        for c in self.curves:
            try:
                self.curves_by_primary_pair[c.pairo.primary].append(c)
            except KeyError:
                self.curves_by_primary_pair[c.pairo.primary] = [c]

    @property
    def is_frozen(self):
        """if True, the container is frozen and can no longer be modified"""
        return self._is_frozen
    
    @is_frozen.setter
    def is_frozen(self, value):
        """allows to freeze the container; once frozen, it cannot be modified"""
        if value:
            self._is_frozen = True
        if self._is_frozen and not value:
            raise ValueError("container is frozen and cannot be unfrozen")
        
    def freeze(self):
        """freezes the container"""
        self.is_frozen = True

    def assert_not_frozen(self):
        """raises an exception if the container is frozen"""
        if self.is_frozen:
            raise ValueError("container is frozen and cannot be modified")
        
    TOKENSCALE = ts.TokenScale1Data
    # default token scale object is the trivial scale (everything one)
    # change this to a different scale object be creating a derived class
    # NOTE. this object is deprectated

    ET = ExchangeType
    
    def scale(self, tkn):
        """returns the scale of ``tkn``"""
        return self.tokenscale.scale(tkn)

    def as_dicts(self):
        """returns list of dictionaries representing the curves [API]"""
        return [c.as_dict() for c in self.curves]
    
    def as_json(self):
        """``as_dicts`` as JSON string [API]"""
        return json.dumps(self.as_dicts())
    
    def as_repr(self):
        """returns a string representation of the container [API]"""
        return ",\n".join([repr(c) for c in self.curves])+","
    
    def as_df(self):
        """returns pandas ``DataFrame`` representing the curves [API]"""
        return pd.DataFrame.from_dict(self.as_dicts()).set_index("cid")
    
    @classmethod
    def from_dicts(cls, dicts):
        """
        alternative constructor: creates container from ``dict`` s [API]
        """
        return cls([ConstantProductCurve.from_dict(d) for d in dicts])

    @classmethod
    def from_df(cls, df):
        """
        alternative constructor: creates container from ``DataFrame`` [API]
        """
        if "cid" in df.columns:
            df = df.set_index("cid")
        df = df.fillna("", inplace=False)
        #print("[from_df] ", df)
        return cls.from_dicts( df.reset_index().to_dict("records") )
        
    def add(self, item):
        """
        adds one or multiple ConstantProductCurves [API]

        :item:      item can be the types in the table below
        
        ========================    ===============================================
        ``item``                    meaning
        ========================    ===============================================
        ``ConstantProductCurve``    a single curve is added
        ``CPCInverter``             the curve underlying the inverter is added
        ``Iterable``                all items in the iterable are added one by one
        ========================    ===============================================
        
        NOTE: the ``+=`` operator is also supported
        """
        self.assert_not_frozen()

        # unwrap iterables...
        try:
            for c in item:
                self.add(c)
            return self
        except TypeError:
            pass

        # ...and CPCInverter objects
        if isinstance(item, CPCInverter):
            item = item.curve

        # at this point, item must be a ConstantProductCurve object
        assert isinstance(
            item, ConstantProductCurve
        ), f"item must be a ConstantProductCurve object {item}"

        if item.cid is None:
            # print("[add] setting cid to", len(self))
            item.set_cid(len(self))
        else:
            pass
            # print("[add] item.cid =", item.cid)
        self.curves_by_cid[item.cid] = item
        self.curveix_by_curve[item] = len(self)
        self.curves += [item]
        # print("[add] ", self.curves_by_primary_pair)
        try:
            self.curves_by_primary_pair[item.pairo.primary].append(item)
        except KeyError:
            self.curves_by_primary_pair[item.pairo.primary] = [item]
        return self

    class PP(Enum):
        """Method for calculating the price of a pair (``enum``)"""
        UNIV3_TIGHTEST = 1 # use the tightest Uniswap v3 range

    def price_for_pair(self, pair, *, method=None, incl_pair=False):
        """
        calculates the price for the pair in question [API]
        
        :pair:          the pair for which to calculate the price
        :method:        calculation method (1)
        :incl_pair:     if ``True``, includes the pair in the result (returns a ``tuple``)
        :return:        the price, or None if no price could be determined

        ======================== ========================================================================
        ``UNIV3_TIGHTEST``       use the price of the tightest Uniswap v3 range only
        ======================== ========================================================================
        """
        method = method or self.PP.UNIV3_TIGHTEST
        assert type(method) == self.PP
        if method == self.PP.UNIV3_TIGHTEST:
            CCf = self.by_params(exchange_name="uni_v3").by_pairs(pair)
            if len(CCf) == 0:
                return None
            fee_min = 1e10
            for c in CCf:
                if c.fee < fee_min:
                    fee_min, c_min = c.fee, c
            return c_min.price(pair, incl_pair=incl_pair)
        else:
            raise ValueError(f"Unknown method {method}")
            
    class AP(Enum):
        """result mode for ``all_prices`` (``enum``)"""
        PRICES = 1
        PATHS = 2
        FULL = 100
    
    def all_prices(self, start, *, start_price=None, pp_method=None, result=None, preferred=None):
        """
        calculates all (1) prices for the tokens in the container, based on curve prices (2) [API]

        :start:         the token from which to start the price discovery (3)
        :start_price:   which price to assing to the ``start`` token (default: 1)
        :pp_method:     see doc for ``price_for_pair``
        :result:        what exactly to return (4)
        :preferred:     preferred tokens to look at when walking the graph (default: None)
        :returns:       usually a prices dict; see note (4) below
        
        IMPORTANT NOTE. THIS METHOD IS NOT CURRENTLY VERY RELIABLE. There are two issue with this code
        
        1. There are always curves in the set that have silly prices; if you happen to run upon those
        then you will get silly prices because you only ever calculate the prices once
        
        2. The code is not deterministic; apparently traversing the graph happens in random order; this
        leads to nodes being visited in different order and therefore with different paths; this
        is compounded by issue 1 because sometimes you hit a bad path, unpredictably
        
        3. The method is slow, and what is slow is calculating the prices even in this cut-down version;
        any attempt to look at more prices and get a consensus will be even slower

        NOTE 1. Only the prices of tokens that can be reached via ``start`` will be
        calculated

        NOTE 2. The prices for each pair are calculated using ``price_for_pair``; the
        parameter ``pp_method`` determines which algorithm is used.

        NOTE 3. In most cases this will be `(W)ETH` or a popular stable coin

        NOTE 4. The following result types are recognized (only use ``PRICES`` aka 
        ``None`` in production)

        ========================== ================================================================================
        ``PRICES``                 returns ``{token: price}`` (default)
        ``PATHS``                  returns prices and ``{token: path}`` where ``path = [start, ..., token]``
        ``FULL``                   like ``PATHS`` but also includes ``Timer`` results
        ========================== ================================================================================
        """
        timer = Timer()
        start_price = start_price or 1
        result = result or self.AP.PRICES
        assert type(result) == self.AP
        PG = PairGraph.from_CC(self)
        timer.record("graph")
        reachable = PG.reachable(start, raw=True, preferred=preferred)
        timer.record("reachable")
            # this returns a dict {path_length: path_info}
            # path_info_list = [(token_1, path_to_token_1), ...]
            # path_to_token = (start, ..., token)
        prices = {start:start_price}
        for l, path_info_list in reachable.items():
            #print(l, len(path_info_list))
            for path_info in path_info_list:
                #token = path_info[0]
                path = path_info[1][l-1:]
                #print(path)
                #print(prices)
                tknq, tknb = path 
                    # the overall path has length l, so this segment must have length 2
                    # tknb is the first token in the path and therefore known, tknq is the new token
                pair = f"{tknb}/{tknq}"
                price_tknq_per_tknb = self.price_for_pair(pair, method=pp_method) 
                    # price is in tknb per tknq which means it is the price of the new token 
                    # in units of the alread known token
                price_tknq = prices[tknq]
                    # this is the price of the quote token, in the desired numeraire
                prices[tknb] = price_tknq_per_tknb * price_tknq
                    # example: price_tknq = 10, price_tknq_per_tknb = 2 ==> price_tknb = 20
                #print(path)
            timer.record(f"l={l} complete", data=dict(n=len(path_info_list)))
        timer.record("complete")
        if result == self.AP.PRICES:
            return prices
        else: 
            paths = reachable
            paths = (l for l in paths.values())
            paths = it.chain(*paths)
            paths = {p[0]: p[1] for p in paths}
            paths[start] = [start]
            if result == self.AP.PATHS:
                return prices, paths
            elif result == self.AP.FULL:
                return prices, paths, timer.result
            else:
                raise ValueError(f"Unknown result mode {result}")

    def _price(self, tknb, tknq):
        """
        returns average price (1) of tknb in tknq (tknb per tknq)
        
        NOTE 1. This price may or may not be meaningful. Use with caution.
        It is used in ``pairs_analysis``
        """
        pairo = Pair.from_tokens(tknb, tknq)
        curves = self.curves_by_primary_pair.get(pairo.primary, None)
        if curves is None:
            return None
        pp = sum(c.pp for c in curves) / len(curves)
        return pp if pairo.is_primary else 1 / pp
    
    class PR(Enum):
        """result mode for ``prices`` (``enum``)"""
        TUPLE = "tuple"
        DICT = "dict"
        DF = "df"

    def prices(self, result=None, *, inclpair=None, primary=None):
        """
        returns tuple or dictionary of the prices of all curves in the container

        :primary:       if ``True`` (default), returns the price quoted in the convention of the primary pair
        :inclpair:      if ``True``, includes the pair in the dictionary
        :result:        what result to return (``PR.TUPLE``, ``PR.DICT``, ``PR.DF``)
        """
        if primary is None: primary = True
        if inclpair is None: inclpair = True
        if result is None: result = self.PR.DICT
        price_g = ((
                c.cid,
                c.primaryp() if primary else c.p, 
                c.pairo.primary if primary else c.pair
            ) for c in self.curves
        )
        
        if result == self.PR.TUPLE:
            if inclpair:
                return tuple(price_g)
            else:
                return tuple(r[1] for r in price_g)
        
        if result == self.PR.DICT:
            if inclpair:
                return {r[0]: (r[1], r[2]) for r in price_g}
            else:
                return {r[0]: r[1] for r in price_g}
        
        if result == self.PR.DF:
            df = pd.DataFrame.from_records(price_g, columns=["cid", "price", "pair"])
            df = df.set_index("cid")
            return df
        raise ValueError(f"unknown result type {result}")

    def __iadd__(self, other):
        """alias for  ``self.add``"""
        return self.add(other)

    def __iter__(self):
        return iter(self.curves)

    def __len__(self):
        return len(self.curves)

    def __getitem__(self, key):
        return self.curves[key]

    def __contains__(self, curve):
        return curve in self.curveix_by_curve

    def tknq_s(self, curves=None):
        """returns ``set`` of all quote tokens (``tkny``, ``tknq``) used by the curves [API]"""
        if curves is None:
            curves = self.curves
        return {c.tkny for c in curves}
    tkny_s = tknq_s

    # def tkny_l(self, curves=None):
    #     """returns ``list`` of all quote tokens (``tkny``, ``tknq``) used by the curves [API]"""
    #     if curves is None:
    #         curves = self.curves
    #     return [c.tkny for c in curves]

    def tknb_s(self, curves=None):
        """returns ``set`` of all base tokens (``tknx``, ``tknb``) used by the curves [API]"""
        if curves is None:
            curves = self.curves
        return {c.tknx for c in curves}
    tknx_s = tknb_s

    # def tknx_l(self, curves=None):
    #     """returns ``set`` of all base tokens (``tknx``, ``tknb``) used by the curves [API]"""
    #     if curves is None:
    #         curves = self.curves
    #     return [c.tknx for c in curves]

    def tkn_s(self, curves=None):
        """
        returns ``set`` of all tokens used by the curves [API]
        """
        return self.tknx_s(curves).union(self.tkny_s(curves))
    tokens = tkn_s

    def tokens_str(self, curves=None):
        """
        returns set of all tokens used by the curves as a ``str`` [API]
        
        similar to ``tokens`` aka ``tkn_s`` but returns a string
        """
        return ",".join(sorted(self.tkn_s(curves)))

    def token_count(self, *, as_dict=False):
        """
        counts the number of times each token appears in the curves
        """
        tokens_l = (c.pair for c in self)
        tokens_l = (t.split("/") for t in tokens_l)
        tokens_l = (t for t in it.chain.from_iterable(tokens_l))
        tokens_l = list(cl.Counter([t for t in tokens_l]).items())
        tokens_l = sorted(tokens_l, key=lambda x: x[1], reverse=True)
        if not as_dict:
            return tokens_l
        return dict(tokens_l)
    
    def pairs(self, *, standardize=True):
        """
        returns ``set`` of all pairs used by the curves [API]

        :standardize:   if False, the pairs are returned as they are in the curves; eg if we have curves
                        for both ETH/USDT and USDT/ETH, both pairs will be returned; if True, only the
                        canonical pair will be returned
        """
        if standardize:
            return {c.pairo.primary for c in self}
        else:
            return {c.pair for c in self}

    def cids(self, *, as_set=False):
        """
        returns ``list`` of all curve ids [API]
        
        :returns:   ``tuple``, or ``set`` if ``as_set=True``
        """
        if as_set:
            return set(c.cid for c in self)
        return tuple(c.cid for c in self)

    @staticmethod
    def pairset(pairs):
        """converts ``str``, ``list`` or ``set`` of pairs into a ``set`` of pairs"""
        if isinstance(pairs, str):
            pairs = (p.strip() for p in pairs.split(","))
        try:
            return set(pairs)
        except:
            return set()

    def _make_symmetric(self, df):
        """
        converts ``df`` into upper triangular matrix by adding the lower triangle
        """
        df = df.copy()
        fields = df.index.union(df.columns)
        df = df.reindex(index=fields, columns=fields)
        df = df + df.T
        df = df.fillna(0).astype(int)
        return df

    class FP(Enum):
        """filter pairs mode for ``filter_pairs`` (``enum``)"""
        ANY = "any"
        ALL = "all"

    def filter_pairs(self, pairs=None, *, anyall=FP.ALL, **conditions):
        """
        filters ``pairs`` according to the target ``conditions`` [API]
        
        :pairs:         list of pairs to filter; if None, all pairs are used
        :anyall:        how conditions are combined (``FP.ANY`` or ``FP.ALL``)
        :conditions:    determines the filtering condition; all or any must be met (1, 2)


        NOTE 1: an arbitrary differentiator can be appended to the condition using "_"
        (eg ``onein_1``, ``onein_2``, ``onein_3``, ...) allowing to specify multiple conditions
        of the same type
        
        NOTE 2: see table below for conditions
                        
        =============   ========================================
        ``condition``   Description                         
        =============   ========================================
        ``bothin``      both tokens must be in the list     
        ``onein``       at least one token must be in the list
        ``notin``       none of the tokens must be in the list
        ``contains``    alias for onein                   
        ``tknbin``      tknb must be in the list            
        ``tknbnotin``   tknb must not be in the list     
        ``tknqin``      tknq must be in the list            
        ``tknqnotin``   tknq must not be in the list     
        =============   ========================================
        
        """
        if pairs is None:
            pairs = self.pairs()
        if not conditions:
            return pairs
        pairs = self.Pair.wrap(pairs)
        results = []
        for condition in conditions:
            #print(f"condition: {condition}", conditions[condition])
            cpairs = self.pairset(conditions[condition])
            condition0 = condition.split("_")[0]
            #print(f"condition: {condition} | {condition0} [{conditions[condition]}]")
            if condition0 == "bothin":
                results += [
                    {str(p) for p in pairs if p.tknb in cpairs and p.tknq in cpairs}
                ]
            elif condition0 == "contains" or condition0 == "onein":
                results += [
                    {str(p) for p in pairs if p.tknb in cpairs or p.tknq in cpairs}
                ]
            elif condition0 == "notin":
                results += [
                    {
                        str(p)
                        for p in pairs
                        if p.tknb not in cpairs and p.tknq not in cpairs
                    }
                ]
            elif condition0 == "tknbin":
                results += [{str(p) for p in pairs if p.tknb in cpairs}]
            elif condition0 == "tknbnotin":
                results += [{str(p) for p in pairs if p.tknb not in cpairs}]
            elif condition0 == "tknqin":
                results += [{str(p) for p in pairs if p.tknq in cpairs}]
            elif condition0 == "tknqnotin":
                results += [{str(p) for p in pairs if p.tknq not in cpairs}]
            else:
                raise ValueError(f"unknown condition {condition}")

        # print(f"results: {results}")
        if anyall == self.FP.ANY:
            # print(f"anyall = {anyall}: union")
            return set.union(*results)
        elif anyall == self.FP.ALL:
            # print(f"anyall = {anyall}: intersection")
            return set.intersection(*results)
        else:
            raise ValueError(f"unknown anyall {anyall}")

    def fp(self, pairs=None, **conditions):
        """alias for ``filter_pairs`` (for interactive use)"""
        return self.filter_pairs(pairs, **conditions)

    def fpb(self, bothin, pairs=None, *, anyall=FP.ALL, **conditions):
        """alias for ``filter_pairs bothin`` (for interactive use)"""
        return self.filter_pairs(
            pairs=pairs, bothin=bothin, anyall=anyall, **conditions
        )

    def fpo(self, onein, pairs=None, *, anyall=FP.ALL, **conditions):
        """alias for ``filter_pairs onein`` (for interactive use)"""
        return self.filter_pairs(pairs=pairs, onein=onein, anyall=anyall, **conditions)

    @classmethod
    def _record(cls, c=None):
        """returns the record (or headings, if none) for the pair c"""
        if not c is None:
            p = cls.Pair(c.pair)
            return (
                c.tknx,
                c.tkny,
                c.tknb,
                c.tknq,
                p.pair,
                p.primary,
                p.is_primary,
                c.p,
                p.pp(c.p),
                c.x,
                c.x_act,
                c.y,
                c.y_act,
                c.cid,
            )
        else:
            return (
                "tknx",
                "tkny",
                "tknb",
                "tknq",
                "pair",
                "primary",
                "is_primary",
                "p",
                "pp",
                "x",
                "xa",
                "y",
                "ya",
                "cid",
            )

    class AT(Enum):
        """Analysis targets for the ``pairs_analysis`` method (``enum``)"""
        LIST = "list"
        LISTDF = "listdf"
        VOLUMES = "volumes"
        #VOLUMESAGG = "vaggr"
        VOLSAGG = "vaggr"
        PIVOTXY = "pivotxy"
        PIVOTXYS = "pivotxys"
        PIVOTBQ = "pivotbq"
        PIVOTBQS = "pivotbqs"
        PRICES = "prices"
        MAX = "max"
        MIN = "min"
        SD = "std"
        SDPC = "stdpc"
        PRICELIST = "pricelist"
        #PRICELISTAGG = "plaggr"
        PLAGG = "plaggr"

    def pairs_analysis(self, *, 
                        target=None, 
                        pretty=False, 
                        pairs=None, 
                        ref_tkn=None,
                        ref_tkn_addr=None,
                        **params
        ):
        """
        returns a ``DataFrame`` with the analysis of the pairs according to the analysis target

        :target:            see table below 

        :pretty:            in some cases, returns a prettier but less useful result
        :pairs:             list of pairs to analyze; if None, all pairs
        :ref_tkn:           reference token for price calculations (1) 
        :ref_tkn_addr:      address of the reference token (default: WETH address)
        :params:            kwargs that some of the analysis targets may use

        NOTE 1. ``ref_tkn`` is either just a string with the address, or a tuple ``(address, symbol)``
        A value of ``None`` will default to ETH with the address of the WETH token
        
        ================  ===========================================
        ``target``        meaning
        ================  ===========================================
        ``AT.LIST``       ``list`` of pairs and associated data
        ``AT.LISTDF``     ditto but as a ``DataFrame``
        ``AT.VOLUMES``    ``list`` of volume per token and curve
        ``AT.VOLSAGG``    ditto but also aggregated by curve
        ``AT.PIVOTXY``    pivot table number of pairs ``tknx``/``tkny``
        ``AT.PIVOTBQ``    ditto but with ``tknb``/``tknq``
        ``AT.PIVOTXYS``   above anlysis but symmetric matrix (1)
        ``AT.PIVOTBQS``   ditto
        ``AT.PRICES``     average prices per (directed) pair
        ``AT.MAX``        ditto max
        ``AT.MIN``        ditto min
        ``AT.SD``         ditto price standard deviation
        ``AT.SDPC``       ditto percentage standard deviation
        ``AT.PRICELIST``  list of prices per curve
        ``AT.PLAGG``      list of prices aggregated by pair
        ================  ===========================================
        """
        target = target or self.AT.PIVOTBQ
        record = self._record
        cols = self._record()
        if ref_tkn is None:
            ref_tkn_name = "ETH"
            ref_tkn_addr = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
        else:
            if isinstance(ref_tkn, str):
                ref_tkn_name = "REF"
                ref_tkn_addr = ref_tkn
                
            else:
                ref_tkn_name, ref_tkn_addr = ref_tkn

        if pairs is None:
            pairs = self.pairs()
        curvedata = (record(c) for c in self.by_pairs(pairs))
        if target == self.AT.LIST:
            return tuple(curvedata)
        df = pd.DataFrame(curvedata, columns=cols)
        if target == self.AT.LISTDF:
            return df

        if target == self.AT.VOLUMES or target == self.AT.VOLSAGG:
            dfb = (
                df[["tknb", "cid", "x", "xa"]]
                .copy()
                .rename(columns={"tknb": "tkn", "x": "amtv", "xa": "amt"})
            )
            dfq = (
                df[["tknq", "cid", "y", "ya"]]
                .copy()
                .rename(columns={"tknq": "tkn", "y": "amtv", "ya": "amt"})
            )
            df1 = pd.concat([dfb, dfq], axis=0)
            df1 = df1.sort_values(["tkn", "cid"])
            if target == self.AT.VOLUMES:
                df1 = df1.set_index(["tkn", "cid"])
                df1["lvg"] = df1["amtv"] / df1["amt"]
                return df1
            df1["n"] = (1,) * len(df1)
            # df1 = df1.groupby(["tkn"]).sum()
            df1 = df1.pivot_table(
                index="tkn",
                values=["amtv", "amt", "n"],
                aggfunc={
                    "amtv": ["sum", AF.herfindahl, AF.herfindahlN],
                    "amt": ["sum", AF.herfindahl, AF.herfindahlN],
                    "n": "count",
                },
            )

            price_ref = (
                self._price(tknb=t, tknq=ref_tkn_addr) if t != ref_tkn_addr else 1 for t in df1.index
            )
            df1["price_ref"] = tuple(price_ref)
            df1["amtv_ref"] = df1[("amtv", "sum")] * df1["price_ref"]
            df1["amt_ref"] = df1[("amt", "sum")] * df1["price_ref"]
            df1["lvg"] = df1["amtv_ref"] / df1["amt_ref"]
            return df1

        if target == self.AT.PIVOTXY or target == self.AT.PIVOTXYS:
            pivot = (
                df.pivot_table(
                    index="tknx", columns="tkny", values="tknb", aggfunc="count"
                )
                .fillna(0)
                .astype(int)
            )
            if target == self.AT.PIVOTXY:
                return pivot
            return self._make_symmetric(pivot)

        if target == self.AT.PIVOTBQ or target == self.AT.PIVOTBQS:
            pivot = (
                df.pivot_table(
                    index="tknb", columns="tknq", values="tknx", aggfunc="count"
                )
                .fillna(0)
                .astype(int)
            )
            if target == self.AT.PIVOTBQ:
                if pretty:
                    return pivot.replace(0, "")
                return pivot
            pivot = self._make_symmetric(pivot)
            if pretty:
                return pivot.replace(0, "")
            return pivot

        if target == self.AT.PRICES:
            pivot = df.pivot_table(
                index="tknb", columns="tknq", values="p", aggfunc="mean"
            )
            pivot = pivot.fillna(0).astype(float)
            if pretty:
                return pivot.replace(0, "")
            return pivot

        if target == self.AT.MAX:
            pivot = df.pivot_table(
                index="tknb", columns="tknq", values="p", aggfunc=np.max
            )
            pivot = pivot.fillna(0).astype(float)
            if pretty:
                return pivot.replace(0, "")
            return pivot

        if target == self.AT.MIN:
            pivot = df.pivot_table(
                index="tknb", columns="tknq", values="p", aggfunc=np.min
            )
            pivot = pivot.fillna(0).astype(float)
            if pretty:
                return pivot.replace(0, "")
            return pivot

        if target == self.AT.SD:
            pivot = df.pivot_table(
                index="tknb", columns="tknq", values="p", aggfunc=np.std
            )
            pivot = pivot.fillna(0).astype(float)
            if pretty:
                return pivot.replace(0, "")
            return pivot

        if target == self.AT.SDPC:
            pivot = df.pivot_table(
                index="tknb", columns="tknq", values="p", aggfunc=AF.sdpc
            )
            if pretty:
                return pivot.replace(0, "")
            return pivot

        if target == self.AT.PRICELIST:
            pivot = df.pivot_table(
                index=["tknb", "tknq", "cid"],
                values=["primary", "pair", "pp", "p"],
                aggfunc={
                    "primary": AF.first,
                    "pair": AF.first,
                    "pp": "mean",
                    "p": "mean",
                },
            )
            return pivot

        if target == self.AT.PLAGG:
            aggfs = [
                "mean",
                "count",
                AF.sdpc100,
                min,
                max,
                AF.rangepc100,
                AF.herfindahl,
            ]
            pivot = df.pivot_table(
                index=["tknb", "tknq"],
                values=["primary", "pair", "pp"],
                aggfunc={"primary": AF.first, "pp": aggfs},
            )
            return pivot

        raise ValueError(f"unknown target {target}")

    def _convert(self, generator, *, as_generator=None, as_cc=None):
        """takes a generator and returns a tuple, generator or ``CurveContainer``"""
        if as_generator is None:
            as_generator = False
        if as_cc is None:
            as_cc = True
        if as_generator:
            return generator
        if as_cc:
            return self.__class__(generator, tokenscale=self.tokenscale)
        return tuple(generator)

    def curveix(self, curve):
        """returns index of curve in container"""
        return self.curveix_by_curve.get(curve, None)

    def by_cid(self, cid):
        """
        returns curve by ``cid`` [API]
        
        WARNING: THE API OF THIS FUNCTION IS NOT CURRENTLY STABLE BECAUSE SINCE WE INTRODUCED
        SUB CIDS THE CID IS NOT UNIQUE ANYMORE; EXPECT CHANGES ALONG THE LINES OF
        TODO-RELEASE
        
        - ``by_cid(cid)`` returns a ``list`` of curves
        - ``by_cid(cid, subcid)`` returns a single curve
        """
        return self.curves_by_cid.get(cid, None)
    
    def by_cids(self, include=None, *, endswith=None, exclude=None, as_generator=None, as_cc=None):
        """
        returns curves by ``cid`` patterns [API]

        :include:   iterable of cids to include, if ``None`` all cids are included; iterable
                    can also be a comma-separated string
        :endswith:  alternative to include, include all cids that end with this string
        :exclude:   iterable of cids to exclude, if ``None`` no cids are excluded
                    exclude beats include
        :returns:   ``tuple``, ``generator`` or ``CurveContainer`` object (default)
        
        SEE BY CID; EVEN THOUGH IT IS LESS OF AN ISSUE AS IN ANY CASE WE RETURN MULTIPLE CURVES
        EXPECTE THE API HERE TO REMAIN BACKWARDS COMPATIBLE BUT DO NOT RELY ON IT
        TODO-RELEASE
        """
        # converts str -> list; everything else not affected
        include = _str2list(include)
        exclude = _str2list(exclude)    
        
        if not include is None and not endswith is None:
            raise ValueError(f"include and endswith cannot be used together")
        if exclude is None:
            exclude = set()
        if include is None and endswith is None:
            result = (c for c in self if not c.cid in exclude)
        else:
            if not include is None:
                result = (self.curves_by_cid[cid] for cid in include if not cid in exclude)
            else:
                result = (c for c in self if c.cid.endswith(endswith) and not c.cid in exclude)
        return self._convert(result, as_generator=as_generator, as_cc=as_cc)
    
    def by_pair(self, pair, *, directed=False, as_generator=None, as_cc=None):
        """
        returns all curves by, possibly directed, ``pair`` [REMOVED (1)]
        
        :returns:   ``tuple``, ``generator`` or ``CurveContainer`` 
                    depending on ``as_generator`` and ``as_cc``
        
        NOTE 1. This function is redundant and has been removed; use ``by_pairs`` 
        instead which is API compatible; using this function will raise an exception
        """
        raise NotImplementedError("`by_pair` has been removed; use `by_pairs` instead which is API compatible")

    def bp(self, pair, *, directed=False, as_generator=None, as_cc=None):
        """alias for by_pairs by with directed=False for interactive use"""
        return self.by_pairs(pair, directed=directed, as_generator=as_generator, as_cc=as_cc)

    def by_pairs(self, pairs=None, *, directed=False, as_generator=None, as_cc=None):
        """
        returns all curves by, possibly directed, ``pairs`` [API]

        :pairs:     set, list or comma-separated string of pairs; if None all pairs are included
        :directed:  if True, pair direction is important (eg ETH/USDC will not return USDC/ETH
                    pairs); if False, pair direction is ignored and both will be returned
        :returns:   ``tuple``, ``generator`` or ``CurveContainer`` object (default)
        """
        pairs = _str2list(pairs)
        if pairs is None:
            result = (c for c in self)
        else:
            pairs = set(pairs)
            if not directed:
                rpairs = set(f"{q}/{b}" for b, q in (p.split("/") for p in pairs))
                # print("[CC] by_pairs: adding reverse pairs", rpairs)
                pairs = pairs.union(rpairs)
            result = (c for c in self if c.pair in pairs)
        return self._convert(result, as_generator=as_generator, as_cc=as_cc)

    def by_filtered_pairs(self, pairs=None, *, anyall=FP.ALL, **conditions):
        """
        shortcut for ``by_pairs(filter_pairs(...))`` [API]
        
        for arguments, see documentation of ``filter_pairs``
        
        The command ``curves = by_filtered_pairs(...)`` is equivalent to
        ::
            
            pairs = cc.filter_pairs(...)
            curves = cc.by_pairs(pairs)
        """
        pairs = self.filter_pairs(pairs, anyall=anyall, **conditions)
        return self.by_pairs(pairs)
    by_fp = by_filtered_pairs
    
    class OP(Enum):
        """Operators for the ``by_params`` method (``enum``)"""
        AND = 1
        OR = 2
        
    def by_params(self, *, _op=None, _as_generator=None, _as_cc=None, **params):
        """
        returns all curves by params [API]

        :_op:       the operation to be performed on multiple sets, either ``OP.AND`` 
                    or ``OP.OR``; note that if you return the curves as a container 
                    (default) then you can chain calls, effectively performing an 
                    ``AND`` operation. ``OP.AND`` is the default
        :params:    keyword arguments in the form ``param=value`` (1)
        :returns:   ``tuple``, ``generator`` or ``CurveContainer`` object (default)
        
        NOTE 1. Parameters can have have a suffix that determines how it operates
        
        =============   ========================================
        no suffix       same as ``_eq``
        ``_eq``         equal to value
        ``_ae``         approximately equal to value
        ``_ne``         not equal to value
        ``_lt``         less than value
        ``_le``         less than or equal to value
        ``_gt``         greater than value
        ``_ge``         greater than or equal to value
        ``__``          hierarchy separator
        =============   ========================================
        
        for example, ``by_params(x_ge=100)`` will return all curves with a parameter
        ``x`` greater than or equal to 100. Hierarchical parameters can be specified
        using double underscores (``__``) eg ``by_params(raw__y_gt=100)`` will return 
        all (Carbon) curves with a parameter ``y`` greater than 100.
        
        Also for the ``eq`` suffix, one can also add a single digit, eg ``eq1``; 
        this allows to check for multiple values of the same paramter. For example,
        
        ::
            
            by_params(x_eq1=100, x_eq2=200)
            
        will return all curves with a parameter ``x`` equal to 100 or 200. The ``ae``
        suffix reports equality within a relative tolerance of ``1e-9``. Obviously,
        the numbers are not allowed to be zero.
        """
        if not params:
            raise ValueError(f"no params given {params}")
        
        # for each of the parameters, create a generator of curves and store them in a list    
        generators = [self._by_param(p,v) for p,v in params.items()]
        
        if len(generators) == 1:
            
            # if there is only one generator, return it
            result = generators[0]
        
        else:
            
            # multiple generators, apply AND or OR operation; first choose operation...
            _op = _op or self.OP.AND
            if _op == self.OP.OR:
                operator = lambda x,y: x.union(y)
            elif _op == self.OP.AND:
                operator = lambda x,y: x.intersection(y)
            else:
                raise ValueError("Invalid operation {_op}; us `OP.AND` or `OP.OR`")
            
            # ...then start with the first generator, and then either union or 
            # intersect with the others incrementally
            result = set(c for c in generators[0])
            for g in generators[1:]:
                result = operator(result, set(c for c in g))
        
        return self._convert(result, as_generator=_as_generator, as_cc=_as_cc)
    
    def by_paramso(self, *, _op=None, **kwargs):
        """exactly the same as ``by_params`` with the default operation as ``OP.OR``"""
        _op = _op or self.OP.OR
        return self.by_params(_op=_op, **kwargs)
        
    _BY_PARAM_OPERATORS = dict(
        
        # strict (in)equality
        eq = _safe(lambda x, y: x == y),    # equal
        ne = _safe(lambda x, y: x != y),    # not equal
        lt = _safe(lambda x, y: x <  y),    # less than
        le = _safe(lambda x, y: x <= y),    # less than or equal
        gt = _safe(lambda x, y: x >  y),    # greater than
        ge = _safe(lambda x, y: x >= y),    # greater than or equal
        
        # approximate (in)equality
        ae = _safe(lambda x, y: abs(y/x-1) < 1e-6 if x != 0 else abs(y) < 1e-6),  
        an = _safe(lambda x, y: not(abs(y/x-1) < 1e-6 if x != 0 else abs(y) < 1e-6)), 
    )
    def _by_param(self, param, pvalue, *, roe=False, dv=None):
        """
        filters curves by a single parameter and value
        
        :param:     parameter name, plus potentially a suffix (1)
        :value:     corresponding value
        :roe:       if True, raises on error, including ``KeyError`` (2)
        :dv:        default value if parameter is not found (only relevant if ``roe`` is False) (2)
        :returns:   generator of curves
        
        NOTE 1. see docstring of ``by_params`` for more details about param syntax and suffix
        
        NOTE 2. For experimental use only; subject to removal without notice
        """
        
        # double underscores represent colons which are hierarchy separators for `P`
        param = ":".join(param.split("__"))
        
        # split the suffix from the parameter; if there is no suffix, or the suffix is invalid,
        try: 
            pname, suffix = param.rsplit("_", maxsplit=1)
            if suffix.startswith("eq"):
                # for example, if the suffix is "eq1", we convert it to "eq"
                # this allows for multiple conditions of the same type
                if len(suffix) == 3 and suffix[-1].isdigit():
                    suffix = "eq"
            operator = self._BY_PARAM_OPERATORS[suffix]
        except:
            pname, suffix = param, "eq"
            operator = self._BY_PARAM_OPERATORS["eq"]
        #print("[_by_param]", pname, suffix)
        return (c for c in self if operator(c.P(pname, dv, raiseonerror=roe), pvalue))
            
    def copy(self):
        """
        returns a copy (1) of the container [API]
        
        NOTE 1. It is only the container object that is copied. The curve objects are 
        shared between the original and the copy
        """
        return self.by_pairs(as_cc=True)

    def by_tknb(self, tknb, *, as_generator=None, as_cc=None):
        """
        returns all curves by base token ``tknb`` (``tknx``) [API]
        
        :returns:   ``tuple``, ``generator`` or ``CurveContainer`` 
                    depending on ``as_generator`` and ``as_cc``
        """
        result = (c for c in self if c.tknb == tknb)
        return self._convert(result, as_generator=as_generator, as_cc=as_cc)
    by_tknx = by_tknb

    def by_tknbs(self, tknbs=None, *, as_generator=None, as_cc=None):
        """
        returns all curves by base tokens ``tknb`` (``tknx``) [API]
        
        :returns:   ``tuple``, ``generator`` or ``CurveContainer`` 
                    depending on ``as_generator`` and ``as_cc``
        """
        if tknbs is None:
            return self.curves
        if isinstance(tknbs, str):
            tknbs = set(t.strip() for t in tknbs.split(","))
        tknbs = set(tknbs)
        result = (c for c in self if c.tknb in tknbs)
        return self._convert(result, as_generator=as_generator, as_cc=as_cc)
    by_tknxs = by_tknbs

    def by_tknq(self, tknq, *, as_generator=None, as_cc=None):
        """
        returns all curves by quote token ``tknq`` (``tkny``) [API]
        
        :returns:   ``tuple``, ``generator`` or ``CurveContainer`` 
                    depending on ``as_generator`` and ``as_cc``
        """
        result = (c for c in self if c.tknq == tknq)
        return self._convert(result, as_generator=as_generator, as_cc=as_cc)
    by_tkny = by_tknq

    def by_tknqs(self, tknqs=None, *, as_generator=None, as_cc=None):
        """
        returns all curves by quote tokens ``tknq`` (``tkny``) [API]
        
        :returns:   ``tuple``, ``generator`` or ``CurveContainer`` 
                    depending on ``as_generator`` and ``as_cc``
        """
        if tknqs is None:
            return self.curves
        if isinstance(tknqs, str):
            tknqs = set(t.strip() for t in tknqs.split(","))
        tknqs = set(tknqs)
        result = (c for c in self if c.tknq in tknqs)
        return self._convert(result, as_generator=as_generator, as_cc=as_cc)
    by_tknys = by_tknqs
    
    def by_tkn(self, tkn, *, as_generator=None, as_cc=None):
        """
        returns all curves by token, regardless whether base or quote [API]
        
        :returns:   ``tuple``, ``generator`` or ``CurveContainer`` 
                    depending on ``as_generator`` and ``as_cc``
        """
        result = (c for c in self if tkn in [c.tknb, c.tknq])
        return self._convert(result, as_generator=as_generator, as_cc=as_cc)

    def by_tkns(self, tkns=None, *, as_generator=None, as_cc=None):
        """
        returns all curves by tokens [API]
        
        :returns:   ``tuple``, ``generator`` or ``CurveContainer`` 
                    depending on ``as_generator`` and ``as_cc``
        """
        if tkns is None:
            return self.curves
        if isinstance(tkns, str):
            tkns = set(t.strip() for t in tkns.split(","))
        tkns = set(tkns)
        result = (c for c in self if (c.tknq in tkns or c.tknb in tkns))
        return self._convert(result, as_generator=as_generator, as_cc=as_cc)
    by_tknys = by_tknqs
    
    SAMPLE_N = 100
    def sample(self, n=None, *, seed=None, print_seed=False):
        """
        returns a new container based on a random sample of curves [API]
        
        :n:             number of curves to sample; if ``None``, ``SAMPLE_N`` is used
        :seed:          optional random seed for replicability
        :print_seed:    if ``True``, prints the ``seed`` used
        :returns:       new ``CurveContainer`` object
        """
        n = n or self.SAMPLE_N
        if seed:
            random.seed(seed)
        else:
            seed = self.seed()
        if print_seed:
            print(f"[sample] seed: {seed}")
        curves = random.sample(self.curves, n)
        return self.__class__(curves, tokenscale=self.tokenscale)
    
    @classmethod
    def seed(cls, maxv=int(1e9)):
        """
        convenience method to create a random seed
        
        :maxv:      maximum value for the seed (default: ``1e9``)
        
        NOTE: the purpose of this function is to create a random seed and to print it before
        using it as a seed; this is useful for replicability
        """
        return random.randint(0, maxv)

    @staticmethod
    def u(minx, maxx):
        """helper: returns uniform random var"""
        return random.uniform(minx, maxx)

    @staticmethod
    def u1():
        """helper: returns uniform [0,1] random var"""
        return random.uniform(0, 1)

    @dataclass
    class xystatsd:
        mean: any
        minv: any
        maxv: any
        sdev: any

    def xystats(self, curves=None):
        """calculates mean, min, max, stdev of x and y"""
        if curves is None:
            curves = self.curves
        tknx = {c.tknq for c in curves}
        tkny = {c.tknb for c in curves}
        assert len(tknx) != 0 and len(tkny) != 0, f"no curves found {tknx} {tkny}"
        assert (
            len(tknx) == 1 and len(tkny) == 1
        ), f"all curves must have same tknq and tknb {tknx} {tkny}"
        x = [c.x for c in curves]
        y = [c.y for c in curves]
        return (
            self.xystatsd(np.mean(x), np.min(x), np.max(x), np.std(x)),
            self.xystatsd(np.mean(y), np.min(y), np.max(y), np.std(y)),
        )

    class PE(Enum):
        """Desired result for the ``price_estimate`` method (``enum``)"""
        PAIR = "pair"
        CURVES = "curves"
        DATA = "data"

    def price_estimate(
        self, *, tknq=None, tknb=None, pair=None, result=None, raiseonerror=True, verbose=False
    ):
        """
        calculates price estimate in the reference token as base token

        :tknq:          quote token to calculate price for
        :tknb:          base token to calculate price for
        :pair:          alternative to tknq, tknb: pair to calculate price for
        :raiseonerror:  if True, raise exception if no price can be calculated
        :result:        what to return (``PE.PAIR``: slashpair, ``PE.CURVES``
                        tuple of curves, ``PE.DATA``: prices, weights)
        :verbose:       whether to print some progress
        :returns:       price (quote per base)
        """
        assert tknq is not None and tknb is not None or pair is not None, (
            f"must specify tknq, tknb or pair [{tknq}, {tknb}, {pair}]"
        )
        assert not (not tknb is None and not pair is None), f"must not specify both tknq, tknb and pair [{tknq}, {tknb}, {pair}]"
        
        if not pair is None:
            tknb, tknq = pair.split("/")
        if tknq == tknb:
            return 1
        if result == self.PE.PAIR:
            return f"{tknb}/{tknq}"
        crvs = (
            c for c in self if not c.at_boundary and c.tknq == tknq and c.tknb == tknb
        )
        rcrvs = (
            c for c in self if not c.at_boundary and c.tknb == tknq and c.tknq == tknb
        )
        crvs = ((c, c.p, c.k) for c in crvs)
        rcrvs = ((c, 1 / c.p, c.k) for c in rcrvs)
        acurves = it.chain(crvs, rcrvs)
        if result == self.PE.CURVES:
            # return dict(curves=tuple(crvs), rcurves=tuple(rcrvs))
            return tuple(acurves)
        data = tuple((r[1], sqrt(r[2])) for r in acurves)
        if verbose:
            print(f"[price_estimate] {tknq}/{tknb} {len(data)} curves")
        if not len(data) > 0:
            if raiseonerror:
                raise ValueError(f"no curves found for {tknq}/{tknb}")
            return None
        prices, weights = zip(*data)
        prices, weights = np.array(prices), np.array(weights)
        if result == self.PE.DATA:
            return prices, weights
        return float(np.average(prices, weights=weights))

    def price_estimates(
        self,
        *,
        tknqs=None,
        tknbs=None,
        triang_tokens=False,
        unwrapsingle=True,
        pairs=False,
        stopatfirst=True,
        raiseonerror=True,
        verbose=False,
    ):
        """
        calculates prices estimates in the reference token as base token

        :tknqs:             list of quote tokens to calculate prices for
        :tknbs:             list of base tokens to calculate prices for
        :triang_tokens:     tokens used as intermediate token for triangulation; 
                            if False'ish (default), no triangulation is performed
        :unwrapsingle:      if there is only one quote token, a 1-d array is returned
        :pairs:             if True, returns the slashpairs instead of the prices
        :raiseonerror:      if True, raise exception if no price can be calculated
        :stopatfirst:       it True, stop at first triangulation match
        :verbose:           if True, print some progress
        :return:            np.array of prices (quote outer, base inner; quote per base)
        """
        # NOTE: this code is relatively slow to compute, on the order of a few seconds
        # for go through the entire token list; the likely reason is that it keeps reestablishing
        # the CurveContainer objects whenever price_estimate is called; there may be a way to
        # speed this up by smartly computing the container objects once and storing them 
        # in a dictionary the is then passed to price_estimate.
        start_time = time.time()
        assert not tknqs is None, "tknqs must be set"
        assert not tknbs is None, "tknbs must be set"
        if isinstance(tknqs, str):
            tknqs = [t.strip() for t in tknqs.split(",")]
        if isinstance(tknbs, str):
            tknbs = [t.strip() for t in tknbs.split(",")]
        if verbose:
            print(f"[price_estimates] tknqs [{len(tknqs)}] = {tknqs} , tknbs [{len(tknbs)}] = {tknbs} ")
        resulttp = self.PE.PAIR if pairs else None
        result = np.array(
            [
                [
                    self.price_estimate(tknb=b, tknq=q, raiseonerror=False, result=resulttp, verbose=verbose)
                    for b in tknbs
                ] 
                for q in tknqs
            ]
        )
        #print(f"[price_estimates] PAIRS [{time.time()-start_time:.2f}s]")
        flattened = result.flatten()
        nmissing = len([r for r in flattened if r is None])
        if verbose:
            print(f"[price_estimates] pair estimates: {len(flattened)-nmissing} found, {nmissing} missing")
            if nmissing > 0 and not triang_tokens:
                print(f"[price_estimates] {nmissing} missing pairs may be triangulated, but triangulation disabled [{triangulate}]")
            if nmissing == 0 and triang_tokens:
                print(f"[price_estimates] no missing pairs, triangulation not needed")
        
        if triang_tokens and nmissing > 0:
            if isinstance(triang_tokens, str):
                triang_tokens = [t.strip() for t in triang_tokens.split(",")]
            if verbose:
                print("[price_estimates] triangulation tokens", triang_tokens)
            for ib, b in enumerate(tknbs):
                #print(f"TOKENB={b:22} [{time.time()-start_time:.4f}s]")
                for iq, q in enumerate(tknqs):
                    #print(f" TOKENQ={q:21} [{time.time()-start_time:.4f}s]")
                    if result[iq][ib] is None:
                        result1 = []
                        for tkn in triang_tokens:
                            #print(f"  TKN={tkn:23} [{time.time()-start_time:.4f}s]")
                            #print(f"[price_estimates] triangulating tknb={b} tknq={q} via {tkn}")
                            b_tkn = self.price_estimate(tknb=b, tknq=tkn, raiseonerror=False)
                            q_tkn = self.price_estimate(tknb=q, tknq=tkn, raiseonerror=False)
                            #print(f"[price_estimates] triangulating {b}/{tkn} = {b_tkn}, {q}/{tkn} = {q_tkn}")
                            if not b_tkn is None and not q_tkn is None:
                                if verbose:
                                    print(f"[price_estimates] triangulated {b}/{q} via {tkn} [={b_tkn/q_tkn}]")
                                result1 += [b_tkn / q_tkn]
                                if stopatfirst:
                                    #print(f"[price_estimates] stop at first")
                                    break
                                # else:
                                #     print(f"[price_estimates] continue {stopatfirst}")
                        result2 = np.mean(result1) if len(result1) > 0 else None
                        #print(f"[price_estimates] final result {b}/{q} = {result2} [{len(result1)}]")
                        result[iq][ib] = result2
        
        flattened = result.flatten()
        nmissing = len([r for r in flattened if r is None])
        if verbose:
            if nmissing > 0:
                missing = {
                    f"{b}/{q}"
                    for ib, b in enumerate(tknbs)
                    for iq, q in enumerate(tknqs)
                    if result[iq][ib] is None
                }
                print(f"[price_estimates] after triangulation {nmissing} missing", missing)
            else:
                print("[price_estimates] no missing pairs after triangulation")  
        if raiseonerror:
            missing = {
                f"{b}/{q}"
                for ib, b in enumerate(tknbs)
                for iq, q in enumerate(tknqs)
                if result[iq][ib] is None
            }
            # print("[price_estimates] result", result)
            if not len(missing) == 0:
                raise ValueError(f"no price found for {len(missing)} pairs", missing, result)

        #print(f"[price_estimates] DONE [{time.time()-start_time:.2f}s]")
        if unwrapsingle and len(tknqs) == 1:
            result = result[0]
        return result

    @dataclass
    class TokenTableEntry:
        """
        associates a single token with the curves on which they appear
        """

        x: list
        y: list

        def __repr__(self):
            return f"TTE(x={self.x}, y={self.y})"

        def __len__(self):
            return len(self.x) + len(self.y)

    def tokentable(self, curves=None):
        """returns dict associating tokens with the curves on which they appeay"""

        if curves is None:
            curves = self.curves

        r = (
            (
                tkn,
                self.TokenTableEntry(
                    x=[i for i, c in enumerate(curves) if c.tknb == tkn],
                    y=[i for i, c in enumerate(curves) if c.tknq == tkn],
                ),
            )
            for tkn in self.tkn_s()
        )
        r = {r[0]: r[1] for r in r if len(r[1]) > 0}
        return r

    Params = Params
    PLOTPARAMS = Params(
        printline="pair = {c.pairp}",  # print line before plotting; {pair} is replaced
        title="{c.pairp}",  # plot title; {pair} and {c} are replaced
        xlabel="{c.tknxp}",  # x axis label; ditto
        ylabel="{c.tknyp}",  # y axis label; ditto
        label="[{c.cid}-{p.exchange}]: p={c.p:.1f}, 1/p={pinv:.1f}, k={c.k:.1f}",  # label for legend; ditto
        marker="*",  # marker for plot
        plotf=dict(
            color="lightgrey", linestyle="dotted"
        ),  # additional kwargs for plot of the _f_ull curve
        plotr=dict(color="grey"),  # ditto for the _r_ange
        plotm=dict(),  # dittto for the _m_arker
        grid=True,  # plot grid if True
        legend=True,  # plot legend if True
        show=True,  # finish with plt.show() if True
        xlim=None,  # x axis limits (as tuple)
        ylim=None,  # y axis limits (as tuple)
        npoints=500,  # number of points to plot
    )

    def plot(self, *, pairs=None, directed=False, curves=None, params=None):
        """
        plots the curves in curvelist or all curves if None

        :pairs:     list of pairs to plot
        :curves:    list of curves to plot
        :directed:  if True, only plot pairs provided; otherwise plot reverse pairs as well
        :params:    plot parameters, as params struct (see PLOTPARAMS)
        """
        p = Params.new(params, defaults=self.PLOTPARAMS.params)

        if pairs is None:
            pairs = self.pairs()

        if isinstance(pairs, str):
            pairs = [pairs]  # necessary, lest we get a set of chars

        pairs = set(pairs)

        if not directed:
            rpairs = set(f"{q}/{b}" for b, q in (p.split("/") for p in pairs))
            # print("[CC] plot: adding reverse pairs", rpairs)
            pairs = pairs.union(rpairs)

        assert curves is None, "restricting curves not implemented yet"

        for pair in pairs:
            # pairp = Pair.prettify_pair(pair)
            curves = self.by_pairs(pair, directed=True, as_cc=False)
            # print("plot", pair, [c.pair for c in curves])
            if len(curves) == 0:
                continue
            if p.printline:
                print(p.printline.format(c=curves[0], p=curves[0].params))
            statx, staty = self.xystats(curves)
            #print(f"[CC::plot] stats x={statx}, y={staty}")
            xr = np.linspace(0.0000001, statx.maxv * 1.2, int(p.npoints))
            for i, c in enumerate(curves):
                # plotf is the full curve
                plt.plot(
                    xr, [c.yfromx_f(x_, ignorebounds=True) for x_ in xr], **p.plotf
                )
                # plotr is the curve with bounds
                plt.plot(xr, [c.yfromx_f(x_) for x_ in xr], **p.plotr)

            plt.gca().set_prop_cycle(None)
            for c in curves:
                # plotm are the markers
                label = (
                    None
                    if not p.label
                    else p.label.format(c=c, p=AD(dct=c.params), pinv=1 / c.p)
                )
                plt.plot(c.x, c.y, marker=p.marker, label=label, **p.plotm)

            plt.title(p.title.format(c=c, p=c.params))
            if p.xlim:
                plt.xlim(p.xlim)
            if p.ylim:
                plt.ylim(p.ylim)
            else:
                plt.ylim((0, staty.maxv * 2))
            plt.xlabel(p.xlabel.format(c=c, p=c.params))
            plt.ylabel(p.ylabel.format(c=c, p=c.params))

            if p.legend:
                if isinstance(p.legend, dict):
                    plt.legend(**p.legend)
                else:
                    plt.legend()

            if p.grid:
                if isinstance(p.grid, dict):
                    plt.grid(**p.grid)
                else:
                    plt.grid(True)

            if p.show:
                if isinstance(p.show, dict):
                    plt.show(**p.show)
                else:
                    plt.show()

    def format(self, *, heading=True, formatid=None):
        """
        returns the results in the given (printable) format

        NOTE: see docs for ``CurveContainer.print_formatted`` for details
        """
        assert len(self.curves) > 0, "no curves to print"
        s = "\n".join(c.format(formatid=formatid) for c in self.curves)
        if heading:
            s = f"{self.curves[0].format(heading=True, formatid=formatid)}\n{s}"
        return s
    
def _flatten(nested_list):
    """
    Generator for flattening a nested list
        
    :nested_list:   iterable containing elements or other iterables
    :returns:       fully flattened iterator 

    EXAMPLE

    :: 
    
        l = [1, 2, [3, (4, 5)], 6]
        lf = list(_flatten(l))
        assert lf == [1, 2, 3, 4, 5, 6]
    """
    for element in nested_list:
        try:
            # if it is iterable other than str: iterate over it...
            if isinstance(element, str):
                yield element
            else:
                yield from _flatten(element)
        except TypeError:
            # ...otherwise just yield it
            yield element

def _str2list(input):
    """
    Converts a comma separated string to a list; other inputs are returns as is
    
    :input:         comma-separated input string, or any other object
    :returns:       list obtained by splitting and stripping the input string, 
                    or the input object as is if not a string
    """
    if not isinstance(input, str):
        return input
    input = input.split(",")
    input = [i.strip() for i in input]
    return input

