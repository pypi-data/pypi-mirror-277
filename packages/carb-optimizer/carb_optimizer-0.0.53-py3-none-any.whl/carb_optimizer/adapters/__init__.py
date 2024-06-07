"""
adapters converting blockchain data to a format suitable for ``ConstantProductCurve``

Note: Those adapters are not strictly speaking in the API code and production
code should not rely on them. However, they may be useful for testing, on the
understanding that there is no guarantee that they will be maintained in a
stable manner. Semantic versioning does apply on the object level.

---
(c) Copyright Bprotocol foundation 2023-24.
All rights reserved.
Licensed under MIT.
"""

from .base import AdapterBase
from .univ2 import UniV2Adapter
from .univ3 import UniV3Adapter
from .carbonv1 import CarbonV1Adapter

from .generic import GenericAdapter
from .token import Token, TokenData



