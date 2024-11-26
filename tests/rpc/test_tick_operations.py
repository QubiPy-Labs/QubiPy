import pytest
from unittest.mock import patch
from qubipy.exceptions import QubiPy_Exceptions
from qubipy.endpoints_rpc import *
import requests
import base64
from ..conftest import *

TICK_INFO_FULL_URL = f"{RPC_URL}{TICK_INFO}"
TICK_DATA_FULL_URL = f"{RPC_URL}{TICK_DATA}"

def test_get_tick_info_success(mock_tick_rpc_response, sample_rpc_tick_info_data, rpc_client):
    """
    Test the get_tick_info method for a successful response.
    
    Verifies that the function returns the expected tick information when the API
    responds successfully.
    """
    with patch('requests.get', return_value=mock_tick_rpc_response) as mock_get:
        result = rpc_client.get_tick_info()
        
        assert result == sample_rpc_tick_info_data
        mock_tick_rpc_response.raise_for_status.assert_called_once()
        mock_tick_rpc_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            TICK_INFO_FULL_URL,
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_tick_info_http_error(mock_http_error_response, rpc_client):
    """
    Test the get_tick_info method for handling an HTTP error response.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the API responds with an HTTP error.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_tick_info()
        
        assert "Failed to retrieve the tick info data" in str(exc_info.value)
        mock_get.assert_called_once_with(
            TICK_INFO_FULL_URL,
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_tick_info_request_exception(rpc_client):
    """
    Test the get_tick_info method for handling a network-related exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when a network-related error occurs.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_tick_info()
        
        assert "Failed to retrieve the tick info data: Network error" in str(exc_info.value)
        mock_get.assert_called_once_with(
            TICK_INFO_FULL_URL,
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_tick_info_timeout(mock_timeout_response, rpc_client):
    """
    Test the get_tick_info method for handling a timeout exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the request times out.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_tick_info()
        
        assert "Failed to retrieve the tick info data: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(
            TICK_INFO_FULL_URL,
            headers=HEADERS,
            timeout=rpc_client.timeout
        )


""" TICK DATA """

def test_get_tick_data_success(mock_tick_data_response, sample_tick_data, rpc_client, sample_tick):
    """
    Test the get_tick_data method for a successful response.
    
    Verifies that the function returns the expected tick data when the API
    responds successfully.
    """
    with patch('requests.get', return_value=mock_tick_data_response) as mock_get:
        result = rpc_client.get_tick_data(sample_tick)
        
        assert result == sample_tick_data
        mock_tick_data_response.raise_for_status.assert_called_once()
        mock_tick_data_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            TICK_DATA_FULL_URL.format(tick=sample_tick),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_tick_data_no_tick(rpc_client):
    """
    Test the get_tick_data method with no tick number provided.
    
    Verifies that the function raises a QubiPy_Exceptions with INVALID_TICK_ERROR when
    no tick number is provided.
    """
    with pytest.raises(QubiPy_Exceptions) as exc_info:
        rpc_client.get_tick_data(None)
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_TICK_ERROR

def test_get_tick_data_http_error(mock_http_error_response, rpc_client, sample_tick):
    """
    Test the get_tick_data method for handling an HTTP error response.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the API responds with an HTTP error.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_tick_data(sample_tick)
        
        assert "Failed to retrieve the tick data" in str(exc_info.value)
        mock_get.assert_called_once_with(
            TICK_DATA_FULL_URL.format(tick=sample_tick),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_tick_data_request_exception(rpc_client, sample_tick):
    """
    Test the get_tick_data method for handling a network-related exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when a network-related error occurs.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_tick_data(sample_tick)
        
        assert "Failed to retrieve the tick data: Network error" in str(exc_info.value)
        mock_get.assert_called_once_with(
            TICK_DATA_FULL_URL.format(tick=sample_tick),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_tick_data_timeout(mock_timeout_response, rpc_client, sample_tick):
    """
    Test the get_tick_data method for handling a timeout exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the request times out.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_tick_data(sample_tick)
        
        assert "Failed to retrieve the tick data: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(
            TICK_DATA_FULL_URL.format(tick=sample_tick),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )