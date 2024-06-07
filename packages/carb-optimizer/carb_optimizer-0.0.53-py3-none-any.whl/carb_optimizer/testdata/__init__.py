"""testdata module"""

from .curves1 import curves_dct_f as curves1_dct_f


def curves_dct_to_tuple_keys(curves_dct):
    """
    converts curves ``dict`` with ``str`` keys to ``tuple`` keys
    
    EXAMPLE
    
    ::

        curves_dct = {'a_b': 1, 'c_d': 2}
        curves_tdct curves_dct_to_tuple_keys(curves_dct)
        assert curves_tdct == {('a', 'b'): 1, ('c', 'd'): 2}
    """
    return {tuple(k.split("_")): v for k,v in curves_dct.items()}

def curves_dct_to_names_dct(curves_dct):
    """
    creates a ``dict`` associating the original keys to the new ``tuple`` keys
    
    EXAMPLE
    
    ::
    
        curves_dct = {'a_b': 1, 'c_d': 2}
        curves_keys = curves_dct_to_tuple_keys(curves_dct)
        assert curves_keys == {('a', 'b'): "a_b", ('c', 'd'): "c_d"}
    """
    return {tuple(k.split("_")): k for k,v in curves_dct.items()}
