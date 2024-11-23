import pytest
from unittest.mock import patch, Mock
from qubipy.exceptions import QubiPy_Exceptions
from qubipy.endpoints_rpc import *
import requests
import json
from ..conftest import *

TRANSACTION_FULL_URL = f"{RPC_URL}{TRANSACTION}"
TRANSACTION_STATUS_FULL_URL = f"{RPC_URL}{TRANSACTION_STATUS}"
TRANSFER_TRANSACTIONS_PER_TICK_FULL_URL = f"{RPC_URL}{TRANSFER_TRANSACTIONS_PER_TICK}"
BROADCAST_TRANSACTION_FULL_URL = f"{RPC_URL}{BROADCAST_TRANSACTION}"

def test_get_transaction_success(mock_transaction_response, sample_transaction_data, rpc_client, sample_tx_id):
    """
    Test the get_transaction method for a successful response.
    
    Verifies that the function returns the expected transaction data when the API
    responds successfully.
    """
    with patch('requests.get', return_value=mock_transaction_response) as mock_get:
        result = rpc_client.get_transaction(sample_tx_id)
        
        assert result == sample_transaction_data
        mock_transaction_response.raise_for_status.assert_called_once()
        mock_transaction_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            TRANSACTION_FULL_URL.format(tx_id=sample_tx_id),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_transaction_no_tx_id(rpc_client):
    """
    Test the get_transaction method with no transaction ID provided.
    
    Verifies that the function raises a QubiPy_Exceptions with INVALID_TX_ID when
    no transaction ID is provided.
    """
    with pytest.raises(QubiPy_Exceptions) as exc_info:
        rpc_client.get_transaction(None)
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_TX_ID

