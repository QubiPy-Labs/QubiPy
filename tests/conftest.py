# conftest.py
import pytest
from unittest.mock import Mock
from qubipy.rpc.rpc_client import QubiPy_RPC
from qubipy.core.core_client import QubiPy_Core
from qubipy.endpoints_rpc import *
from qubipy.endpoints_core import *
import requests
import base64

HEADERS = {'Content-Type': 'application/json', 'accept': 'application/json'}
RPC_URL = "https://rpc.qubic.org/v1"
CORE_URL = "https://api.qubic.org/v1"

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

""" RICH LIST """

@pytest.fixture
def sample_page():
   return 1

@pytest.fixture
def sample_page_size():
   return 20

@pytest.fixture
def sample_rich_list_data():
   return {
       'entities': [
           {
               'identity': 'BYBYFUMBVLPUCANXEXTSKVMGFCJBMTLPPOFVPNSATABMWDGTMFXPLZLBCXJL',
               'balance': '10988257022786'
           },
           {
               'identity': 'VUEYKUCYYHXKDGOSCWAIEECECDBCXVUSUAJRVXUQVAQPGIOABLGGLXDAXTNK',
               'balance': '5638925835721'
           }
       ]
   }

@pytest.fixture
def mock_rich_list_response(sample_rich_list_data):
   response = Mock()
   response.raise_for_status.return_value = None
   response.json.return_value = {'richList': sample_rich_list_data}
   return response

""" COMPUTORS """

@pytest.fixture
def sample_epoch():
    return 134

@pytest.fixture
def sample_computors_data():
    return {
        'epoch': 134,
        'identities': [
            'KSOHJQTNNFLLXBXVWQAXZKZVGVQDJCMCRUQIIBSVCFZLGJGNOBQZNAWCNLON',
            'IWLLOBAWRLMFQDGWGXZJYGYCYXLATRLOJYPWQCHAFESMBJXCXJFGBWADCMQL',
            'CIBJIZDJQFANUEJCDYLCTLSEFWABSOMVMEMJKYIRNGEWEIGOIKNXBAZBBUBB'
        ],
        'signatureHex': '22b48edf2d0dcc0deaff66ee0b52125dde3217797cfefe8198811137ffb4699c455f48ff818bb0790a6584a11fe6446e72f5cddb96fb105e9c0c2ee1d3500200'
    }

@pytest.fixture
def mock_computors_response(sample_computors_data):
    response = Mock()
    response.raise_for_status.return_value = None
    response.json.return_value = {'computors': sample_computors_data}
    return response

""" SMART CONTRACT """

@pytest.fixture
def sample_smart_contract_data():
   return "AMqaO0BCDwBAS0wA"

@pytest.fixture
def sample_contract_params():
   return {
       'contract_index': '1',
       'input_type': '1',
       'input_size': '0',
       'request_data': ''
   }

@pytest.fixture
def mock_smart_contract_response(sample_smart_contract_data):
   response = Mock()
   response.raise_for_status.return_value = None
   response.json.return_value = {'responseData': sample_smart_contract_data}
   return response

""" TRANSACTION """

@pytest.fixture
def sample_tx_id():
   return "bmtmtgbuxzriledlwttgaatvgwdfqxhgjoltvsjvrfcphthdezdaidcaemih"

@pytest.fixture
def sample_transaction_data():
   return {
       'sourceId': 'PCQRHZBMMMTCDAROMBXXLDSPAVJCGKUYMZILJCUHRDGSACXMUAGSEPVAXUCG',
       'destId': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFXIB',
       'amount': '1000000',
       'tickNumber': 17110120,
       'inputType': 2,
       'inputSize': 64,
       'inputHex': '91b48b82e9a59a87fe84ebabb0e7957e9333f7d38f831c19a498ffafe42bab66716c692d6370756c86023ed19299a315a71ccbc2619f0a0afad27a7edede1358',
       'signatureHex': 'b95ad759a021f73e4387c833386d29653870013383ea86e668b96e19f2aee64d17ce0fbad2e1952314b3e6df7be0cfb68fdc099f48b7175751a4d40e61f90800',
       'txId': 'bmtmtgbuxzriledlwttgaatvgwdfqxhgjoltvsjvrfcphthdezdaidcaemih'
   }

