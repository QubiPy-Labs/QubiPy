"""
client.py
This file contains the main QubiPy Client class which handles
the interaction with the Qubic API, making HTTP requests and handling responses.
"""

import requests
from typing import Optional, Dict, Any
import json
from exceptions import QubiPy_Exceptions
from endpoints import *
from config import *

class QubiPy:
    def __init__(self, base_url: str = BASE_URL, timeout=TIMEOUT):
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
            return data.get('approvedTransactions', {})

        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the approved transactions from the API: {str(E)}") from None
    
    def get_balance(self, wallet_id: str = None) -> Dict[str, Any]:

        """
        Retrieves the balance of a specific wallet from the API.

        Args:
            wallet_id (str, optional): The ID of the wallet for which to retrieve the balance. If not provided, an exception is raised.

        Returns:
            Dict[str, Any]: A dictionary containing the wallet balance. If no balance is found, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If the wallet ID is not provided or is invalid.
            QubiPy_Exceptions: If there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """
        
        if not wallet_id:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_ADDRESS_ID)


        endpoint = WALLET_BALANCE.format(id = wallet_id)

        try:
            response = requests.get(f'{self.base_url}{endpoint}', timeout=self.timeout)
            response.raise_for_status()  # Raise an exception for bad HTTP status codes
            data = response.json()
            return data.get('balance', {})
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the balance data from the API, check the address ID and try again: {str(E)}") from None
    
    def get_rpc_status(self) -> Dict[str, Any]:

        """
        Retrieves the current RPC status from the API.

        Returns:
            Dict[str, Any]: A dictionary containing the RPC status information. This typically includes server health, version, and other metadata.

        Raises:
            QubiPy_Exceptions: If there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """

        try:
            response = requests.get(f'{self.base_url}{STATUS}', timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data  
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the RPC status: {str(E)}") from None
    
    def get_chain_hash(self, tick_number: Optional[int] = None) -> Dict[str, Any]:

        """
        Retrieves the chain hash (hexadecimal digest) for a specific tick number from the API.

        Args:
            tick_number (Optional[int]): The tick number for which to retrieve the chain hash. If not provided, an exception is raised.

        Returns:
            Dict[str, Any]: A dictionary containing the chain hash. If no chain hash is found, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If the tick number is not provided or is invalid.
            QubiPy_Exceptions: If there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """

        if not tick_number:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_TICK_ERROR)
        
        endpoint = CHAIN_HASH.format(tick = tick_number)

        try:
            response = requests.get(f'{self.base_url}{endpoint}', timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get('hexDigest', {})
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the chain hash: {str(E)}") from None
    
    def get_quorum_tick_data(self, tick_number: Optional[int] = None) -> Dict[str, Any]:

        """
        Retrieves quorum data for a specific tick (block height) from the API.

        Args:
            tick_number (Optional[int]): The tick number for which to retrieve the quorum data. If not provided, an exception is raised.

        Returns:
            Dict[str, Any]: A dictionary containing the quorum data for the specified tick number. If no data is found, the dictionary may be empty.

        Raises:
            QubiPy_Exceptions: If the tick number is not provided or is invalid.
            QubiPy_Exceptions: If there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """

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

        """
        Retrieves the store hash for a specific tick (block height) from the API.

        Args:
            tick_number (Optional[int]): The tick number for which to retrieve the store hash. If not provided, an exception is raised.

        Returns:
            Dict[str, Any]: A dictionary containing the store hash data for the specified tick number. The structure of the dictionary is determined by the API response.

        Raises:
            QubiPy_Exceptions: If the tick number is not provided or is invalid.
            QubiPy_Exceptions: If there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """

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

        """
        Retrieves transaction data for a specific transaction ID from the API.

        Args:
            tx_id (Optional[str]): The transaction ID for which to retrieve data. If not provided, an exception is raised.

        Returns:
            Dict[str, Any]: A dictionary containing the transaction data associated with the specified transaction ID. If no transaction is found, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If the transaction ID is not provided or is invalid.
            QubiPy_Exceptions: If there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """

        if not tx_id:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_TX_ID)
        
        endpoint = TRANSACTION.format(tx_id = tx_id)

        try:
            response = requests.get(f'{self.base_url}{endpoint}', timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get('transaction', {})
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the transaction data: {str(E)}") from None
    
    def get_transaction_status(self, tx_id: Optional[str] = None) -> Dict[str, Any]:

        """
        Retrieves the status of a specific transaction using its transaction ID from the API.

        Args:
            tx_id (Optional[str]): The transaction ID for which to retrieve the status. If not provided, an exception is raised.

        Returns:
            Dict[str, Any]: A dictionary containing the status of the transaction associated with the specified transaction ID. If no status is found, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If the transaction ID is not provided or is invalid.
            QubiPy_Exceptions: If there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """

        if not tx_id:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_TX_ID)

        endpoint = TRANSACTION_STATUS.format(tx_id = tx_id)

        try:
            response = requests.get(f'{self.base_url}{endpoint}', timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get('transactionStatus', {})
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the transaction status: {str(E)}") from None
    
    def get_transfer_transactions_per_tick(self, identity: Optional[str] = None, startTick: Optional[str] = None, endTick: Optional[str] = None) -> Dict[str, Any]:

        """
        Retrieves transfer transactions for a specific identity within a specified range of ticks from the API.

        Args:
            identity (Optional[str]): The identity for which to retrieve transfer transactions. If not provided, an exception is raised.
            startTick (Optional[str]): The starting tick for the range of transactions. If not provided, an exception is raised.
            endTick (Optional[str]): The ending tick for the range of transactions. If not provided, an exception is raised.

        Returns:
            Dict[str, Any]: A dictionary containing the transfer transactions within the specified range of ticks for the given identity. 

        Raises:
            QubiPy_Exceptions: If the identity is not provided or is invalid.
            QubiPy_Exceptions: If either the startTick or endTick is not provided or is invalid.
            QubiPy_Exceptions: If there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """

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

        """
        Performs a health check on the API to verify its availability and status.

        Returns:
            Dict[str, Any]: A dictionary containing the health check status and related information from the API.

        Raises:
            QubiPy_Exceptions: If there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """

        endpoint = HEALTH_CHECK

        try:
            response = requests.get(f'{self.base_url}{endpoint}', timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the health check: {str(E)}") from None
    
    def get_computors(self, epoch: Optional[int] = None) -> Dict[str, Any]:

        """
        Retrieves computors associated with a specific epoch from the API.

        Args:
            epoch (Optional[int]): The epoch for which to retrieve computors. If not provided, an exception is raised.

        Returns:
            Dict[str, Any]: A dictionary containing the computors associated with the specified epoch. If no computors are found, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If the epoch is not provided or is invalid.
            QubiPy_Exceptions: If there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """

        if not epoch:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_EPOCH)
        
        endpoint = COMPUTORS.format(epoch = epoch)
        

        try:
            response = requests.get(f'{self.base_url}{endpoint}', timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get('computors', {})
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the computors: {str(E)}") from None
    
    def query_smart_contract(self) -> Dict[str, Any]:
        pass

    def get_tick_info(self) -> Dict[str, Any]:

        """
        Retrieves information about the current tick from the API.

        Returns:
            Dict[str, Any]: A dictionary containing the tick information. If no tick information is found, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """

        try:
            response = requests.get(f'{self.base_url}{TICK_INFO}', timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get('tickInfo', {})
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the tick info data: {str(E)}") from None
    
    def get_issued_assets(self, identity: Optional[int] = None) -> Dict[str, Any]:

        """
        Retrieves the list of assets issued by a specific identity from the API.

        Args:
            identity (Optional[int]): The identity for which to retrieve the issued assets. Raises an exception if not provided.

        Returns:
            Dict[str, Any]: A dictionary containing the issued assets for the specified identity. If no issued assets are found, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If the identity is not provided or invalid.
            QubiPy_Exceptions: If there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """

        if not identity:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_ADDRESS_ID)
        
        endpoint = ISSUED_ASSETS.format(identity = identity)

        try:
            response = requests.get(f'{self.base_url}{endpoint}', timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get('issuedAssets', {})
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the list of assets issued by a specific identity: {str(E)}") from None
    
    def get_owned_assets(self, identity: Optional[int] = None) -> Dict[str, Any]:

        """
        Retrieves the list of assets owned by a specific identity from the API.

        Args:
            identity (Optional[int]): The identity for which to retrieve the owned assets. Raises an exception if not provided.

        Returns:
            Dict[str, Any]: A dictionary containing the owned assets for the specified identity. If no owned assets are found, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If the identity is not provided or invalid.
            QubiPy_Exceptions: If there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """

        if not identity:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_ADDRESS_ID)
        
        endpoint = OWNED_ASSETS.format(identity = identity)

        try:
            response = requests.get(f'{self.base_url}{endpoint}', timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get('ownedAssets', {})
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the owned assets: {str(E)}") from None
    
    def get_possessed_assets(self, identity: Optional[int] = None) -> Dict[str, Any]:

        """
        Retrieves the list of assets possessed by a specific identity from the API.

        Args:
            identity (Optional[int]): The identity for which to retrieve the possessed assets. Raises an exception if not provided.

        Returns:
            Dict[str, Any]: A dictionary containing the possessed assets for the specified identity. If no possessed assets are found, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If the identity is not provided or invalid.
            QubiPy_Exceptions: If there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """
        
        if not identity:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_ADDRESS_ID)
        
        endpoint = POSSESSED_ASSETS.format(identity = identity)

        try:
            response = requests.get(f'{self.base_url}{endpoint}', timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get('possessedAssets', {})
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the possessed assets: {str(E)}") from None

    def get_block_height(self) -> Dict[str, Any]:

        """
        Retrieves the current block height from the API.

        Returns:
            Dict[str, Any]: A dictionary containing the current block height. 
                            If the block height is not found, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """

        try:
            response = requests.get(f'{self.base_url}{BLOCK_HEIGHT}', timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get('blockHeight', {})
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the block height: {str(E)}") from None
    
    def get_latest_stats(self) -> Dict[str, Any]:

        """
        Retrieves the latest statistics from the RPC server.

        Returns:
            Dict[str, Any]: A dictionary containing the latest statistics. 
                            If no statistics are found, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """

        try:
            response = requests.get(f'{self.base_url}{LATEST_STATS}', timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get('data', {})
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the latest stats from the RPC Server: {str(E)}") from None


if __name__ == '__main__':
    a = QubiPy()
    print(a.get_latest_tick())