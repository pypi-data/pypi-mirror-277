"""
launching other adapters


---
(c) Copyright Bprotocol foundation 2023-24.
All rights reserved.
Licensed under MIT.
"""
__VERSION__ = "1.0-rc3"  # TODO-RELEASE
__DATE__ = "01/Jun/2024+"

import gzip
import json
from enum import Enum

from ..enums import ExchangeType as ET
from .carbonv1 import CarbonV1Adapter
from .univ2 import UniV2Adapter
from .univ3 import UniV3Adapter
from .token import Token, TokenData


class GenericAdapter:
    """
    effectively a factory class for the other adapters in this module
    
    NOTE. This class is not meant to be instantiated. It implements the same signature
    class methods as the other adapters, and those return the respective adapter 
    instances.
    """
    __VERSION__ = __VERSION__
    __DATE__ = __DATE__
    
    def __init__(self):
        raise ValueError("this class is not meant to be instantiated")
    
    ADAPTER_MAP = {
        ET.CARBON_V1: CarbonV1Adapter,
        ET.UNI_V2: UniV2Adapter,
        ET.UNI_V3: UniV3Adapter
    }
    
    class AdaptorError(Exception):
        """base class for error raised by this class"""
        pass
    
    class UnknownExchangeTypeError(AdaptorError):
        """raised when an unknown exchange type is encountered"""
        pass
    
    class MissingAdapterError(AdaptorError):
        """raised when the exchange is valid but the adapter is missing"""
        pass
    
    @classmethod
    def adapter(cls, record):
        """
        returns the adapter class for the given record
        
        :raises:   ``UnknownExchangeTypeError`` or ``MissingAdapterError``
        """
        try:
            exchange_type = record['platform_id']
        except KeyError:
            exchange_type = record['exchange_type']
            
        try:
            exchange_type = ET(exchange_type)
        except ValueError:
            raise cls.UnknownExchangeTypeError(f"unknown exchange type [{exchange_type}]", record)
        
        try:
            Adapter = cls.ADAPTER_MAP[exchange_type]
        except KeyError:
            raise cls.MissingAdapterError(f"exchange type not implemented [{exchange_type}]", record)
        return Adapter
        
    @classmethod
    def from_data(cls, record, dec_lookup=None):
        """
        instantiates adapter instanced depending on the record content
        
        :data:          the data ``dict`` from the system
        :dec_lookup:    decimals lookup ``dict``
        :returns:       ``list`` of instances
        """
        return cls.adapter(record).from_data(record, dec_lookup=dec_lookup)
    
    class ERROR_HANDLING(Enum):
        """How to handle errors in the data reading process (``enum``)"""
        RAISE = 0
        SKIP = 1
        WARN = 2
        WARNLONG = 3
        DIAGNOSTIC = 4
    EH = ERROR_HANDLING
    
    @classmethod
    def create_curve(cls, record, dec_lookup=None, *, error_handling=None):
        """
        creates curves directly from a record with persistent class instance (1)
        
        :record:            the data record ``dict`` from the system
        :dec_lookup:        a ``dict`` with token decimals, extracted from the system data 
                            using the ``Token`` class
        :error_handling:    how to handle errors; one of ``ERROR_HANDLING``
        :returns:           ``list`` of curves 
        """
        error_handling = error_handling or cls.ERROR_HANDLING.RAISE
        if not isinstance(error_handling, cls.ERROR_HANDLING):
            raise ValueError("error_handling must be an instance of ERROR_HANDLING", error_handling)
        
        try:
            return cls.adapter(record).create_curve(record, dec_lookup=dec_lookup)
        except Exception as e:
            if error_handling == cls.ERROR_HANDLING.RAISE:
                raise
            if error_handling == cls.ERROR_HANDLING.DIAGNOSTIC:
                print("[create_curve] error reading curves", e)
                print("record\n", record)
                raise
            if error_handling == cls.ERROR_HANDLING.WARNLONG:
                print("[create_curve] error reading curves", record, e)
            elif error_handling == cls.ERROR_HANDLING.WARN:
                print("[create_curve] error reading curves", e)
            return []

    
    @classmethod
    def create_curves(cls, records, dec_lookup=None, *, 
                    flatten=True, error_handling=None):
        """
        creates curves directly from a record with persistent class instance (2)
        
        :records:           list of records, each of which is being passed to create_curve
        :dec_lookup:        as for ``create_curve``
        :flatten:           if True, the result ``list`` is flattened
        :error_handling:    how to handle errors; one of ``ERROR_HANDLING``
        :returns:           ``list`` of curves 
        """
        error_handling = error_handling or cls.ERROR_HANDLING.RAISE
        result = [
            cls.create_curve(record, dec_lookup=dec_lookup, error_handling=error_handling) 
            for record in records
        ]
        if flatten:
            return [curve for sublist in result for curve in sublist]
        else:
            return result
        
    @classmethod
    def _from_file_v0_1(cls, full_curve_data, *, error_handling=None, incl_tokens=False):
        """
        reads the token data from a file (``v0.1.0`` format)
        
        :full_curve_data:   the full curve data read from the file
        
        Other parameters and return: see ``from_file``
        """
        tokens = full_curve_data["tokens"]
        token_data = TokenData(tokens)
        dec_lookup = token_data.dec_lookup()
        
        curves = full_curve_data["curves"]
        result = cls.create_curves(
            curves, 
            dec_lookup=dec_lookup, 
            error_handling=error_handling
        )
        if incl_tokens:
            return result, token_data
        return result

    @classmethod
    def _from_file_v0_2(cls, full_curve_data, *, error_handling=None, incl_tokens=False):
        """
        reads the token data from a file (``v0.2.0`` format)
        
        :full_curve_data:   the full curve data read from the file
        
        Other parameters and return: see ``from_file``
        """
        tokens = full_curve_data["tokens"]
        token_data = TokenData(tokens)
        dec_lookup = token_data.dec_lookup()
        
        curves = full_curve_data["curves"]
        result = cls.create_curves(
            curves, 
            dec_lookup=dec_lookup, 
            #error_handling=error_handling,
            error_handling=cls.ERROR_HANDLING.DIAGNOSTIC,
        )
        if incl_tokens:
            return result, token_data
        return result

    
    @classmethod
    def from_file(cls, fname, *, error_handling=None, incl_tokens=False):
        """
        reads the token data from a file (any supported format)
        
        :fname:             filename with the data
        :error_handling:    how to handle errors; one of ``ERROR_HANDLING``
        :incl_tokens:       if True, the token data is included in the result
        :returns:           ``list`` of curves, or a ``tuple`` with ``(curves, tokens)``
                            where tokens are returned as ``TokenData`` instance
        """
        with gzip.open(fname, 'rt', encoding='utf-8') as f:
            full_curve_data = json.load(f)
        
        version = full_curve_data["version"]
        version_t = tuple(version.split(".")[:2])
        
        nc = len(full_curve_data["curves"])
        nt = len(full_curve_data["tokens"])
        print(f"[from_file] loading `{fname}` [version = {version}; {nc} curves, {nt} tokens]")

        if version_t == ("0", "1"):
            result = cls._from_file_v0_1(full_curve_data, error_handling=error_handling, incl_tokens=incl_tokens)
        elif version_t == ("0", "2"):
            result = cls._from_file_v0_2(full_curve_data, error_handling=error_handling, incl_tokens=incl_tokens)
        else:
            raise ValueError(f"unsupported data version {version}")
        
        return result
