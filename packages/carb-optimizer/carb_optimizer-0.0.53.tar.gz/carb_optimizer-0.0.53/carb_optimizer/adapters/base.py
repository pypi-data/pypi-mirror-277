"""
abstract base class for adapters

Adapters convert blockchain data into a format that is suitable for the ``ConstantProductCurve`` class. 
Currently the following adapters are available:

- ``UniV2Adapter``: for Uniswap V2 and related
- ``UniV3Adapter``: for Uniswap V3 and related
- ``CarbonAdapter``: for Carbon and releated

---
(c) Copyright Bprotocol foundation 2023-24.
All rights reserved.
Licensed under MIT.
"""
__VERSION__ = "1.0-beta2" 
__DATE__ = "14/May/2024"

from abc import ABC, abstractmethod
from dataclasses import dataclass, InitVar
from enum import Enum
from ..helpers.dcbase import DCBase

@dataclass
class AdapterBase(ABC, DCBase):
    """
    adapter base class
    
    :tkn0:          Token 0 (address, symbol, or identifier)
    :tkn1:          ditto Token 1
    :tkn0_dec:      Token 0 decimals (1)
    :tkn1_dec:      Token 1 decimals (1)
    :fee_cbp:       fee in 0.01 basis point (``int``) 
    :dec_lookup:    Decimals lookup ``dict`` (1)
    
    NOTE. All parameters must be provided as keyword arguments.
    
    NOTE 1. The token decimals can either be provided as parameters ``tkn0_dec, tkn1_dec`` or 
    a lookup dict can be provided that allows looking up the decimals from the ``tkn0``, ``tkn1``.
    If decimals cannot be found, a ``DecimalsMissingError`` exception is raised. The lookup dict
    keys must all be lowercase.
    """  
    __VERSION__ = __VERSION__
    __DATE__ = __DATE__
    
    tkn0: str
    tkn1: str
    tkn0_dec: int = None
    tkn1_dec: int = None
    fee_cbp: int = None
    dec_lookup: InitVar[dict] = None
    cid: str = None
    
    def __post_init__(self, dec_lookup=None):
        
        #print("dec_lookup", dec_lookup)
        dec_lookup = dec_lookup or {}
        
        if self.tkn0_dec is None:
            try: 
                self.tkn0_dec = dec_lookup[self.tkn0]
            except KeyError:
                try:
                    self.tkn0_dec = dec_lookup[self.tkn0.lower()]
                except KeyError:
                    #print("dec_lookup", dec_lookup)
                    raise self.DecimalsMissingError(f"must provide tkn0_dec for {self.tkn0}", dec_lookup)

        if self.tkn1_dec is None:
            try:
                self.tkn1_dec = dec_lookup[self.tkn1]
            except KeyError:
                try:
                    self.tkn1_dec = dec_lookup[self.tkn1.lower()]
                except KeyError:
                    raise self.DecimalsMissingError(f"must provide tkn1_dec for {self.tkn1}", dec_lookup)
        
        if self.fee_cbp is None:
            self.fee_cbp = 0
            
        try:
            assert isinstance(self.tkn0_dec, int)
            assert isinstance(self.tkn1_dec, int)
            assert isinstance(self.fee_cbp, int)
        except AssertionError:
            raise self.ParameterError("parameters must be integers", self.__dict__)

    class AdapterError(Exception):
        """base class for adapter errors"""
        pass
    
    class DecimalsMissingError(AdapterError): 
        """token decimals are missing and cannot be implied"""
        pass
    
    class ParameterError(AdapterError):
        """paramters are missing or invalid"""
        pass
    
    @property
    def pair(self):
        """
        the directed pair ``tkn0/tkn1`` (1)
        
        NOTE 1. ``tkn0`` is the base token, ``tkn1`` is the quote token
        """
        return f"{self.tkn0}/{self.tkn1}"
    
    @property
    def fee_bp(self):
        """
        fee in basis points as ``float``; eg ``1.5`` for ``0.015%`` fee 
        """
        return self.fee_cbp/100
    
    @property
    def fee(self):
        """
        fee; eg ``0.01`` for ``1%`` fee
        """
        return self.fee_bp/10_000  
    
    @property
    def dec_factor_wei0_per_wei1(self):
        r"""
        token wei of ``tkn0`` per token wei of ``tkn1`` at price=1 ("decimals factor")
        
        .. math::
        
            \mathrm{decf} = 10^{d_0-d_1}
        
        where :math:`d_0, d_1` are the decimals of ``tkn0`` and ``tkn1`` respectively
        """
        return 10**(self.tkn0_dec-self.tkn1_dec)
    decf = dec_factor_wei0_per_wei1
    
    @property
    def p_convention(self):
        """
        returns price convention of the regular prices (``p``, ``Pa``, ``Pb``)
            
        :returns:   "``tkn1`` per ``tkn0``" as ``str``
        """
        return f"{self.tkn1} per {self.tkn0}"
    
    @property
    def price_tkn0_per_tkn1(self):
        """
        returns the inverse price in token units (quoted in ``tkn0`` per ``tkn1``)
        
        NOTE: this function simply calls ``self.price_tkn1_per_tkn0``; do not modify
        """
        return 1/self.price_tkn1_per_tkn0
    
    @property
    def p(self):
        """
        returns the regular price in token units (quoted in ``tkn1`` per ``tkn0``)
        
        NOTE: this function is an alias for ``self.price_tkn1_per_tkn0``; do not modify
        """
        return self.price_tkn1_per_tkn0
    
    @property
    @abstractmethod
    def price_tkn1_per_tkn0(self):
        """
        returns the regular price in token units (quoted in ``tkn1`` per ``tkn0``)
        
        NOTE: this function must be overridden in the derived class; the functions
        ``price_tkn0_per_tkn1`` and ``p`` will then be automatically defined
        """
        pass
    
    @abstractmethod
    def k(*, as_wei=False):
        r"""
        the pool invariant ``k``
        
        :as_wei:    if ``True``, return as wei, else (default) in token units
        
        For constant product pools the pool invariant ``k`` is the product of the token balances:
        
        .. math::
        
            k = x\cdot y
        
        """
        pass
    
    @abstractmethod
    def kbar(*, as_wei=False):
        r"""
        the pool invariant ``kbar``
        
        :as_wei:    if ``True``, return as wei, else (default) in token units
        
        For constant product pools the pool invariant is the square root of the product 
        of the token balances:
        
        .. math::
        
            \bar k = \sqrt{k} = \sqrt{x\cdot y}
        
        It has nicer scaling properties than the standard pool invariant ``k``.
        
        """
        pass
    
    @abstractmethod
    def cpc_params(self, **kwargs):
        """
        returns a ``dict`` suitable for ``ConstantProductCurve`` constructors
        
        :kwargs:    additional kwargs add to the ``dict``
        :returns:   ``dict`` suitable for ``ConstantProductCurve.from_xxx`` (1)
        
        NOTE 1. Different adapters may link into different curve constructors.
        """
        pass
    
    @abstractmethod
    def cpc(self, **kwargs):
        """
        returns a ``ConstantProductCurve`` instance
        
        :kwargs:    additional kwargs for the ``CPC`` constructor
        :returns:   ``list`` of ``CPC`` instances
        """
        pass

    class RESULT(Enum):
        RESULT = 0
        RAW = 1
    
    @classmethod
    def create_curve(cls, record, dec_lookup=None):
        """
        creates curves directly from a record with persistent class instance (1)
        
        :record:        the data record ``dict`` from the system
        :dec_lookup:    a ``dict`` with token decimals, extracted from the system data 
                        using the ``Token`` class
        :returns:       ``list`` of curves (2)
        
        NOTE 1. This method call ``self.cpc`` which at this level is a and abstract method
        and must be implemented in the derived class 
        
        NOTE 2. Usually this method will return a list containing exactly one curve; however,
        eg Carbon curves are instantiated in pairs, one for each direction.
        """
        adapters = cls.from_data(record, dec_lookup)
        nested_l = [a.cpc() for a in adapters]
        flat_l   = [crv for sub_l in nested_l for crv in sub_l]
        return flat_l 
    
    def amt_tkn0(self, *, as_wei=False, incl_token=False):
        """
        returns the actual ``tkn0`` reserve amount in token or wei units
        
        :as_wei:        if ``True``, result in wei units, else (default) in token units
        :incl_token:    if ``True``, returns a tuple ``(amt, token)``, else (default) ``amt``
        
        NOTE: this function calls ``_amt_tkn0`` which needs to be implemented in the derived 
        class; do not modify this function
        """
        amt = self._amt_tkn0(as_wei=as_wei)
        if not incl_token: return amt
        return (amt, self.tkn0 + (" wei" if as_wei else ""))
    
    def amt_tkn1(self, *, as_wei=False, incl_token=False):
        """
        returns the actual ``tkn1`` reserve amount in token or wei units
        
        :as_wei:        if ``True``, result in wei units, else (default) in token units
        :incl_token:    if ``True``, returns a tuple ``(amt, token)``, else (default) ``amt``
        
        NOTE: this function calls ``_amt_tkn1`` which needs to be implemented in the derived 
        class; do not modify this function
        """
        amt = self._amt_tkn1(as_wei=as_wei)
        if not incl_token: return amt
        return (amt, self.tkn1 + (" wei" if as_wei else ""))
    
    @abstractmethod   
    def _amt_tkn0(self, *, as_wei=False):
        """
        returns the actual ``tkn0`` reserve amount in token or wei units
        
        :as_wei:        if ``True``, result in wei units, else (default) in token units
        """
        pass
    
    @abstractmethod   
    def _amt_tkn1(self, *, as_wei=False):
        """
        returns the actual ``tkn1`` reserve amount in token or wei units
        
        :as_wei:        if ``True``, result in wei units, else (default) in token units
        """
        pass
    
class _TestAdapter(AdapterBase):
    """``AdapterBase`` with all abstract methods stubbed out; for testing only"""
    def k(x): 
        pass
    
    def kbar(x): 
        pass
    
    @classmethod
    def cpc_params(cls, **x): 
        pass
    
    @classmethod
    def cpc(cls, **x): 
        pass
    
    @property
    def price_tkn1_per_tkn0(self): 
        pass
    
    def _amt_tkn0(x): 
        pass
    
    def _amt_tkn1(x): 
        pass