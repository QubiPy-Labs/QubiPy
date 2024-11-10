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

""" RPC STATUS """

@pytest.fixture
def sample_rpc_status_data():
    return {
        'lastProcessedTick': {
            'tickNumber': 17088292,
            'epoch': 134
        },
        'lastProcessedTicksPerEpoch': {
            '133': 17032837,
            '134': 17088292
        },
        'skippedTicks': [
            {'startTick': 1, 'endTick': 13359999},
            {'startTick': 17032838, 'endTick': 17032838}
        ],
        'processedTickIntervalsPerEpoch': [
            {
                'epoch': 133,
                'intervals': [{'initialProcessedTick': 16910000, 'lastProcessedTick': 17032837}]
            },
            {
                'epoch': 134,
                'intervals': [{'initialProcessedTick': 17032839, 'lastProcessedTick': 17088292}]
            }
        ],
        'emptyTicksPerEpoch': {
            '133': 3528,
            '134': 1302
        }
    }

@pytest.fixture
def mock_rpc_status_response(sample_rpc_status_data):
    response = Mock()
    response.raise_for_status.return_value = None
    response.json.return_value = sample_rpc_status_data
    return response

""" HEALTH CHECK """

@pytest.fixture
def sample_health_check_data():
    return {'status': True}

@pytest.fixture
def mock_health_check_response(sample_health_check_data):
    response = Mock()
    response.raise_for_status.return_value = None
    response.json.return_value = sample_health_check_data
    return response

""" BLOCK HEIGHT """

@pytest.fixture
def sample_block_height_data():
   return {
       'tick': 17088516,
       'duration': 3,
       'epoch': 134,
       'initialTick': 17032839
   }

@pytest.fixture
def mock_block_height_response(sample_block_height_data):
   response = Mock()
   response.raise_for_status.return_value = None
   response.json.return_value = {'blockHeight': sample_block_height_data}
   return response

""" LATEST STATS """

@pytest.fixture
def sample_latest_stats_data():
   return {
       'timestamp': '1731159377',
       'circulatingSupply': '120484458286056',
       'activeAddresses': 475436,
       'price': 1.428e-06,
       'marketCap': '172051808',
       'epoch': 134,
       'currentTick': 17088558,
       'ticksInCurrentEpoch': 55719,
       'emptyTicksInCurrentEpoch': 1308,
       'epochTickQuality': 97.652504,
       'burnedQus': '13515541713944'
   }

@pytest.fixture
def mock_latest_stats_response(sample_latest_stats_data):
   response = Mock()
   response.raise_for_status.return_value = None
   response.json.return_value = {'data': sample_latest_stats_data}
   return response

""" ISSUED ASSETS """

@pytest.fixture
def sample_identity():
   return "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFXIB"

@pytest.fixture
def sample_issued_assets_data():
   return [
       {
           'data': {
               'issuerIdentity': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFXIB',
               'type': 1,
               'name': 'RANDOM',
               'numberOfDecimalPlaces': 0,
               'unitOfMeasurement': [0, 0, 0, 0, 0, 0, 0]
           },
           'info': {
               'tick': 17089203,
               'universeIndex': 0
           }
       },
       {
           'data': {
               'issuerIdentity': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFXIB',
               'type': 1,
               'name': 'QX',
               'numberOfDecimalPlaces': 0,
               'unitOfMeasurement': [0, 0, 0, 0, 0, 0, 0]
           },
           'info': {
               'tick': 17089203,
               'universeIndex': 1
           }
       }
   ]

@pytest.fixture
def mock_issued_assets_response(sample_issued_assets_data):
   response = Mock()
   response.raise_for_status.return_value = None
   response.json.return_value = {'issuedAssets': sample_issued_assets_data}
   return response

""" OWNED ASSETS """

@pytest.fixture
def sample_owned_assets_data():
   return [{
       'data': {
           'ownerIdentity': 'CFBMEMZOIDEXQAUXYYSZIURADQLAPWPMNJXQSNVQZAHYVOPYUKKJBJUCTVJL',
           'type': 2,
           'padding': 0,
           'managingContractIndex': 1,
           'issuanceIndex': 12267528,
           'numberOfUnits': '130510491365',
           'issuedAsset': {
               'issuerIdentity': 'CFBMEMZOIDEXQAUXYYSZIURADQLAPWPMNJXQSNVQZAHYVOPYUKKJBJUCTVJL',
               'type': 1,
               'name': 'CFB',
               'numberOfDecimalPlaces': 0,
               'unitOfMeasurement': [0, -48, 0, -48, 35, 24, 21]
           }
       },
       'info': {
           'tick': 17089329,
           'universeIndex': 12267529
       }
   }]

@pytest.fixture
def mock_owned_assets_response(sample_owned_assets_data):
   response = Mock()
   response.raise_for_status.return_value = None
   response.json.return_value = {'ownedAssets': sample_owned_assets_data}
   return response

""" POSSESSED ASSETS """

