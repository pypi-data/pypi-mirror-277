"""
Carbon encoded curve according to the Bancor SDK

source: 
- <https://github.com/bancorprotocol/fastlane-bot/blob/main/fastlane_bot/utils.py>
- <https://github.com/bancorprotocol/arb-analyzer/blob/main/arb_analyzer/exchanges/carbon_v1/utils.py>

---
(c) Copyright Bprotocol foundation 2023-24.
All rights reserved.
"""

import math
from dataclasses import dataclass


@dataclass
class EncodedOrder:
    """
    a single curve as encoded by the SDK

    :token:      token address
    :y:          number of token wei to sell on the curve
    :z:          curve capacity in number of token wei
    :A:          curve parameter A, multiplied by 2**48, encoded
    :B:          curve parameter B, multiplied by 2**48, encoded
    ----
    :A_:         curve parameter A in proper units
    :B_:         curve parameter B in proper units
    :p_start:    start token wei price of the order (in dy/dx)
    :p_end:      end token wei price of the order (in dy/dx)
    """

    token: str
    y: int
    z: int
    A: int
    B: int

    ONE = 2**48

    @classmethod
    def from_sdk(cls, token, order):
        return cls(token=token, **order)

    @property
    def descr(self):
        s = self
        return f"selling {s.token} @ ({1 / s.p_start}..{1 / s.p_end})  [TKNwei] per {s.token}wei"

    def __getitem__(self, item):
        return getattr(self, item)

    @classmethod
    def decodeFloat(cls, value):
        """undoes the mantisse/exponent encoding in A,B"""
        return (value % cls.ONE) << (value // cls.ONE)

    @classmethod
    def decode(cls, value):
        """decodes A,B to float"""
        return cls.decodeFloat(int(value)) / cls.ONE

    @staticmethod
    def bitLength(value):
        "minimal number of bits needed to represent the value"
        return len(bin(value).lstrip("0b")) if value > 0 else 0

    @classmethod
    def encodeRate(cls, value):
        "encodes a rate float to an A,B (using cls.ONE for scaling)"
        data = int(math.sqrt(value) * cls.ONE)
        length = cls.bitLength(data // cls.ONE)
        return (data >> length) << length

    @classmethod
    def encodeFloat(cls, value):
        "encodes a long int value as mantisse/exponent into a shorter integer"
        exponent = cls.bitLength(value // cls.ONE)
        mantissa = value >> exponent
        return mantissa | (exponent * cls.ONE)

    @classmethod
    def encode(cls, y, p_start_hi, p_end_lo, p_marg=None, z=None, token=None):
        """
        alternative constructor: creates a new encoded order from the given parameters

        :y:             number of token wei currently available to sell on the curve (loading)
        :p_start_hi:    start token wei price of the order (in dy/dx; highest)
        :p_end_lo:      end token wei price of the order (in dy/dx; lowest)
        :p_marg:        marginal token wei price of the order (in dy/dx)*
        :z:             curve capacity in number of token wei*

        *at most one of p_marg and z can be given; if neither is given,
        z is assumed to be equal to y
        """
        if token is None:
            token = "TKN"
        if p_marg is not None and z is not None:
            raise ValueError("at most one of p_marg and z can be given")
        if z is None:
            if p_marg is not None and p_marg >= p_start_hi or p_marg is None:
                z = y
            else:
                z = y * (p_start_hi - p_end_lo) // (p_marg - p_start_hi)
        return cls(
            y=int(y),
            z=int(z),
            A=cls.encodeFloat(cls.encodeRate(p_start_hi) - cls.encodeRate(p_end_lo)),
            B=cls.encodeFloat(cls.encodeRate(p_end_lo)),
            token=token,
        )

    @classmethod
    def encode_yzAB(cls, y, z, A, B, token=None):
        """
        encode A,B into the SDK format

        :y:    number of token wei currently available to sell on the curve (loading; as int)
        :z:    curve capacity in number of token wei (as int)
        :A:    curve parameter A (as float)
        :B:    curve parameter B (as float)
        """
        return cls(
            y=int(y),
            z=int(z),
            A=cls.encodeFloat(A),
            B=cls.encodeFloat(B),
            token=str(token),
        )

    @dataclass
    class DecodedOrder:
        """
        a single curve with the values of A,B decoded and as floats
        """

        y: int
        z: int
        A: float
        B: float

    @property
    def decoded(self):
        """
        returns a the order with A, B decoded as floats
        """
        return self.DecodedOrder(y=self.y, z=self.z, A=self.A_, B=self.B_)

    @property
    def A_(self):
        return self.decode(self.A)

    @property
    def B_(self):
        return self.decode(self.B)

    @property
    def p_end(self):
        return self.B_ * self.B_

    @property
    def p_start(self):
        return (self.B_ + self.A_) ** 2

    @property
    def p_marg(self):
        if self.y == self.z:
            return self.p_start
        elif self.y == 0:
            return self.p_end
        raise NotImplementedError("p_marg not implemented for non-full / empty orders")
        A = self.decodeFloat(self.A)
        B = self.decodeFloat(self.B)
        return self.decode(B + A * self.y / self.z) ** 2
        # https://github.com/bancorprotocol/carbon-simulator/blob/beta/benchmark/core/trade/impl.py
        # 'marginalRate' : decodeRate(B + A if y == z else B + A * y / z),