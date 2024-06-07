"""
managing token related data and data formats

---
(c) Copyright Bprotocol foundation 2023-24.
All rights reserved.
Licensed under MIT.
"""
__VERSION__ = "1.0-rc3"  # TODO-RELEASE
__DATE__ = "01/Jun/2024+"

from dataclasses import dataclass
import json
import gzip
from ..helpers.dcbase import DCBase

@dataclass
class Token(DCBase):
    """
    represent that data for a single token
    
    :addr:          token address
    :dec:           token decimals
    :symbol:        token symbol
    :price:         token price (in USD per token)
    :has_symbol:    if True, the symbol has not been inferred from the address
    """
    addr: str
    dec: int
    symbol: str = None
    price: float = None
    has_symbol: bool = True
    
    def __post_init__(self):
        if self.symbol is None:
            self.symbol = self.addr[2:8]
            self.has_symbol = False
        try:
            assert isinstance(self.addr, str)
            assert isinstance(self.dec, int)
            assert isinstance(self.symbol, str)
            assert isinstance(self.has_symbol, bool)
        except AssertionError:
            raise ValueError("parameters must be not `None` and of the right type", self.__dict__)

            
    @classmethod
    def from_data_v0_1_0(cls, data):
        """
        create a token from a data dict
        
        :data:      token data according to the ``v0.1.0`` data format
        
        
        DATA FORMAT v0.1.0::
        ::
            {
                'id': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
                'decimals': '18',
                'symbol': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
                'usd_price': None
            }
        """
        addr, symbol = data['id'], data['symbol']
        if symbol == addr: symbol = None
        return cls(
            addr=addr,
            dec=int(data['decimals']),
            symbol=symbol,
            price=data['usd_price']
        )
        
    @classmethod
    def from_data_v0_2_0(cls, data):
        """
        create a token from a data dict
        
        :data:      token data according to the ``v0.2.0`` data format
        
        
        DATA FORMAT v0.2.0::
        ::
            {
                'id': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2', 
                'decimals': '18', 
                'symbol': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2', 
                'usd_price': None
            }
        """
        addr, symbol = data['id'], data['symbol']
        if symbol == addr: symbol = None
        return cls(
            addr=addr,
            dec=int(data['decimals']),
            symbol=symbol,
            price=data['usd_price']
        )
        
    @classmethod
    def from_data(cls, data, *, version_t=None):
        """
        create a token from a data dict
        
        :data:          token data according to the latest data format
        :version_t:     version of the data, as tuple ``(major, minor)``
        """
        if version_t is None or version_t == ("0", "1"):
            #print("[Token.from_data] using v0.1.0")
            return cls.from_data_v0_1_0(data)
        elif version_t == ("0", "2"):
            #print("[Token.from_data] using v0.2.0")
            return cls.from_data_v0_2_0(data)
        else:
            raise ValueError("unsupported data version", version_t)

class TokenData:
    """
    container for ``Token`` records
    
    :data:          token data in various formats (1)
    :version_t:     version of the data, as tuple ``(major, minor)``
    
    supported formats are iterables of ``Token`` or ``dict``; the latter must either
    be according to the latest format, or have ``version`` set to the correct version
    """
    def __init__(self, data=None, *, version_t=None):
        self._data = dict()
        if data:
            for token in data:
                self.add(token, version_t=version_t)
        
    def add(self, token, *, version_t=None):
        """
        add a token to the container
        
        :token:         token data as ``Token`` or ``dict
        :version_t:     version of the data, as tuple ``(major, minor)``
        """
        if isinstance(token, dict):
            token = Token.from_data(token, version_t=version_t)
        if not isinstance(token, Token):
            raise ValueError("token must be a `Token` or a `dict`", token)
        if token.addr in self._data:
            raise ValueError(f"token with address {token.addr} already exists", token)
        self._data[token.addr] = token
        
    def __getitem__(self, key):
        return self._data[key]
    
    def __iadd__(self, token):
        self.add(token)
        return self
    
    def __repr__(self):
        lines = [repr(t) for t in self._data.values()]
        result = ",\n".join(lines)
        return f"{self.__class__.__name__}([\n{result}\n])"
    
    def __len__(self):
        return len(self._data)
    
    def __iter__(self):
        return iter(self._data.values())
    
    def __contains__(self, key):
        if isinstance(key, Token):
            key = key.addr
        return key in self._data
    
    def dec_lookup(self):
        """
        returns a lookup ``dict`` for token decimals (``addr`` is lower case)
        """
        return {t.addr.lower(): t.dec for t in self._data.values()}
    
    
    @classmethod
    def from_file(cls, fname):
        """
        reads the token data from a file (all knowns formats)
        """
        with gzip.open(fname, 'rt', encoding='utf-8') as f:
            full_curve_data = json.load(f)
        version = full_curve_data["version"]
        version_t = tuple(version.split(".")[:2])
        tokens = full_curve_data["tokens"]
        # if not version_t in (("0", "1"), ("0", "2")):
        #     raise ValueError(f"unsupported data version {version}")
        return cls(tokens, version_t=version_t)
    
        