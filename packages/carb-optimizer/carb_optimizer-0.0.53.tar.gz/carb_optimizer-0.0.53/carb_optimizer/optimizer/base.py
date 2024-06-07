"""
Optimization library base module

This module is the base module of the optimization library, defining the
``OptimizerBase`` class and the classes that it contains. It's extended
hierarchy is as indicated below (the left-most lines indicate inheritance, the
other ones membership; the result classes follow an inheritance in line with
their encompassing classes.

Data classes
:: 

    SimpleResult (1)
    └─ SimpleNumericResult (1)
    
    OptimizerResult (1)
    |
    ├─ ArbOptimizerResult (2)
    |   |
    |   ├─ MargPOptimizerResult (2, TODO)
    |   └─ GraphOptimizerResult (6, TODO)
    |
    └─ ConvexOptimizerResult (3)
        └─ NofeesOptimizerResult (3)
        
    TradeInstruction (2)

Operational classes
::

    OptimizerBase (1)
    |  
    └─ ArbOptimizerBase (2)
        |  
        ├─ MargPPairOptimizer (4)
        ├─ MargPFullOptimizer (5)
        ├─ ConvexOptimizer (3)
        └─ GraphOptimizer (6)
    
the objects are contained in the following files
        
======  ===============================
1       `base.py`
2       `arboptimizer.py`
3       `convexoptimizer.py`
4       `margppairoptimizer.py`
5       `margpfulloptimizer.py`
6       `graphoptimizer.py`
======  ===============================
    
    
---
(c) Copyright Bprotocol foundation 2023. 
Licensed under MIT
"""
__VERSION__ = "6.0-rc3"
__DATE__ = "01/Jun/2024+"

from abc import ABC, abstractmethod
import pandas as pd
import numpy as np
import time
import pickle
from dataclasses import dataclass, field, InitVar
from scipy.optimize import minimize_scalar

from ..helpers.dcbase import DCBase
from ..helpers.timer import Timer
from ..helpers.attrdict import AttrDict

@dataclass
class OptimizerResult(DCBase, ABC):
    """
    base class for all optimizer results [API]

    :result:        optimization *result* number (negative number for net outflow, ie arbitrage)
    :error:         the error message, or ``None``
    :time:          time taken to solve the optimization
    :method:        method used to solve the optimization
    :O:             the optimizer object that created this result
                    (``Initvar``; accessible as ``optimizer``)
    """
    result: float = field(repr=True, default=None)
    error: str = field(repr=True, default=None)
    time: float = field(repr=False, default=None, compare=False)
    method: str = field(repr=False, default=None)
    info: dict = field(repr=False, default=None, compare=False)
    O: InitVar = None
    
    
    def __post_init__(self, O=None):
        if not O is None:
            assert issubclass(type(O), OptimizerBase), f"O must be a subclass of OptimizerBase {O}"
        self._optimizer = O
    
    @property
    @abstractmethod
    def result_token(self):
        """
        the (token) unit in which the result is expressed [API]
        """
        raise NotImplementedError("result_token must be implemented in derived class")
    
    @property
    def optimizer(self):
        """returns the optimizer object that created this result, or ``None`` if not set [API]"""
        return self._optimizer

    def __float__(self):
        return float(self.result)
    
    def __int__(self):
        return int(float(self))
    
    @property
    def is_error(self):
        """whether the object represents an error result [API]"""
        return not self.error is None


@dataclass
class SimpleResult(DCBase):
    """
    wraps a result with some context information
    
    :result:    the actual result number obtained (or None if error)
                float(result) ==> result.result (if not error!)
    :error:     if this is an error result, explains the error
    :name:      name of the result, or how has been obtained
    :context:   a ``dict`` containing additional context (converted to ``AttrDict``)
    """
    result: float = None
    error: str = None
    name: str = None
    context: AttrDict = field(default=None, repr=False)
    
    def __post_init__(self):
        if self.result is None:
            if self.error is None:
                raise ValueError("Must provide either result or error message")
        if not self.error is None:
            if not self.result is None:
                raise ValueError(f"An error result can't contain a result field [r={self.result}, e={self.error}]")
        if self.context is None:
            self.context = AttrDict()
        if not isinstance(self.context, AttrDict):
            self.context = AttrDict(self.context)
            
    def __float__(self):
        if self.is_error:
            raise ValueError("cannot convert error result to float", self)
        return float(self.result)
    
    def __int__(self):
        return int(round(float(self)))
    
    def __bool__(self):
        return bool(float(self))

    @property
    def is_error(self):
        """returns True if an error occurred during the optimization [API]"""
        return not self.error is None

@dataclass
class SimpleNumericResult(SimpleResult):
    """
    extends ``SimpleResult`` with additional fields important for numeric calculations (1)
    
    :N:         number of iterations it took to achieve the result (1)
    :time:      wall-clock time it took to compute the result (1)
    
    NOTE 1. The code using this class should not rely on those fields being filled
    with reasonable numbers. 
    """
    N: int = 0
    time: int = 0

def _v2n(v):
    """
    converts verbosity level to ``int`` value
    
    - ``None``, ``False`` -> 0
    - ``True`` -> 1
    - ``<number>`` -> ``int(number)``
    - anything else -> 1
    """
    if v is None: return 0
    if v is False: return 0
    if v is True:return 1
    try: return int(v)
    except: return 1
    
