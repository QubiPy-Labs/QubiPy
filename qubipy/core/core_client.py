"""
core_client.py
This file contains the main QubiPy_Core Client class which handles
the interaction with the Qubic API, making HTTP requests and handling responses.
"""

import requests
from typing import Dict, Any
import json

from qubipy.exceptions import *
from qubipy.config import *
from qubipy.endpoints_core import *
from qubipy.utils import *
import json

class QubiPy_Core:
    def __init__(self, core_url: str = CORE_URL, timeout=TIMEOUT):
        self.core_url = core_url
        self.timeout = timeout
    
    def get_computors(self) -> Dict[str, Any]:

        """
        Retrieves the list of computors from the core server.

        Returns:
            Dict[str, Any]: A dictionary containing the computors data from the server. 
                            If no data is retrieved, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If there is an issue with the API request, such as a network error, invalid response, or timeout.
        """

        try:
            response = requests.get(f'{self.core_url}{CORE_COMPUTORS}', timeout=self.timeout)
            response.raise_for_status()  # Raise an exception for bad HTTP status codes
            data = response.json()
            return data
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f'Error when getting computors: {str(E)}') from None
    
    def get_entity_info(self, id: str | None = None) -> Dict[str, Any]:

        """
        Retrieves information about a specific entity from the core server based on the provided entity ID.

        Args:
            id (Optional[str]): The ID of the entity to retrieve information for. Must be a valid string.
                                If no ID is provided, an exception is raised.

        Returns:
            Dict[str, Any]: A dictionary containing the entity's information. If no data is available, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If the provided ID is invalid or not provided, or if there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """
        
        if not id:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_ADDRESS_ID)

        payload = {
            'id': id
        }

        try:
            response = requests.post(f'{self.core_url}{ENTITY_INFO}', headers=HEADERS, json=payload, timeout=self.timeout)
            response.raise_for_status()  # Raise an exception for bad HTTP status codes
            data = response.json()
            return data
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f'Error when getting entity info: {str(E)}') from None

    
    def get_tick_data(self, tick: int | None = None) -> Dict[str, Any]:

        """
        Retrieves tick data from the core server for the specified tick value.

        Args:
            tick (Optional[int]): The tick value for which data is to be retrieved. Must be a positive integer.
                                If not provided, an exception is raised.

        Returns:
            Dict[str, Any]: A dictionary containing the tick data. If no data is available, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If the provided tick value is invalid or not provided, 
                            or if there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """

        if not tick:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_TICK_ERROR)


        payload = {
            "tick": tick
            }
        
        try:
            response = requests.post(f'{self.core_url}{CORE_TICK_DATA}', headers=HEADERS, json=payload, timeout=self.timeout)
            response.raise_for_status()  # Raise an exception for bad HTTP status codes
            data = response.json()
            return data
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f'Error when getting tick data: {str(E)}') from None
    
    
    def get_tick_info(self) -> Dict[str, Any]:

        """
        Retrieves general tick information from the core server.

        Returns:
            Dict[str, Any]: A dictionary containing the tick information. If no data is available, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If there is an issue with the API request, such as a network error, invalid response, or timeout.
        """

        try:
            response = requests.get(f'{self.core_url}{CORE_TICK_INFO}', headers=HEADERS, timeout=self.timeout)
            response.raise_for_status()  # Raise an exception for bad HTTP status codes
            data = response.json()
            return data
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f'Error when getting tick info: {str(E)}') from None
    
    def get_tick_quorum_vote(self, tick: int | None = None) -> Dict[str, Any]:

        """
        Retrieves quorum vote data for a specific tick from the core server.

        Args:
            tick (Optional[int]): The tick value for which quorum vote data is to be retrieved. Must be a positive integer.
                                If not provided, an exception is raised.

        Returns:
            Dict[str, Any]: A dictionary containing the quorum vote data for the specified tick. 
                            If no data is available, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If the provided tick value is invalid or not provided, 
                            or if there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """

        if not tick:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_TICK_ERROR)
        
        payload = {
            'tick': tick
        }

        try:
            response = requests.post(f'{self.core_url}{TICK_QUORUM_VOTE}', headers=HEADERS, json=payload, timeout=self.timeout)
            response.raise_for_status()  # Raise an exception for bad HTTP status codes
            data = response.json()
            return data
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f'Error when getting tick quorum vote: {str(E)}') from None
    
    def get_tick_transactions(self, tick: int | None = None) -> Dict[str, Any]:

        """
        Retrieves transaction data for a specific tick from the core server.

        Args:
            tick (Optional[int]): The tick value for which transaction data is to be retrieved. Must be a positive integer.
                                If not provided, an exception is raised.

        Returns:
            Dict[str, Any]: A dictionary containing the transactions for the specified tick. 
                            If no transactions are found, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If the provided tick value is invalid or not provided, 
                            or if there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """

        if not tick:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_TICK_ERROR)
        
        payload = {
            'tick': tick
        }

        try:
            response = requests.post(f'{self.core_url}{TICK_TRANSACTIONS}', headers=HEADERS, json=payload, timeout=self.timeout)
            response.raise_for_status()  # Raise an exception for bad HTTP status codes
            data = response.json()
            return data.get('transactions', {})
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f'Error when getting tick transactions: {str(E)}') from None
        
    def get_tick_transactions_status(self, tick: int | None = None) -> Dict[str, Any]:

        """
        Retrieves the status of transactions for a specific tick from the core server.

        Args:
            tick (Optional[int]): The tick value for which the transaction status is to be retrieved. Must be a positive integer.
                                If not provided, an exception is raised.

        Returns:
            Dict[str, Any]: A dictionary containing the status of transactions for the specified tick. 
                            If no status data is available, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If the provided tick value is invalid or not provided, 
                            or if there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """

        if not tick:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_TICK_ERROR)
        
        payload = {
            'tick': tick
        }

        try:
            response = requests.post(f'{self.core_url}{TICK_TRANSACTION_STATUS}', headers=HEADERS, json=payload, timeout=self.timeout)
            response.raise_for_status()  # Raise an exception for bad HTTP status codes
            data = response.json()
            return data
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f'Error when getting tick transaction status: {str(E)}') from None
        
    """ QUOTTERY SERVICES """

    def get_active_bets(self) -> Dict[str, Any]:

        """
        Retrieves the list of active bets from the core server.

        Returns:
            Dict[str, Any]: A dictionary containing the active bets data. 
                            If no data is available, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If there is an issue with the API request, such as a network error, invalid response, or timeout.
        """

        try:
            response = requests.get(f'{self.core_url}{ACTIVE_BETS}', headers=HEADERS, timeout=self.timeout)
            response.raise_for_status()  # Raise an exception for bad HTTP status codes
            data = response.json()
            return data
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f'Error when getting active bets: {str(E)}') from None
    
    def get_active_bets_by_creator(self, creator_id: str | None = None) -> Dict[str, Any]:

        """
        Retrieves the list of active bets created by a specific creator from the core server.

        Args:
            creator_id (Optional[str]): The ID of the creator whose active bets are to be retrieved. 
                                        Must be a valid string. If not provided, an exception is raised.

        Returns:
            Dict[str, Any]: A dictionary containing the active bets created by the specified creator. 
                            If no data is available, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If the provided creator ID is invalid or not provided, 
                            or if there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """

        if not creator_id:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_ADDRESS_ID)
        
        payload = {
            'creatorId': creator_id
        }


        try:
            response = requests.get(f'{self.core_url}{ACTIVE_BETS_BY_CREATOR}', headers=HEADERS, params=payload, timeout=self.timeout)
            response.raise_for_status()  # Raise an exception for bad HTTP status codes
            data = response.json()
            return data
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f'Error when getting active bets by creator: {str(E)}') from None
    
    def get_basic_info(self) -> Dict[str, Any]:

        """
        Retrieves basic information from the core server.

        Returns:
            Dict[str, Any]: A dictionary containing the basic information data.
                            If no data is available, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If there is an issue with the API request, such as a network error, invalid response, or timeout.
        """

        try:
            response = requests.get(f'{self.core_url}{BASIC_INFO}', headers=HEADERS, timeout=self.timeout)
            response.raise_for_status()  # Raise an exception for bad HTTP status codes
            data = response.json()
            return data
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f'Error when getting basic info: {str(E)}') from None
    
    def get_bet_info(self, bet_id: int | None = None) -> Dict[str, Any]:

        """
        Retrieves information about a specific bet using its ID from the core server.

        Args:
            bet_id (Optional[int]): The ID of the bet to retrieve information for. 
                                    Must be a positive integer. If not provided, an exception is raised.

        Returns:
            Dict[str, Any]: A dictionary containing the information for the specified bet. 
                            If no data is available, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If the provided bet ID is invalid or not provided, 
                            or if there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """

        if not bet_id:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_BET_ID)
        
        payload = {
            'betId': bet_id
        }


        try:
            response = requests.get(f'{self.core_url}{BET_INFO}', headers=HEADERS, params=payload, timeout=self.timeout)
            response.raise_for_status()  # Raise an exception for bad HTTP status codes
            data = response.json()
            return data
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f'Error when getting bet info by id: {str(E)}') from None
        
    def get_bettors_by_bet_options(self, bet_id: int | None = None, bet_option: int | None = None) -> Dict[str, Any]:

        """
        Retrieves a list of bettors for a specific bet and bet option from the core server.

        Args:
            bet_id (Optional[int]): The ID of the bet to retrieve bettors for. Must be a positive integer.
                                    If not provided, an exception is raised.
            bet_option (Optional[int]): The option of the bet for which to retrieve bettors. 
                                        Must be a positive integer. If not provided, an exception is raised.

        Returns:
            Dict[str, Any]: A dictionary containing the list of bettors for the specified bet and bet option. 
                            If no data is available, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If the provided bet ID or bet option is invalid or not provided, 
                            or if there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """

        if not bet_id or not bet_option:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_BET_OPTIONS)
        
        payload = {
            'betId': bet_id,
            'betOption': bet_option
        }


        try:
            response = requests.get(f'{self.core_url}{BETTORS_BY_BET_OPTIONS}', headers=HEADERS, params=payload, timeout=self.timeout)
            response.raise_for_status()  # Raise an exception for bad HTTP status codes
            data = response.json()
            return data
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f'Error when getting bet info by id: {str(E)}') from None
    
    """ QX SERVICES """

    def get_qx_asset_ask_orders(self, asset_name: str | None = None, issuer_id: str | None = None, offset: str | None = None) -> Dict[str, Any]:

        """
        Retrieves ask orders for a specified asset from the QX system.

        Args:
            asset_name (Optional[str]): The name of the asset for which to retrieve ask orders.
                                        Must be a valid asset identifier. If not provided, an exception is raised.
            issuer_id (Optional[str]): The ID of the issuer associated with the asset. 
                                    Must be a valid issuer identifier. If not provided, an exception is raised.
            offset (Optional[str]): The offset for pagination in the results. If not provided, an exception is raised.

        Returns:
            Dict[str, Any]: A dictionary containing ask order details for the specified asset, issuer, and offset.
                            If no data is available, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If any of the required parameters (`asset_name`, `issuer_id`, or `offset`) is invalid or not provided,
                            or if there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """

        if not asset_name or not issuer_id or not offset:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_QX_ASSET_DATA)
        
        payload = {
            'assetName': asset_name,
            'issuerId': issuer_id,
            'offset': offset,
        }

        try:
            response = requests.get(f'{self.core_url}{QX_ASSET_ASK_ORDERS}', headers=HEADERS, params=payload, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f'Error when getting QX data: {str(E)}') from None
        
    def get_qx_asset_bid_orders(self, asset_name: str | None = None, issuer_id: str | None = None, offset: str | None = None) -> Dict[str, Any]:

        """
        Retrieves bid orders for a specified asset from the QX system.

        Args:
            asset_name (Optional[str]): The name of the asset for which to retrieve bid orders.
                                        Must be a valid asset identifier. If not provided, an exception is raised.
            issuer_id (Optional[str]): The ID of the issuer associated with the asset.
                                    Must be a valid issuer identifier. If not provided, an exception is raised.
            offset (Optional[str]): The offset for pagination in the results. If not provided, pagination will start from the first result.

        Returns:
            Dict[str, Any]: A dictionary containing bid order details for the specified asset, issuer, and offset.
                            If no data is available, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If the required parameters (`asset_name` or `issuer_id`) are invalid or not provided,
        """

        if not asset_name or not issuer_id:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_QX_ASSET_DATA)
        
        payload = {
            'assetName': asset_name,
            'issuerId': issuer_id,
            'offset': offset,
        }

        try:
            response = requests.get(f'{self.core_url}{QX_ASSET_BID_ORDERS}', headers=HEADERS, params=payload, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f'Error when getting QX bid orders: {str(E)}') from None
    
    def get_qx_entity_ask_orders(self, entity_id: str | None = None, offset: str | None = None) -> Dict[str, Any]:

        """
        Retrieves ask orders for a specified entity from the QX system.

        Args:
            entity_id (Optional[str]): The unique identifier for the entity whose ask orders are to be retrieved.
                                    Must be a valid entity ID. If not provided, an exception is raised.
            offset (Optional[str]): The offset for pagination in the results. If not provided, pagination will start from the first result.

        Returns:
            Dict[str, Any]: A dictionary containing ask order details for the specified entity and offset.
                            If no data is available, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If the required parameter `entity_id` is invalid or not provided,
                            or if there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """

        if not entity_id:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_QX_ASSET_DATA)
        
        payload = {
            'entityId': entity_id,
            'offset': offset,
        }

        try:
            response = requests.get(f'{self.core_url}{QX_ENTITY_ASK_ORDERS}', headers=HEADERS, params=payload, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f'Error when getting QX entity ask orders: {str(E)}') from None
    
    def get_qx_entity_bid_orders(self, entity_id: str | None = None, offset: str | None = None) -> Dict[str, Any]:

        """
        Retrieves bid orders for a specified entity from the QX system.

        Args:
            entity_id (Optional[str]): The unique identifier for the entity whose bid orders are to be retrieved.
                                    Must be a valid entity ID. If not provided, an exception is raised.
            offset (Optional[str]): The offset for pagination in the results. If not provided, pagination will start from the first result.

        Returns:
            Dict[str, Any]: A dictionary containing bid order details for the specified entity and offset.
                            If no data is available, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If the required parameter `entity_id` is invalid or not provided,
                            or if there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """

        if not entity_id:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_QX_ASSET_DATA)
        
        payload = {
            'entityId': entity_id,
            'offset': offset,
        }

        try:
            response = requests.get(f'{self.core_url}{QX_ENTITY_BID_ORDERS}', headers=HEADERS, params=payload, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f'Error when getting QX entity bid orders: {str(E)}') from None


    def get_qx_fees(self) -> Dict[str, Any]:

        """
        Retrieves the current fee structure from the QX system.

        Returns:
            Dict[str, Any]: A dictionary containing details of the current QX fees.
                            If no data is available, an empty dictionary is returned.

        Raises:
            QubiPy_Exceptions: If there is an issue with the API request (e.g., network error, invalid response, or timeout).
        """
        try:
            response = requests.get(f'{self.core_url}{QX_FEES}', headers=HEADERS, timeout=self.timeout)
            response.raise_for_status() # Raise an exception for bad HTTP status codes
            data = response.json()
            return data
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f"Error when getting QX fees: {str(E)}") from None
        
    def get_monero_mining_stats(self) -> Dict[str, Any]:

        """
        Retrieves current Monero mining statistics from the external Monero system.

        This function makes an API call to fetch real-time or recent data related
        to Monero network mining.

        Returns:
            Dict[str, Any]: A dictionary containing various statistics related to Monero mining,
                            such as pool and network hashrates, network difficulty, block height,
                            and other relevant pool/miner data. The exact structure and content
                            depend on the Monero API response.

        Raises:
            QubiPy_Exceptions: If there is an issue during the API request execution (e.g.,
                            a network connection error, a non-2xx HTTP status code from the
                            API server, a timeout during the request, or if the API
                            response cannot be parsed as valid JSON).
        """
        try:
            response = requests.get(f'{MONERO_URL}{MONERO_MINING_STATS}', headers=HEADERS, timeout=self.timeout)
            response.raise_for_status() # Raise an exception for bad HTTP status codes
            data = response.json()
            return data
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f"Error when getting the monero mining stats: {str(E)}") from None
    
