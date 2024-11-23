import pytest
from unittest.mock import patch
from qubipy.exceptions import QubiPy_Exceptions
from qubipy.endpoints_core import *
import requests
from ..conftest import *

TICK_DATA_FULL_URL = f"{CORE_URL}{CORE_TICK_DATA}"
TICK_INFO_FULL_URL = f"{CORE_URL}{CORE_TICK_INFO}"
TICK_QUORUM_VOTE_FULL_URL = f"{CORE_URL}{TICK_QUORUM_VOTE}"
TICK_TRANSACTIONS_FULL_URL = f"{CORE_URL}{TICK_TRANSACTIONS}"


def test_get_tick_data_success(mock_tick_data_core_response, sample_tick_data_core, core_client, sample_tick):
    """
    Test the get_tick_data method for a successful response.
    
    Verifies that the function returns the expected tick data when the API
    responds successfully.
    """
    with patch('requests.post', return_value=mock_tick_data_core_response) as mock_post:
        result = core_client.get_tick_data(sample_tick)
        
        assert result == sample_tick_data_core
        mock_tick_data_core_response.raise_for_status.assert_called_once()
        mock_tick_data_core_response.json.assert_called_once()
        
        expected_payload = {"tick": sample_tick}
        mock_post.assert_called_once_with(
            TICK_DATA_FULL_URL,
            headers=HEADERS,
            json=expected_payload,
            timeout=core_client.timeout
        )

def test_get_tick_data_no_tick(core_client):
    """
    Test the get_tick_data method with no tick provided.
    
    Verifies that the function raises a QubiPy_Exceptions with INVALID_TICK_ERROR when
    no tick is provided.
    """
    with pytest.raises(QubiPy_Exceptions) as exc_info:
        core_client.get_tick_data(None)
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_TICK_ERROR

def test_get_tick_data_http_error(mock_http_error_response, core_client, sample_tick):
    """
    Test the get_tick_data method for handling an HTTP error response.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the API responds with an HTTP error.
    """
    with patch('requests.post', return_value=mock_http_error_response) as mock_post:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_tick_data(sample_tick)
        
        assert "Error when getting tick data" in str(exc_info.value)
        
        expected_payload = {"tick": sample_tick}
        mock_post.assert_called_once_with(
            TICK_DATA_FULL_URL,
            headers=HEADERS,
            json=expected_payload,
            timeout=core_client.timeout
        )

def test_get_tick_data_request_exception(core_client, sample_tick):
    """
    Test the get_tick_data method for handling a network-related exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when a network-related error occurs.
    """
    with patch('requests.post', side_effect=requests.RequestException("Network error")) as mock_post:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_tick_data(sample_tick)
        
        assert "Error when getting tick data: Network error" in str(exc_info.value)
        
        expected_payload = {"tick": sample_tick}
        mock_post.assert_called_once_with(
            TICK_DATA_FULL_URL,
            headers=HEADERS,
            json=expected_payload,
            timeout=core_client.timeout
        )

def test_get_tick_data_timeout(core_client, sample_tick):
    """
    Test the get_tick_data method for handling a timeout exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the request times out.
    """
    with patch('requests.post', side_effect=requests.Timeout("Request timed out")) as mock_post:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_tick_data(sample_tick)
        
        assert "Error when getting tick data: Request timed out" in str(exc_info.value)
        
        expected_payload = {"tick": sample_tick}
        mock_post.assert_called_once_with(
            TICK_DATA_FULL_URL,
            headers=HEADERS,
            json=expected_payload,
            timeout=core_client.timeout
        )

""" TICK INFO """

def test_get_tick_info_success(mock_tick_info_response, sample_tick_info_data, core_client):
    """
    Test the get_tick_info method for a successful response.
    
    Verifies that the function returns the expected tick info when the API
    responds successfully.
    """
    with patch('requests.get', return_value=mock_tick_info_response) as mock_get:
        result = core_client.get_tick_info()
        
        assert result == sample_tick_info_data
        mock_tick_info_response.raise_for_status.assert_called_once()
        mock_tick_info_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            TICK_INFO_FULL_URL,
            headers=HEADERS,
            timeout=core_client.timeout
        )

def test_get_tick_info_http_error(mock_http_error_response, core_client):
    """
    Test the get_tick_info method for handling an HTTP error response.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the API responds with an HTTP error.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_tick_info()
        
        assert "Error when getting tick info" in str(exc_info.value)
        mock_get.assert_called_once_with(
            TICK_INFO_FULL_URL,
            headers=HEADERS,
            timeout=core_client.timeout
        )

def test_get_tick_info_request_exception(core_client):
    """
    Test the get_tick_info method for handling a network-related exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when a network-related error occurs.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_tick_info()
        
        assert "Error when getting tick info: Network error" in str(exc_info.value)
        mock_get.assert_called_once_with(
            TICK_INFO_FULL_URL,
            headers=HEADERS,
            timeout=core_client.timeout
        )

