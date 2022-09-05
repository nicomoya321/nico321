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


from .type import type

class OffsetMeta(type):
    """
    Metaclass that allows us to pretend that all BaseOffset subclasses
        inherit from DateOffset (which is needed for backward-compatibility).
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def __instancecheck__(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def __subclasscheck__(cls, *args, **kwargs): # real signature unknown
        pass


