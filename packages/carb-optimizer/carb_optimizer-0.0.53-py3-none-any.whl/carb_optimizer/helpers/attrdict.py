"""
This module defines the ``AttrDict`` class, a dictionary that allows for attribute-style access.
"""

class AttrDict(dict):
    """
    A dictionary that allows for attribute-style access
    
    see https://stackoverflow.com/questions/4984647/accessing-dict-keys-like-an-attribute
    """
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self
    
    def __getattr__(self, __name):
        return None
    
    # def __repr__(self):
    #     return f"AttrDict({super(AttrDict, self).__repr__(self)})"