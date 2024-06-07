"""allows for the lookup of a symbol based on a token address"""
from dataclasses import dataclass
import pandas as pd

from ..adapters  import Token, TokenData
from .attrdict import AttrDict
    
class SymbolLookup(TokenData):
    """
    allows for the lookup of a symbol based on a token address
    """
    def address_to_symbol(self, addr):
        """
        converts single address to symbol
        
        :addr:      token address, or iterable thereof
        :returns:   token symbol, or the address if the symbol is not available
        """
        if not isinstance(addr, str):
            return [self.address_to_symbol(p) for p in addr]
        try:
            return self[addr].symbol
        except KeyError:
            return addr
        
    def addresses_to_symbol(self, pair, *, sep="/"):
        """
        converts a ``sep`` separated string of addresses (typically, a pair) to symbols
        
        :pair:      ``str`` with two token addresses separated by ``sep``, , or iterable thereof
        :sep:       separator (default: ``/``)
        :returns:   new pair as ``str``, addresses converted with ``address_to_symbol``
        
        NOTE. This works on separated strings of any length, not just pairs; notable it also
        works on single addresses, therefore in practice use of ``address_to_symbol`` is
        not necessary
        """
        if not isinstance(pair, str):
            return [self.addresses_to_symbol(p, sep=sep) for p in pair]
        return sep.join([self.address_to_symbol(t) for t in pair.split(sep)])
    a2s = addresses_to_symbol
    
    def decimals(self, addr):
        """
        retrieves the decimals of an address
        
        :addr:      token address, or iterable thereof
        :returns:   token decimals (raises ``KeyError`` if the address is not found )
        """
        if not isinstance(addr, str):
            return [self.decimals(p) for p in addr]
        return self[addr].dec
    d = decimals
    
    def join(self, iterable, *, sep=", "):
        """joins an iterable of strings with ``sep`` (convenience function)"""
        return sep.join(iterable)
    j = join
    
    def token_dict(self):
        """
        returns the token data as a ``AttrDict``
        
        allows convenience access to the token addresses via the symbol
        
        ::
            SL = SymbolLookup(...)
            T = SL.token_dict()
            T.WETH                  # 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2
            
        """
        return AttrDict({v.symbol:  v.addr for k, v in self._data.items()})
    T = token_dict

    @property
    def tokens(self):
        """
        returns the token data
        """
        return list(self._data.values())
    
    @classmethod
    def from_TokenData(cls, token_data):
        """
        alternative constructor: from a ``TokenData`` instance
        
        NOTE: this is a shallow copy, ie the new instance shares the token data 
        with the original; if ``add_symbols`` is called on one of them, both will
        be updated
        """
        new_obj = cls()
        new_obj._data = token_data._data
        return new_obj
    
    @classmethod
    def from_tokenlist(cls, fn, chain=None):
        """
        alternative constructor: from a tokenlist
        
        :fn:        file name token list in the format indicated below
        :chain:     if not ``None``, restricts the token list to the chain
        
        token list format
        ::
        
            ,tokenAddress,symbol,decimals,chain
            0,0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE,ETH,18,ethereum
            1,0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2,WETH,18,ethereum
            2,0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48,USDC,6,ethereum
        """
        df = pd.read_csv(fn)
        if not chain is None:
            df = df[df.chain == chain]
        #return df
        print(f"[from_tokenlist] loading `{fn}` [chain={chain}, {len(df)} tokens]")
        records = df.to_dict(orient='records')
        tl = [Token(addr=r["tokenAddress"], symbol=r["symbol"], dec=r["decimals"]) for r in records]
        return TokenData(tl)
    
    def add_symbols(self, symbol_list, *, add=False):
        """
        add a list of symbols to the token data
        
        :symbol_list:       a ``TokenData`` whose symbols are to be added to this instance
        :add:               if ``True``, if the token does not exist, it is added
        :returns:           ``self``
        """
        for tkn in symbol_list:
            if tkn.addr in self._data:
                # tokens already in the data are updated
                if tkn.symbol is None or tkn.symbol == tkn.addr:
                    # if symbol is None or trivial: don't update
                    #print("[add_symbols] skipping", tkn.addr, tkn.symbol)
                    continue
                record = self._data[tkn.addr]
                record.symbol = tkn.symbol
                record.has_symbol = True
            else:
                # new tokens are added
                if add:
                    #print("[add_symbols] adding", tkn.addr, tkn.symbol)
                    self.add(tkn)
                else:
                    pass
                    #print("[add_symbols] not adding", tkn.addr, tkn.symbol)
    

    