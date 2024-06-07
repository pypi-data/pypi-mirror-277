"""base class for reading release info into other classes"""

from .release_number import __RELEASE_NUMBER__, __RELEASE_DATE__

from dataclasses import dataclass, field
class ReleaseInfo:
    """allows reading release info into the class"""
    _release_number: int = __RELEASE_NUMBER__
        # this is added as a member to the dataclass so that in case the dataclass
        # is serialized this info is included in the serialization; obviously this
        # number is considered read-only
        
        # the __RELEASE_DATE__ info is hardcoded into the `release_date_cm` class
        # method and into the `release_date` property as there is no need to 
        # serialize this (redundant) information
    
    @property
    def release_number(self):
        """
        returns the release number of the library in which this object was created
        """
        return self._release_number
    
    @classmethod
    def release_number_cm(cls):
        """like ``release_number`` but accessible as classmethod"""
        return cls._release_number
    
    @property
    def release_date(self):
        """
        returns the release date of the library in which this object was created
        """
        return self.release_date_cm()
    
    @classmethod
    def release_date_cm(cls):
        """like ``release_date`` but accessible as classmethod"""
        return __RELEASE_DATE__
    
    @classmethod 
    def version_str(cls, *, incl_class=False):
        """
        creates a full version string (1) including release number
        
        :incl_class:     if ``True`` (default), include the class name into the version string
        :returns:       the version string
        
        NOTE 1. This method requires the presence ot ``__VERSION__`` and ``__DATE__`` as 
        class attributes as they will be included into the version string.
        """
        v,d = cls.__VERSION__, cls.__DATE__
        rn, rd = cls.release_number_cm(), cls.release_date_cm()
        if incl_class:
            vstr = f"Version v{v}, {d}; release {rn})"
            vstr = f"{cls.__name__.split('.')[-1]} [{vstr}]"
        else:
            vstr = f"Version v{v} ({d}; release {rn})"
        return vstr
    
    