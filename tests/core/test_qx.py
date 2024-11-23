import pytest
from unittest.mock import patch
from qubipy.exceptions import QubiPy_Exceptions
from qubipy.endpoints_core import *
import requests
from ..conftest import *

""" QX ASK ORDERS """

QX_ASSET_ASK_ORDERS_FULL_URL = f"{CORE_URL}{QX_ASSET_ASK_ORDERS}"
QX_ASSET_BID_ORDERS_FULL_URL = f"{CORE_URL}{QX_ASSET_BID_ORDERS}"
QX_ENTITY_ASK_ORDERS_FULL_URL = f"{CORE_URL}{QX_ENTITY_ASK_ORDERS}"
QX_ENTITY_BID_ORDERS_FULL_URL = f"{CORE_URL}{QX_ENTITY_BID_ORDERS}"
QX_FEES_FULL_URL = f"{CORE_URL}{QX_FEES}"


def test_get_qx_asset_ask_orders_success(mock_qx_ask_orders_response, sample_qx_ask_orders_data, core_client, sample_qx_params):
    """
    Test the get_qx_asset_ask_orders method for a successful response.
    
    Verifies that the function returns the expected ask orders when the API
    responds successfully.
    """
    with patch('requests.get', return_value=mock_qx_ask_orders_response) as mock_get:
        result = core_client.get_qx_asset_ask_orders(
            sample_qx_params['asset_name'],
            sample_qx_params['issuer_id'],
            sample_qx_params['offset']
        )
        
        assert result == sample_qx_ask_orders_data
        mock_qx_ask_orders_response.raise_for_status.assert_called_once()
        mock_qx_ask_orders_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            QX_ASSET_ASK_ORDERS_FULL_URL,
            headers=HEADERS,
            params={
                'assetName': sample_qx_params['asset_name'],
                'issuerId': sample_qx_params['issuer_id'],
                'offset': sample_qx_params['offset']
            },
            timeout=core_client.timeout
        )

def test_get_qx_asset_ask_orders_no_data(core_client):
    """
    Test the get_qx_asset_ask_orders method with missing required data.
    
    Verifies that the function raises a QubiPy_Exceptions with INVALID_QX_ASSET_DATA when
    required parameters are not provided.
    """
    with pytest.raises(QubiPy_Exceptions) as exc_info:
        core_client.get_qx_asset_ask_orders(None, None, None)
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_QX_ASSET_DATA

def test_get_qx_asset_ask_orders_http_error(mock_http_error_response, core_client, sample_qx_params):
    """
    Test the get_qx_asset_ask_orders method for handling an HTTP error response.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_qx_asset_ask_orders(
                sample_qx_params['asset_name'],
                sample_qx_params['issuer_id'],
                sample_qx_params['offset']
            )
        
        assert "Error when getting QX data" in str(exc_info.value)
        mock_get.assert_called_once_with(
            QX_ASSET_ASK_ORDERS_FULL_URL,
            headers=HEADERS,
            params={
                'assetName': sample_qx_params['asset_name'],
                'issuerId': sample_qx_params['issuer_id'],
                'offset': sample_qx_params['offset']
            },
            timeout=core_client.timeout
        )

def test_get_qx_asset_ask_orders_request_exception(core_client, sample_qx_params):
    """
    Test the get_qx_asset_ask_orders method for handling a network-related exception.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_qx_asset_ask_orders(
                sample_qx_params['asset_name'],
                sample_qx_params['issuer_id'],
                sample_qx_params['offset']
            )
        
        assert "Error when getting QX data: Network error" in str(exc_info.value)
        mock_get.assert_called_once_with(
            QX_ASSET_ASK_ORDERS_FULL_URL,
            headers=HEADERS,
            params={
                'assetName': sample_qx_params['asset_name'],
                'issuerId': sample_qx_params['issuer_id'],
                'offset': sample_qx_params['offset']
            },
            timeout=core_client.timeout
        )

