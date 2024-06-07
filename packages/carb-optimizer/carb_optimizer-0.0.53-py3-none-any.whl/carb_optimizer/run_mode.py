"""
defines the ``RunMode`` enum, determining whether the optimizer is running in research or production mode

---
(c) Copyright Bprotocol foundation 2024. 
Licensed under MIT
"""
__VERSION__ = "1.0-alpha1" #TODO-RELEASE
__DATE__ = "17/May/2024+"

from enum import Enum
from dataclasses import dataclass, field

@dataclass
class RunModeType:
    """
    the run mode gates certain part of the code, depending on the mode of operation
    
    Run modes are
    
    ====================    =============================================================
    Mode                    Description
    ====================    =============================================================   
    ``PRODUCTION``          production mode (default); raises on gating violations
    ``PROD_DISPENSATIONS``  like ``PRODUCTION``, but allows excluding exceptional cases
                            that are still being dealt with
    ``PROD_WARNINGS``       like ``PRODUCTION``, but issues warnings instead of raising
    ``RESEARCH``            research mode; no gating, no warnings
    ====================    =============================================================
    
    Note that the `RunMode` object -- a singleton object instantiated in the `run_mode`
    module -- can be imported from the top level library and is therefore already imported 
    in sessions that import `interactive`. So a typical research notebook would start 
    
    ::
        from carb_optimizer.interactive import *
        RunMode.research()
    
    and from this point onwards all gating is disabled. Similarly, code that imports
    `testing` also imports `interactive` so here the same applies for NBTests:
    
    ::
        from carb_optimizer.testing import *
        RunMode.research()   
    
    Production code on the other hand should usually do nothing and just make 
    sure it does not run into gates.
    
    """
    __VERSION__ = __VERSION__
    __DATE__ = __DATE__
    
    class RUN_MODE(Enum):
        """Run mode (for gating; ``enum``)"""
        PRODUCTION = 1
        PROD_DISPENSATIONS = 2
        PROD_WARNINGS = 90
        RESEARCH = 100
    
    _run_mode: RUN_MODE = field(default=RUN_MODE.PRODUCTION, init=False, repr=True)
    # _is_set: bool = field(default=False, init=False, repr=True)
    
    # NOTE: the _is_set mechanism does not seem to work in tests; apparently when there is
    # more than one test running in a file the setter is called repeatedly, leading for the
    # test collection to fail. So we are not using it for now.
    
    def __post_init__(self):
        assert isinstance(self.run_mode, self.RUN_MODE), f"invalid run mode {self.run_mode}"
    
    class RunModeError(Exception):
        """run mode error base class"""
        pass
    
    # class IllegalParameterChangeError(RunModeError):
    #     """trying to illegally change parameters of the RunMode object"""
    #     pass
    
    class GatingError(RunModeError):
        """gating violation error"""
        pass
    
    @property
    def run_mode(self):
        return self._run_mode
    
    @run_mode.setter
    def run_mode(self, run_mode):
        """set the run mode"""
        assert isinstance(run_mode, self.RUN_MODE), f"invalid run mode {run_mode}"
        # if not self._is_set is False:
        #     raise self.IllegalParameterChangeError("run mode has already been set")
        self._run_mode = run_mode
        # self._is_set = True
        
    # @property
    # def is_set(self):
    #     return self._is_set
    
    # @is_set.setter
    # def is_set(self, value):
    #     raise self.IllegalParameterChangeError("not allowed to change the 'is_set' attribute")
    
    def research(self):
        """set the run mode to research"""
        self.run_mode = self.RUN_MODE.RESEARCH
        
    def assert_research_mode(self, message = None, *, dispensation=None):
        """
        asserts that the run mode is research
        
        :message:           a message to be printed in case of a gating violation
        :dispensation:      a string describing a registered dispensation
        """
        if self.run_mode == self.RUN_MODE.RESEARCH:
            return True
        
        if self.run_mode in [self.RUN_MODE.PRODUCTION, self.RUN_MODE.PROD_DISPENSATIONS]:
            raise self.GatingError(f"production mode gating violation: {message} ({self.run_mode})")
        
        if self.run_mode == self.RUN_MODE.PROD_WARNINGS:
            print(f"[WARNING] production mode gating violation {message} ({self.run_mode})")
            return False
    
RunMode = RunModeType()

def _research_mode_function():
    """a function that can be gated by the run mode"""
    RunMode.assert_research_mode("gated test function")
    print("succeeded calling research mode function")
    