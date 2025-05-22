"""
config.py
API client configuration: base URL, timeouts, global parameters, etc.
"""

RPC_URL = 'https://rpc.qubic.org/v1'

CORE_URL = 'https://api.qubic.org/v1'

MONERO_URL = 'https://xmr-stats.qubic.org' # This URL is only used to obtain monero mining stats.

TIMEOUT = 5

HEADERS = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}