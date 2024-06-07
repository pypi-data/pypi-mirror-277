"""
parsing Uniswap v2 contract values

This class converts internal Uniswap v2 contract values into values that make sense
from a financial perspective, either in Wei or in token units. It also allows to
convert Uniswap v2 contract parameters into generic constant product curve parameters
that are suitable for the Carbon ``ConstantProductCurve`` class.

---
(c) Copyright Bprotocol foundation 2023-24.
All rights reserved.
Licensed under MIT.
"""
__VERSION__ = "2.0-rc3"  # TODO-RELEASE
__DATE__ = "01/Jun/2024+"

import math as m
from dataclasses import dataclass

from .base import AdapterBase
from ..curves import ConstantProductCurve as CPC

@dataclass
class UniV2Adapter(AdapterBase):
    """
    adapter for Uniswap v3 contract values
    
    :tkn0_wei:      ``tkn0`` amount in wei units
    :tkn1_wei:      ``tkn1`` amount in wei units
    
    see ``AdapterBase`` for additional parameters
    """
    __VERSION__ = __VERSION__
    __DATE__ = __DATE__
    
    tkn0_wei: int = None
    tkn1_wei: int = None
    
    def __post_init__(self, dec_lookup=None):
        
        super().__post_init__(dec_lookup=dec_lookup)
        
        try:
            assert isinstance(self.tkn0_wei, int)
            assert isinstance(self.tkn1_wei, int)
        except AssertionError:
            raise self.ParameterError("parameters must be not `None` and of the right type", self.__dict__)

    def k(self, as_wei=False):
        r"""
        returns :math:`k = x\cdot y` in token or wei units
        
        :as_wei:    if ``True``, return as wei, else (default) in token units
        :returns:   ``k`` as ``int`` (wei) or ``float`` (token units)
        """
        k = self.tkn0_wei*self.tkn1_wei
        if as_wei: return k
        return k/10**(self.tkn0_dec+self.tkn1_dec)

    
    def kbar(self, as_wei=False):
        r"""
        returns :math:`\bar k = \sqrt{x\cdot y}` in token or wei units
        
        :as_wei:    if ``True``, return as wei, else (default) in token units
        :returns:   ``kbar`` in wei or token units, as ``float``         
        """
        return m.sqrt(self.k(as_wei=as_wei))
    
    def _amt_tkn0(self, *, as_wei=False):
        """
        returns the ``tkn0`` reserve amount in token or wei units
        
        :as_wei:        if ``True``, result in wei units, else (default) in token units
        """
        if as_wei: return self.tkn0_wei
        return self.tkn0_wei/10**self.tkn0_dec

        
    def _amt_tkn1(self, *, as_wei=False):
        """
        returns the actual ``tkn1`` reserve amount in token or wei units
        
        :as_wei:        if ``True``, result in wei units, else (default) in token units
        """
        if as_wei: return self.tkn1_wei
        return self.tkn1_wei/10**self.tkn1_dec
    
    @property
    def price_tkn1_per_tkn0(self):
        """
        returns the regular price in token units (quoted in ``tkn1`` per ``tkn0``)
        """
        return self.tkn1_wei / self.tkn0_wei * self.decf
    
    def cpc_params(self, **kwargs):
        """
        returns a ``dict`` suitable for ``ConstantProductCurve``
        
        :kwargs:        additional kwargs add to the ``dict``
        :returns:       ``dict`` suitable for ``ConstantProductCurve.from_univ2``
        """
        return dict(
            liq_tknb=self.amt_tkn0(),
            liq_tknq=self.amt_tkn1(),
            pair = self.pair,
            fee = self.fee,
            cid = self.cid,
            **kwargs,
        )
        

    def cpc(self, **kwargs):
        """
        creates a list of ``CPC`` instances from the data in this class 
        """
        return CPC.from_univ2(**self.cpc_params())
    
    @classmethod
    def from_data_v0_1_0(cls, record, dec_lookup=None, *, result=None):
        """
        creates Uniswap v2 records from ``v0.1.0`` data
        
        :data:          the Carbon v1 data ``dict`` from the system
        :returns:       ``list`` of instances
        
        EXAMPLE INPUT RECORD
        
        ::
        
            {
                'id': 'uniswapv2-ethereum-8',
                'exchange_type': 3,
                'exchange_name': 'uniswap_v3',
                'fee': 3000,
                'pair': [
                    '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48',
                    '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
                ],
                'native': {
                    'liq_tkn0': '123876559918',
                    'liq_tkn1': '39665706051873202176',
                }
            }
        """
        result = result or cls.RESULT.RESULT
        assert isinstance(result, cls.RESULT), f"result must be a {cls.RESULT} enum {result}"
        
        rn = record['native']
        pair = record['pair']
        data = dict(
            cid = record['id'],
            tkn0 = pair[0],
            tkn1 = pair[1],
            fee_cbp = record['fee'],
            tkn0_wei = int(rn["liq_tkn0"]),
            tkn1_wei = int(rn["liq_tkn1"]),
            #dec_lookup = {k:v for k,v in dec_lookup.items() if k in pair},
            dec_lookup = dec_lookup,
        )
        if result == cls.RESULT.RAW:
            return data
        return [cls(**data)]
    from_data = from_data_v0_1_0