@pytest.fixture
def mock_transaction_response(sample_transaction_data):
   response = Mock()
   response.raise_for_status.return_value = None
   response.json.return_value = {'transaction': sample_transaction_data}
   return response

""" TX STATUS """

@pytest.fixture
def sample_transaction_status_data():
   return {
       'txId': 'bmtmtgbuxzriledlwttgaatvgwdfqxhgjoltvsjvrfcphthdezdaidcaemih',
       'moneyFlew': True
   }

@pytest.fixture
def mock_transaction_status_response(sample_transaction_status_data):
   response = Mock()
   response.raise_for_status.return_value = None
   response.json.return_value = {'transactionStatus': sample_transaction_status_data}
   return response

""" TRANSFER TX PER TICK """

@pytest.fixture
def sample_transfer_params():
   return {
       'identity': 'PCQRHZBMMMTCDAROMBXXLDSPAVJCGKUYMZILJCUHRDGSACXMUAGSEPVAXUCG',
       'start_tick': 17110120,
       'end_tick': 17110120
   }

@pytest.fixture
def sample_transfer_transactions_data():
   return {
       'transferTransactionsPerTick': [{
           'tickNumber': 17110120,
           'identity': 'PCQRHZBMMMTCDAROMBXXLDSPAVJCGKUYMZILJCUHRDGSACXMUAGSEPVAXUCG',
           'transactions': [{
               'sourceId': 'PCQRHZBMMMTCDAROMBXXLDSPAVJCGKUYMZILJCUHRDGSACXMUAGSEPVAXUCG',
               'destId': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFXIB',
               'amount': '1000000',
               'tickNumber': 17110120,
               'inputType': 2,
               'inputSize': 64,
               'inputHex': '91b48b82e9a59a87fe84ebabb0e7957e9333f7d38f831c19a498ffafe42bab66716c692d6370756c86023ed19299a315a71ccbc2619f0a0afad27a7edede1358',
               'signatureHex': 'b95ad759a021f73e4387c833386d29653870013383ea86e668b96e19f2aee64d17ce0fbad2e1952314b3e6df7be0cfb68fdc099f48b7175751a4d40e61f90800',
               'txId': 'bmtmtgbuxzriledlwttgaatvgwdfqxhgjoltvsjvrfcphthdezdaidcaemih'
           }]
       }]
   }

@pytest.fixture
def mock_transfer_transactions_response(sample_transfer_transactions_data):
   response = Mock()
   response.raise_for_status.return_value = None
   response.json.return_value = sample_transfer_transactions_data
   return response

""" BROADCAST TX """


@pytest.fixture
def sample_tx_bytes():
    return b"AQU+cSLitBL4WVnmI3C5DGHbmmyuBZHmfbLI+dkE2aj758XuwfEcBOVVKpnPEttRegeSlP1eNX4a5hSXt56VHOgDAAAAAAAAOR8FAQAAAACEKB6pxq142nVDVkTqMxsde1vExu+iWv/hEGvlSgNAStJ9KTJqwwoQoAMdl+vjN8w9aPYGLgLvl+QC4BZGRykA"

@pytest.fixture
def sample_broadcast_response():
    return bytearray(b'\x01\x05>q"\xe2\xb4\x12\xf8YY\xe6#p\xb9\x0ca\xdb\x9al\xae\x05\x91\xe6}\xb2\xc8\xf9\xd9\x04\xd9\xa8\xfb\xe7\xc5\xee\xc1\xf1\x1c\x04\xe5U*\x99\xcf\x12\xdbQz\x07\x92\x94\xfd^5~\x1a\xe6\x14\x97\xb7\x9e\x95\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x9f!\x05\x01\x00\x00\x00\x00\x05\x82\xd5\x11\x98\x0eRp\xbb\x02\x97\xf0B\xf8\xde\x1e\xaf\x9dU\xb2\xcbQ\xc6\x89\xc37L\xf6!\xb6j\xe3\x86\x84\xf6\xa1/\xac\xadV\xe8\xd6\xfaA\x07\xc3\xc8\x1c\xbc\x0e\xfc\xcd\xf3\x88\xa2\xde8\x8at(\xcd\xc0\x08\x00')