def test_get_qx_asset_ask_orders_timeout(core_client, sample_qx_params):
    """
    Test the get_qx_asset_ask_orders method for handling a timeout exception.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_qx_asset_ask_orders(
                sample_qx_params['asset_name'],
                sample_qx_params['issuer_id'],
                sample_qx_params['offset']
            )
        
        assert "Error when getting QX data: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(
            QX_ASSET_ASK_ORDERS_FULL_URL,
            headers=HEADERS,
            params={
                'assetName': sample_qx_params['asset_name'],
                'issuerId': sample_qx_params['issuer_id'],
                'offset': sample_qx_params['offset']
            },
            timeout=core_client.timeout
        )

""" BID ORDERS """

def test_get_qx_asset_bid_orders_success(mock_qx_bid_orders_response, sample_qx_bid_orders_data, core_client, sample_qx_params):
    """
    Test the get_qx_asset_bid_orders method for a successful response.
    
    Verifies that the function returns the expected bid orders when the API
    responds successfully.
    """
    with patch('requests.get', return_value=mock_qx_bid_orders_response) as mock_get:
        result = core_client.get_qx_asset_bid_orders(
            sample_qx_params['asset_name'],
            sample_qx_params['issuer_id'],
            sample_qx_params['offset']
        )
        
        assert result == sample_qx_bid_orders_data
        mock_qx_bid_orders_response.raise_for_status.assert_called_once()
        mock_qx_bid_orders_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            QX_ASSET_BID_ORDERS_FULL_URL,
            headers=HEADERS,
            params={
                'assetName': sample_qx_params['asset_name'],
                'issuerId': sample_qx_params['issuer_id'],
                'offset': sample_qx_params['offset']
            },
            timeout=core_client.timeout
        )

def test_get_qx_asset_bid_orders_no_data(core_client):
    """
    Test the get_qx_asset_bid_orders method with missing required data.
    
    Verifies that the function raises a QubiPy_Exceptions with INVALID_QX_ASSET_DATA when
    required parameters are not provided.
    """
    with pytest.raises(QubiPy_Exceptions) as exc_info:
        core_client.get_qx_asset_bid_orders(None, None, None)
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_QX_ASSET_DATA

def test_get_qx_asset_bid_orders_http_error(mock_http_error_response, core_client, sample_qx_params):
   """
   Test the get_qx_asset_bid_orders method for handling an HTTP error response.
   """
   with patch('requests.get', return_value=mock_http_error_response) as mock_get:
       with pytest.raises(QubiPy_Exceptions) as exc_info:
           core_client.get_qx_asset_bid_orders(
               sample_qx_params['asset_name'],
               sample_qx_params['issuer_id'],
               sample_qx_params['offset']
           )
       
       assert "Error when getting QX bid orders" in str(exc_info.value)
       mock_get.assert_called_once_with(
           QX_ASSET_BID_ORDERS_FULL_URL,
           headers=HEADERS,
           params={
               'assetName': sample_qx_params['asset_name'],
               'issuerId': sample_qx_params['issuer_id'],
               'offset': sample_qx_params['offset']
           },
           timeout=core_client.timeout
       )

def test_get_qx_asset_bid_orders_request_exception(core_client, sample_qx_params):
   """
   Test the get_qx_asset_bid_orders method for handling a network-related exception.
   """
   with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
       with pytest.raises(QubiPy_Exceptions) as exc_info:
           core_client.get_qx_asset_bid_orders(
               sample_qx_params['asset_name'],
               sample_qx_params['issuer_id'],
               sample_qx_params['offset']
           )
       
       assert "Error when getting QX bid orders: Network error" in str(exc_info.value)
       mock_get.assert_called_once_with(
           QX_ASSET_BID_ORDERS_FULL_URL,
           headers=HEADERS,
           params={
               'assetName': sample_qx_params['asset_name'],
               'issuerId': sample_qx_params['issuer_id'],
               'offset': sample_qx_params['offset']
           },
           timeout=core_client.timeout
       )

def test_get_qx_asset_bid_orders_timeout(core_client, sample_qx_params):
   """
   Test the get_qx_asset_bid_orders method for handling a timeout exception.
   """
   with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
       with pytest.raises(QubiPy_Exceptions) as exc_info:
           core_client.get_qx_asset_bid_orders(
               sample_qx_params['asset_name'],
               sample_qx_params['issuer_id'],
               sample_qx_params['offset']
           )
       
       assert "Error when getting QX bid orders: Request timed out" in str(exc_info.value)
       mock_get.assert_called_once_with(
           QX_ASSET_BID_ORDERS_FULL_URL,
           headers=HEADERS,
           params={
               'assetName': sample_qx_params['asset_name'],
               'issuerId': sample_qx_params['issuer_id'],
               'offset': sample_qx_params['offset']
           },
           timeout=core_client.timeout
       )

""" ENTITY ASK ORDERS """

def test_get_qx_entity_ask_orders_success(mock_entity_ask_orders_response, sample_entity_ask_orders_data, core_client, sample_entity_id):
    """
    Test the get_qx_entity_ask_orders method for a successful response.
    
    Verifies that the function returns the expected entity ask orders when the API
    responds successfully.
    """
    with patch('requests.get', return_value=mock_entity_ask_orders_response) as mock_get:
        result = core_client.get_qx_entity_ask_orders(sample_entity_id)
        
        assert result == sample_entity_ask_orders_data
        mock_entity_ask_orders_response.raise_for_status.assert_called_once()
        mock_entity_ask_orders_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            QX_ENTITY_ASK_ORDERS_FULL_URL,
            headers=HEADERS,
            params={'entityId': sample_entity_id, 'offset': None},
            timeout=core_client.timeout
        )


def test_get_qx_entity_ask_orders_no_entity_id(core_client):
    """
    Test the get_qx_entity_ask_orders method with no entity ID provided.
    
    Verifies that the function raises a QubiPy_Exceptions with INVALID_QX_ASSET_DATA when
    no entity ID is provided.
    """
    with pytest.raises(QubiPy_Exceptions) as exc_info:
        core_client.get_qx_entity_ask_orders(None)
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_QX_ASSET_DATA

def test_get_qx_entity_ask_orders_http_error(mock_http_error_response, core_client, sample_entity_id):
    """
    Test the get_qx_entity_ask_orders method for handling an HTTP error response.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_qx_entity_ask_orders(sample_entity_id)
        
        assert "Error when getting QX entity ask orders" in str(exc_info.value)
        mock_get.assert_called_once_with(
            QX_ENTITY_ASK_ORDERS_FULL_URL,
            headers=HEADERS,
            params={'entityId': sample_entity_id, 'offset': None},
            timeout=core_client.timeout
        )

