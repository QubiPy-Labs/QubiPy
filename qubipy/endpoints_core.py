"""
endpoints_core.py
Defines the endpoints used by the Qubic CORE API.
This facilitates the centralization of routes and their possible future update.
"""

COMPUTORS = '/core/getComputors'

ENTITY_INFO = '/core/getEntityInfo'

TICK_DATA = '/core/getTickData'

TICK_INFO = '/core/getTickInfo'

TICK_QUORUM_VOTE = '/core/getTickQuorumVote'

TICK_TRANSACTIONS = '/core/getTickTransactions'

# QUOTTERY SERVICE

ACTIVE_BETS = '/quottery/getActiveBets'

ACTIVE_BETS_BY_CREATOR = '/quottery/getActiveBetsByCreator'

BASIC_INFO = '/quottery/getBasicInfo'

BET_INFO = '/quottery/getBetInfo'

BETTORS_BY_BET_OPTIONS = '/quottery/getBettorsByBetOption'