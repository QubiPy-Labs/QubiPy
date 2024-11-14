import pytest
from unittest.mock import patch, Mock
from qubipy.rpc.rpc_client import QubiPy_RPC
from qubipy.exceptions import QubiPy_Exceptions
from qubipy.endpoints_rpc import *
import requests
from ..conftest import *

ISSUED_ASSETS_FULL_URL = f"{RPC_URL}{ISSUED_ASSETS}"
OWNED_ASSETS_FULL_URL = f"{RPC_URL}{OWNED_ASSETS}"
POSSESSED_ASSETS_FULL_URL = f"{RPC_URL}{POSSESSED_ASSETS}"

def test_get_issued_assets_success(mock_issued_assets_response, sample_issued_assets_data, rpc_client, sample_identity):
    """
    Test the get_issued_assets method for a successful response.
    
    Verifies that the function returns the expected list of issued assets when the API
    responds successfully.
    """
    with patch('requests.get', return_value=mock_issued_assets_response) as mock_get:
        result = rpc_client.get_issued_assets(sample_identity)
        
        assert result == sample_issued_assets_data
        mock_issued_assets_response.raise_for_status.assert_called_once()
        mock_issued_assets_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            ISSUED_ASSETS_FULL_URL.format(identity=sample_identity),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_issued_assets_no_identity(rpc_client):
    """
    Test the get_issued_assets method with no identity provided.
    
    Verifies that the function raises a QubiPy_Exceptions with INVALID_ADDRESS_ID when
    no identity is provided.
    """
    with pytest.raises(QubiPy_Exceptions) as exc_info:
        rpc_client.get_issued_assets(None)
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_ADDRESS_ID

def test_get_issued_assets_http_error(mock_http_error_response, rpc_client, sample_identity):
    """
    Test the get_issued_assets method for handling an HTTP error response.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the API responds with an HTTP error.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_issued_assets(sample_identity)
        
        assert "Failed to retrieve the list of assets issued by a specific identity" in str(exc_info.value)
        mock_get.assert_called_once_with(
            ISSUED_ASSETS_FULL_URL.format(identity=sample_identity),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_issued_assets_request_exception(rpc_client, sample_identity):
    """
    Test the get_issued_assets method for handling a network-related exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when a network-related error occurs.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_issued_assets(sample_identity)
        
        assert "Failed to retrieve the list of assets issued by a specific identity: Network error" in str(exc_info.value)
        mock_get.assert_called_once_with(
            ISSUED_ASSETS_FULL_URL.format(identity=sample_identity),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_issued_assets_timeout(mock_timeout_response, rpc_client, sample_identity):
    """
    Test the get_issued_assets method for handling a timeout exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the request times out.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_issued_assets(sample_identity)
        
        assert "Failed to retrieve the list of assets issued by a specific identity: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(
            ISSUED_ASSETS_FULL_URL.format(identity=sample_identity),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

""" OWNED ASSETS """

def test_get_owned_assets_success(mock_owned_assets_response, sample_owned_assets_data, rpc_client, sample_identity):
    """
    Test the get_owned_assets method for a successful response.
    
    Verifies that the function returns the expected list of owned assets when the API
    responds successfully.
    """
    with patch('requests.get', return_value=mock_owned_assets_response) as mock_get:
        result = rpc_client.get_owned_assets(sample_identity)
        
        assert result == sample_owned_assets_data
        mock_owned_assets_response.raise_for_status.assert_called_once()
        mock_owned_assets_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            OWNED_ASSETS_FULL_URL.format(identity=sample_identity),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_owned_assets_no_identity(rpc_client):
    """
    Test the get_owned_assets method with no identity provided.
    
    Verifies that the function raises a QubiPy_Exceptions with INVALID_ADDRESS_ID when
    no identity is provided.
    """
    with pytest.raises(QubiPy_Exceptions) as exc_info:
        rpc_client.get_owned_assets(None)
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_ADDRESS_ID

def test_get_owned_assets_http_error(mock_http_error_response, rpc_client, sample_identity):
    """
    Test the get_owned_assets method for handling an HTTP error response.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the API responds with an HTTP error.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_owned_assets(sample_identity)
        
        assert "Failed to retrieve the owned assets" in str(exc_info.value)
        mock_get.assert_called_once_with(
            OWNED_ASSETS_FULL_URL.format(identity=sample_identity),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_owned_assets_request_exception(rpc_client, sample_identity):
    """
    Test the get_owned_assets method for handling a network-related exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when a network-related error occurs.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_owned_assets(sample_identity)
        
        assert "Failed to retrieve the owned assets: Network error" in str(exc_info.value)
        mock_get.assert_called_once_with(
            OWNED_ASSETS_FULL_URL.format(identity=sample_identity),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_owned_assets_timeout(mock_timeout_response, rpc_client, sample_identity):
    """
    Test the get_owned_assets method for handling a timeout exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the request times out.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_owned_assets(sample_identity)
        
        assert "Failed to retrieve the owned assets: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(
            OWNED_ASSETS_FULL_URL.format(identity=sample_identity),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

""" POSSESSED ASSETS """

def test_get_possessed_assets_success(mock_possessed_assets_response, sample_possessed_assets_data, rpc_client, sample_identity):
    """
    Test the get_possessed_assets method for a successful response.
    
    Verifies that the function returns the expected list of possessed assets when the API
    responds successfully.
    """
    with patch('requests.get', return_value=mock_possessed_assets_response) as mock_get:
        result = rpc_client.get_possessed_assets(sample_identity)
        
        assert result == sample_possessed_assets_data
        mock_possessed_assets_response.raise_for_status.assert_called_once()
        mock_possessed_assets_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            POSSESSED_ASSETS_FULL_URL.format(identity=sample_identity),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_possessed_assets_no_identity(rpc_client):
    """
    Test the get_possessed_assets method with no identity provided.
    
    Verifies that the function raises a QubiPy_Exceptions with INVALID_ADDRESS_ID when
    no identity is provided.
    """
    with pytest.raises(QubiPy_Exceptions) as exc_info:
        rpc_client.get_possessed_assets(None)
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_ADDRESS_ID

def test_get_possessed_assets_http_error(mock_http_error_response, rpc_client, sample_identity):
    """
    Test the get_possessed_assets method for handling an HTTP error response.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the API responds with an HTTP error.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_possessed_assets(sample_identity)
        
        assert "Failed to retrieve the possessed assets" in str(exc_info.value)
        mock_get.assert_called_once_with(
            POSSESSED_ASSETS_FULL_URL.format(identity=sample_identity),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_possessed_assets_request_exception(rpc_client, sample_identity):
    """
    Test the get_possessed_assets method for handling a network-related exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when a network-related error occurs.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_possessed_assets(sample_identity)
        
        assert "Failed to retrieve the possessed assets: Network error" in str(exc_info.value)
        mock_get.assert_called_once_with(
            POSSESSED_ASSETS_FULL_URL.format(identity=sample_identity),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_possessed_assets_timeout(mock_timeout_response, rpc_client, sample_identity):
    """
    Test the get_possessed_assets method for handling a timeout exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the request times out.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_possessed_assets(sample_identity)
        
        assert "Failed to retrieve the possessed assets: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(
            POSSESSED_ASSETS_FULL_URL.format(identity=sample_identity),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )