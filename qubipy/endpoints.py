"""
endpoints.py
Defines the endpoints used by the Qubic API.
This facilitates the centralization of routes and their possible future update.
"""

BASE_URL = 'https://rpc.qubic.org/v1'

LATEST_TICK = '/latestTick'

BROADCAST_TRANSACTION = '/broadcast-transaction'

APPROVED_TRANSACTIONS_FOR_TICK = '/ticks/{tick_number}/approved-transactions'

TICK_DATA = '/ticks/{tick_number}/tick-data'

WALLET_BALANCE = '/balances/{wallet_id}'

STATUS = '/status'

CHAIN_HASH = '/ticks/{tick_number}/chain-hash'

QUORUM_TICK_DATA = '/ticks/{tick_number}/quorum-tick-data'

STORE_HASH = '/ticks/{tick_number}/store-hash'

TRANSACTION = '/transactions/{tx_id}'

TRANSACTION_STATUS = '/tx-status/{tx_id}'

TRANSFER_TRANSACTIONS_PER_TICK = '/identities/{identity}/transfer-transacions'

HEALTH_CHECK = '/healthcheck'

COMPUTORS = '/epochs/{epoch}/computors'

QUERY_SC = '/querySmartContract'

TICK_INFO = '/tick-info'

ISSUED_ASSETS = '/assets/{identity}/issued'

OWNED_ASSETS = '/assets/{identity}/owned'

POSSESSED_ASSETS = '/assets/{identity}/possessed'

BLOCK_HEIGHT = '/block-height'

LATEST_STATS = '/latest-stats'