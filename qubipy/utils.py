"""
utils.py
Auxiliary functions for validations, data formatting, response handling, etc.
Example: input parameter validation or API response cleanup.
"""
from qubipy.exceptions import *

def check_pages_format(page_1: int, page_2: int):

    """
    Validates the format and range of the given page numbers.

    Args:
        page_1 (int): The first page number to validate. Must be an integer between 0 and 100.
        page_2 (int): The second page number to validate. Must be an integer between 0 and 100.

    Raises:
        QubiPy_Exceptions: If either page_1 or page_2 is not an integer or falls outside the allowed range (0-100).
    """

    if not isinstance(page_1, int) or not isinstance(page_2, int):
        raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_DATA_FORMAT)

    if page_1 < 0 or page_2 < 0 or page_1 > 100 or page_2 > 100:
        raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_PAGES)

def check_ticks_format(start_tick: int, end_tick: int):

    """
    Validates the format and values of the given tick range.

    Args:
        start_tick (int): The starting tick to validate. Must be a positive integer.
        end_tick (int): The ending tick to validate. Must be a positive integer.

    Raises:
        QubiPy_Exceptions: If either start_tick or end_tick is not an integer, or if their values are less than or equal to zero.
    """

    if not isinstance(start_tick, int) or not isinstance(end_tick, int):
        raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_DATA_FORMAT)
    
    if start_tick <= 0 or end_tick <= 0:
        raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_START_TICK_AND_END_TICK)
    

def check_index(index):
    """
    Validates that the string representation of the input represents
    a non-negative integer index (composed only of digits).

    This function handles inputs that might be integers or strings
    representing non-negative integers. It converts the input to its
    string form and checks if this string is non-empty and contains
    only decimal digits.

    Args:
        index: The input value to validate. Expected to be a value
               whose string representation is a non-empty sequence of digits.

    Raises:
        QubiPy_Exceptions.INVALID_INDEX: If the string representation of the
                                         input is empty or contains any
                                         character that is not a decimal digit.
    """

    format_index = str(index)

    if not format_index or not format_index.isdigit():
        raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_INDEX)


def is_tx_bytes_invalid(tx: bytes) -> bool:
    """
    Validates that the input transaction data is in bytes format.

    Args:
        tx (bytes): The transaction data to validate. Must be of type bytes or bytearray
                   and not empty.

    Returns:
        bool: True if the transaction data is invalid, False if valid
    """
    return not isinstance(tx, (bytes, bytearray)) or len(tx) == 0

   
def is_wallet_id_invalid(wallet_id: str) -> bool:
    """
    Checks if the provided wallet ID is invalid.

    Args:
        wallet_id (str): The wallet ID to validate. Must be exactly 60 characters long.

    Returns:
        bool: True if the wallet ID is invalid, False if valid
    """
    return not isinstance(wallet_id, str) or len(wallet_id) != 60 or not wallet_id.isalpha()