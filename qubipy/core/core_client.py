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
    
    def get_computors(self):

        try:
            response = requests.get(f'{self.core_url}{COMPUTORS}', timeout=self.timeout)
            response.raise_for_status()  # Raise an exception for bad HTTP status codes
            data = response.json()
            return data
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f'Error when getting computors: {str(E)}') from None
    
    def get_entity_info(self, id: Optional[str] = None):
        
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
            raise QubiPy_Exceptions(f'Error when getting computors: {str(E)}') from None

    
    def get_tick_data(self, tick):

        payload = {
            "tick": tick
            }
        
        try:
            response = requests.post(f'{self.core_url}{TICK_DATA}', headers=HEADERS, json=payload, timeout=self.timeout)
            response.raise_for_status()  # Raise an exception for bad HTTP status codes
            data = response.json()
            return data
        except requests.RequestException as E:
            raise QubiPy_Exceptions(f'Error when getting computors: {str(E)}') from None

    
