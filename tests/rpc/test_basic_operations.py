import pytest
from unittest.mock import patch, Mock
from qubipy.rpc.rpc_client import QubiPy_RPC
from qubipy.exceptions import QubiPy_Exceptions
from qubipy.endpoints_rpc import *
import requests
from ..conftest import *

FULL_URL = f"{RPC_URL}{LATEST_TICK}"
BALANCE_FULL_URL = f"{RPC_URL}{WALLET_BALANCE}"
RPC_STATUS_FULL_URL = f"{RPC_URL}{STATUS}"
HEALTH_CHECK_FULL_URL = f"{RPC_URL}{HEALTH_CHECK}"
BLOCK_HEIGHT_FULL_URL = f"{RPC_URL}{BLOCK_HEIGHT}"
LATEST_STATS_FULL_URL = f"{RPC_URL}{LATEST_STATS}"

""" LATEST TICK TEST """

def test_get_latest_tick_success(mock_successful_response, rpc_client):
    """
    Test the get_latest_tick method for a successful API response.
    
    This test verifies that the get_latest_tick method correctly retrieves the 
    latest tick data when the API returns a successful response with a valid tick number.
    
    It ensures that:
    - The returned tick data matches the expected value
    - The raise_for_status and json methods are called once
    - The requests.get call is made with the correct URL, headers, and timeout
    """
    with patch('requests.get', return_value=mock_successful_response) as mock_get:
        result = rpc_client.get_latest_tick()
        
        assert result == 17021024
        mock_successful_response.raise_for_status.assert_called_once()
        mock_successful_response.json.assert_called_once()
        mock_get.assert_called_once_with(FULL_URL, headers=HEADERS, timeout=rpc_client.timeout)

def test_get_latest_tick_http_error(mock_http_error_response, rpc_client):
    """
    Test the get_latest_tick method for handling an HTTP error response.

    This test verifies that the get_latest_tick method raises a QubiPy_Exceptions 
    exception with the expected error message when the API responds with an HTTP error 
    (e.g., 500 Server Error). 

    It ensures that:
    - The exception message contains "Error when getting the last Tick"
    - The requests.get call is made with the correct URL, headers, and timeout
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_latest_tick()
        
        assert "Error when getting the last Tick" in str(exc_info.value)
        mock_get.assert_called_once_with(FULL_URL, headers=HEADERS, timeout=rpc_client.timeout)

def test_get_latest_tick_request_exception(rpc_client):
    """
    Test the get_latest_tick method for handling a network-related exception.

    This test verifies that the get_latest_tick method raises a QubiPy_Exceptions 
    exception with the expected error message when a network-related error occurs 
    (e.g., connection failure or timeout).

    It ensures that:
    - The exception message contains "Error when getting the last Tick: Network error"
    - The requests.get call is made with the correct URL, headers, and timeout
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_latest_tick()
        
        assert "Error when getting the last Tick: Network error" in str(exc_info.value)
        mock_get.assert_called_once_with(FULL_URL, headers=HEADERS, timeout=rpc_client.timeout)