def test_get_qx_entity_ask_orders_request_exception(core_client, sample_entity_id):
    """
    Test the get_qx_entity_ask_orders method for handling a network-related exception.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_qx_entity_ask_orders(sample_entity_id)
        
        assert "Error when getting QX entity ask orders: Network error" in str(exc_info.value)
        mock_get.assert_called_once_with(
            QX_ENTITY_ASK_ORDERS_FULL_URL,
            headers=HEADERS,
            params={'entityId': sample_entity_id, 'offset': None},
            timeout=core_client.timeout
        )

def test_get_qx_entity_ask_orders_timeout(core_client, sample_entity_id):
    """
    Test the get_qx_entity_ask_orders method for handling a timeout exception.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_qx_entity_ask_orders(sample_entity_id)
        
        assert "Error when getting QX entity ask orders: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(
            QX_ENTITY_ASK_ORDERS_FULL_URL,
            headers=HEADERS,
            params={'entityId': sample_entity_id, 'offset': None},
            timeout=core_client.timeout
        )

""" ENTITY BID ORDERS """
def test_get_qx_entity_bid_orders_success(mock_entity_bid_orders_response, sample_entity_bid_orders_data, core_client, sample_entity_id):
    """
    Test the get_qx_entity_bid_orders method for a successful response.
    
    Verifies that the function returns the expected entity bid orders when the API
    responds successfully.
    """
    with patch('requests.get', return_value=mock_entity_bid_orders_response) as mock_get:
        result = core_client.get_qx_entity_bid_orders(sample_entity_id)
        
        assert result == sample_entity_bid_orders_data
        mock_entity_bid_orders_response.raise_for_status.assert_called_once()
        mock_entity_bid_orders_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            QX_ENTITY_BID_ORDERS_FULL_URL,
            headers=HEADERS,
            params={'entityId': sample_entity_id, 'offset': None},
            timeout=core_client.timeout
        )

def test_get_qx_entity_bid_orders_with_offset(mock_entity_bid_orders_response, sample_entity_bid_orders_data, core_client, sample_entity_id):
    """
    Test the get_qx_entity_bid_orders method with optional offset parameter.
    """
    offset = "0"
    with patch('requests.get', return_value=mock_entity_bid_orders_response) as mock_get:
        result = core_client.get_qx_entity_bid_orders(sample_entity_id, offset)
        
        assert result == sample_entity_bid_orders_data
        mock_get.assert_called_once_with(
            QX_ENTITY_BID_ORDERS_FULL_URL,
            headers=HEADERS,
            params={'entityId': sample_entity_id, 'offset': offset},
            timeout=core_client.timeout
        )