@pytest.fixture
def mock_broadcast_response(sample_broadcast_response):
    response = Mock()
    response.raise_for_status.return_value = None
    response.json.return_value = sample_broadcast_response
    return response

""" TICK INFO """

@pytest.fixture
def sample_rpc_tick_info_data():
   return {
       'tick': 17184008,
       'duration': 2,
       'epoch': 135,
       'initialTick': 17160956
   }

@pytest.fixture
def mock_tick_rpc_response(sample_rpc_tick_info_data):
   response = Mock()
   response.raise_for_status.return_value = None
   response.json.return_value = {'tickInfo': sample_rpc_tick_info_data}
   return response

""" TICK DATA """

@pytest.fixture
def sample_tick_data():
    return {
        'computorIndex': 345,
        'epoch': 135,
        'tickNumber': 17184941,
        'timestamp': '1731615775000',
        'varStruct': '',
        'timeLock': 'juE3j+95kHUoVk7gFLqIvm+GftVEbFhtr4yu7cYTFHY=',
        'transactionIds': ['hqomnbbvsdgukctjbyyqxdvcieecrfjpbncnzgbavfxswmltttotjckdprgn'],
        'contractFees': [],
        'signatureHex': '918b4c3a5014e8abc95a7a9c4670e90638272b1e81435c01d21bc80f27156a14581f5664fcc00f87c245c93fb8e2589dd9eb16e83ac36d677e2e1aeae33c1400'
    }

@pytest.fixture
def mock_tick_data_response(sample_tick_data):
    response = Mock()
    response.raise_for_status.return_value = None
    response.json.return_value = {'tickData': sample_tick_data}
    return response


""" CORE """

@pytest.fixture
def core_client():
    return QubiPy_Core(core_url=CORE_URL)

# TICK DATA

@pytest.fixture
def sample_tick_data_core():
   return {
       'computorIndex': 241,
       'epoch': 135,
       'tick': 17230129,
       'timestamp': '2024-11-17T12:17:37Z',
       'varStruct': '',
       'timeLock': '26+PJYtP4rMXfx4rFCffFaTifdoExu2CyMQ1HZi5l1I=',
       'transactionIds': [
           'npiptjnwzkeslanefedyxzupznjdidtmarrczavoebijdpxcvfbwahoaiypm',
           'snelaqofuixokfcenrexrwzgslldlyltvpipritfufyflrlmewostovemvzd',
           'wxzkuwsoqbuwmgjtvvckirncjescqjmuikdwycqirayprbfdaacrofgggxgk',
           'wrnryaevlgdcnaqbfiebqjhrjueesjgzebxixkjkteebpuilnvnzqapedqqi',
           'dvuwbbslirisjdldwlqktpnmrgdbshgkykguslwdhdosmhcpkbjgdztgprrb'
       ],
       'contractFees': [],
       'signature': 'KzhMtxmj9oN5NG9V7EB8OyrIlRBPDw76OGiSIg1pVL7ouYH6WVgiRzdmqJRaK2TFfDkSP7cFl0YmaKjQGKUVAA=='
   }

@pytest.fixture
def mock_tick_data_core_response(sample_tick_data_core):
   response = Mock()
   response.raise_for_status.return_value = None
   response.json.return_value = sample_tick_data_core
   return response

""" TICK INFO """

@pytest.fixture
def sample_tick_info_data():
   return {
       'tick': 17231284,
       'durationInSeconds': 2,
       'epoch': 135,
       'numberOfAlignedVotes': 0,
       'numberOfMisalignedVotes': 0,
       'initialTickOfEpoch': 17160956
   }

