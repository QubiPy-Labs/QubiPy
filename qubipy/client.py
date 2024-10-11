"""
client.py
This file contains the main QubicAPIClient class which handles
the interaction with the Qubic API, making HTTP requests and handling responses.
"""

import requests
from typing import Optional, Dict, Any
import json
from exceptions import QubiPy_Exceptions
from endpoints import *

class QubiPy:
    def __init__(self, base_url: str = BASE_URL, timeout=5):
        self.base_url = base_url
        self.timeout = timeout
    
    def get_latest_tick(self) -> Dict[str, Any]:
        """
        Retrieves the latest tick (block height) from the API.
        
        Returns:
            Dict[str, Any]: A dictionary containing the latest tick information or an error message if no tick is found.
        
        Raises:
            QubiPy_Exceptions: If there is an issue retrieving the tick from the API.
        """

        try:
            response = requests.get(f'{self.base_url}{LATEST_TICK}', timeout=self.timeout)
            response.raise_for_status()  # Raise an exception for bad HTTP status codes
            data = response.json()
            return data.get('latestTick', 'No tick found')
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f'Error when getting the last Tick: {str(E)}') from None
        
    def broadcast_transaction(self):
        pass

    def get_approved_transaction_for_tick(self, tick: Optional[int] = None) -> Dict[str, Any]:
        """
        Retrieves the approved transactions for a specific tick (block height) from the API.

        Args:
            tick (Optional[int]): The tick number for which to retrieve approved transactions. If not provided, an exception is raised.

        Returns:
            Dict[str, Any]: A dictionary containing the approved transactions for the given tick. If no approved transactions are found, the key 'approvedTransactions' may be None or an empty dictionary.

        Raises:
            QubiPy_Exceptions: If the tick number is not provided or invalid.
            QubiPy_Exceptions: If there is an issue with the API request (e.g., network error or invalid response).
    """

        if not tick:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_TICK_ERROR)
    
        endpoint = APPROVED_TRANSACTIONS_FOR_TICK.format(tick_number = tick)

        try:
            response = requests.get(f'{self.base_url}{endpoint}')
            response.raise_for_status()
            data = response.json()
            return data.get('approvedTransactions')

        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the approved transactions from the API: {str(E)}") from None
    
    def get_balance(self, wallet_id: str = None) -> Dict[str, Any]:
        
        if not wallet_id:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_ADDRESS_ID)


        endpoint = WALLET_BALANCE.format(id = wallet_id)

        try:
            response = requests.get(f'{self.base_url}{endpoint}', timeout=self.timeout)
            response.raise_for_status()  # Raise an exception for bad HTTP status codes
            data = response.json()
            return data.get('balance')
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the balance data from the API, check the address ID and try again: {str(E)}") from None
    
    def get_rpc_status(self) -> Dict[str, Any]:

        try:
            response = requests.get(f'{self.base_url}{STATUS}', timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data  
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the RPC status: {str(E)}") from None
    
    def get_chain_hash(self, tick_number: Optional[int] = None) -> Dict[str, Any]:

        if not tick_number:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_TICK_ERROR)
        
        endpoint = CHAIN_HASH.format(tick = tick_number)

        try:
            response = requests.get(f'{self.base_url}{endpoint}', timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get('hexDigest')
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the chain hash: {str(E)}") from None
    
    def get_quorum_tick_data(self, tick_number: Optional[int] = None) -> Dict[str, Any]:

        if not tick_number:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_TICK_ERROR)
        
        endpoint = QUORUM_TICK_DATA.format(tick = tick_number)

        try:
            response = requests.get(f'{self.base_url}{endpoint}', timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the quorum tick data: {str(E)}") from None

    def get_store_hash(self, tick_number: Optional[int] = None) -> Dict[str, Any]:
        if not tick_number:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_TICK_ERROR)
        
        endpoint = STORE_HASH.format(tick = tick_number)

        try:
            response = requests.get(f'{self.base_url}{endpoint}', timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the store hash: {str(E)}") from None
    
    def get_transaction(self, tx_id: Optional[str] = None) -> Dict[str, Any]:

        if not tx_id:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_TX_ID)
        
        endpoint = TRANSACTION.format(tx_id = tx_id)

        try:
            response = requests.get(f'{self.base_url}{endpoint}', timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get('transaction')
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the transaction data: {str(E)}") from None
    
    def get_transaction_status(self, tx_id: Optional[str] = None) -> Dict[str, Any]:

        if not tx_id:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_TX_ID)

        endpoint = TRANSACTION_STATUS.format(tx_id = tx_id)

        try:
            response = requests.get(f'{self.base_url}{endpoint}', timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get('transactionStatus')
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the transaction status: {str(E)}") from None
    
    def get_transfer_transactions_per_tick(self, identity: Optional[str] = None, startTick: Optional[str] = None, endTick: Optional[str] = None) -> Dict[str, Any]:

        if not identity:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_ADDRESS_ID)
    
        
        if not startTick or not endTick:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_START_TICK_AND_END_TICK)
        
        endpoint = TRANSFER_TRANSACTIONS_PER_TICK.format(id = identity)

        params = {
            'startTick': startTick,
            'endTick': endTick
        }

        try:
            response = requests.get(f'{self.base_url}{endpoint}', params=params, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the transfer transactions: {str(E)}") from None
    
    def get_health_check(self) -> Dict[str, Any]:

        endpoint = HEALTH_CHECK

        try:
            response = requests.get(f'{self.base_url}{endpoint}', timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the health check: {str(E)}") from None
    
    def get_computors(self, epoch: Optional[int] = None) -> Dict[str, Any]:

        if not epoch:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_EPOCH)
        
        endpoint = COMPUTORS.format(epoch = epoch)
        

        try:
            response = requests.get(f'{self.base_url}{endpoint}', timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get('computors')
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the computors: {str(E)}") from None

