import pytest
from unittest.mock import patch
from qubipy.exceptions import QubiPy_Exceptions
from qubipy.endpoints_rpc import *
import requests
from ..conftest import *


RICH_LIST_FULL_URL = f"{RPC_URL}{RICH_LIST}"

def test_get_rich_list_success(mock_rich_list_response, sample_rich_list_data, rpc_client, sample_page, sample_page_size):
    """
    Test the get_rich_list method for a successful response.
    
    Verifies that the function returns the expected rich list when the API
    responds successfully.
    """
    with patch('requests.get', return_value=mock_rich_list_response) as mock_get:
        result = rpc_client.get_rich_list(sample_page, sample_page_size)
        
        
        assert result.get('richList', {}) == sample_rich_list_data
        mock_rich_list_response.raise_for_status.assert_called_once()
        mock_rich_list_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            RICH_LIST_FULL_URL,
            params={'page': sample_page, 'pageSize': sample_page_size},
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_rich_list_no_pages(rpc_client):
    """
    Test the get_rich_list method with no page parameters provided.
    
    Verifies that the function raises a QubiPy_Exceptions with INVALID_PAGES when
    no page parameters are provided.
    """
    with pytest.raises(QubiPy_Exceptions) as exc_info:
        rpc_client.get_rich_list(None, None)
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_PAGES

def test_get_rich_list_http_error(mock_http_error_response, rpc_client, sample_page, sample_page_size):
    """
    Test the get_rich_list method for handling an HTTP error response.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the API responds with an HTTP error.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_rich_list(sample_page, sample_page_size)
        
        assert "Failed to retrieve the rich list" in str(exc_info.value)
        mock_get.assert_called_once_with(
            RICH_LIST_FULL_URL,
            params={'page': sample_page, 'pageSize': sample_page_size},
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_rich_list_request_exception(rpc_client, sample_page, sample_page_size):
    """
    Test the get_rich_list method for handling a network-related exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when a network-related error occurs.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_rich_list(sample_page, sample_page_size)
        
        assert "Failed to retrieve the rich list: Network error" in str(exc_info.value)
        mock_get.assert_called_once_with(
            RICH_LIST_FULL_URL,
            params={'page': sample_page, 'pageSize': sample_page_size},
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_rich_list_timeout(mock_timeout_response, rpc_client, sample_page, sample_page_size):
    """
    Test the get_rich_list method for handling a timeout exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the request times out.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_rich_list(sample_page, sample_page_size)
        
        assert "Failed to retrieve the rich list: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(
            RICH_LIST_FULL_URL,
            params={'page': sample_page, 'pageSize': sample_page_size},
            headers=HEADERS,
            timeout=rpc_client.timeout
        )