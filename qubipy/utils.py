"""
utils.py
Auxiliary functions for validations, data formatting, response handling, etc.
Example: input parameter validation or API response cleanup.
"""
from exceptions import *

def check_pages_format(page_1: int, page_2: int):

    if not isinstance(page_1, int) or not isinstance(page_2, int):
        raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_DATA_FORMAT)

    if page_1 < 0 or page_2 < 0 or page_1 > 100 or page_2 > 100:
        raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_PAGES)

def check_ticks_format(start_tick: int, end_tick: int):

    if not isinstance(start_tick, int) or not isinstance(end_tick, int):
        raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_DATA_FORMAT)
    
    if start_tick <= 0 or end_tick <= 0:
        raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_START_TICK_AND_END_TICK)
