"""
rpc_client.py
This file contains the main QubiPy_RPC Client class which handles
the interaction with the Qubic API, making HTTP requests and handling responses.
"""

import requests
from typing import Dict, Any
import json

from qubipy.exceptions import *
from qubipy.config import *
from qubipy.endpoints_rpc import *
from qubipy.utils import *
import base64
import json

class QubiPy_RPC:
    def __init__(self, rpc_url: str = RPC_URL, timeout=TIMEOUT):
        self.rpc_url = rpc_url
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
            response = requests.get(f'{self.rpc_url}{LATEST_TICK}', headers=HEADERS, timeout=self.timeout)
            response.raise_for_status()  # Raise an exception for bad HTTP status codes
            data = response.json()
            return data.get('latestTick', {})
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f'Error when getting the last Tick: {str(E)}') from None
        
    def broadcast_transaction(self, tx: bytes) -> Dict[str, Any]:
        """
        Broadcasts a transaction to the Qubic network.

        Args:
            tx (bytes): The transaction data to broadcast as bytes.

        Returns:
            Dict[str, Any]: The response from the API after broadcasting the transaction.

        Raises:
            QubiPy_Exceptions: If there is an issue broadcasting the transaction.
        """
        tx_encoded = base64.b64encode(tx).decode('utf-8')
        payload = json.dumps({
            "encodedTransaction": tx_encoded
        })
        try:
            response = requests.post(
                f'{self.rpc_url}{BROADCAST_TRANSACTION}',
                data=payload,
                headers={'Content-Type': 'application/json'},
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as http_err:
            if response.status_code == 400:
                try:
                    error_response = response.json()
                    error_code = error_response.get('code')
                    error_message = error_response.get('message', '')
                    raise QubiPy_Exceptions(f"API Error {error_code}: {error_message}")
                except json.JSONDecodeError:
                    raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_JSON_RESPONSE)
            else:
                raise QubiPy_Exceptions(f'HTTP error occurred: {str(http_err)}') from None
        except requests.RequestException as e:
            raise QubiPy_Exceptions(f'Error broadcasting the transaction: {str(e)}') from None

    def get_approved_transaction_for_tick(self, tick: int | None = None) -> Dict[str, Any]:
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
    
        endpoint = APPROVED_TRANSACTIONS_FOR_TICK.format(tick = tick)

        try:
            response = requests.get(f'{self.rpc_url}{endpoint}', headers=HEADERS, timeout=TIMEOUT)
            response.raise_for_status()
            data = response.json()
            return data.get('approvedTransactions', {})

        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the approved transactions from the API: {str(E)}") from None
    
    def get_balance(self, wallet_id: str | None = None) -> Dict[str, Any]:

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
            response = requests.get(f'{self.rpc_url}{endpoint}', headers=HEADERS, timeout=self.timeout)
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
            response = requests.get(f'{self.rpc_url}{STATUS}', headers=HEADERS, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data  
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the RPC status: {str(E)}") from None
    
    def get_chain_hash(self, tick_number: int | None = None) -> Dict[str, Any]:

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
            response = requests.get(f'{self.rpc_url}{endpoint}', headers=HEADERS, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get('hexDigest', {})
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the chain hash: {str(E)}") from None
    
    def get_quorum_tick_data(self, tick_number: int | None = None) -> Dict[str, Any]:

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
            response = requests.get(f'{self.rpc_url}{endpoint}', headers=HEADERS, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the quorum tick data: {str(E)}") from None

    def get_store_hash(self, tick_number: int | None = None) -> Dict[str, Any]:

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
            response = requests.get(f'{self.rpc_url}{endpoint}', headers=HEADERS, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the store hash: {str(E)}") from None
    
    def get_transaction(self, tx_id: str | None = None) -> Dict[str, Any]:

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
            response = requests.get(f'{self.rpc_url}{endpoint}', headers=HEADERS, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get('transaction', {})
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the transaction data: {str(E)}") from None
    
    def get_transaction_status(self, tx_id: str | None = None) -> Dict[str, Any]:

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
            response = requests.get(f'{self.rpc_url}{endpoint}', headers=HEADERS, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get('transactionStatus', {})
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the transaction status: {str(E)}") from None
    
    def get_transfer_transactions_per_tick(self, identity: str | None = None, start_tick: int | None = None, end_tick: int | None = None) -> Dict[str, Any]:

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
    
        
        if not start_tick or not end_tick:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_START_TICK_AND_END_TICK)
        
        check_ticks_format(start_tick, end_tick)
        
        endpoint = TRANSFER_TRANSACTIONS_PER_TICK.format(id = identity)

        payload = {
            'startTick': start_tick,
            'endTick': end_tick
        }

        try:
            response = requests.get(f'{self.rpc_url}{endpoint}', headers=HEADERS, params=payload, timeout=self.timeout)
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
            response = requests.get(f'{self.rpc_url}{endpoint}', headers=HEADERS, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the health check: {str(E)}") from None
    
    def get_computors(self, epoch: int | None = None) -> Dict[str, Any]:

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
            response = requests.get(f'{self.rpc_url}{endpoint}', headers=HEADERS, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get('computors', {})
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the computors: {str(E)}") from None
    
    
    def query_smart_contract(self, contract_index: int | None = None, input_type: int | None = None, input_size: int | None = None, request_Data: str | None = None) -> Dict[str, Any]:
        """
        Query a smart contract to the Qubic network
        
        Args:
            contractIndex (Optional[int], optional): Contract Index to query
            inputType (Optional[int], optional): Input type to query
            inputSize (Optional[int], optional): The input size to query
            requestData (Optional[str], optional): The request data to query the smart contract
            
        Returns:
            Dict[str, Any]: The response from the API after querying the smart contract.
            
        Raises:
            QubiPy_Exceptions: If the request data is invalid base64 encoded string.
            QubiPy_Exceptions: If there is an issue querying the smart contract (e.g., network error, invalid response, or timeout).
        """
        
        request_Data_encoded = base64.b64encode(request_Data.encode('utf-8')).decode('utf-8')

        payload = {
            "contractIndex": contract_index,
            "inputType": input_type,
            "inputSize": input_size,
            "requestData": request_Data_encoded
        }
        
        try:
            response = requests.post(f'{self.rpc_url}{QUERY_SC}', headers=HEADERS, json=payload, timeout=TIMEOUT)
            response.raise_for_status()
            data = response.json()
            return data.get('responseData', {})
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to query SC: {str(E)}") from None


    def get_tick_info(self) -> Dict[str, Any]:

        """
        Retrieves information about the current tick from the API.

        Returns:
            Dict[str, Any]: A dictionary containing the tick information. If no tick information is found, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """

        try:
            response = requests.get(f'{self.rpc_url}{TICK_INFO}', headers=HEADERS, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get('tickInfo', {})
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the tick info data: {str(E)}") from None
    
    def get_issued_assets(self, identity: str | None = None) -> Dict[str, Any]:

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
            response = requests.get(f'{self.rpc_url}{endpoint}', headers=HEADERS, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get('issuedAssets', {})
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the list of assets issued by a specific identity: {str(E)}") from None
    
    def get_owned_assets(self, identity: str | None = None) -> Dict[str, Any]:

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
            response = requests.get(f'{self.rpc_url}{endpoint}', headers=HEADERS, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get('ownedAssets', {})
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the owned assets: {str(E)}") from None
    
    def get_possessed_assets(self, identity: str | None = None) -> Dict[str, Any]:

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
            response = requests.get(f'{self.rpc_url}{endpoint}', headers=HEADERS, timeout=self.timeout)
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
            response = requests.get(f'{self.rpc_url}{BLOCK_HEIGHT}', headers=HEADERS, timeout=self.timeout)
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
            response = requests.get(f'{self.rpc_url}{LATEST_STATS}', headers=HEADERS, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get('data', {})
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the latest stats from the RPC Server: {str(E)}") from None
    

    def get_rich_list(self, page_1: int | None = None, page_size: int | None = None) -> Dict[str, Any]:

        """
        Retrieves the rich list from the RPC server based on the provided page and page size.

        Args:
            page_1 (Optional[int], optional): The page number to retrieve. Must be a positive integer.
            page_size (Optional[int], optional): The number of entries per page. Must be a positive integer.

        Returns:
            Dict[str, Any]: A dictionary containing the rich list data. If no data is available, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If page_1 or page_size are not provided or are invalid, 
                            or if there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """

        if not page_1 or not page_size:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_PAGES)
        
        check_pages_format(page_1, page_size)
        
        payload = {
            'page': page_1,
            'pageSize': page_size
        }

        try:
            response = requests.get(f'{self.rpc_url}{RICH_LIST}', params=payload, headers=HEADERS, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get('richList', {})
        except requests.exceptions.RequestException as E:
            raise QubiPy_Exceptions(f"Failed to retrieve the rich list: {str(E)}") from None