def test_get_qx_entity_bid_orders_no_entity_id(core_client):
    """
    Test the get_qx_entity_bid_orders method with no entity ID provided.
    
    Verifies that the function raises a QubiPy_Exceptions with INVALID_QX_ASSET_DATA when
    no entity ID is provided.
    """
    with pytest.raises(QubiPy_Exceptions) as exc_info:
        core_client.get_qx_entity_bid_orders(None)
    
    assert str(exc_info.value) == QubiPy_Exceptions.INVALID_QX_ASSET_DATA

def test_get_qx_entity_bid_orders_http_error(mock_http_error_response, core_client, sample_entity_id):
    """
    Test the get_qx_entity_bid_orders method for handling an HTTP error response.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_qx_entity_bid_orders(sample_entity_id)
        
        assert "Error when getting QX entity bid orders" in str(exc_info.value)
        mock_get.assert_called_once_with(
            QX_ENTITY_BID_ORDERS_FULL_URL,
            headers=HEADERS,
            params={'entityId': sample_entity_id, 'offset': None},
            timeout=core_client.timeout
        )

def test_get_qx_entity_bid_orders_request_exception(core_client, sample_entity_id):
    """
    Test the get_qx_entity_bid_orders method for handling a network-related exception.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_qx_entity_bid_orders(sample_entity_id)
        
        assert "Error when getting QX entity bid orders: Network error" in str(exc_info.value)
        mock_get.assert_called_once_with(
            QX_ENTITY_BID_ORDERS_FULL_URL,
            headers=HEADERS,
            params={'entityId': sample_entity_id, 'offset': None},
            timeout=core_client.timeout
        )

def test_get_qx_entity_bid_orders_timeout(core_client, sample_entity_id):
    """
    Test the get_qx_entity_bid_orders method for handling a timeout exception.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_qx_entity_bid_orders(sample_entity_id)
        
        assert "Error when getting QX entity bid orders: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(
            QX_ENTITY_BID_ORDERS_FULL_URL,
            headers=HEADERS,
            params={'entityId': sample_entity_id, 'offset': None},
            timeout=core_client.timeout
        )


""" QX FEES """

def test_get_qx_fees_success(mock_qx_fees_response, sample_qx_fees_data, core_client):
    """
    Test the get_qx_fees method for a successful response.
    
    Verifies that the function returns the expected QX fees when the API
    responds successfully.
    """
    with patch('requests.get', return_value=mock_qx_fees_response) as mock_get:
        result = core_client.get_qx_fees()
        
        assert result == sample_qx_fees_data
        mock_qx_fees_response.raise_for_status.assert_called_once()
        mock_qx_fees_response.json.assert_called_once()
        mock_get.assert_called_once_with(
            QX_FEES_FULL_URL,
            headers=HEADERS,
            timeout=core_client.timeout
        )

def test_get_qx_fees_http_error(mock_http_error_response, core_client):
    """
    Test the get_qx_fees method for handling an HTTP error response.
    """
    with patch('requests.get', return_value=mock_http_error_response) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_qx_fees()
        
        assert "Error when getting QX fees" in str(exc_info.value)
        mock_get.assert_called_once_with(
            QX_FEES_FULL_URL,
            headers=HEADERS,
            timeout=core_client.timeout
        )

def test_get_qx_fees_request_exception(core_client):
    """
    Test the get_qx_fees method for handling a network-related exception.
    """
    with patch('requests.get', side_effect=requests.RequestException("Network error")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_qx_fees()
        
        assert "Error when getting QX fees: Network error" in str(exc_info.value)
        mock_get.assert_called_once_with(
            QX_FEES_FULL_URL,
            headers=HEADERS,
            timeout=core_client.timeout
        )

def test_get_qx_fees_timeout(core_client):
    """
    Test the get_qx_fees method for handling a timeout exception.
    """
    with patch('requests.get', side_effect=requests.Timeout("Request timed out")) as mock_get:
        with pytest.raises(QubiPy_Exceptions) as exc_info:
            core_client.get_qx_fees()
        
        assert "Error when getting QX fees: Request timed out" in str(exc_info.value)
        mock_get.assert_called_once_with(
            QX_FEES_FULL_URL,
            headers=HEADERS,
            timeout=core_client.timeout
        )