def test_get_latest_tick_timeout(mock_timeout_response, rpc_client):
    """
    Test the get_latest_tick method for handling a timeout exception.

    This test verifies that the get_latest_tick method raises a QubiPy_Exceptions 
    exception with the expected error message when the request times out.

    It ensures that:
    - The exception message contains "Error when getting the last Tick: Request timed out"
    - The requests.get call is made with the correct URL, headers, and timeout
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_latest_tick()
        
        assert "Error when getting the last Tick: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(FULL_URL, headers=HEADERS, timeout=rpc_client.timeout)

""" GET BALANCE TEST """

def test_get_balance_success(mock_balance_response, sample_balance_data, rpc_client, sample_wallet_id):
    """
    Test the get_balance method with a valid wallet ID.
    
    Verifies that the function returns the expected balance when a valid wallet ID is provided.
    """
    with patch('requests.get', return_value=mock_balance_response) as mock_get:
        result = rpc_client.get_balance(sample_wallet_id)
        
        assert result == sample_balance_data
        mock_balance_response.raise_for_status.assert_called_once()
        mock_balance_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            BALANCE_FULL_URL.format(id=sample_wallet_id),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_balance_no_wallet_id(rpc_client):
    """
    Test the get_balance method with no wallet ID provided.
    
    Verifies that the function raises a QubiPy_Exceptions.INVALID_ADDRESS_ID when no wallet ID is provided.
    """
    with pytest.raises(QubiPy_Exceptions) as exc_info:
        rpc_client.get_balance(None)
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_ADDRESS_ID

def test_get_balance_http_error(mock_http_error_response, rpc_client, sample_wallet_id):
    """
    Test the get_balance method for handling an HTTP error response.
    
    Simulates an HTTP error and verifies that the function raises a QubiPy_Exceptions
    exception with an appropriate message.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_balance(sample_wallet_id)
        
        assert "Failed to retrieve the balance data from the API" in str(exc_info.value)
        mock_get.assert_called_once_with(
            BALANCE_FULL_URL.format(id=sample_wallet_id),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_balance_request_exception(rpc_client, sample_wallet_id):
    """
    Test the get_balance method for handling a network-related exception.
    
    Simulates a network-related error and verifies that the function raises 
    a QubiPy_Exceptions exception with an appropriate message.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_balance(sample_wallet_id)
        
        assert "Failed to retrieve the balance data from the API" in str(exc_info.value)
        mock_get.assert_called_once_with(
            BALANCE_FULL_URL.format(id=sample_wallet_id),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_balance_timeout(mock_timeout_response, rpc_client, sample_wallet_id):
    """
    Test the get_balance method for handling a timeout exception.
    
    Simulates a timeout error and verifies that the function raises a QubiPy_Exceptions 
    exception with an appropriate message when the request times out.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_balance(sample_wallet_id)
            
        assert "Failed to retrieve the balance data from the API, check the address ID and try again: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(
            BALANCE_FULL_URL.format(id=sample_wallet_id),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

""" GET RPC STATUS """

def test_get_rpc_status_success(mock_rpc_status_response, sample_rpc_status_data, rpc_client):
    """
    Test the get_rpc_status method for a successful response.
    
    Verifies that the function returns the expected RPC status data when the API
    responds successfully.
    """
    with patch('requests.get', return_value=mock_rpc_status_response) as mock_get:
        result = rpc_client.get_rpc_status()
        
        assert result == sample_rpc_status_data
        mock_rpc_status_response.raise_for_status.assert_called_once()
        mock_rpc_status_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            RPC_STATUS_FULL_URL,
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_rpc_status_http_error(mock_http_error_response, rpc_client):
    """
    Test the get_rpc_status method for handling an HTTP error response.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the API responds with an HTTP error.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_rpc_status()
        
        assert "Failed to retrieve the RPC status" in str(exc_info.value)
        mock_get.assert_called_once_with(
            RPC_STATUS_FULL_URL,
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_rpc_status_request_exception(rpc_client):
    """
    Test the get_rpc_status method for handling a network-related exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when a network-related error occurs.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_rpc_status()
        
        assert "Failed to retrieve the RPC status: Network error" in str(exc_info.value)
        mock_get.assert_called_once_with(
            RPC_STATUS_FULL_URL,
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_rpc_status_timeout(mock_timeout_response, rpc_client):
    """
    Test the get_rpc_status method for handling a timeout exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the request times out.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_rpc_status()
        
        assert "Failed to retrieve the RPC status: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(
            RPC_STATUS_FULL_URL,
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

""" HEALTH CHECK TEST """

def test_get_health_check_success(mock_health_check_response, sample_health_check_data, rpc_client):
    """
    Test the get_health_check method for a successful response.
    
    Verifies that the function returns the expected health check status when the API
    responds successfully.
    """
    with patch('requests.get', return_value=mock_health_check_response) as mock_get:
        result = rpc_client.get_health_check()
        
        assert result == sample_health_check_data
        mock_health_check_response.raise_for_status.assert_called_once()
        mock_health_check_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            HEALTH_CHECK_FULL_URL,
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_health_check_http_error(mock_http_error_response, rpc_client):
    """
    Test the get_health_check method for handling an HTTP error response.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the API responds with an HTTP error.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_health_check()
        
        assert "Failed to retrieve the health check" in str(exc_info.value)
        mock_get.assert_called_once_with(
            HEALTH_CHECK_FULL_URL,
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_health_check_request_exception(rpc_client):
    """
    Test the get_health_check method for handling a network-related exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when a network-related error occurs.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_health_check()
        
        assert "Failed to retrieve the health check: Network error" in str(exc_info.value)
        mock_get.assert_called_once_with(
            HEALTH_CHECK_FULL_URL,
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_health_check_timeout(mock_timeout_response, rpc_client):
    """
    Test the get_health_check method for handling a timeout exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the request times out.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_health_check()
        
        assert "Failed to retrieve the health check: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(
            HEALTH_CHECK_FULL_URL,
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

""" BLOCK HEIGHT TEST """

def test_get_block_height_success(mock_block_height_response, sample_block_height_data, rpc_client):
    """
    Test the get_block_height method for a successful response.
    
    Verifies that the function returns the expected block height data when the API
    responds successfully.
    """
    with patch('requests.get', return_value=mock_block_height_response) as mock_get:
        result = rpc_client.get_block_height()
        
        assert result == sample_block_height_data
        mock_block_height_response.raise_for_status.assert_called_once()
        mock_block_height_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            BLOCK_HEIGHT_FULL_URL,
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_block_height_http_error(mock_http_error_response, rpc_client):
    """
    Test the get_block_height method for handling an HTTP error response.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the API responds with an HTTP error.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_block_height()
        
        assert "Failed to retrieve the block height" in str(exc_info.value)
        mock_get.assert_called_once_with(
            BLOCK_HEIGHT_FULL_URL,
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_block_height_request_exception(rpc_client):
    """
    Test the get_block_height method for handling a network-related exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when a network-related error occurs.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_block_height()
        
        assert "Failed to retrieve the block height: Network error" in str(exc_info.value)
        mock_get.assert_called_once_with(
            BLOCK_HEIGHT_FULL_URL,
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_block_height_timeout(mock_timeout_response, rpc_client):
    """
    Test the get_block_height method for handling a timeout exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the request times out.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_block_height()
        
        assert "Failed to retrieve the block height: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(
            BLOCK_HEIGHT_FULL_URL,
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

""" LATEST STATS """

def test_get_latest_stats_success(mock_latest_stats_response, sample_latest_stats_data, rpc_client):
    """
    Test the get_latest_stats method for a successful response.
    
    Verifies that the function returns the expected latest statistics when the API
    responds successfully.
    """
    with patch('requests.get', return_value=mock_latest_stats_response) as mock_get:
        result = rpc_client.get_latest_stats()
        
        assert result == sample_latest_stats_data
        mock_latest_stats_response.raise_for_status.assert_called_once()
        mock_latest_stats_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            LATEST_STATS_FULL_URL,
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_latest_stats_http_error(mock_http_error_response, rpc_client):
    """
    Test the get_latest_stats method for handling an HTTP error response.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the API responds with an HTTP error.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_latest_stats()
        
        assert "Failed to retrieve the latest stats from the RPC Server" in str(exc_info.value)
        mock_get.assert_called_once_with(
            LATEST_STATS_FULL_URL,
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_latest_stats_request_exception(rpc_client):
    """
    Test the get_latest_stats method for handling a network-related exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when a network-related error occurs.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_latest_stats()
        
        assert "Failed to retrieve the latest stats from the RPC Server: Network error" in str(exc_info.value)
        mock_get.assert_called_once_with(
            LATEST_STATS_FULL_URL,
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_latest_stats_timeout(mock_timeout_response, rpc_client):
    """
    Test the get_latest_stats method for handling a timeout exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the request times out.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_latest_stats()
        
        assert "Failed to retrieve the latest stats from the RPC Server: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(
            LATEST_STATS_FULL_URL,
            headers=HEADERS,
            timeout=rpc_client.timeout
        )