class OptimizerBase(ABC):
    """
    abstract base class for all optimizers (generic numeric iterms only; specific for curves)
    """
    __VERSION__ = __VERSION__
    __DATE__ = __DATE__
    
    @property
    @abstractmethod
    def kind(self):
        """
        returns the kind of optimizer (as ``str``) [API]
        
        abstract property, must be overridden in derived class
        """
        pass
        
    class OptimizerError(Exception):
        """
        base class for all optimizer errors; also used for generic errors [API]
        """
        pass
    
    class OptimizerConvergenceError(OptimizerError):
        """
        raised when the optimizer did not converge [API]
        """
        pass
    
    class OptimizerValueError(OptimizerError, ValueError):
        """
        raised when optimizer parameters are inconsistent / outside acceptable ranges [API]
        """
        pass
        
    def pickle(self, basefilename, addts=True):
        """
        pickles the object to a file
        """
        if addts:
            filename = f"{basefilename}.{int(time.time()*100)}.optimizer.pickle"
        else:
            filename = f"{basefilename}.optimizer.pickle"
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def unpickle(cls, basefilename):
        """
        unpickles the object from a file
        """
        with open(f"{basefilename}.optimizer.pickle", "rb") as f:
            object = pickle.load(f)
        assert isinstance(object, cls), f"unpickled object is not of type {cls}"
        return object

    SimpleResult = SimpleResult
    SimpleNumericResult = SimpleNumericResult
    
    DERIVH = 1e-6

    @classmethod
    def _deriv(cls, func, x):
        """
        computes the derivative of `func` at point `x` (stencil size ``DERIVH``)
        """
        h = cls.DERIVH
        return (func(x + h) - func(x - h)) / (2 * h)

    @classmethod
    def _deriv2(cls, func, x):
        """
        computes the second derivative of `func` at point `x` (stencil size ``DERIVH``)
        """
        h = cls.DERIVH
        return (func(x + h) - 2 * func(x) + func(x - h)) / (h * h)

    @classmethod
    def _findmin_gd(cls, func, x0, *, learning_rate=0.1, N=100):
        """
        finds the minimum of `func` using gradient descent starting at `x0`
        
        :func:              function to optimize (must take one parameter)
        :x0:                starting point
        :learning_rate:     learning rate parameter
        :N:                 number of iterations; always goes full length here
                            there is no convergence check
        """
        x = x0
        for _ in range(N):
            x -= learning_rate * cls._deriv(func, x)
        return cls.SimpleNumericResult(result=x, name="gradient-min")

    @classmethod
    def _findmax_gd(cls, func, x0, *, learning_rate=0.1, N=100):
        """
        finds the maximum of `func` using gradient descent, starting at `x0`
        
        :func:              function to optimize (must take one parameter)
        :x0:                starting point
        :learning_rate:     learning rate parameter
        :N:                 number of iterations; always goes full length here
                            there is no convergence check
        """
        x = x0
        for _ in range(N):
            x += learning_rate * cls._deriv(func, x)
        return cls.SimpleNumericResult(result=x, name="gradient-max")

    @classmethod
    def _findminmax_nr(cls, func, x0, *, max_iter=20, verbosity=0):
        """
        finds the minimum or maximum (1) of func using Newton Raphson, starting at x0
        
        :func:      function to optimize (must take one parameter)
        :x0:        starting point
        :max_iter:  maximim number of iterations; algo will return either at this stage,
                    or when the location moved by less than ``FMM_TOL`` (2)
        :verbosity: verbosity level, info (``1``) or debug (``10,20,...``)
        :returns:   result of the optimization as SimpleNumericResult
        
        NOTE 1. Whether a minimum or maximum is found depends on the curvature at
        the starting point
        
        NOTE 2. In the future we may add convergence condition base on the value of
        the first derivative, or better ``f'/f``
        """
        timer = Timer()
        x = x0
        if verbosity >= 10:
            print(f"[fmm_nr] start value x0 = {x0}, max iter = {max_iter}")
        assert max_iter > 0, f"max_iter must be >0 [{max_iter}]"
        for counter in range(max_iter):
            try:
                x_old = x
                d  = cls._deriv(func, x)
                d2 = cls._deriv2(func, x)
                x -=  d / d2
                if verbosity >= 10:
                    print(f"[fmm_nr:{counter}] x={x} dx={x-x_old} d={d} d2={d2}")
                if x_old != 0:
                    if abs(x/x_old - 1) < cls.FMM_TOL:
                        break
            except Exception as e:
                return cls.SimpleNumericResult(
                    result=None,
                    error=f"Newton Raphson failed: {e} [x={x}, x0={x0}]",
                    name="newtonraphson",
                )
        return cls.SimpleNumericResult(result=x, name="fmm_newtonraphson", 
                                    N=counter+1, time=float(timer.end()))

    _findmin = _findminmax_nr
    _findmax = _findminmax_nr

    FMM_TOL = 1e-6 # tolerance for findminmax (where used)
    
    @classmethod
    def _verbosity(cls, params):
        """
        returns numeric verbosity level ``10*debug + info`` based on params dict (1)
        
        NOTE 1. The function looks for ``debug`` and ``info`` keys in the param dict.
        It converts them to integers and returns ``10*debug + info``.
        
        
        USAGE
        ::

            import verbosity as v
            verbosity = v.verbosity(params)
            
            if verbosity >= 1:
                print('info message')
                
            if verbosity >= 10:
                print('level 1 debug message')
                
            if verbosity >= 20:
                print('level 2 debug message')
        """
        if params is None: return 0
        debug = _v2n(params.get('debug', None))
        info = _v2n(params.get('info', None))
        return 10*debug + info
    
    @classmethod
    def _findminmax_bs(cls, func, a, b):
        """
        find minimum or maximum (1) via bisection on derivative
        
        :func:      the target function
        :a:         lower bracket end (2)
        :b:         upper bracket end (2)
        :returns:   the result as SimpleNumericResult
        
        NOTE 1. if the interval ``[a,b]`` contains multiple maxima or minima (or both)
        convergence depends on how exactly the bracketing progresses and is apparently
        random
        
        NOTE 2. The algo does not currently check whether the first derivatives are in
        different directions at ``a,b`` which is a sufficient albeit not strictly necessary
        condition for the existence of an extreme value
        """
        assert a < b, f"a must be smaller than b [{a}, {b}]"
        while (b - a) / 2 > cls.FMM_TOL:
            midpoint = (a + b) / 2
            derivative = cls._deriv2(func, midpoint)
            if derivative == 0:
                return cls.SimpleNumericResult(midpoint, name="fmm_bisect")
            elif derivative > 0:
                b = midpoint
            else:
                a = midpoint
        return cls.SimpleNumericResult((a + b) / 2, name="fmm_bisect")

    @classmethod
    def _findminmax_gs(cls, func, a, b):
        """
        find min or max via golden section search
        
        :func:  target function
        :a:     lower bracketing value
        :b:     upper bracketing value
        
        TODO: BROKEN
        """
        assert a < b, f"a must be smaller than b [{a}, {b}]"
        PHI = (1 + 5 ** 0.5) / 2  # Golden ratio
        RESPHI = 2 - PHI
        
        c = b - RESPHI * (b - a)
        d = a + RESPHI * (b - a)
        
        while abs(b - a) > cls.FMM_TOL:
            if func(c) < func(d):
                b = d
            else:
                a = c
                
            c = b - RESPHI * (b - a)
            d = a + RESPHI * (b - a)
            
        return cls.SimpleNumericResult((a + b) / 2, name="fmm_goldensection")

    @classmethod
    def _findminmax_brent(cls, func, a, b):
        """
        find min or max via the Brent method
        
        :func:      target function
        :a:         lower bracketing value
        :b:         upper bracketing value
        :returns:   the result as SimpleNumericResult
        
        TODO: BROKEN?
        """
        golden_ratio = (3 - np.sqrt(5)) / 2

        x = w = v = a + golden_ratio * (b - a)
        fx = fw = fv = func(x)
        d = e = 0

        for _ in range(1000):  # Maximum number of iterations
            m = 0.5 * (a + b)
            tol1 = cls.FMM_TOL * np.abs(x) + cls.FMM_TOL / 10
            tol2 = 2 * tol1

            # Check if the current interval is small enough
            if np.abs(x - m) <= (tol2 - 0.5 * (b - a)):
                break

            p = q = r = 0
            if np.abs(e) > tol1:
                r = (x - w) * (fx - fv)
                q = (x - v) * (fx - fw)
                p = (x - v) * q - (x - w) * r
                q = 2 * (q - r)
                if q > 0:
                    p = -p
                q = np.abs(q)
                r = e
                e = d

                if (np.abs(p) < np.abs(0.5 * q * r)) and (p > q * (a - x)) and (p < q * (b - x)):
                    d = p / q
                    u = x + d
                    if (u - a) < tol2 or (b - u) < tol2:
                        d = np.sign(m - x) * tol1
                else:
                    e = (b - x) if x < m else (a - x)
                    d = golden_ratio * e
            else:
                e = (b - x) if x < m else (a - x)
                d = golden_ratio * e

            u = x + d if np.abs(d) >= tol1 else x + np.sign(d) * tol1
            fu = func(u)

            if fu <= fx:
                if u < x:
                    b = x
                else:
                    a = x

                v, w, x = w, x, u
                fv, fw, fx = fw, fx, fu
            else:
                if u < x:
                    a = u
                else:
                    b = u

                if fu <= fw or w == x:
                    v, w = w, u
                    fv, fw = fw, fu
                elif fu <= fv or v == x or v == w:
                    v = u
                    fv = fu

        return cls.SimpleNumericResult(x, name="fmm_brent")

    @classmethod
    def _findminmax_spb(cls, func, a, b):
        """
        find min or max via the Brent method in SciPy
        
        :func:      target function
        :a:         lower bracketing value
        :b:         upper bracketing value
        :returns:   the result as SimpleNumericResult
        """
        try:
            result = minimize_scalar(func, bracket=(a,b), name='brent')
            return cls.SimpleNumericResult(result.x, name="fmm_scipy_brent")
        except Exception as e:
            return cls.SimpleNumericResult(
                result=None,
                error=f"Brent method failed: {e} [a={a}, b={b}]",
                name="fmm_scipy_brent",
            )
            
    GOALSEEKEPS = 1e-9 # double has 15 digits

    @classmethod
    def _goalseek(cls, func, a, b, *, eps=None):
        """
        finds the value of `x` where `func(x)` x is zero, using a bisection between a,b
        
        :func:      function for which to find the zero (must take one parameter)
        :a:         lower bound a (1)
        :b:         upper bound b (1)
        :eps:       desired accuracy (default: ``GOALSEEKEPS``)
        :returns:   the result as SimpleNumericResult (2)
        
        NOTE 1. we must have func(a) * func(b) < 0
        
        NOTE 2. Because the result is returned as ``SimpleNumericResult`` this function will never
        fail / raise; instead the error is returned in the result class
        """
        if eps is None: 
            eps = cls.GOALSEEKEPS
        #print(f"[_goalseek] eps = {eps}, GOALSEEKEPS = {cls.GOALSEEKEPS}")
        if func(a) * func(b) > 0:
            return cls.SimpleNumericResult(
                result=None,
                error=f"function must have different signs at a,b [{a}, {b}, {func(a)} {func(b)}]",
                name="bisection",
            )
            #raise ValueError("function must have different signs at a,b")
        counter = 0
        while (b/a-1) > eps:
            c = (a + b) / 2
            if func(c) == 0:
                return cls.SimpleNumericResult(result=c, name="bisection")
            elif func(a) * func(c) < 0:
                b = c
            else:
                a = c
            counter += 1
            if counter > 200:
                raise ValueError(f"_goalseek did not converge; possible epsilon too small [{eps}]")
        return cls.SimpleNumericResult(result=(a + b) / 2, name="bisection")

    @staticmethod
    def posx(vector):
        """
        returns the positive elements of the vector, zeroes elsewhere
        """
        if isinstance(vector, np.ndarray):
            return np.maximum(0, vector)
        return tuple(max(0, x) for x in vector)

    @staticmethod
    def negx(vector):
        """
        returns the negative elements of the vector, zeroes elsewhere
        """
        if isinstance(vector, np.ndarray):
            return np.minimum(0, vector)
        return tuple(min(0, x) for x in vector)

    @staticmethod
    def a(vector):
        """helper: returns vector as np.array"""
        return np.array(vector)

    @staticmethod
    def t(vector):
        """helper: returns vector as tuple"""
        return tuple(vector)

    @staticmethod
    def F(func, rg):
        """helper: returns list of [func(x) for x in rg]"""
        return [func(x) for x in rg]
    
    @staticmethod
    def flatten_and_convert_to_df(data):
        """
        takes (list of) dicts of list and converts them to DataFrame
        

        EXAMPLE INPUT DATA
        ::

            data = [
                {'a': [1000000, 2000000], 'b': [3000000, 4000000]},
                {'a': [5000000, 6000000], 'b': [7000000, 8000000]},
                {'a': [9000000, 10000000], 'b': [11000000, 12000000]}
            ]

        EXAMPLE OUTPUT DATAFRAME

        ::

                    a_1       a_2       b_1       b_2
            0   1000000   2000000   3000000   4000000
            1   5000000   6000000   7000000   8000000
            2   9000000  10000000  11000000  12000000
        """
        flattened_data = []
        for entry in data:
            flattened_entry = {}
            for key, value in entry.items():
                for i, item in enumerate(value):
                    flattened_entry[f"{key}_{i+1}"] = item
            flattened_data.append(flattened_entry)
        df = pd.DataFrame(flattened_data)
        return df