def test_get_transaction_http_error(mock_http_error_response, rpc_client, sample_tx_id):
    """
    Test the get_transaction method for handling an HTTP error response.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the API responds with an HTTP error.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_transaction(sample_tx_id)
        
        assert "Failed to retrieve the transaction data" in str(exc_info.value)
        mock_get.assert_called_once_with(
            TRANSACTION_FULL_URL.format(tx_id=sample_tx_id),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_transaction_request_exception(rpc_client, sample_tx_id):
    """
    Test the get_transaction method for handling a network-related exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when a network-related error occurs.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_transaction(sample_tx_id)
        
        assert "Failed to retrieve the transaction data: Network error" in str(exc_info.value)
        mock_get.assert_called_once_with(
            TRANSACTION_FULL_URL.format(tx_id=sample_tx_id),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_transaction_timeout(rpc_client, sample_tx_id):
    """
    Test the get_transaction method for handling a timeout exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the request times out.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_transaction(sample_tx_id)
        
        assert "Failed to retrieve the transaction data: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(
            TRANSACTION_FULL_URL.format(tx_id=sample_tx_id),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

""" TX STATUS """

def test_get_transaction_status_success(mock_transaction_status_response, sample_transaction_status_data, rpc_client, sample_tx_id):
    """
    Test the get_transaction_status method for a successful response.
    
    Verifies that the function returns the expected transaction status when the API
    responds successfully.
    """
    with patch('requests.get', return_value=mock_transaction_status_response) as mock_get:
        result = rpc_client.get_transaction_status(sample_tx_id)
        
        assert result == sample_transaction_status_data
        mock_transaction_status_response.raise_for_status.assert_called_once()
        mock_transaction_status_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            TRANSACTION_STATUS_FULL_URL.format(tx_id=sample_tx_id),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_transaction_status_no_tx_id(rpc_client):
    """
    Test the get_transaction_status method with no transaction ID provided.
    
    Verifies that the function raises a QubiPy_Exceptions with INVALID_TX_ID when
    no transaction ID is provided.
    """
    with pytest.raises(QubiPy_Exceptions) as exc_info:
        rpc_client.get_transaction_status(None)
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_TX_ID

def test_get_transaction_status_http_error(mock_http_error_response, rpc_client, sample_tx_id):
    """
    Test the get_transaction_status method for handling an HTTP error response.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the API responds with an HTTP error.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_transaction_status(sample_tx_id)
        
        assert "Failed to retrieve the transaction status" in str(exc_info.value)
        mock_get.assert_called_once_with(
            TRANSACTION_STATUS_FULL_URL.format(tx_id=sample_tx_id),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_transaction_status_request_exception(rpc_client, sample_tx_id):
    """
    Test the get_transaction_status method for handling a network-related exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when a network-related error occurs.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_transaction_status(sample_tx_id)
        
        assert "Failed to retrieve the transaction status: Network error" in str(exc_info.value)
        mock_get.assert_called_once_with(
            TRANSACTION_STATUS_FULL_URL.format(tx_id=sample_tx_id),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_transaction_status_timeout(mock_timeout_response, rpc_client, sample_tx_id):
    """
    Test the get_transaction_status method for handling a timeout exception.
    
    Verifies that the function raises a QubiPy_Exceptions exception with an
    appropriate message when the request times out.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_transaction_status(sample_tx_id)
        
        assert "Failed to retrieve the transaction status: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(
            TRANSACTION_STATUS_FULL_URL.format(tx_id=sample_tx_id),
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

""" TRANSFER TX PER TICK """

def test_get_transfer_transactions_per_tick_success(mock_transfer_transactions_response, sample_transfer_transactions_data, rpc_client, sample_transfer_params):
    """
    Test the get_transfer_transactions_per_tick method for a successful response.
    
    Verifies that the function returns the expected transfer transactions when the API
    responds successfully.
    """
    with patch('requests.get', return_value=mock_transfer_transactions_response) as mock_get:
        result = rpc_client.get_transfer_transactions_per_tick(
            sample_transfer_params['identity'],
            sample_transfer_params['start_tick'],
            sample_transfer_params['end_tick']
        )
        
        assert result == sample_transfer_transactions_data
        mock_transfer_transactions_response.raise_for_status.assert_called_once()
        mock_transfer_transactions_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            TRANSFER_TRANSACTIONS_PER_TICK_FULL_URL.format(id=sample_transfer_params['identity']),
            params={'startTick': sample_transfer_params['start_tick'], 'endTick': sample_transfer_params['end_tick']},
            headers=HEADERS,
            timeout=rpc_client.timeout
        )

def test_get_transfer_transactions_per_tick_no_identity(rpc_client, sample_transfer_params):
    """
    Test the get_transfer_transactions_per_tick method with no identity provided.
    
    Verifies that the function raises a QubiPy_Exceptions with INVALID_ADDRESS_ID when
    no identity is provided.
    """
    with pytest.raises(QubiPy_Exceptions) as exc_info:
        rpc_client.get_transfer_transactions_per_tick(None, 
            sample_transfer_params['start_tick'],
            sample_transfer_params['end_tick']
        )
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_ADDRESS_ID

def test_get_transfer_transactions_per_tick_no_ticks(rpc_client, sample_transfer_params):
    """
    Test the get_transfer_transactions_per_tick method with no tick values provided.
    
    Verifies that the function raises a QubiPy_Exceptions with INVALID_START_TICK_AND_END_TICK when
    no tick values are provided.
    """
    with pytest.raises(QubiPy_Exceptions) as exc_info:
        rpc_client.get_transfer_transactions_per_tick(
            sample_transfer_params['identity'],
            None,
            None
        )
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_START_TICK_AND_END_TICK

def test_get_transfer_transactions_per_tick_http_error(mock_http_error_response, rpc_client, sample_transfer_params):
    """
    Test the get_transfer_transactions_per_tick method for handling an HTTP error response.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_transfer_transactions_per_tick(
                sample_transfer_params['identity'],
                sample_transfer_params['start_tick'],
                sample_transfer_params['end_tick']
            )
        
        assert "Failed to retrieve the transfer transactions" in str(exc_info.value)

def test_get_transfer_transactions_per_tick_request_exception(rpc_client, sample_transfer_params):
    """
    Test the get_transfer_transactions_per_tick method for handling a network-related exception.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_transfer_transactions_per_tick(
                sample_transfer_params['identity'],
                sample_transfer_params['start_tick'],
                sample_transfer_params['end_tick']
            )
        
        assert "Failed to retrieve the transfer transactions: Network error" in str(exc_info.value)

def test_get_transfer_transactions_per_tick_timeout(mock_timeout_response, rpc_client, sample_transfer_params):
    """
    Test the get_transfer_transactions_per_tick method for handling a timeout exception.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.get_transfer_transactions_per_tick(
                sample_transfer_params['identity'],
                sample_transfer_params['start_tick'],
                sample_transfer_params['end_tick']
            )
        
        assert "Failed to retrieve the transfer transactions: Request timed out" in str(exc_info.value)

""" BROADCAST TRANSACTION """

def test_broadcast_transaction_success(mock_broadcast_response, sample_broadcast_response, rpc_client, sample_tx_bytes):
  """
  Test the broadcast_transaction method for a successful response.
  
  Verifies that the function returns the expected bytearray response when the API
  successfully broadcasts the transaction.
  """
  with patch('requests.post', return_value=mock_broadcast_response) as mock_post:
      result = rpc_client.broadcast_transaction(sample_tx_bytes)
      
      assert result == sample_broadcast_response
      mock_broadcast_response.raise_for_status.assert_called_once()
      mock_broadcast_response.json.assert_called_once()
      
      expected_payload = {
          "encodedTransaction": base64.b64encode(sample_tx_bytes).decode('utf-8')
      }
      
      mock_post.assert_called_once_with(
          BROADCAST_TRANSACTION_FULL_URL,
          data=json.dumps(expected_payload),
          headers={'Content-Type': 'application/json'},
          timeout=rpc_client.timeout
      )

def test_broadcast_transaction_no_tx(rpc_client):
    """
    Test the broadcast_transaction method with no transaction data provided.
    
    Verifies that the function raises a QubiPy_Exceptions with INVALID_TX_BYTES message when
    no transaction data or invalid data is provided.
    """
    with pytest.raises(QubiPy_Exceptions) as exc_info:
        rpc_client.broadcast_transaction(None)
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_TX_BYTES

    with pytest.raises(QubiPy_Exceptions) as exc_info:
        rpc_client.broadcast_transaction("not bytes")
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_TX_BYTES

def test_broadcast_transaction_http_error(mock_http_error_response, rpc_client, sample_tx_bytes):
    """
    Test the broadcast_transaction method for handling an HTTP error response.
    """
    mock_http_error_response.status_code = 500
    with patch('requests.post', return_value=mock_http_error_response) as mock_post:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            rpc_client.broadcast_transaction(sample_tx_bytes)
        
        assert "HTTP error occurred: 500 Server Error" in str(exc_info.value)


def test_broadcast_transaction_request_exception(rpc_client, sample_tx_bytes):
  """
  Test the broadcast_transaction method for handling a network-related exception.
  """
  with patch('requests.post', side_effect=requests.RequestException("Network error")) as mock_post:
      with pytest.raises(QubiPy_Exceptions) as exc_info:
          rpc_client.broadcast_transaction(sample_tx_bytes)
      
      assert "Error broadcasting the transaction: Network error" in str(exc_info.value)

def test_broadcast_transaction_timeout(mock_timeout_response, rpc_client, sample_tx_bytes):
  """
  Test the broadcast_transaction method for handling a timeout exception.
  """
  with patch('requests.post', side_effect=requests.Timeout("Request timed out")) as mock_post:
      with pytest.raises(QubiPy_Exceptions) as exc_info:
          rpc_client.broadcast_transaction(sample_tx_bytes)
      
      assert "Error broadcasting the transaction: Request timed out" in str(exc_info.value)

def test_broadcast_transaction_400_error(rpc_client, sample_tx_bytes):
  """
  Test the broadcast_transaction method for handling a 400 error with specific error details.
  """
  error_response = Mock()
  error_response.status_code = 400
  error_response.json.return_value = {
      'code': 'INVALID_TRANSACTION',
      'message': 'Invalid transaction format'
  }
  error_response.raise_for_status.side_effect = requests.HTTPError("400 Client Error")
  
  with patch('requests.post', return_value=error_response) as mock_post:
      with pytest.raises(QubiPy_Exceptions) as exc_info:
          rpc_client.broadcast_transaction(sample_tx_bytes)
      
      assert "API Error INVALID_TRANSACTION: Invalid transaction format" in str(exc_info.value)