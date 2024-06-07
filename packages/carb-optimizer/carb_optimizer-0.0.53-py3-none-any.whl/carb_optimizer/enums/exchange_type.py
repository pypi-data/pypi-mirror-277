"""
defines the ``ExchangeType`` enum

---
(c) Copyright Bprotocol foundation 2024. 
Licensed under MIT
"""
from enum import Enum

class ExchangeType(Enum):
    """
    defines the ``exchange_type`` as per conventions in the Fastlane Contract (``enum``)
    """
    # see https://github.com/bancorprotocol/bancor-arbitrage/blob/main/contracts/arbitrage/BancorArbitrage.sol#L88-L101
    
    UNKNOWN = -1
    BANCOR_V2 = 1
    BANCOR_V3 = 2
    UNI_V2 = 3
    UNI_V3 = 4
    SUSHISWAP = 5
    CARBON_V1 = 6
    BALANCER = 7
    CARBON_POL = 8
    CURVE = 9
    WETH = 10
    SOLIDLY = 11
    VELODROME = 12
    XFAI_V0 = 13
    
    
# ExchangeTypeNames = {
#     ExchangeType.BANCOR_V2:     "bancor_v2",
#     ExchangeType.BANCOR_V3:     "bancor_v3",
#     ExchangeType.UNISWAP_V2:    "uniswap_v2",
#     ExchangeType.UNISWAP_V3:    "uniswap_v3",  
#     ExchangeType.SUSHISWAP:     "sushiswap",
#     ExchangeType.CARBON_V1:     "carbon_v1",
#     ExchangeType.BALANCER:      "balancer",
#     ExchangeType.CARBON_POL:    "carbon_pol",
#     ExchangeType.CURVE:         "curve",
#     ExchangeType.WETH:          "weth",
#     ExchangeType.SOLIDLY:       "solidly",
#     ExchangeType.VELODROME:     "velodrome",
#     ExchangeType.XFAI_V0:       "xfai_v0",
# }
ExchangeTypeNames = None




