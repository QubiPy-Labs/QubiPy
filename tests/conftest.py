# conftest.py
import pytest
from unittest.mock import Mock
from qubipy.rpc.rpc_client import QubiPy_RPC
from qubipy.endpoints_rpc import *
import requests

HEADERS = {'Content-Type': 'application/json', 'accept': 'application/json'}
RPC_URL = "https://rpc.qubic.org/v1"

@pytest.fixture
def sample_tick():
    return 17021024

@pytest.fixture
def sample_approved_transaction_data():
    return [{
        'sourceId': 'VUEYKUCYYHXKDGOSCWAIEECECDBCXVUSUAJRVXUQVAQPGIOABLGGLXDAXTNK',
        'destId': 'DFZSCECHMTCGUFUXKSXLGUITCMZAWJEIJNRQFYJYYENQZUVFAZFLQAXGCNJH',
        'amount': '47472785',
        'tickNumber': 17056942,
        'inputType': 0,
        'inputSize': 0,
        'inputHex': '',
        'signatureHex': '9d4c36d925a3bebdc7ad9df6af19986769e8b87789a4a45e3510fe9b0c7e56578112cd499f8b7b0e4f3f0889c2bf61ccb655b70bb9cad36f3c927ea566e11600',
        'txId': 'ywgbsjnvpjavjgsdbbwhrrjgctmcnanxybugdroubhijserehrnkurgexuue'
    }]

@pytest.fixture
def mock_approved_transaction_response(sample_approved_transaction_data):
    response = Mock()
    response.raise_for_status.return_value = None
    response.json.return_value = {'approvedTransactions': sample_approved_transaction_data}
    return response


@pytest.fixture
def mock_successful_response():
    response = Mock()
    response.raise_for_status.return_value = None
    response.json.return_value = {'latestTick': 17021024}
    return response

@pytest.fixture
def mock_http_error_response():
    response = Mock()
    response.raise_for_status.side_effect = requests.HTTPError("500 Server Error")
    return response

@pytest.fixture
def rpc_client():
    return QubiPy_RPC(rpc_url=RPC_URL)

@pytest.fixture
def mock_timeout_response():
    response = Mock()
    response.raise_for_status.side_effect = requests.Timeout("Request timed out")
    return response

""" WALLET ID """

@pytest.fixture
def sample_wallet_id():
    return "EGOCTGJSNPNEJFSSCTOKAEBKMEEDGLXXVFFHUWHBFEHZOGLMEMAUQZOAVKAN"

@pytest.fixture
def sample_balance_data():
    return {
        'id': 'EGOCTGJSNPNEJFSSCTOKAEBKMEEDGLXXVFFHUWHBFEHZOGLMEMAUQZOAVKAN',
        'balance': '20000000',
        'validForTick': 17088186,
        'latestIncomingTransferTick': 17087621,
        'latestOutgoingTransferTick': 17088111,
        'incomingAmount': '20783623007',
        'outgoingAmount': '20763623007',
        'numberOfIncomingTransfers': 2844,
        'numberOfOutgoingTransfers': 11882
    }

@pytest.fixture
def mock_balance_response(sample_balance_data):
    response = Mock()
    response.raise_for_status.return_value = None
    response.json.return_value = {'balance': sample_balance_data}
    return response