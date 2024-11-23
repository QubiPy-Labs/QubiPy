import pytest
from unittest.mock import patch, Mock
from qubipy.core.core_client import QubiPy_Core
from qubipy.exceptions import QubiPy_Exceptions
from qubipy.endpoints_core import *
import requests
from ..conftest import *

ACTIVE_BETS_FULL_URL = f"{CORE_URL}{ACTIVE_BETS}"
ACTIVE_BETS_BY_CREATOR_FULL_URL = f"{CORE_URL}{ACTIVE_BETS_BY_CREATOR}"
BASIC_INFO_FULL_URL = f"{CORE_URL}{BASIC_INFO}"
BET_INFO_FULL_URL = f"{CORE_URL}{BET_INFO}"

def test_get_active_bets_success(mock_active_bets_response, sample_active_bets_data, core_client):
    """
    Test the get_active_bets method for a successful response.
    
    Verifies that the function returns the expected list of active bet IDs when the API
    responds successfully.
    """
    with patch('requests.get', return_value=mock_active_bets_response) as mock_get:
        result = core_client.get_active_bets()
        
        assert result == sample_active_bets_data
        mock_active_bets_response.raise_for_status.assert_called_once()
        mock_active_bets_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            ACTIVE_BETS_FULL_URL,
            headers=HEADERS,
            timeout=core_client.timeout
        )

def test_get_active_bets_http_error(mock_http_error_response, core_client):
    """
    Test the get_active_bets method for handling an HTTP error response.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the API responds with an HTTP error.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_active_bets()
        
        assert "Error when getting active bets" in str(exc_info.value)
        mock_get.assert_called_once_with(
            ACTIVE_BETS_FULL_URL,
            headers=HEADERS,
            timeout=core_client.timeout
        )

def test_get_active_bets_request_exception(core_client):
    """
    Test the get_active_bets method for handling a network-related exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when a network-related error occurs.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_active_bets()
        
        assert "Error when getting active bets: Network error" in str(exc_info.value)
        mock_get.assert_called_once_with(
            ACTIVE_BETS_FULL_URL,
            headers=HEADERS,
            timeout=core_client.timeout
        )

def test_get_active_bets_timeout(mock_timeout_response, core_client):
    """
    Test the get_active_bets method for handling a timeout exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the request times out.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_active_bets()
        
        assert "Error when getting active bets: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(
            ACTIVE_BETS_FULL_URL,
            headers=HEADERS,
            timeout=core_client.timeout
        )

""" ACTIVE BETS BY CREATOR """

def test_get_active_bets_by_creator_success(mock_active_bets_by_creator_response, sample_active_bets_by_creator_data, core_client, sample_creator_id):
    """
    Test the get_active_bets_by_creator method for a successful response.
    
    Verifies that the function returns the expected list of active bet IDs for a specific creator
    when the API responds successfully.
    """
    with patch('requests.get', return_value=mock_active_bets_by_creator_response) as mock_get:
        result = core_client.get_active_bets_by_creator(sample_creator_id)
        
        assert result == sample_active_bets_by_creator_data
        mock_active_bets_by_creator_response.raise_for_status.assert_called_once()
        mock_active_bets_by_creator_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            ACTIVE_BETS_BY_CREATOR_FULL_URL,
            headers=HEADERS,
            params={'creatorId': sample_creator_id},
            timeout=core_client.timeout
        )

def test_get_active_bets_by_creator_no_creator_id(core_client):
    """
    Test the get_active_bets_by_creator method with no creator ID provided.
    
    Verifies that the function raises a QubiPy_Exceptions with INVALID_ADDRESS_ID when
    no creator ID is provided.
    """
    with pytest.raises(QubiPy_Exceptions) as exc_info:
        core_client.get_active_bets_by_creator(None)
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_ADDRESS_ID

def test_get_active_bets_by_creator_http_error(mock_http_error_response, core_client, sample_creator_id):
    """
    Test the get_active_bets_by_creator method for handling an HTTP error response.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_active_bets_by_creator(sample_creator_id)
        
        assert "Error when getting active bets by creator" in str(exc_info.value)
        mock_get.assert_called_once_with(
            ACTIVE_BETS_BY_CREATOR_FULL_URL,
            headers=HEADERS,
            params={'creatorId': sample_creator_id},
            timeout=core_client.timeout
        )

