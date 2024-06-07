"""
parsing Carbon v1 contract values

This class converts internal Carbon v1 contract values into values that make sense
from a financial perspective, either in Wei or in token units. It also allows to
convert Carbon v1 contract parameters into generic constant product curve parameters
that are suitable for the Carbon ``ConstantProductCurve`` class.

---
(c) Copyright Bprotocol foundation 2023-24.
All rights reserved.
Licensed under MIT.
"""
__VERSION__ = "2.0-rc3"  # TODO-RELEASE
__DATE__ = "01/Jun/2024+"

from math import sqrt
from dataclasses import dataclass

from .base import AdapterBase
from .carbon_encoded_order import EncodedOrder as CarbonEncodedOrder
from ..curves import ConstantProductCurve as CPC

@dataclass
class CarbonV1Adapter(AdapterBase):
    """
    adapter for CarbonV1 contract values
    
    :tkny:       the token on the Carbon y axis, ie the token being sold (1) 
    :y_wei:      number of tokens to sell on the curve (in token wei)
    :z_wei:      curve capacity, as token wei
    :A_enc:      curve parameter A, multiplied by ``ONE``, encoded
    :B_enc:      curve parameter B, multiplied by ``ONE``, encoded
    
    see ``AdapterBase`` for additional parameters
    
    NOTE 1. Carbon curves always place the token being sold on the y axis; this can be confusing
    because there is no longer a fixed relationship between ``tknb``, ``tknq`` and ``tkny``.
    Specifically, as Carbon strategies typically contain a buy and a sell curve for the same
    token pair, every carbon strategy contains two curves where ``tkny`` represents different
    tokens.

    """
    __VERSION__ = __VERSION__
    __DATE__ = __DATE__
    
    tkny: str = None
    y_wei: int = None
    z_wei: int = None
    A_enc: int = None
    B_enc: int = None

            
        
    ONE = CarbonEncodedOrder.ONE # 2**48
    
    def __post_init__(self, dec_lookup=None):
        
        super().__post_init__(dec_lookup)
        
        try:
            assert isinstance(self.tkny, str)
            assert isinstance(self.y_wei, int)
            assert isinstance(self.z_wei, int)
            assert isinstance(self.A_enc, int)
            assert isinstance(self.B_enc, int)
        except AssertionError:
            raise self.ParameterError("parameters must be not `None` and of the right type", self.__dict__)

        if self.tkny != self.tkn0 and self.tkny != self.tkn1:
            raise self.ParameterError(f"`tkny` ({self.tkny}) must be either `tkn0` ({self.tkn0}) or `tkn1` ({self.tkn1})", self.__dict__)
        
        self._encoder = CarbonEncodedOrder(token=self.tkny, y=self.y_wei, z=self.z_wei, A=self.A_enc, B=self.B_enc)
        self._decoded = self._encoder.decoded
        
    @property
    def d(self):
        """
        returns the decoded order, as dataclass
        
        NOTE: this is the cached result of ``CarbonEncodedOrder.decoded``
        """
        return self._decoded
    
    def y(self, as_wei=False):
        """
        curve parameter ``y``
        
        :as_wei:    if ``True``, returns the value in wei, else (default) in token units
        """
        if as_wei: return self.d.y  
        if self.sells_tkn0:
            return self.d.y/10**self.tkn0_dec
        else:
            return self.d.y/10**self.tkn1_dec
    
    def y_int(self, as_wei=False):
        """
        curve parameter ``y_int``, alias for ``z``
        
        :as_wei:    if ``True``, returns the value in wei, else (default) in token units
        """
        if as_wei: return self.d.z
        if self.sells_tkn0:
            return self.d.z/10**self.tkn0_dec
        else:
            return self.d.z/10**self.tkn1_dec
    
    def A(self, as_wei=False):
        """
        curve parameter A as ``float``
        
        :as_wei:    if ``True``, returns the value in wei, else (default) in token units
        """
        if as_wei: return self.d.A
        if self.sells_tkn0:
            return self.d.A / sqrt(self.dec_factor_wei0_per_wei1)
        else:
            return self.d.A * sqrt(self.dec_factor_wei0_per_wei1)
    
    def B(self, as_wei=False):
        """
        curve parameter B as ``float``
        
        :as_wei:    if ``True``, returns the value in wei, else (default) in token units
        """
        if as_wei: return self.d.B
        if self.sells_tkn0:
            return self.d.B / sqrt(self.dec_factor_wei0_per_wei1)
        else:
            return self.d.B * sqrt(self.dec_factor_wei0_per_wei1)
        
    def pA(self, as_wei=False):
        """
        curve parameter ``pA = (A+B)**2``
        
        :as_wei:    if ``True``, returns the value in wei, else (default) in token units
        """
        x = self.A(as_wei) + self.B(as_wei)
        return x*x
    
    def pB(self, as_wei=False):
        """
        curve parameter ``pB = B**2``
        
        :as_wei:    if ``True``, returns the value in wei, else (default) in token units
        """
        x = self.B(as_wei)
        return x*x
    
    @property
    def sells_tkn0(self):
        """
        ``True`` iff the curve sells ``tkn0`` (otherwise it sells ``tkn1``)
        
        NOTE: single Carbon curves ("orders") are uni-directional and therefore only ever
        sell (and hold) on token of the pair. A Carbon strategy typically consists of two
        curves, one for each direction.
        """
        return self.tkny == self.tkn0
    
    @property
    def descr(self):
        """returns the description from the encoder"""
        return self._encoder.descr
    
    def _amt_tkn0(self, *, as_wei=False):
        if self.sells_tkn0:
            return self.y(as_wei)
        else:
            return 0
    
    def _amt_tkn1(self, *, as_wei=False):
        if self.sells_tkn0:
            return 0
        else:
            return self.y(as_wei)
    
    def cpc_params(self, **kwargs):
        """
        returns a ``dict`` suitable for ``ConstantProductCurve``
        
        :kwargs:        additional kwargs add to the ``dict``
        :returns:       ``dict`` suitable for ``ConstantProductCurve.from_carbonv1``
        """
        return dict(
            cid = self.cid,
            tkny = self.tkny,
            y = self.y(),
            yint = self.y_int(),
            A = self.A(),
            B = self.B(),
            pair = self.pair,
            fee = self.fee,
            **kwargs,
        )
        
    def cpc(self, **kwargs):
        """
        creates a list of ``CPC`` instances from the data in this class 
        """
        return CPC.from_carbonv1(**self.cpc_params())
    
    def k(self, *, as_wei=False):
        raise NotImplementedError("not implemented for Carbon v1")
    
    def kbar(self, *, as_wei=False):
        raise NotImplementedError("not implemented for Carbon v1")
    
    def price_tkn1_per_tkn0(self, *, as_wei=False):
        raise NotImplementedError("not implemented for Carbon v1")


    @classmethod
    def from_data_v0_1_0(cls, record, dec_lookup=None, *, result=None):
        """
        creates Carbon records from ``v0.1.0`` data
        
        :data:          the Carbon v1 data ``dict`` from the system
        :returns:       ``list`` of instances
        
        EXAMPLE INPUT RECORD
        
        ::
        
            {
                'id': 'carbon-ethereum-14',
                'exchange_type': 6,
                'exchange_name': 'carbon_v1',
                'fee': 2000,
                'pair': [
                    '0xf04a8ac553FceDB5BA99A64799155826C136b0Be',
                    '0xdAC17F958D2ee523a2206206994597C13D831ec7'
                ],
                'strategyId': '103786121910886231356329255266689304494929',
                'native': {
                    'y_0': '926400260440038489828145',
                    'y_1': '5957',
                    'z_0': '926400260440038489828145',
                    'z_1': '3000000000',
                    'A_0': '6701695110995569',
                    'A_1': '8103120',
                    'B_0': '6404666349060909',
                    'B_1': '19903286'}
            }
        """
        #print("dec_lookup", dec_lookup)
        result = result or cls.RESULT.RESULT
        assert isinstance(result, cls.RESULT), f"result must be a {cls.RESULT} enum {result}"
        
        rn = record['native']
        pair = record['pair']
        data1 = dict(
            cid = record['id'],
            tkn0 = pair[0],
            tkn1 = pair[1],
            fee_cbp = record['fee'],
            #dec_lookup = {k:v for k,v in dec_lookup.items() if k in pair},
            dec_lookup = dec_lookup,
        )
        data2 = {
            ix: {_FIELDNM[k]: int(rn[f"{k}_{ix}"]) for k in "yzAB"}
            for ix in (0, 1)
        }
        if result == cls.RESULT.RAW:
            return {**data1, **data2}
        result = [
            cls(**{**data1, **d, "tkny":pair[ix]})
            for ix, d in data2.items()
        ]
        return result
    from_data = from_data_v0_1_0
    
    

_FIELDNM = dict(
    y = "y_wei",
    z = "z_wei",
    A = "A_enc",
    B = "B_enc",
)     
    