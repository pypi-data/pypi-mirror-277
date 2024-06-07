"""
This module defines the ``DCBase`` class, a convenient base class for ``dataclass`` objects.
"""

from dataclasses import asdict, fields
import pandas as pd

class DCBase:
    """
    base class for all ``dataclass`` objects, adding some useful methods
    
    USAGE
    
    .. code-block:: python
    
        @dataclass
        class MyDataClass(DCBase):
            ...
        
        myobj = MyDataClass(...)
        myobj.as_dict()
        myobj.as_tuple()
        myobj.fields()
        ...
    """

    def as_dict(self, *, exclude=None, include=None, dct=None):
        """
        converts this dataclass object to a ``dict``

        :include:   comprehensive list of fields to include in the DataFrame (default: all fields)
        :exclude:   list of fields to exclude from the DataFrame (applied AFTER include)
        :dct:       dict used instead of contents of the dataclass (useful for subclasses
                    that want to add additional fields to the dict)
        """
        if dct is None:
            dct = asdict(self)
        if not include is None:
            dct = {k: dct[k] for k in include}
        if not exclude is None:
            dct = {k: dct[k] for k in dct if not k in exclude}
        return dct
    
    def as_tuple(self, **kwargs):
        """
        converts this dataclass object to a ``tuple``
        
        NOTE: parameters are passed to ``as_dict``; returns ``dct.values()`` as ``tuple``
        """
        return tuple(self.as_dict(**kwargs).values())

    
    def as_df(self, *, index=None, **kwargs):
        """
        converts this object to a DataFrame (kwargs are passed to asdict)

        :index:     the index of the DataFrame (default: None)
        """
        dct = self.as_dict(**kwargs)
        try:
            df = pd.DataFrame([dct])
            if not index is None:
                df.set_index(index, inplace=True)
            return df
        except Exception as e:
            return f"ERROR: {e}"
        
    @classmethod
    def l2df(cls, lst, **kwargs):
        """
        converts an iterable of dataclass objects to ``DataFrame`` objects and concatenates them

        :lst:       an iterable of dataclass objects
        :kwargs:    passed to the as_df method of each object in the list
        :returns:   a DataFrame, or an error message if the conversion fails
        """
        try:
            return pd.concat([x.as_df(**kwargs) for x in lst])
        except Exception as e:
            return f"ERROR: {e}"
        
        
    def fields(self):
        """returns the fields of this dataclass object"""
        return fields(self)



