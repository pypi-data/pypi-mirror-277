"""
helper functions for interactive use
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as m
import scipy as sp
import scipy.linalg as spl
import scipy.sparse as sps
import scipy.sparse.linalg as spsl
import networkx as nx
import json

from . import __VERSION__ as CO_VERSION, __DATE__ as CO_DATE
from . import *
from . import adapters as ca
from . import arbgraphs as ag
from . import analyzer as al
from .enums import ExchangeType as ET
from .helpers.symbol_lookup import SymbolLookup
from .helpers.attrdict import AttrDict as AD
from .helpers.timer import Timer

def load_curves(fn, *, incl_tokens=False):
    """
    alias for ``GenericAdapter.from_file``
    
    :fn:        filename
    :returns:   ``list`` of curves
    """
    return ca.GenericAdapter.from_file(fn, incl_tokens=incl_tokens)

def load_curves_and_tokens(fn, *, incl_tokens=True):
    """
    alias for ``GenericAdapter.from_file(., incl_tokens=True)``
    
    :fn:        filename
    :returns:   ``tuple`` with ``(curves, tokens)``
    """
    return ca.GenericAdapter.from_file(fn, incl_tokens=incl_tokens)

def execute(command, fn, **kwargs):
    """
    executes ``command(fn, **kwargs)`` with different path adjustments (1) for ``fn``

    :returns:   ``tuple`` ``(fn, result)``

    USAGE

    ::
        DATA_FN = 'myfile.json.gz'
        FULL_DATA_FN, _ = execute(ca.TokenData.from_file, DATA_FN)

    NOTE 1. Paths tried are ``.``, ``_data``, ``NBTest/_data``
    """
    try:
        print(f"trying {fn}")
        return fn, command(fn, **kwargs)
    except:
        fn = f"_data/{fn}"
        print(f"trying {fn}")
        try:
            return fn, command(fn, **kwargs)
        except:
            print(f"trying {fn}")
            fn = f"NBTests/{fn}"
            return fn, command(fn, **kwargs)

def setup_symbol_lookup(token_data, tokenlist_fn, chain):
    """
    convenience function to setup a symbol lookup object
    
    :token_data:    token data as obtained from the curves (typically does not contain meaningful symbols)
    :tokenlist_fn:  filename of hardcoded list of well known token symbols that update the ones from token data
    :chain:         chain name (eg "ethereum"), as used in the tokenlist file
    :returns:       ``a2s``, ``a2sj``, ``T``,  ``SL``
    
    ================    ====================================================================================================
    ``a2s``             function that maps address to symbol (``SL.a2s``)
    ``a2sj``            ``a2s`` followed by ``SL.j`` to make the output more compact
    ``T``               the ``T`` object to easily obtain well known token addresses (1)   
    ``tokenlist_fn``    the filename from where to load the token list
    ================    ====================================================================================================
    
    NOTE 1. Eg ``T`` allows to obtain the address of WETH as ``T.WETH``
    
    EXAMPLE USAGE
    ::
    
        DATA_FN = 'curves.json.gz'
        TOKENLIST_FN = 'tokenlist.csv'
        
        FULL_DATA_FN, _ = execute(ca.TokenData.from_file, DATA_FN)
        FULL_TOKENLIST_FN, _ = execute(SymbolLookup.from_tokenlist, TOKENLIST_FN, chain="ethereum")
        curves, token_data = load_curves_and_tokens(FULL_DATA_FN)
        a2s, a2sj, T, SL = setup_symbol_lookup(token_data, FULL_TOKENLIST_FN, "ethereum")
    """
    SL = SymbolLookup.from_TokenData(token_data)
    SLtl = SymbolLookup.from_tokenlist(tokenlist_fn, chain=chain)
    SL.add_symbols(SLtl)
    a2s = SL.a2s
    a2sj = lambda x: SL.j(SL.a2s(x))
    T = SL.T()
    return a2s, a2sj, T, SL

def fcbp(curve):
    """``fee`` of ``curve`` in 1/100 of a basis point (``int``)"""
    return int(curve.fee * 10_000 * 100)

def inv(x):
    """inverse of ``x`` (0 if division by zero)"""
    try:
        return 1 / x
    except:
        return 1e200
    
def weighted_average_sd(values, weights):
    """
    weighted average and standard deviation
    
    :values:    list of values
    :weights:   list of weights
    :returns:   tuple ``(average, sd)``
    """
    average = np.average(values, weights=weights)
    variance = np.average((values - average) ** 2, weights=weights)
    return average, m.sqrt(variance)

T = AD(
    WETH="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    ETH="0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE",
    WBTC="0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599",
    BTC="0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599",
    USDC="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    USDT="0xdAC17F958D2ee523a2206206994597C13D831ec7",
    DAI="0x6B175474E89094C44Da98b954EedeAC495271d0F",
    LINK="0x514910771AF9Ca656af840dff83E8264EcF986CA",
    BNT="0x1F573D6Fb3F13d689FF844B4cE37794d79a7FF1C",
    HEX="0x2b591e99afE9f32eAA6214f7B7629768c40Eeb39",
    UNI="0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984",
    FRAX="0x3432B6A60D23Ca0dFCa7761B7ab56459D9C964D0",
    ICHI="0x903bEF1736CDdf2A537176cf3C64579C3867A881",
)


def fmt2(x):
    return f"{x:,.2f}"
def fmt0(x):
    return f"{x:,.0f}"

_n = lambda x: isinstance(x, (int, float))
    # is numeric type
    
fmt = AD(
    id = lambda x: x,
    d0 = lambda x: f"{x:,.0f}" if _n(x) else x,
    d1 = lambda x: f"{x:,.1f}" if _n(x) else x,
    d2 = lambda x: f"{x:,.2f}" if _n(x) else x,
)

