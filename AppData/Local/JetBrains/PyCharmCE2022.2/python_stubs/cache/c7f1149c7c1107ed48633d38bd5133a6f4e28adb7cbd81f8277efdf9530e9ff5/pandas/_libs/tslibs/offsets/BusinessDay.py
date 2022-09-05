# encoding: utf-8
# module pandas._libs.tslibs.offsets
# from C:\Users\nicon\PycharmProjects\pythonProject\venv\lib\site-packages\pandas\_libs\tslibs\offsets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import operator as operator # C:\Users\nicon\AppData\Local\Programs\Python\Python310\lib\operator.py
import re as re # C:\Users\nicon\AppData\Local\Programs\Python\Python310\lib\re.py
import time as time # <module 'time' (built-in)>
import warnings as warnings # C:\Users\nicon\AppData\Local\Programs\Python\Python310\lib\warnings.py
import numpy as np # C:\Users\nicon\PycharmProjects\pythonProject\venv\lib\site-packages\numpy\__init__.py
from pandas._libs.properties import cache_readonly

from pandas._libs.tslibs.timedeltas import Timedelta

from pandas._libs.tslibs.timestamps import Timestamp


from .BusinessMixin import BusinessMixin

class BusinessDay(BusinessMixin):
    """ DateOffset subclass representing possibly n business days. """
    def apply_index(self, *args, **kwargs): # real signature unknown
        pass

    def is_on_offset(self, *args, **kwargs): # real signature unknown
        pass

    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def _apply_array(self, *args, **kwargs): # real signature unknown
        pass

    def _offset_str(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    _attributes = (
        'n',
        'normalize',
        'offset',
    )
    _period_dtype_code = 5000
    _prefix = 'B'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000025BC9C23B70>'


