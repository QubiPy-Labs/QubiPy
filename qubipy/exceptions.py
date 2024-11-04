"""
exceptions.py
This file defines custom exceptions specific to the Qubic API,
allowing for clearer handling of errors and failure messages.
"""

class QubiPy_Exceptions(Exception):
    
    """Custom exceptions for the class"""

    INVALID_TICK_ERROR = 'You need to enter a valid tick number'

    TICK_NOT_COMPATIBLE = 'Your tick is incompatible, the tick must be higher than the current tick'

    INVALID_ADDRESS_ID = 'You need to enter a valid address ID.'

    INVALID_TX_ID = 'You need to enter a valid tx ID'

    INVALID_START_TICK_AND_END_TICK = 'You need to enter a valid starting tick and a valid ending tick'
    
    INVALID_EPOCH = 'You need to enter a valid epoch'

    INVALID_JSON_RESPONSE = 'Invalid JSON response from the API.'

    INVALID_EPOCH = 'You need to enter a valid epoch'

    INVALID_PAGES = 'Page size must be between 1 and 100'

    INVALID_DATA_FORMAT = 'Invalid data format detected, please try again'

    INVALID_BET_ID = 'Invalid bet ID, try again'

    INVALID_BET_OPTIONS = 'Invalid bet options and bet ID'

    INVALID_QX_ASSET_DATA = 'Invalid QX data, check your asset name, issuer id and offest'

    INVALID_DATA_VALUE = 'Invalid data, enter an integer'
