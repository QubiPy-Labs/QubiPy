"""
endpoints_core.py
Defines the endpoints used by the Qubic CORE API.
This facilitates the centralization of routes and their possible future update.
"""

# CORE SERVICE

CORE_COMPUTORS = '/core/getComputors'

ENTITY_INFO = '/core/getEntityInfo'

CORE_TICK_DATA = '/core/getTickData'

CORE_TICK_INFO = '/core/getTickInfo'

TICK_QUORUM_VOTE = '/core/getTickQuorumVote'

TICK_TRANSACTIONS = '/core/getTickTransactions'

TICK_TRANSACTION_STATUS = '/core/getTickTransactionsStatus'

# QUOTTERY SERVICE

ACTIVE_BETS = '/quottery/getActiveBets'

ACTIVE_BETS_BY_CREATOR = '/quottery/getActiveBetsByCreator'

BASIC_INFO = '/quottery/getBasicInfo'

BET_INFO = '/quottery/getBetInfo'

BETTORS_BY_BET_OPTIONS = '/quottery/getBettorsByBetOption'

# QX SERVICE

QX_ASSET_ASK_ORDERS = '/qx/getAssetAskOrders'

QX_ASSET_BID_ORDERS = '/qx/getAssetBidOrders'

QX_ENTITY_ASK_ORDERS = '/qx/getEntityAskOrders'

QX_ENTITY_BID_ORDERS = '/qx/getEntityBidOrders'

QX_FEES = '/qx/getFees'

# MONERO MINING STATS

MONERO_MINING_STATS = '/stats'