@pytest.fixture
def mock_tick_info_response(sample_tick_info_data):
   response = Mock()
   response.raise_for_status.return_value = None
   response.json.return_value = sample_tick_info_data
   return response

""" TICK QUORUM VOTE """

@pytest.fixture
def sample_quorum_vote_data():
   return {
       'sharedVotes': [{
           'vote': {
               'epoch': 135,
               'tick': 17230129,
               'timestamp': '2024-11-17T12:17:33Z',
               'prevResourceTestingDigest': '2bf+xCHAZig=',
               'prevSpectrumDigest': '/4ncDD+WwxyiJo5uUz5IVL0qNTY7hZy02+CQGRxhD8M=',
               'prevUniverseDigest': 'YzUicyBfLcTHZiLPtkTCex+0m+7PKsoVgjlfuBjG8Q8=',
               'prevComputerDigest': 'aLxBzY4Kpvs39Yusz1uI0G9l9ti5edF+tAuquX60CQQ=',
               'txDigest': 'xInhPblD/hZ6A5Wt6a3PUw0yWAvMFRIK9FjvrmQe8rI='
           },
           'numberOfVotes': 566
       }],
       'saltedVotesPerComputorIndex': {
           '0': {
               'resourceTestingDigest': 'ScYrYuIglwE=',
               'spectrumDigest': 'p45K+xoV6E2QLmMTQWVJ6qnsBZwXEPCagqe1owAPZZE=',
               'universeDigest': 'MXHhqOJScWRboOOG+Z37FE6hgCFnU1125X0wc8r73gM=',
               'computerDigest': 'izhUv9Tlr3j2ihZ5+mw2jheV2SueLkn7lio+YpNuHgM=',
               'expectedNextTickTxDigest': 'ms/BZNP96sKTDrQXIp1+ZBrsL9WJh8L96nIGId8Iz7c=',
               'signature': 'ni6dVKBSk6ZGJDP4PIzPIGZ81MttuGBBcYYPPrhFNFFhfLYGBqEgnmW+n6gmwHz+XPaKMrQqynDI5NrgoOMBAA=='
           },
           '1': {
               'resourceTestingDigest': 'PfsmAlBafMk=',
               'spectrumDigest': 'cLLx49cMhKWBN3rJ7AjwKYAyeCOx30O4YAs+IV1UmWU=',
               'universeDigest': 'CQxrL5TNuyKhuhimIEbOJt9RpabVqGFR50mK54R+ZNI=',
               'computerDigest': 'G9/VATRSuVS1cJIc5QnazcD7mmegQp6dull3gZpJGHw=',
               'expectedNextTickTxDigest': 'ms/BZNP96sKTDrQXIp1+ZBrsL9WJh8L96nIGId8Iz7c=',
               'signature': 'HH07BVk3rDCKppsB+tlnUwC7SObSnOyjv3XbzHbfxemY60EeZYpxJfaWBIDeBcYoVUzYlOljpoPiFwZfJSgcAA=='
           }
       }
   }

@pytest.fixture
def mock_quorum_vote_response(sample_quorum_vote_data):
   response = Mock()
   response.raise_for_status.return_value = None
   response.json.return_value = sample_quorum_vote_data
   return response

""" TICK TX """

@pytest.fixture
def sample_tick_transactions_data():
   return [
       {
           'sourceId': 'SOXEANRWFXOTQFTKLPHNLOVHOSACNLYOSIVJPJUTHFBJTZIAFYTXLPUDLSCF',
           'destId': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFXIB',
           'amount': '1000000',
           'tick': 17230129,
           'inputType': 2,
           'inputSize': 64,
           'input': 'Bdfj75u9AfksRMeUFTaTQ4UZhhzP8zAAsjbBlQ/HPxBxbGktY3B1bIcB6rlXM/9L+MwY+ZBeoo7fn8dEoWYTYg==',
           'signature': 'SyH6GQ7XOkXBUSlkBicOcwaxSjmgY+XuVrKyglFVq46mvXU2w97igxxW+/sHAz/soQgsE8iYPmD/Lniu+80dAA==',
           'txId': 'wxzkuwsoqbuwmgjtvvckirncjescqjmuikdwycqirayprbfdaacrofgggxgk',
           'digest': 'gBXAiVBFpt8TsyLiwfHsXEr4hThW8PMWWs9g1rqx09Y='
       }
   ]

