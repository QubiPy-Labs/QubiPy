import pytest
from unittest.mock import patch
from qubipy.exceptions import QubiPy_Exceptions
from qubipy.endpoints_rpc import *
import requests
from ..conftest import *

CHAIN_HASH_FULL_URL = f"{RPC_URL}{CHAIN_HASH}"
QUORUM_TICK_DATA_FULL_URL = f"{RPC_URL}{QUORUM_TICK_DATA}"
STORE_HASH_FULL_URL = f"{RPC_URL}{STORE_HASH}"

def test_get_chain_hash_success(mock_chain_hash_response, sample_chain_hash_data, rpc_client, sample_tick):
    """
    Test the get_chain_hash method for a successful response.
    
    Verifies that the function returns the expected chain hash when the API
    responds successfully.
    """
    with patch('requests.get', return_value=mock_chain_hash_response) as mock_get:
        result = rpc_client.get_chain_hash(sample_tick)
        
        assert result == sample_chain_hash_data
        mock_chain_hash_response.raise_for_status.assert_called_once()
        mock_chain_hash_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            CHAIN_HASH_FULL_URL.format(tick=sample_tick),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_chain_hash_no_tick(rpc_client):
    """
    Test the get_chain_hash method with no tick number provided.
    
    Verifies that the function raises a QubiPy_Exceptions with INVALID_TICK_ERROR when
    no tick number is provided.
    """
    with pytest.raises(QubiPy_Exceptions) as exc_info:
        rpc_client.get_chain_hash(None)
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_TICK_ERROR

def test_get_chain_hash_http_error(mock_http_error_response, rpc_client, sample_tick):
    """
    Test the get_chain_hash method for handling an HTTP error response.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the API responds with an HTTP error.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_chain_hash(sample_tick)
        
        assert "Failed to retrieve the chain hash" in str(exc_info.value)
        mock_get.assert_called_once_with(
            CHAIN_HASH_FULL_URL.format(tick=sample_tick),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_chain_hash_request_exception(rpc_client, sample_tick):
    """
    Test the get_chain_hash method for handling a network-related exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when a network-related error occurs.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_chain_hash(sample_tick)
        
        assert "Failed to retrieve the chain hash: Network error" in str(exc_info.value)
        mock_get.assert_called_once_with(
            CHAIN_HASH_FULL_URL.format(tick=sample_tick),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_chain_hash_timeout(mock_timeout_response, rpc_client, sample_tick):
    """
    Test the get_chain_hash method for handling a timeout exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the request times out.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_chain_hash(sample_tick)
        
        assert "Failed to retrieve the chain hash: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(
            CHAIN_HASH_FULL_URL.format(tick=sample_tick),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

""" QUORUM TICK DATA """

def test_get_quorum_tick_data_success(mock_quorum_tick_data_response, sample_quorum_tick_data, rpc_client, sample_tick):
    """
    Test the get_quorum_tick_data method for a successful response.
    
    Verifies that the function returns the expected quorum tick data when the API
    responds successfully.
    """
    with patch('requests.get', return_value=mock_quorum_tick_data_response) as mock_get:
        result = rpc_client.get_quorum_tick_data(sample_tick)
        
        assert result == sample_quorum_tick_data
        mock_quorum_tick_data_response.raise_for_status.assert_called_once()
        mock_quorum_tick_data_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            QUORUM_TICK_DATA_FULL_URL.format(tick=sample_tick),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_quorum_tick_data_no_tick(rpc_client):
    """
    Test the get_quorum_tick_data method with no tick number provided.
    
    Verifies that the function raises a QubiPy_Exceptions with INVALID_TICK_ERROR when
    no tick number is provided.
    """
    with pytest.raises(QubiPy_Exceptions) as exc_info:
        rpc_client.get_quorum_tick_data(None)
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_TICK_ERROR

def test_get_quorum_tick_data_http_error(mock_http_error_response, rpc_client, sample_tick):
    """
    Test the get_quorum_tick_data method for handling an HTTP error response.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the API responds with an HTTP error.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_quorum_tick_data(sample_tick)
        
        assert "Failed to retrieve the quorum tick data" in str(exc_info.value)
        mock_get.assert_called_once_with(
            QUORUM_TICK_DATA_FULL_URL.format(tick=sample_tick),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_quorum_tick_data_request_exception(rpc_client, sample_tick):
    """
    Test the get_quorum_tick_data method for handling a network-related exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when a network-related error occurs.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_quorum_tick_data(sample_tick)
        
        assert "Failed to retrieve the quorum tick data: Network error" in str(exc_info.value)
        mock_get.assert_called_once_with(
            QUORUM_TICK_DATA_FULL_URL.format(tick=sample_tick),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_quorum_tick_data_timeout(mock_timeout_response, rpc_client, sample_tick):
    """
    Test the get_quorum_tick_data method for handling a timeout exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the request times out.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_quorum_tick_data(sample_tick)
        
        assert "Failed to retrieve the quorum tick data: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(
            QUORUM_TICK_DATA_FULL_URL.format(tick=sample_tick),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

""" STORE HASH """

def test_get_store_hash_success(mock_store_hash_response, sample_store_hash_data, rpc_client, sample_tick):
    """
    Test the get_store_hash method for a successful response.
    
    Verifies that the function returns the expected store hash when the API
    responds successfully.
    """
    with patch('requests.get', return_value=mock_store_hash_response) as mock_get:
        result = rpc_client.get_store_hash(sample_tick)
        
        assert result == sample_store_hash_data
        mock_store_hash_response.raise_for_status.assert_called_once()
        mock_store_hash_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            STORE_HASH_FULL_URL.format(tick=sample_tick),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_store_hash_no_tick(rpc_client):
    """
    Test the get_store_hash method with no tick number provided.
    
    Verifies that the function raises a QubiPy_Exceptions with INVALID_TICK_ERROR when
    no tick number is provided.
    """
    with pytest.raises(QubiPy_Exceptions) as exc_info:
        rpc_client.get_store_hash(None)
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_TICK_ERROR

def test_get_store_hash_http_error(mock_http_error_response, rpc_client, sample_tick):
    """
    Test the get_store_hash method for handling an HTTP error response.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the API responds with an HTTP error.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_store_hash(sample_tick)
        
        assert "Failed to retrieve the store hash" in str(exc_info.value)
        mock_get.assert_called_once_with(
            STORE_HASH_FULL_URL.format(tick=sample_tick),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_store_hash_request_exception(rpc_client, sample_tick):
    """
    Test the get_store_hash method for handling a network-related exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when a network-related error occurs.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_store_hash(sample_tick)
        
        assert "Failed to retrieve the store hash: Network error" in str(exc_info.value)
        mock_get.assert_called_once_with(
            STORE_HASH_FULL_URL.format(tick=sample_tick),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_store_hash_timeout(mock_timeout_response, rpc_client, sample_tick):
    """
    Test the get_store_hash method for handling a timeout exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the request times out.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_store_hash(sample_tick)
        
        assert "Failed to retrieve the store hash: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(
            STORE_HASH_FULL_URL.format(tick=sample_tick),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )