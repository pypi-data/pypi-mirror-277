"""
simple representation of a pair of tokens, used by cpc and arbgraph

---
(c) Copyright Bprotocol foundation 2023. 
Licensed under MIT
"""
__VERSION__ = "3.0"
__DATE__ = "07/May/2024"

from dataclasses import dataclass, field, InitVar


@dataclass
class SimplePair:
    """
    represents a token pair [API]
    
    :pair:      the pair, in one of the formats indicated below
    
    ::
    
        P = SimplePair
        pair  = P("TKNB/TKNQ")
        pair1 = P(dict(tknb="TKNB", tknq="TKNQ"))
        pair2 = P(["TKNB", "TKNQ"])
        pair3 = P(pair.from_tokens(tknb="TKNB", tknq="TKNQ"))
        pair4 = P(pair)

    A key functionality of this class is to bring pairs into a canonical form. For example,
    the pair "ETH/USDC" is effectively the same as the pair "USDC/ETH". However, because
    the roles of the tokens are exchanged a lot of numbers are different. In particular, the
    prices invert :math:`p \\rightarrow 1/p`. 
    
    This class provides a way to normalize pairs. It does so with a hardcoded list of "numeraire"
    tokens (in ``NUMERAIRE_TOKENS``). Each token has a numerical rank, and the lower ranked token
    will be the numeraire. Tokens not on the list are ranked at the end, and ranked amongst each
    other in alphabetical order.
    
    This class has the notion of a ``primary`` which is the pair according to those rules above.
    For example
    
    ::
    
        P = SimplePair
        P("ETH/USDC").primary                           # "ETH/USDC"
        P("USDC/ETH").primary                           # "ETH/USDC"
        P("ETH/USDC") != P("USDC/ETH")                  # True
        P("ETH/USDC").primary == P("USDC/ETH").primary  # True
    """

    __VERSION__ = __VERSION__
    __DATE__ = __DATE__

    tknb: str = field(init=False)
    tknq: str = field(init=False)
    pair: InitVar[str] = None

    def __post_init__(self, pair):
        if isinstance(pair, self.__class__):
            self.tknb = pair.tknb
            self.tknq = pair.tknq
        elif isinstance(pair, dict):
            self.tknb = pair["tknb"]
            self.tknq = pair["tknq"]
        elif isinstance(pair, str):
            sp = pair.split("/")
            if len(sp) != 2:
                raise ValueError(f"pair must be a string of the form 'tknb/tknq' {pair}, sp={sp}")
            self.tknb, self.tknq = sp
        elif pair is False:
            # used in alternative constructors
            pass
        else:
            try:
                self.tknb, self.tknq = pair
            except:
                raise ValueError(f"pair must be a string or list of two strings {pair}")

    @classmethod
    def from_tokens(cls, tknb, tknq):
        """
        alternative constructor from tokens [API]
        
        :tknb:      the base token
        :tknq:      the quote token
        
        ::
  
            SimplePair.from_tokens(tknb="ETH", tknq="USDC")   
                # SimplePair("ETH/USDC")
        """
        pair = cls(False)
        pair.tknb = tknb
        pair.tknq = tknq
        return pair

    def __str__(self):
        return f"{self.tknb}/{self.tknq}"

    @property
    def pair(self):
        """
        string representation of the pair [API]
        
        ::
        
            SimplePair("ETH/USDC").pair_t   # "ETH/USDC"
        """
        return str(self)

    @property
    def pair_t(self):
        """
        tuple representation of the pair [API]
        
        ::
        
            SimplePair("ETH/USDC").pair_t   # ("ETH", "USDC")
        """
        return (self.tknb, self.tknq)

    @property
    def pair_r(self):
        """
        returns the reversed pair as string [API]
        
        ::
        
            SimplePair("ETH/USDC").pair_r   # "USDC/ETH"
        """
        return f"{self.tknq}/{self.tknb}"

    @property
    def pair_rt(self):
        """
        tuple representation of the reversed pair [API]
        
        ::
        
            SimplePair("ETH/USDC").pair_rt   # ("USDC", "ETH")
        """
        return (self.tknq, self.tknb)

    @property
    def tknx(self):
        """
        alias for ``tknb`` [API]
        
        ::
        
            SimplePair("ETH/USDC").tknb  # "ETH"
            SimplePair("ETH/USDC").tknx  # "ETH"
        """
        return self.tknb

    @property
    def tkny(self):
        """
        alias for ``tknq`` [API]
        
        ::
        
            SimplePair("ETH/USDC").tknq  # "USDC"
            SimplePair("ETH/USDC").tkny  # "USDC"
        """
        return self.tknq

    # TODO: THIS IS NOT CONSISTENT WITH HAVING TOKEN ADDRESSES AS WE DO NOW
    NUMERAIRE_TOKENS = {
        tkn: i*10
        for i, tkn in enumerate(
            [
                "USDC",
                "USDT",
                "DAI",
                "TUSD",
                "BUSD",
                "PAX",
                "GUSD",
                "USDS",
                "sUSD",
                "mUSD",
                "HUSD",
                "USDN",
                "USDP",
                "USDQ",
                "BNT",
                "ETH",
                "WETH",
                "WBTC",
                "BTC",
            ]
        )
    }

    @classmethod
    def n(cls, tkn):
        """normalize the token name (remove the id, if any)"""
        if len(tkn.split("/")) > 1:
            return "/".join([cls.n(t) for t in tkn.split("/")])
        return tkn.split("-")[0].split("(")[0]

    @property
    def tknb_n(self):
        """normalized ``tknb``"""
        return self.n(self.tknb)

    @property
    def tknq_n(self):
        """normalized ``tknq``"""
        return self.n(self.tknq)

    @property
    def pair_n(self):
        """normalized ``pair``"""
        return f"{self.tknb_n}/{self.tknq_n}"

    @property
    def tknx_n(self):
        """normalized ``tknx``"""
        return self.n(self.tknx)

    @property
    def tkny_n(self):
        """normalized ``tkny``"""
        return self.n(self.tkny)

    @property
    def is_primary(self):
        """
        whether the representation is primary or secondary [API]
        
        ::
        
            SimplePair("ETH/USDC").is_primary   # True
            SimplePair("USDC/ETH").is_primary   # False
        """
        tknqix = self.NUMERAIRE_TOKENS.get(self.tknq_n, 1e10)
        tknbix = self.NUMERAIRE_TOKENS.get(self.tknb_n, 1e10)
        if tknqix == tknbix:
            return self.tknb < self.tknq
        return tknqix < tknbix

    def primary_price(self, p):
        """
        returns the primary price (p if primary, 1/p if secondary) [API]
        
        ::
        
            pair = SimplePair("USDC/ETH")
            pair.pp_convention              # "ETH per USDC"
            p = 1/2000                      # price [ETH per USDC]
            pair.primary_price(p)           # 2000 [USDC per ETH]
            
            pair = SimplePair("ETH/USDC")
            pair.pp_convention              # "USDC per ETH"
            p = 2000                        # price [USD per ETH]
            pair.primary_price(p)           # 2000 [USDC per ETH]
        """
        if self.is_primary:
            return p
        else:
            if p == 0:
                return float("nan")
        return 1 / p

    pp = primary_price

    @property
    def pp_convention(self):
        """
        returns the primary price convention [API]
        
        Example:
        
        ::

            SimplePair("ETH/USDC").pp_convention  # "USDC per ETH"
            SimplePair("USDC/ETH").pp_convention  # "ETH per USDC"
        
        """
        tknb, tknq = self.primary_n.split("/")
        return f"{tknq} per {tknb}"

    @property
    def primary(self):
        """
        returns the primary pair as string [API]
        
        ::
            
            SimplePair("ETH/USDC").primary  # "ETH/USDC"
            SimplePair("USDC/ETH").primary  # "ETH/USDC"
        """
        return self.pair if self.is_primary else self.pair_r

    @property
    def primary_n(self):
        """the primary pair, normalized"""
        tokens = self.primary.split("/")
        tokens = [self.n(t) for t in tokens]
        return "/".join(tokens)

    @property
    def primary_tknb(self):
        """returns the primary normalized tknb"""
        return self.tknb_n if self.is_primary else self.tknq_n

    @property
    def primary_tknq(self):
        """returns the primary normalized tknq"""
        return self.tknq_n if self.is_primary else self.tknb_n

    @property
    def secondary(self):
        """
        returns the secondary pair [API]
        
        ::
            
            SimplePair("ETH/USDC").secondary  # "USDC/ETH"
            SimplePair("USDC/ETH").secondary  # "USDC/ETH"
        """
        return self.pair_r if self.is_primary else self.pair

    @property
    def secondary_n(self):
        """the secondary pair, normalized"""
        tokens = self.secondary.split("/")
        tokens = [self.n(t) for t in tokens]
        return "/".join(tokens)

    @classmethod
    def wrap(cls, pairlist):
        """wraps a list of strings into Pairs [API]"""
        return tuple(cls(p) for p in pairlist)

    @classmethod
    def unwrap(cls, pairlist):
        """unwraps a list of Pairs into strings [API]"""
        return tuple(str(p) for p in pairlist)
