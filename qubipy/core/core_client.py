"""
rpc_client.py
This file contains the main QubiPy_RPC Client class which handles
the interaction with the Qubic API, making HTTP requests and handling responses.
"""

import requests
from typing import Optional, Dict, Any
import json

from qubipy.exceptions import *
from qubipy.config import *
from qubipy.endpoints_core import *
from qubipy.utils import *
import base64
import json

class QubiPy_Core:
    def __init__(self, core_url: str = CORE_URL, timeout=TIMEOUT):
        self.core_url = core_url
        self.timeout = timeout
    
    def get_computors(self) -> Dict[str, Any]:

        try:
            response = requests.get(f'{self.core_url}{COMPUTORS}', timeout=self.timeout)
            response.raise_for_status()  # Raise an exception for bad HTTP status codes
            data = response.json()
            return data
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f'Error when getting computors: {str(E)}') from None
    
    def get_entity_info(self, id: Optional[str] = None) -> Dict[str, Any]:
        
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

    
    def get_tick_data(self, tick: Optional[int] = None) -> Dict[str, Any]:

        if not tick:
            raise QubiPy_Exceptions(QubiPy_Exceptions.INVALID_TICK_ERROR)


        payload = {
            "tick": tick
            }
        
        try:
            response = requests.post(f'{self.core_url}{TICK_DATA}', headers=HEADERS, json=payload, timeout=self.timeout)
            response.raise_for_status()  # Raise an exception for bad HTTP status codes
            data = response.json()
            return data
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f'Error when getting tick data: {str(E)}') from None
    
    
    def get_tick_info(self) -> Dict[str, Any]:

        try:
            response = requests.get(f'{self.core_url}{TICK_INFO}', headers=HEADERS, timeout=self.timeout)
            response.raise_for_status()  # Raise an exception for bad HTTP status codes
            data = response.json()
            return data
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f'Error when getting tick info: {str(E)}') from None
    
    def get_tick_quorum_vote(self, tick: Optional[int] = None) -> Dict[str, Any]:

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
    
    def get_tick_transactions(self, tick: Optional[int] = None) -> Dict[str, Any]:

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
        
    def get_tick_transactions_status(self, tick: Optional[int] = None) -> Dict[str, Any]:

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

        try:
            response = requests.get(f'{self.core_url}{ACTIVE_BETS}', headers=HEADERS, timeout=self.timeout)
            response.raise_for_status()  # Raise an exception for bad HTTP status codes
            data = response.json()
            return data
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f'Error when getting active bets: {str(E)}') from None
    
    def get_active_bets_by_creator(self, creator_id: Optional[str] = None) -> Dict[str, Any]:

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

        try:
            response = requests.get(f'{self.core_url}{BASIC_INFO}', headers=HEADERS, timeout=self.timeout)
            response.raise_for_status()  # Raise an exception for bad HTTP status codes
            data = response.json()
            return data
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f'Error when getting computors: {str(E)}') from None
    
    def get_bet_info(self, bet_id: Optional[int] = None) -> Dict[str, Any]:

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
        
    def get_bettors_by_bet_options(self, bet_id: Optional[int] = None, bet_option: Optional[int] = None) -> Dict[str, Any]:

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
    
