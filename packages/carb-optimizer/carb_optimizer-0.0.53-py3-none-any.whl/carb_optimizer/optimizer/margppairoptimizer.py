"""
optimization library -- Pair Optimizer module [final optimizer class]


The pair optimizer uses a marginal price method in one dimension to find the optimal
solution. It uses a bisection method to find the root of the transfer equation, therefore
it only work for a single pair. To use it on multiple pairs, use MargPFullOptimizer instead.

---
This module is still subject to active research, and comments and suggestions are welcome. 
The corresponding author is Stefan Loesch <stefan@bancor.network>

(c) Copyright Bprotocol foundation 2023. 
Licensed under MIT
"""
__VERSION__ = "6.0-rc3" # TODO-RELEASE
__DATE__ = "01/Jun/2024+"

import numpy as np
import time
from enum import Enum

from ..curves import CPCInverter
from .arboptimizerbase import ArbOptimizerBase, MargPOptimizerResult

class MargPPairOptimizer(ArbOptimizerBase):
    """
    implements the marginal price optimization method for pairs [API]
    """
    __VERSION__ = __VERSION__
    __DATE__ = __DATE__
    
    MargPOptimizerResult = MargPOptimizerResult
    
    @property
    def kind(self):
        return "margp_pair"
    
    PAIROPTIMIZEREPS = 1e-15
    
    class SO(Enum):
        """desired result types for the optimizer (``enum``)"""
        DXDYVECFUNC = "dxdyvecfunc"
        DXDYSUMFUNC = "dxdysumfunc"
        DXDYVALXFUNC = "dxdyvalxfunc"
        DXDYVALYFUNC = "dxdyvalyfunc"
        PMAX = "pmax"
        GLOBALMAX = "globalmax"
        TARGETTKN = "targettkn"
    
    def optimize(self, targettkn=None, result=None, *, params=None):
        """
        a marginal price optimizer that works only on curves on one pair [API]

        :result:            determines what to return (see table below)
        :targettkn:         token to optimize for (if ``result==SO.TARGETTKN``); must be ``None`` if
                            ``result==SO.GLOBALMAX``; result defaults to the corresponding value
                            depending on whether or not ``targettkn`` is ``None``
        :params:            ``dict`` of parameters
        :eps:               accuracy parameter passed to ``bisection`` method (default: 1e-6)
        :returns:           depending on the `result` parameter 

        ===================     ==============================================================================      
        ``result``              returns
        ===================     ==============================================================================      
        ``SO.DXDYVECFUNC``      function of ``p`` returning vector of dx,dy values                                     
        ``SO.DXDYSUMFUNC``      function of ``p`` returning sum of dx,dy values                                        
        ``SO.DXDYVALXFUNC``     function of ``p`` returning value of dx,dy sum in units of ``tknx``                       
        ``SO.DXDYVALYFUNC``     ditto tkny                                                                        
        ``SO.TARGETTKN``        optimizes for one token, the other is zero
        ``SO.PMAX``             optimal ``p`` value for global max (1)                                                 
        ``SO.GLOBALMAX``        global max of ``sum dx*p + dy`` (1)                                                    
        ``None``                ``SO.TARGETTKN``                                         
        ===================     ==============================================================================      

        NOTE 1: the modes ``SO.PMAX`` and ``SO.GLOBALMAX`` are deprecated and the code may or 
        may not be working properly; if every those functions are needed they need to 
        be reviewed and tests need to be added (most tests have been disabled)
        """
        result = result or self.SO.TARGETTKN
        assert not result == self.SO.PMAX, "mode PMAX no longer supported"
        assert not result == self.SO.GLOBALMAX, "mode GLOBALMAX no longer supported"
        
        start_time = time.time()
        if params is None:
            params = dict()
        curves_t = CPCInverter.wrap(self.CC)
        assert len(curves_t) > 0, "no curves found"
        c0 = curves_t[0]
        #print("[MargPPairOptimizer.optimize] curves_t", curves_t[0].pair)
        pairs = set(c.pair for c in curves_t)
        assert (len(pairs) == 1), f"pair_optimizer only works on curves of exactly one pair [{pairs}]"
        assert not (targettkn is None and result == self.SO.TARGETTKN), "targettkn must be set if result==SO.TARGETTKN"
        assert not (targettkn is not None and result == self.SO.GLOBALMAX), f"targettkn must be None if result==SO.GLOBALMAX [{targettkn}]"

        dxdy = lambda r: (np.array(r[0:2]))

        dxdyfromp_vec_f = lambda p: tuple(dxdy(c.dxdyfromp_f(p)) for c in curves_t)
        if result == self.SO.DXDYVECFUNC:
            return dxdyfromp_vec_f

        dxdyfromp_sum_f = lambda p: sum(dxdy(c.dxdyfromp_f(p)) for c in curves_t)
        if result == self.SO.DXDYSUMFUNC:
            return dxdyfromp_sum_f

        dxdyfromp_valy_f = lambda p: np.dot(dxdyfromp_sum_f(p), np.array([p, 1]))
        if result == self.SO.DXDYVALYFUNC:
            return dxdyfromp_valy_f

        dxdyfromp_valx_f = lambda p: dxdyfromp_valy_f(p) / p
        if result == self.SO.DXDYVALXFUNC:
            return dxdyfromp_valx_f

        if result is None:
            if targettkn is None:
                result = self.SO.GLOBALMAX
            else:
                result = self.SO.TARGETTKN

        if result == self.SO.GLOBALMAX or result == self.SO.PMAX:
            p_avg = np.mean([c.p for c in curves_t])
            p_optimal = self._findmax(dxdyfromp_valx_f, p_avg)
            #opt_result = dxdyfromp_valx_f(float(p_optimal))
            full_result = dxdyfromp_sum_f(float(p_optimal))
            opt_result  = full_result[0]
            if result == self.SO.PMAX:
                return p_optimal
            if targettkn == c0.tknx:
                p_optimal_t = (1/float(p_optimal),)
            else:
                p_optimal_t = (float(p_optimal),)
            #method = "globalmax-pair"
        
        elif result == self.SO.TARGETTKN:
            p_min = np.min([c.p for c in curves_t])
            p_max = np.max([c.p for c in curves_t])
            eps = params.get("eps", self.PAIROPTIMIZEREPS)
            
            assert targettkn in {c0.tknx, c0.tkny,}, f"targettkn {targettkn} not in {c0.tknx}, {c0.tkny}"
            
            # we are now running a _goalseek == 0 on the token that is NOT the target token
            if targettkn == c0.tknx:
                othertkn = c0.tkny
                func = lambda p: dxdyfromp_sum_f(p)[1]
                p_optimal = self._goalseek(func, p_min * 0.99, p_max * 1.01, eps=eps)
                p_optimal_val = 1/float(p_optimal)
                full_result = dxdyfromp_sum_f(float(p_optimal))
                opt_result  = full_result[0]
                
            else:
                othertkn = c0.tknx
                func = lambda p: dxdyfromp_sum_f(p)[0]
                p_optimal = self._goalseek(func, p_min * 0.99, p_max * 1.01, eps=eps)
                p_optimal_val = float(p_optimal)
                full_result = dxdyfromp_sum_f(float(p_optimal))
                opt_result = full_result[1]
            #print("[MargPPairOptimizer.optimize] p_optimal", p_optimal, "full_result", full_result)
        
        else:
            raise ValueError(f"unknown result type {result}")
        
        if p_optimal.is_error:
            return self.MargPOptimizerResult(
                method=self.kind,
                O=self,
                time=time.time() - start_time,
                targettkn=targettkn,
                curves=curves_t,
                #n_iterations=None,
                errormsg="bisection did not converge",
            )

        p_optimal_d = {othertkn: p_optimal_val, targettkn: 1.0}
        return self.MargPOptimizerResult(
            method=self.kind,
            O=self,
            result=opt_result,
            time=time.time() - start_time,
            targettkn=targettkn,
            curves=curves_t,
            p_optimal = p_optimal_d,
            #dtokens={c0.tknx:full_result[0], c0.tkny:full_result[1]},
            #n_iterations=None, # not available
        )
    