@pytest.fixture
def sample_possessed_assets_data():
   return [{
       'data': {
           'possessorIdentity': 'CFBMEMZOIDEXQAUXYYSZIURADQLAPWPMNJXQSNVQZAHYVOPYUKKJBJUCTVJL',
           'type': 3,
           'padding': 0,
           'managingContractIndex': 1,
           'issuanceIndex': 12267529,
           'numberOfUnits': '130510491365',
           'ownedAsset': {
               'ownerIdentity': 'CFBMEMZOIDEXQAUXYYSZIURADQLAPWPMNJXQSNVQZAHYVOPYUKKJBJUCTVJL',
               'type': 3,
               'padding': 0,
               'managingContractIndex': 1,
               'issuanceIndex': 12267529,
               'numberOfUnits': '130510491365',
               'issuedAsset': {
                   'issuerIdentity': 'CFBMEMZOIDEXQAUXYYSZIURADQLAPWPMNJXQSNVQZAHYVOPYUKKJBJUCTVJL',
                   'type': 1,
                   'name': 'CFB',
                   'numberOfDecimalPlaces': 0,
                   'unitOfMeasurement': [0, -48, 0, -48, 35, 24, 21]
               }
           }
       },
       'info': {
           'tick': 17089367,
           'universeIndex': 12267530
       }
   }]

@pytest.fixture
def mock_possessed_assets_response(sample_possessed_assets_data):
   response = Mock()
   response.raise_for_status.return_value = None
   response.json.return_value = {'possessedAssets': sample_possessed_assets_data}
   return response

""" CHAIN HASH """

@pytest.fixture
def sample_chain_hash_data():
   return "2a8d4845f9de63318a88ab2f2d723ba1f656f3e90214843608bc7e86949704ee"

@pytest.fixture
def mock_chain_hash_response(sample_chain_hash_data):
   response = Mock()
   response.raise_for_status.return_value = None
   response.json.return_value = {'hexDigest': sample_chain_hash_data}
   return response

""" QUORUM TICK DATA """

@pytest.fixture
def sample_quorum_tick_data():
    return {
        'quorumTickData': {
            'quorumTickStructure': {
                'epoch': 134,
                'tickNumber': 17109368,
                'timestamp': '1731256305000',
                'prevResourceTestingDigestHex': '34db5c0d34e83778',
                'prevSpectrumDigestHex': 'eaaa8e9796c77c4fbcbb053085f1b3fb563a552ceead4250d43fa30a6c1dba9b',
                'prevUniverseDigestHex': '05b9f286367a3c5cc570c7094e29a27f79222d5c8f33fccd3a04fac830baee63',
                'prevComputerDigestHex': '31d6125e3abcc3f4346219f505ae0ff68c7ab57088cf1d238875e901d49524f7',
                'txDigestHex': 'a7fcd26e475a6b89800d190656dd8819585a3205f9b9c528b269a86ac3bc60b6'
            },
            'quorumDiffPerComputor': {
                '7': {
                    'saltedResourceTestingDigestHex': '5f80d38310005ce1',
                    'saltedSpectrumDigestHex': 'f3b0d39abfa3cf6d2e7741fd3b3468d2d76b4482dcadae130c06859b2b9ece48',
                    'saltedUniverseDigestHex': 'd00538954de165056684211acf6cac7b344d73e67b9a159e140c4a8167fdb553',
                    'saltedComputerDigestHex': '30f557ae9288cc7907191071e90815617e5e8648bbebcb749ac4fa16083af2b2',
                    'expectedNextTickTxDigestHex': 'ba24336be17ea9e67f348cc89ba3a86785b9eece09a92fddadcd8ec007ccf931',
                    'signatureHex': 'f706fbbb4a12630145f8ddfbb025783e4e5b23d4e3b06487e9f5bc2b600837371c2c544c4a4ea6704be454e7819acc7d2005c81e91baf9d73cbda9aff49f0700'
                },
                '8': {
                    'saltedResourceTestingDigestHex': 'b6c4cf705c270e39',
                    'saltedSpectrumDigestHex': 'e76ed9421b83d70963afa888957d6d368d8b14d2e31028d585f986ad0234507f',
                    'saltedUniverseDigestHex': 'c6a80db95531fb2293771b4b52e79a4533725e19652d99d04d825dcc02b445e5',
                    'saltedComputerDigestHex': '1f43d25b4895625f84d724d2ec983796fab07b1ab809c9575e3ecba5e9fec4a2',
                    'expectedNextTickTxDigestHex': 'ba24336be17ea9e67f348cc89ba3a86785b9eece09a92fddadcd8ec007ccf931',
                    'signatureHex': '9755aa77f9f0ee1412531785faf3d91b00d2067aa8bd58214c1fff0257a33c7fab582c41f5e499a76bfee08449f366117e25ac1ca6f5c4d48b6343847d8c1c00'
                }
            }
        }
    }

@pytest.fixture
def mock_quorum_tick_data_response(sample_quorum_tick_data):
    response = Mock()
    response.raise_for_status.return_value = None
    response.json.return_value = sample_quorum_tick_data
    return response

""" CHAIN HASH """

@pytest.fixture
def sample_store_hash_data():
   return {'hexDigest': 'e42bc16369f52cb4a2b497f9b69a7bedc75ad7f9b2ad8a6f9c1e1669859a1f14'}

@pytest.fixture
def mock_store_hash_response(sample_store_hash_data):
   response = Mock()
   response.raise_for_status.return_value = None
   response.json.return_value = sample_store_hash_data
   return response