@pytest.fixture
def mock_tick_transactions_response(sample_tick_transactions_data):
   response = Mock()
   response.raise_for_status.return_value = None
   response.json.return_value = {'transactions': sample_tick_transactions_data}
   return response

""" QUOTTERY """

@pytest.fixture
def sample_active_bets_data():
   return {
       'activeBetIds': [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 
                       43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
   }

@pytest.fixture
def mock_active_bets_response(sample_active_bets_data):
   response = Mock()
   response.raise_for_status.return_value = None
   response.json.return_value = sample_active_bets_data
   return response

""" CREATOR BETS """

@pytest.fixture
def sample_creator_id():
   return "MENJJUJDUNWGYEOEMGAHXBTAOFOCQDQTHRYRZDGYPBNYECWASFPLUIJHMHLC"

@pytest.fixture
def sample_active_bets_by_creator_data():
   return {
       'activeBetIds': [29, 30]
   }

@pytest.fixture
def mock_active_bets_by_creator_response(sample_active_bets_by_creator_data):
   response = Mock()
   response.raise_for_status.return_value = None
   response.json.return_value = sample_active_bets_by_creator_data
   return response

""" BASIC INFO """

@pytest.fixture
def sample_basic_info_data():
   return {
       'fees': {
           'slotPerDay': '10',
           'gameOperator': '50',
           'shareholder': '1000',
           'burn': '200'
       },
       'minimumBetSlotAmount': '10000',
       'issuedBets': '67',
       'moneyFlowData': {
           'total': '8819892431',
           'issueBet': '756234200',
           'joinBet': '7694514502',
           'finalizeBet': '369143729'
       },
       'economicsData': {
           'earnedAmountShareholder': '1125377929',
           'paidAmountShareholder': '0',
           'earnedAmountBetWinner': '5475201717',
           'distributedAmount': '5475201717',
           'burnedAmount': '90728793'
       },
       'gameOperatorId': 'KSWMTEIAYCLGXCDEXWZWFXUUGSGCTTZUIINDTYCNZABBJHVCBYEPFWXFIPBF'
   }

@pytest.fixture
def mock_basic_info_response(sample_basic_info_data):
   response = Mock()
   response.raise_for_status.return_value = None
   response.json.return_value = sample_basic_info_data
   return response

""" BET INFO """

@pytest.fixture
def sample_bet_id():
   return 45

@pytest.fixture
def sample_bet_info_data():
   return {
       'id': 45,
       'creatorId': 'OWUVKWHTVEKHDEAIFKTELAROUGCDRONSPPWIYANAGAKLOXCFGYXYLMQDUREL',
       'description': 'Qubic Price by end of November\x00\x00',
       'options': [
           {
               'description': 'Above $3000/billion on CMC\x00\x00\x00\x00\x00\x00',
               'state': 12
           },
           {
               'description': 'On or below $3000/billion on CMC',
               'state': 26
           }
       ],
       'oracles': [
           {
               'id': 'JDHSYZJHTVYLNCLNFFOTOVVVDBJBZTCZNEOYXVFXSGGKKTCNOSLXYRBBFOTA',
               'feePercentage': 2
           }
       ],
       'votes': [],
       'minimumBetAmount': '10000000',
       'maximumBetSlotPerOption': 250,
       'openTime': '2024-11-03T19:57:40Z',
       'closeTime': '2024-11-30T23:59:00Z',
       'endTime': '2024-12-01T12:00:00Z'
   }

@pytest.fixture
def mock_bet_info_response(sample_bet_info_data):
   response = Mock()
   response.raise_for_status.return_value = None
   response.json.return_value = sample_bet_info_data
   return response

""" BETTORS BY BET OPTION """

pass

""" QX """

@pytest.fixture
def sample_qx_params():
   return {
       'asset_name': 'QX',
       'issuer_id': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFXIB',
       'offset': '1'
   }

@pytest.fixture
def sample_qx_ask_orders_data():
   return {
       'orders': [
           {
               'entityId': 'RANDAIIPOIYBMGSSNBSCSHPQEWPARIZYWHRWGMDVLGEWNBZNHIGECFKCGQDO',
               'price': '28500000000',
               'numberOfShares': '1'
           },
           {
               'entityId': 'XOHNXGRPAFEGTAOYFVHYCFKQNXSBNWAPNVPGDJZVHBFOSCVZOEDEUVODIGUG',
               'price': '30000000000',
               'numberOfShares': '1'
           },
           {
               'entityId': 'VMRDVJVNIWWFQGBSOZRFKVUZKKSDZAZBWBPVELWWXAOIASIQZVPYAQLBJHLD',
               'price': '32123456789',
               'numberOfShares': '1'
           },
           {
               'entityId': 'DWUHAKJGWERZYARTKQAKQBWJGCOCPYGDLPHJAUAQNGUXRMLQKEJALAIFAFBE',
               'price': '34990000000',
               'numberOfShares': '1'
           }
       ]
   }

@pytest.fixture
def mock_qx_ask_orders_response(sample_qx_ask_orders_data):
   response = Mock()
   response.raise_for_status.return_value = None
   response.json.return_value = sample_qx_ask_orders_data
   return response

""" BID ORDERS """

@pytest.fixture
def sample_qx_bid_orders_data():
   return {
       'orders': [
           {
               'entityId': 'SSOYXBGWWOCLGCXYTTUEHFRKRCHBBTGNZFVYGWIPWCFYAYFQADNJYNAEWRAO',
               'price': '1000000001',
               'numberOfShares': '1'
           },
           {
               'entityId': 'PEKBRHZQKMGCQBTAHXHZRXQRLBACJIHAGWHMPIJTZBWIJVTIWQOVMGJDTPFO',
               'price': '100000001',
               'numberOfShares': '10'
           }
       ]
   }

@pytest.fixture
def mock_qx_bid_orders_response(sample_qx_bid_orders_data):
   response = Mock()
   response.raise_for_status.return_value = None
   response.json.return_value = sample_qx_bid_orders_data
   return response

""" ASK ORDERS """

@pytest.fixture
def sample_entity_id():
   return "UBGIZFTLNCRKAFJBIUUYWTOMEFEDVPTZZZBKNSZODERUXBJPWQZSPGYAMCYH"

@pytest.fixture
def sample_entity_ask_orders_data():
   return {
       'orders': [
           {
               'issuerId': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFXIB',
               'assetName': 'MLM',
               'price': '1390000000',
               'numberOfShares': '1'
           }
       ]
   }

@pytest.fixture
def mock_entity_ask_orders_response(sample_entity_ask_orders_data):
   response = Mock()
   response.raise_for_status.return_value = None
   response.json.return_value = sample_entity_ask_orders_data
   return response

""" BID ORDERS """

@pytest.fixture
def sample_entity_bid_orders_data():
   return {
       'orders': [
           {
               'issuerId': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFXIB',
               'assetName': 'QTRY',
               'price': '475000000',
               'numberOfShares': '1'
           },
           {
               'issuerId': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFXIB',
               'assetName': 'RANDOM',
               'price': '170000000',
               'numberOfShares': '1'
           }
       ]
   }

@pytest.fixture
def mock_entity_bid_orders_response(sample_entity_bid_orders_data):
   response = Mock()
   response.raise_for_status.return_value = None
   response.json.return_value = sample_entity_bid_orders_data
   return response


""" QX FEES """

@pytest.fixture
def sample_qx_fees_data():
  return {
      'assetIssuanceFee': 1000000000,
      'transferFee': 1000000,
      'tradeFee': 5000000
  }

@pytest.fixture
def mock_qx_fees_response(sample_qx_fees_data):
  response = Mock()
  response.raise_for_status.return_value = None
  response.json.return_value = sample_qx_fees_data
  return response