def test_get_active_bets_by_creator_request_exception(core_client, sample_creator_id):
    """
    Test the get_active_bets_by_creator method for handling a network-related exception.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_active_bets_by_creator(sample_creator_id)
        
        assert "Error when getting active bets by creator: Network error" in str(exc_info.value)
        mock_get.assert_called_once_with(
            ACTIVE_BETS_BY_CREATOR_FULL_URL,
            headers=HEADERS,
            params={'creatorId': sample_creator_id},
            timeout=core_client.timeout
        )

def test_get_active_bets_by_creator_timeout(mock_timeout_response, core_client, sample_creator_id):
    """
    Test the get_active_bets_by_creator method for handling a timeout exception.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_active_bets_by_creator(sample_creator_id)
        
        assert "Error when getting active bets by creator: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(
            ACTIVE_BETS_BY_CREATOR_FULL_URL,
            headers=HEADERS,
            params={'creatorId': sample_creator_id},
            timeout=core_client.timeout
        )

""" BASIC INFO """

def test_get_basic_info_success(mock_basic_info_response, sample_basic_info_data, core_client):
    """
    Test the get_basic_info method for a successful response.
    
    Verifies that the function returns the expected basic information when the API
    responds successfully.
    """
    with patch('requests.get', return_value=mock_basic_info_response) as mock_get:
        result = core_client.get_basic_info()
        
        assert result == sample_basic_info_data
        mock_basic_info_response.raise_for_status.assert_called_once()
        mock_basic_info_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            BASIC_INFO_FULL_URL,
            headers=HEADERS,
            timeout=core_client.timeout
        )

def test_get_basic_info_http_error(mock_http_error_response, core_client):
    """
    Test the get_basic_info method for handling an HTTP error response.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the API responds with an HTTP error.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_basic_info()
        
        assert "Error when getting basic info" in str(exc_info.value)
        mock_get.assert_called_once_with(
            BASIC_INFO_FULL_URL,
            headers=HEADERS,
            timeout=core_client.timeout
        )

def test_get_basic_info_request_exception(core_client):
    """
    Test the get_basic_info method for handling a network-related exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when a network-related error occurs.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_basic_info()
        
        assert "Error when getting basic info: Network error" in str(exc_info.value)
        mock_get.assert_called_once_with(
            BASIC_INFO_FULL_URL,
            headers=HEADERS,
            timeout=core_client.timeout
        )

def test_get_basic_info_timeout(mock_timeout_response, core_client):
    """
    Test the get_basic_info method for handling a timeout exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the request times out.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_basic_info()
        
        assert "Error when getting basic info: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(
            BASIC_INFO_FULL_URL,
            headers=HEADERS,
            timeout=core_client.timeout
        )

""" BET INFO """

def test_get_bet_info_success(mock_bet_info_response, sample_bet_info_data, core_client, sample_bet_id):
    """
    Test the get_bet_info method for a successful response.
    
    Verifies that the function returns the expected bet information when the API
    responds successfully.
    """
    with patch('requests.get', return_value=mock_bet_info_response) as mock_get:
        result = core_client.get_bet_info(sample_bet_id)
        
        assert result == sample_bet_info_data
        mock_bet_info_response.raise_for_status.assert_called_once()
        mock_bet_info_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            BET_INFO_FULL_URL,
            headers=HEADERS,
            params={'betId': sample_bet_id},
            timeout=core_client.timeout
        )

def test_get_bet_info_no_bet_id(core_client):
    """
    Test the get_bet_info method with no bet ID provided.
    
    Verifies that the function raises a QubiPy_Exceptions with INVALID_BET_ID when
    no bet ID is provided.
    """
    with pytest.raises(QubiPy_Exceptions) as exc_info:
        core_client.get_bet_info(None)
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_BET_ID

def test_get_bet_info_http_error(mock_http_error_response, core_client, sample_bet_id):
    """
    Test the get_bet_info method for handling an HTTP error response.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_bet_info(sample_bet_id)
        
        assert "Error when getting bet info by id" in str(exc_info.value)
        mock_get.assert_called_once_with(
            BET_INFO_FULL_URL,
            headers=HEADERS,
            params={'betId': sample_bet_id},
            timeout=core_client.timeout
        )

def test_get_bet_info_request_exception(core_client, sample_bet_id):
    """
    Test the get_bet_info method for handling a network-related exception.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_bet_info(sample_bet_id)
        
        assert "Error when getting bet info by id: Network error" in str(exc_info.value)
        mock_get.assert_called_once_with(
            BET_INFO_FULL_URL,
            headers=HEADERS,
            params={'betId': sample_bet_id},
            timeout=core_client.timeout
        )

def test_get_bet_info_timeout(mock_timeout_response, core_client, sample_bet_id):
    """
    Test the get_bet_info method for handling a timeout exception.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_bet_info(sample_bet_id)
        
        assert "Error when getting bet info by id: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(
            BET_INFO_FULL_URL,
            headers=HEADERS,
            params={'betId': sample_bet_id},
            timeout=core_client.timeout
        )