def test_get_tick_info_timeout(core_client):
    """
    Test the get_tick_info method for handling a timeout exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the request times out.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_tick_info()
        
        assert "Error when getting tick info: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(
            TICK_INFO_FULL_URL,
            headers=HEADERS,
            timeout=core_client.timeout
        )

""" TICK QUORUM VOTE """

def test_get_tick_quorum_vote_success(mock_quorum_vote_response, sample_quorum_vote_data, core_client, sample_tick):
    """
    Test the get_tick_quorum_vote method for a successful response.
    
    Verifies that the function returns the expected quorum vote data when the API
    responds successfully.
    """
    with patch('requests.post', return_value=mock_quorum_vote_response) as mock_post:
        result = core_client.get_tick_quorum_vote(sample_tick)
        
        assert result == sample_quorum_vote_data
        mock_quorum_vote_response.raise_for_status.assert_called_once()
        mock_quorum_vote_response.json.assert_called_once()
        
        expected_payload = {"tick": sample_tick}
        mock_post.assert_called_once_with(
            TICK_QUORUM_VOTE_FULL_URL,
            headers=HEADERS,
            json=expected_payload,
            timeout=core_client.timeout
        )

def test_get_tick_quorum_vote_no_tick(core_client):
    """
    Test the get_tick_quorum_vote method with no tick provided.
    
    Verifies that the function raises a QubiPy_Exceptions with INVALID_TICK_ERROR when
    no tick is provided.
    """
    with pytest.raises(QubiPy_Exceptions) as exc_info:
        core_client.get_tick_quorum_vote(None)
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_TICK_ERROR

def test_get_tick_quorum_vote_http_error(mock_http_error_response, core_client, sample_tick):
    """
    Test the get_tick_quorum_vote method for handling an HTTP error response.
    """
    with patch('requests.post', return_value=mock_http_error_response) as mock_post:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_tick_quorum_vote(sample_tick)
        
        assert "Error when getting tick quorum vote" in str(exc_info.value)
        
        expected_payload = {"tick": sample_tick}
        mock_post.assert_called_once_with(
            TICK_QUORUM_VOTE_FULL_URL,
            headers=HEADERS,
            json=expected_payload,
            timeout=core_client.timeout
        )

def test_get_tick_quorum_vote_request_exception(core_client, sample_tick):
    """
    Test the get_tick_quorum_vote method for handling a network-related exception.
    """
    with patch('requests.post', side_effect=requests.RequestException("Network error")) as mock_post:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_tick_quorum_vote(sample_tick)
        
        assert "Error when getting tick quorum vote: Network error" in str(exc_info.value)
        
        expected_payload = {"tick": sample_tick}
        mock_post.assert_called_once_with(
            TICK_QUORUM_VOTE_FULL_URL,
            headers=HEADERS,
            json=expected_payload,
            timeout=core_client.timeout
        )

def test_get_tick_quorum_vote_timeout(core_client, sample_tick):
    """
    Test the get_tick_quorum_vote method for handling a timeout exception.
    """
    with patch('requests.post', side_effect=requests.Timeout("Request timed out")) as mock_post:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_tick_quorum_vote(sample_tick)
        
        assert "Error when getting tick quorum vote: Request timed out" in str(exc_info.value)
        
        expected_payload = {"tick": sample_tick}
        mock_post.assert_called_once_with(
            TICK_QUORUM_VOTE_FULL_URL,
            headers=HEADERS,
            json=expected_payload,
            timeout=core_client.timeout
        )

""" TICK TX """

def test_get_tick_transactions_success(mock_tick_transactions_response, sample_tick_transactions_data, core_client, sample_tick):
    """
    Test the get_tick_transactions method for a successful response.
    
    Verifies that the function returns the expected transactions when the API
    responds successfully.
    """
    with patch('requests.post', return_value=mock_tick_transactions_response) as mock_post:
        result = core_client.get_tick_transactions(sample_tick)
        
        assert result == sample_tick_transactions_data
        mock_tick_transactions_response.raise_for_status.assert_called_once()
        mock_tick_transactions_response.json.assert_called_once()
        
        expected_payload = {"tick": sample_tick}
        mock_post.assert_called_once_with(
            TICK_TRANSACTIONS_FULL_URL,
            headers=HEADERS,
            json=expected_payload,
            timeout=core_client.timeout
        )

def test_get_tick_transactions_no_tick(core_client):
    """
    Test the get_tick_transactions method with no tick provided.
    
    Verifies that the function raises a QubiPy_Exceptions with INVALID_TICK_ERROR when
    no tick is provided.
    """
    with pytest.raises(QubiPy_Exceptions) as exc_info:
        core_client.get_tick_transactions(None)
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_TICK_ERROR

def test_get_tick_transactions_http_error(mock_http_error_response, core_client, sample_tick):
    """
    Test the get_tick_transactions method for handling an HTTP error response.
    """
    with patch('requests.post', return_value=mock_http_error_response) as mock_post:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_tick_transactions(sample_tick)
        
        assert "Error when getting tick transactions" in str(exc_info.value)
        
        expected_payload = {"tick": sample_tick}
        mock_post.assert_called_once_with(
            TICK_TRANSACTIONS_FULL_URL,
            headers=HEADERS,
            json=expected_payload,
            timeout=core_client.timeout
        )

def test_get_tick_transactions_request_exception(core_client, sample_tick):
    """
    Test the get_tick_transactions method for handling a network-related exception.
    """
    with patch('requests.post', side_effect=requests.RequestException("Network error")) as mock_post:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_tick_transactions(sample_tick)
        
        assert "Error when getting tick transactions: Network error" in str(exc_info.value)
        
        expected_payload = {"tick": sample_tick}
        mock_post.assert_called_once_with(
            TICK_TRANSACTIONS_FULL_URL,
            headers=HEADERS,
            json=expected_payload,
            timeout=core_client.timeout
        )

def test_get_tick_transactions_timeout(core_client, sample_tick):
    """
    Test the get_tick_transactions method for handling a timeout exception.
    """
    with patch('requests.post', side_effect=requests.Timeout("Request timed out")) as mock_post:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_tick_transactions(sample_tick)
        
        assert "Error when getting tick transactions: Request timed out" in str(exc_info.value)
        
        expected_payload = {"tick": sample_tick}
        mock_post.assert_called_once_with(
            TICK_TRANSACTIONS_FULL_URL,
            headers=HEADERS,
            json=expected_payload,
            timeout=core_client.timeout
        )