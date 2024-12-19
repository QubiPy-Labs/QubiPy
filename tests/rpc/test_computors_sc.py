import pytest
from unittest.mock import patch
from qubipy.exceptions import QubiPy_Exceptions
from qubipy.endpoints_rpc import COMPUTORS, QUERY_SC
import requests
import base64
from ..conftest import *

COMPUTORS_FULL_URL = f"{RPC_URL}{COMPUTORS}"
QUERY_SC_FULL_URL = f"{RPC_URL}{QUERY_SC}"


def test_get_computors_success(mock_computors_response, sample_computors_data, rpc_client, sample_epoch):
    """
    Test the get_computors method for a successful response.
    
    Verifies that the function returns the expected computors data when the API
    responds successfully.
    """
    with patch('requests.get', return_value=mock_computors_response) as mock_get:
        result = rpc_client.get_computors(sample_epoch)
        
        assert result == sample_computors_data
        mock_computors_response.raise_for_status.assert_called_once()
        mock_computors_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            COMPUTORS_FULL_URL.format(epoch=sample_epoch),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )
    

def test_get_computors_no_epoch(rpc_client):
    """
    Test the get_computors method with no epoch provided.
    
    Verifies that the function raises a QubiPy_Exceptions with INVALID_EPOCH when
    no epoch is provided.
    """
    with pytest.raises(QubiPy_Exceptions) as exc_info:
        rpc_client.get_computors(None)
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_EPOCH

def test_get_computors_http_error(mock_http_error_response, rpc_client, sample_epoch):
    """
    Test the get_computors method for handling an HTTP error response.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the API responds with an HTTP error.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_computors(sample_epoch)
        
        assert "Failed to retrieve the computors" in str(exc_info.value)
        mock_get.assert_called_once_with(
            COMPUTORS_FULL_URL.format(epoch=sample_epoch),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_computors_request_exception(rpc_client, sample_epoch):
    """
    Test the get_computors method for handling a network-related exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when a network-related error occurs.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_computors(sample_epoch)
        
        assert "Failed to retrieve the computors: Network error" in str(exc_info.value)
        mock_get.assert_called_once_with(
            COMPUTORS_FULL_URL.format(epoch=sample_epoch),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_computors_timeout(rpc_client, sample_epoch):
    """
    Test the get_computors method for handling a timeout exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the request times out.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_computors(sample_epoch)
        
        assert "Failed to retrieve the computors: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(
            COMPUTORS_FULL_URL.format(epoch=sample_epoch),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

""" SMART CONTRACT """

def test_query_smart_contract_success(mock_smart_contract_response, sample_smart_contract_data, rpc_client, sample_contract_params):
    """
    Test the query_smart_contract method for a successful response.
    
    Verifies that the function returns the expected smart contract response when the API
    responds successfully.
    """
    with patch('requests.post', return_value=mock_smart_contract_response) as mock_post:
        result = rpc_client.query_smart_contract(
            sample_contract_params['contract_index'],
            sample_contract_params['input_type'],
            sample_contract_params['input_size'],
            sample_contract_params['request_data']
        )
        
        assert result == sample_smart_contract_data
        mock_smart_contract_response.raise_for_status.assert_called_once()
        mock_smart_contract_response.json.assert_called_once()
        
        expected_payload = {
            "contractIndex": sample_contract_params['contract_index'],
            "inputType": sample_contract_params['input_type'],
            "inputSize": sample_contract_params['input_size'],
            "requestData": base64.b64encode(sample_contract_params['request_data'].encode('utf-8')).decode('utf-8')
        }
        
        mock_post.assert_called_once_with(
            QUERY_SC_FULL_URL,
            headers=HEADERS,
            json=expected_payload,
            timeout=rpc_client.timeout
        )

def test_query_smart_contract_invalid_data(rpc_client):
    """
    Test the query_smart_contract method with invalid or missing smart contract data.
    
    Verifies that the function raises a QubiPy_Exceptions with INVALID_SC_DATA when
    the smart contract data is not valid or is missing.
    """
    with pytest.raises(QubiPy_Exceptions) as exc_info:
        rpc_client.query_smart_contract(None, None, None, None)
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_SC_DATA

    # También podemos probar con algunos datos inválidos
    with pytest.raises(QubiPy_Exceptions) as exc_info:
        rpc_client.query_smart_contract('', '', '', '')
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_SC_DATA

def test_query_smart_contract_http_error(mock_http_error_response, rpc_client, sample_contract_params):
    """
    Test the query_smart_contract method for handling an HTTP error response.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the API responds with an HTTP error.
    """
    with patch('requests.post', return_value=mock_http_error_response) as mock_post:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.query_smart_contract(
                sample_contract_params['contract_index'],
                sample_contract_params['input_type'],
                sample_contract_params['input_size'],
                sample_contract_params['request_data']
            )
        
        assert "Failed to query SC" in str(exc_info.value)

def test_query_smart_contract_request_exception(rpc_client, sample_contract_params):
    """
    Test the query_smart_contract method for handling a network-related exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when a network-related error occurs.
    """
    with patch('requests.post', side_effect=requests.RequestException("Network error")) as mock_post:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.query_smart_contract(
                sample_contract_params['contract_index'],
                sample_contract_params['input_type'],
                sample_contract_params['input_size'],
                sample_contract_params['request_data']
            )
        
        assert "Failed to query SC: Network error" in str(exc_info.value)

def test_query_smart_contract_timeout(rpc_client, sample_contract_params):
    """
    Test the query_smart_contract method for handling a timeout exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the request times out.
    """
    with patch('requests.post', side_effect=requests.Timeout("Request timed out")) as mock_post:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.query_smart_contract(
                sample_contract_params['contract_index'],
                sample_contract_params['input_type'],
                sample_contract_params['input_size'],
                sample_contract_params['request_data']
            )
        
        assert "Failed to query SC: Request timed out" in str(exc_info.value)