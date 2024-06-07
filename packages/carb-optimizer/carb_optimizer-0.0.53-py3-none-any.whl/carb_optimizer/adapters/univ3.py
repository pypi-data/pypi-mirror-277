"""
parsing Uniswap v3 contract values

This class converts internal Uniswap v3 contract values into values that make sense
from a financial perspective, either in Wei or in token units. It also allows to
convert Uniswap v3 contract parameters into generic constant product curve parameters
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
from ..curves import ConstantProductCurve as CPC

# tick spacing as function of fee (fee in 0.01 basis points)
_TICKSP = {
    1: 1,
    8: 1,
    10: 1,
    40: 8,
    80: 1,
    100: 1,
    250: 5,
    300: 60,
    450: 10,
    500: 10,
    1000: 200,
    2500: 50,
    3000: 60,
    10000: 200,
}

@dataclass
class UniV3Adapter(AdapterBase):
    """
    adapter for Uniswap v3 contract values
    
    :sp96:          Uniswap v3 parameters (sqrt price in Q96)
    :tick:          tick value of the range
    :liquidity:     Uniswap v3 ``L`` parameter
    :ticksp:        tick spacing; usually looked up as ``TICKSP[fee_cbp]``

    
    see ``AdapterBase`` for additional parameters

    """
    __VERSION__ = __VERSION__
    __DATE__ = __DATE__
    
    sp96: int = None # sqrt_price_q96
    tick: int = None
    liquidity: int = None
    ticksp: int = None 

    TICKSP = _TICKSP
    Q96 = 2**96
    Q192 = 2**192
    
    def __post_init__(self, dec_lookup=None):
        
        super().__post_init__(dec_lookup=dec_lookup)
        
        if self.ticksp is None:
            try:
                self.ticksp = self.TICKSP[self.fee_cbp]
            except KeyError:
                raise self.ParameterError(f"fee_cbp {self.fee_cbp} not found in TICKSP", self.__dict__)
            
        try:
            assert isinstance(self.sp96, int)
            assert isinstance(self.tick, int)
            assert isinstance(self.liquidity, int)
            assert isinstance(self.ticksp, int)
            assert isinstance(self.fee_cbp, int)
        except AssertionError:
            raise self.ParameterError("parameters must be not `None` and of the right type", self.__dict__)

    @classmethod
    def from_dict(cls, d, *, dec_lookup=None, tkn0_dec=None, tkn1_dec=None):
        """
        alternative constructor from a ``dict`` (and additional parameters)
        
        :d:             ``dict`` with keys ``token0``, ``token1``, ``sqrt_price_q96``, ``tick``, 
                        ``tick_spacing``, ``liquidity``, ``fee_cbp``
        :tkn0_dec:      optional token0 decimals value (eg 6, 18)
        :tkn1_dec:      optional token1 decimals value (eg 6, 18)
        :dec_lookup:    optional dictionary of token address to decimals (eg {"0x123...": 18})
        
        EXAMPLE INPUT RECORD
        
        ::
        
            curve_data = {
                'token0': 'SOCKS',
                'token1': 'WETH',
                'sqrt_price_q96': 359531392686823136782270075879,
                'tick': 30250,
                'tick_spacing': 60,
                'liquidity': 143364393559918602,
                'fee_cbp': 3000
            }
        
        
        """
        return cls(
            tkn0 = d["token0"],
            tkn1 = d["token1"],
            sp96 = d["sqrt_price_q96"],
            tick = d["tick"],
            ticksp = d["tick_spacing"],
            liquidity = d["liquidity"],
            fee_cbp = d["fee_cbp"],
            dec_lookup = dec_lookup,
            tkn0_dec = tkn0_dec,
            tkn1_dec = tkn1_dec,
        )

    @classmethod
    def from_bot(cls, botdata, dec_lookup):
        """
        alternative constructor the bot data ``dict``
        
        :botdata:       bot data dictionary
        :dec_lookup:    dictionary of token identifier (eg, address) to decimals
        
        The ``botdata`` format is as in the example below
        ::
        
            botdata = [{
                'id': 'uniswapv3-ethereum-3',
                'exchange_type': 'uniswap_v3',
                'exchange_name': 'uniswap_v3',
                'fee': 10000,
                'pair': ['USDC', 'WETH'],
                'native': {
                    'liquidity': '167100867368302576',
                    'sqrt_price_q96': '1433586986662264995872928531337282',
                    'tick': 196076,
                    'tick_spacing': 200
                }
            }]
            
        In this case the minimum working ``dec_lookup`` would be
        
        ::
            
            dec_lookup = {
                'USDC': 6,
                'WETH': 18,
            }
        """
        return cls(
            tkn0 = botdata["pair"][0],
            tkn1 = botdata["pair"][1],
            sp96 = int(botdata["native"]["sqrt_price_q96"]),
            tick = botdata["native"]["tick"],
            ticksp = botdata["native"]["tick_spacing"],
            liquidity = int(botdata["native"]["liquidity"]),
            fee_cbp = botdata["fee"],
            dec_lookup = dec_lookup,
        )

    @property
    def tickab(self):
        r"""
        returns the tick values of Pa and Pb
        
        .. math::
            
                \mathrm{tick_a} \simeq \mathrm{tick},\ \mathrm{tick_b} = \mathrm{tick_a} + \mathrm{ticksp}
        
        Note: ``tick_a`` is ``tick`` snapped to close ``ticksp`` value
        """
        ticka = (self.tick // self.ticksp) * self.ticksp
        return ticka, ticka + self.ticksp
    
    @property
    def papb_wei(self):
        r"""
        ``Paw`` and ``Pbw`` values, as wei prices ``tkn1`` per ``tkn0``
        
        :returns:  ``(Paw, Pbw)`` as ``tuple`` (wei units, ``tkn1`` per ``tkn0``)
        
        .. math::
        
            P_{(a,b)w} = 1.0001^{\mathrm{tick_{a,b}}}
        """
        ta, tb = self.tickab
        return (1.0001**ta, 1.0001**tb)
    
    @property
    def papb_tkn1_per_tkn0(self):
        r"""
        ``Pa`` and ``Pb`` values, in units of ``tkn1`` per ``tkn0``
        
        :returns:   ``(Pa, Pb)`` as ``tuple`` (token units, ``tkn1`` per ``tkn0``)
        
        .. math::
            
            P_{(a,b)} = P_{(a,b)w} \times \mathrm{decf} = P_{(a,b)w} \times 10^{d_0-d_1}
        """
        par,pbr = self.papb_wei
        return (par*self.decf, pbr*self.decf) 
    papb = papb_tkn1_per_tkn0

    # @property
    # def papb_tkn0_per_tkn1(self):
    #     """
    #     ``Pa`` and ``Pb`` values in units of ``tkn0`` per ``tkn1``
    #     """
    #     pa,pb = self.papb_tkn1_per_tkn0
    #     return (1/pa, 1/pb)
    
    @classmethod
    def price_wei(cls, sp96):
        r"""
        price ``tkn1`` per ``tkn0`` in wei units
        
        :sp96:      sqrt wei price ``tkn1`` per ``tkn0`` in Q96
        
        .. math::
        
            P_{w} = \frac{\mathrm{sp96}^2}{\mathrm{Q192}}
            
        where :math:`\mathrm{Q192} = 2^{192}, \mathrm{Q96} = 2^{96}`
        
        """
        return sp96 ** 2 / cls.Q192
    
    @property
    def price_tkn1_per_tkn0(self):
        """
        returns the regular price in token units (quoted in ``tkn1`` per ``tkn0``)
        """
        return self.price_wei(self.sp96) * self.decf
    
    @classmethod
    def sp96_from_price_wei(cls, price_wei):
        r"""
        calculates ``sp96`` from a wei price ``Pw``
        
        :price_wei:     price in wei units, ``tkn1`` per ``tkn0``
        
        NOTE: the result is returned as ``int`` but the calculation goes via ``float`` for 
        the square root so some precision may be lost.
        
        .. math::
        
            \mathrm{sp96} = \sqrt{P_w} * Q96
            
        where :math:`\mathrm{Q96} = 2^{96}`
        """
        return int(sqrt(price_wei * cls.Q96**2)) 
    
    @property
    def L_wei(self):
        r"""
        Uniswap  ``L`` in wei units (as ``int``)
        
        NOTE: Uniswap :math:`L` is equivalent to Carbon :math:`\bar k`
        """
        return self.liquidity
    
    @property
    def L2_wei(self):
        r"""
        Uniswap  ``L-squared`` in wei units (as ``int``)
        
        NOTE: Uniswap :math:`L^2` is equivalent to Carbon :math:`k`
        """
        return self.L_wei**2
    
    def L(self, as_wei=False):
        """Uniswap  ``L`` in ``wei`` (int) or token (``float``; default) units"""
        if as_wei: return self.L_wei
        return self.L_wei/10**(0.5*(self.tkn0_dec+self.tkn1_dec))

    def k(self, as_wei=False):
        r"""
        returns :math:`k = x\cdot y` (Uniswap ``L^2``) in token or wei units
        
        :as_wei:    if ``True``, return as wei, else (default) in token units
        :returns:   ``k`` as ``int`` (wei) or ``float`` (token units)
        
        .. math::
        
            k = x\cdot y = L^2
        """
        kbar = self.kbar(as_wei=as_wei)
        return kbar**2
    
    def kbar(self, as_wei=False):
        r"""
        returns :math:`\bar k = \sqrt{x\cdot y}` (Uniswap ``L``) in token or wei units
        
        :as_wei:    if ``True``, return as wei, else (default) in token units
        :returns:   ``kbar`` as ``int`` (wei) or ``float`` (token units)
        
        .. math::
        
            \bar k = \sqrt{k} = \sqrt{x\cdot y} = L 
            
        """
        return self.L(as_wei=as_wei)
        # kbar_wei = self.L_wei
        # if as_wei: return kbar_wei
        # return kbar_wei/10**(0.5*(self.tkn0_dec+self.tkn1_dec))
    
    def _amt_tkn0(self, *, as_wei=False):
        """
        returns the actual ``tkn0`` reserve amount in token or wei units
        
        :as_wei:        if ``True``, result in wei units, else (default) in token units
        """
        _, pb = self.papb
        sqrtPb = sqrt(pb)
        sqrtP = sqrt(self.p)
        amt_tkn0 = self.liquidity * (sqrtPb - sqrtP) / (sqrtP * sqrtPb) if (sqrtP * sqrtPb)!=0 else 0
        amt_tkn0 *= self.decf # <<<< TODO: IS THIS CORRECT? apparently so...
        if as_wei:
            amt_tkn0 *= 10**self.tkn0_dec
        return amt_tkn0
        
    def _amt_tkn1(self, *, as_wei=False):
        """
        returns the actual ``tkn1`` reserve amount in token or wei units
        
        :as_wei:        if ``True``, result in wei units, else (default) in token units
        """
        pa, _ = self.papb
        sqrtPa = sqrt(pa)
        sqrtP = sqrt(self.p)
        amt_tkn1 = self.liquidity * (sqrtP - sqrtPa)
        amt_tkn1 *= self.decf # <<<< TODO: IS THIS CORRECT? apparently so...
        if as_wei:
            amt_tkn1 *= 10**self.tkn1_dec
        return amt_tkn1
        
    # def tvl(self, *, astkn0=False, incl_token=False):
    #     """
    #     returns the total value locked in the pool
        
    #     :astkn0:        if ``True``, returns the TVL in ``tkn0`` units, else (default) in ``tkn1`` units
    #     :incl_token:    if ``True``, returns a tuple ``(TVL, token)``, else just the TVL
        
    #     NOTE: it seems this liquidity is wei liquidity (!) TODO
    #     """
    #     amt_tkn0, amt_tkn1 = self.amt_tkn0(), self.amt_tkn1()
    #     tvl_tkn0 = amt_tkn0 + amt_tkn1*self.price_tkn0_per_tkn1
    #     tvl = tvl_tkn0 if astkn0 else tvl_tkn0*self.price_tkn1_per_tkn0
    #     if not incl_token:
    #         return tvl
    #     return (tvl, self.tkn0 if astkn0 else self.tkn1)
    
    def cpc_params(self, **kwargs):
        """
        returns a ``dict`` suitable for ``ConstantProductCurve``
        
        :kwargs:        additional kwargs add to the ``dict``
        :returns:       ``dict`` suitable for ``ConstantProductCurve.from_univ3``
        """
        pa,pb = self.papb
        pm = self.p
        pmar = pm/pa - 1
        pmbr = pm/pb - 1
        #print("[cpc_params]", pa, pm, pb, pmar, pmbr)
        if pmar < 0:
            #print("[cpc_params] pmar<0; asserting just rounding", pa, pm, pmar)
            assert pmar > -1e-10, f"pm below pa beyond rounding error [{pm}, {pa}, {pmar}]"
        if abs(pmar)<1e-10:
            #print("[cpc_params] setting pm to pa", pa, pm, pmar)
            pm = pa
        
        if pmbr < 0:
            #print("[cpc_params] pmbr>0; asserting just rounding", pm, pb, pmbr)
            assert pmbr < 1e-10, f"pm abve pb beyond rounding error [{pm}, {pb}, {pmbr}]"
        if abs(pmbr)<1e-10:
            #print("[cpc_params] setting pm to pb", pm, pb, pmbr)
            pm = pb
            
        return dict(
            cid = self.cid,
            Pmarg = pm,
            uniL = self.L(),
            uniPa = pa,
            uniPb = pb,
            pair = self.pair,
            fee = self.fee,
            **kwargs,
        )
    
    def cpc(self, **kwargs):
        """
        creates a list of ``CPC`` instances from the data in this class 
        """
        return CPC.from_univ3(**self.cpc_params())
    
    @classmethod
    def from_data_v0_1_0(cls, record, dec_lookup=None, *, result=None):
        """
        creates Uniswap v3 records from ``v0.1.0`` data
        
        :data:          the Carbon v1 data ``dict`` from the system
        :returns:       ``list`` of instances
        
        EXAMPLE INPUT RECORD
        
        ::
        
            {
                'id': 'uniswapv3-ethereum-8',
                'exchange_type': 4,
                'exchange_name': 'uniswap_v3',
                'fee': 3000,
                'pair': [
                    '0x23B608675a2B2fB1890d3ABBd85c5775c51691d5',
                    '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'],
                'native': {
                    'liquidity': '143364393559918602',
                    'sqrt_price_q96': '359531392686823136782270075879',
                    'tick': 30250,
                    'tick_spacing': 60
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
            sp96 = int(rn["sqrt_price_q96"]),
            tick = int(rn["tick"]),
            liquidity = int(rn["liquidity"]),
            ticksp = int(rn["tick_spacing"]),
            #dec_lookup = {k:v for k,v in dec_lookup.items() if k in pair},
            dec_lookup = dec_lookup,
        )
        if result == cls.RESULT.RAW:
            return data
        return [cls(**data)]
    from_data = from_data_v0_1_0
    
    
    # def info(self):
    #     """
    #     returns info string
    #     """
    #     pa, pb = self.papb
    #     p = self.p
    #     s  = f"Uniswap v3 Range {self.tkn0}/{self.tkn1} (fee={self.fee*100:.02f}%)\n"
    #     s += f"  Pa = {pa:12,.3f}   P={p:12,.3f}   Pb = {pb:12,.3f} {self.tkn1} per {self.tkn0}\n"
    #     s += f"1/Pa = {1/pa:12,.3f} 1/P={1/p:12,.3f} 1/Pb = {1/pb:12,.3f} {self.tkn0} per {self.tkn1}\n---\n"
    
    #     s += f" full P = {p}, full 1/P = {1/p}\n"
    #     return s
