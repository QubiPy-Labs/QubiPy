## Let's see some more advanced examples of how to use the library.

## RPC examples

Here is some advanced examples with the RPC Server.

### Get the balance from a wallet address
```python
from qubipy.rpc.rpc_client import QubiPy_RPC

RPC = QubiPy_RPC()
wallet_balance = RPC.get_balance('IJFDMOBGBPKVJFFUVFOXYJSFVQYAKRIBPRHXNPRXLALSKYDVLNNSUPBAQJFC')

print(wallet_balance)

"""
{
   'id': 'IJFDMOBGBPKVJFFUVFOXYJSFVQYAKRIBPRHXNPRXLALSKYDVLNNSUPBAQJFC',
   'balance': '80000000',
   'validForTick': 17664386,
   'latestIncomingTransferTick': 17664378,
   'latestOutgoingTransferTick': 17664378,
   'incomingAmount': '33073556140',
   'outgoingAmount': '32993556140',
   'numberOfIncomingTransfers': 828072,
   'numberOfOutgoingTransfers': 18265
}
"""
```

### Get transaction
```python
from qubipy.rpc.rpc_client import QubiPy_RPC

RPC = QubiPy_RPC()
transaction_info = RPC.get_transaction('rlinciclnsqteajcanbecoedphdftskhikawqvedkfzbmiclqqnpgoagsbpb')

print(transaction_info)

"""
{
   'sourceId': 'FGKEMNSAUKDCXFPJPHHSNXOLPRECNPJXPIVJRGKFODFFVKWLSOGAJEQAXFIJ',
   'destId': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFXIB',
   'amount': '1000000',
   'tickNumber': 17767809,
   'inputType': 2,
   'inputSize': 64,
   'inputHex': '72c56a241b10e5c982bffa7368e7280a046785e1fb659610df3c03f4508d420f716c692b637564618b025950bc2b53a778644261ade91a22c85ef752da7ee162',
   'signatureHex': '8ecb184c3da2dc9ee673189590846f3dea8877ad72eb04dec0be1e36791436c5b9254fd7dbe2c44352a20bed3b01973d8974320cf4a8f99c45eb662410f81300',
   'txId': 'rlinciclnsqteajcanbecoedphdftskhikawqvedkfzbmiclqqnpgoagsbpb'
}
"""
```

### Build a transaction
You can build a transaction and brodcast it :

```python
from qubipy.tx.utils import create_tx
from qubipy.rpc.rpc_client import QubiPy_RPC

seed = ""
destination_id = ""
amount = 1000

rpc = QubiPy_RPC()
tick = rpc.get_latest_tick()

# Build transaction
tx, signed_tx, signature, tx_hash = create_tx(seed, destination_id, amount, tick + 5)

# Broadcast Transaction
tx_broadcasted = rpc.broadcast_transaction(signed_tx)

print(f"Transaction data: {tx_broadcasted}")
```

### Get rich list
The first parameter corresponds to the page from which you want to start searching and the second parameter corresponds to the limit of results you want to get. In our case, we want the first page with 5 results.

```python
from qubipy.rpc.rpc_client import QubiPy_RPC

RPC = QubiPy_RPC()
rich_list = RPC.get_rich_list(1, page_size=5)

print(f"Rich list: {rich_list}")

"""
{
   'entities': [
       {
           'identity': 'BYBYFUMBVLPUCANXEXTSKVMGFCJBMTLPPOFVPNSATABMWDGTMFXPLZLBCXJL',
           'balance': '10769223275898'
       },
       {
           'identity': 'VUEYKUCYYHXKDGOSCWAIEECECDBCXVUSUAJRVXUQVAQPGIOABLGGLXDAXTNK',
           'balance': '8779905691304'
       },
       {
           'identity': 'JAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAVKHO',
           'balance': '8382986726601'
       },
       {
           'identity': 'EXNRRBDPYFQPXFPXCMUHZVEEBRQCBEAUDYUBHKGTRCKHVSRAQXWHQCXDLZXL',
           'balance': '2411151184744'
       },
       {
           'identity': 'QZYSHUTAJSTEXAYKBOVSOSSQQXHDHZAVNXLJFYOKVCZTJXPBQNDLRODBZXUC',
           'balance': '2130000088435'
       }
   ]
}
"""
```

## CORE examples
Here is some advanced examples with the CORE Server.

### Get the tick info from the CORE server
```python
from qubipy.core.core_client import QubiPy_Core

CORE = QubiPy_Core()
tick_info = CORE.get_tick_info()

print(f"Tick info: {tick_info}")

"""
{
   'tick': 17650910,
   'durationInSeconds': 6,
   'epoch': 138,
   'numberOfAlignedVotes': 0,
   'numberOfMisalignedVotes': 0,
   'initialTickOfEpoch': 17560000
}
"""
```

### Get active bets
```python
from qubipy.core.core_client import QubiPy_Core

CORE = QubiPy_Core()
active_bets = CORE.get_active_bets()
print(f"Active bets: {active_bets['activeBetIds']}")

"""
Formatted output for better readability:

Active bets: [
    32, 33, 35, 36, 40, 41, 44, 47, 48, 49, 
    50, 51, 54, 57, 60, 61, 62, 63, 64, 67, 
    70, 81, 82, 83, 84, 85, 86, 87, 88, 89, 
    91, 92, 100, 101, 106, 108, 109, 110, 111, 
    112, 113, 114, 115, 116, 117, 118, 119, 120, 
    121, 122, 123, 124
]
"""
```

### Get entity info
```python
from qubipy.core.core_client import QubiPy_Core

CORE = QubiPy_Core()
entity_info = CORE.get_entity_info('PEKBRHZQKMGCQBTAHXHZRXQRLBACJIHAGWHMPIJTZBWIJVTIWQOVMGJDTPFO')
print(entity_info)

"""
{
   'entity': {
       'id': 'PEKBRHZQKMGCQBTAHXHZRXQRLBACJIHAGWHMPIJTZBWIJVTIWQOVMGJDTPFO',
       'incomingAmount': '124656867974',
       'outgoingAmount': '98503037090',
       'numberOfIncomingTransfers': 824214,
       'numberOfOutgoingTransfers': 514,
       'latestIncomingTransferTick': 17881948,
       'latestOutgoingTransferTick': 17881948
   },
   'validForTick': 17948970,
   'spectrumIndex': 7434551,
   'siblingIds': [
       'GIDNABDPPDFPECDPYUQZEBZONVJAXCTRQXRGHCLPNAOMEAHMULYQBQQEZRBE',
       'WUTXDWZRYSBHOEHBZSVCWIRXSAPAZFMZSJFHOGDTIAYOPAIKGUNGIOLEVFVO',
       'NZUUNSQJEAXQAACZVEGHEHDNQRLDZRHXDJKCJLCXODFQQJTHGCMIRZDFAXBD',
       'HFSHRQUTQONGFDTXKPPAGHEMJSHBLTWVQKZMKVGYYEDSTPBIRBTMHSRCUKUO',
       'PGXXITTPEGARXGSHDTBVFYRVBXFHZBXPIQQNBQKJHEGXZGDTTCYGITFGSKBG',
       'EFEDDOBGUVASHBTCYRCUZOXQTLUDMKMCEYFHDLETIFAUDPLYOZYQUPEBAXGC',
       'DNYAQMGQRFCUMBUCEIFRNYSCYUXDWNWTTLFQQFDCEBVCTOWGLVXLCNBESPJE',
       'MSWZOKQKAWZUECKOEWOPMNUBSQSDAHTHYIFMSYRRKBZSJJLHLECBOUUDNNHO',
       'VLGDDEHZIRWAEBWEGQNSGTERLCLBMDBSDMPJGUIQAGFQZECTVUZKRPVFCLJK',
       'CADVHWJMDNOJJGPDAVPYOUNDPWEABLSDLPGHCWJWGDFTYIVFBAZIBTDBQKVL',
       'NZMCNGVNHCNGXBWOOXRQJHWBTVNFOIZJSKKQMLWBRAMSTHXSOUASMDXGUBVM',
       'FJLQONKEVQTVPBNVOWYIJVMIHOKBHTULFSWLNFEZBCIJFMZYYXDMQUODYGUN',
       'HHJHCHBBRIQNZEGMAEPNUACZNSWCVHMTXGEWBMABADSGIYGYKESGKZRFNVBH',
       'PUWRGBATLXSJWASGAFNPRVIJNFMGXBGSRGKIHAYIVFMQXDIXJWNLCKIFYZED',
       'KJUCEXRPQACLMALWLZKVEHCRGWPGBWPKBXFUBONQIHHXZIKIDJUAOZJFSTFH',
       'PVVKMINHCDCNLBDMPSHKLLHAYKWAYPJDVJZKOYCVAAJFPHAABSBAQBOAJICJ',
       'GGDLTTHODZBWZGSZPGNRGKXLMYOAGNNQCPINZWYAGCAOVVBVTPIWOBLBFPXG',
       'JTTVUUBLZDJTCHYCDAGDGARQWDFGBNWEBAZXMCMGCDDQCEMZPCNNABMDZZBH',
       'RHRNWBOZYZSARANTWKXIVENJFCOCDMXIURCEBDMYVBJFYZWZAMGWMFAGZVEI',
       'CDCNVCVZCIMENFRMQNQBZQAJKLTDNTTIGOARTMTIWEGBINEAMXWCDIXBTTQH',
       'IXLNLZWTRLIHNEXKAXLQMCFVTPSBWFESWWMMCPQVMDEMBILPOKKPNQYFARSA',
       'ZCVVNOXVIVTGEARJQLXTFEDZQQKDVEEWJXQQIUNDQBULHTMBFHKGMJPBCRDI',
       'AQBLSKBZFGFLRASIVFQLJLPZNXMCYXCVXRZMAXWFXCOPWMFTDRJAWRLADLME',
       'GUBHFUQQRPKMEDXDTZRVBOKJAYXBVQEMEJWNWYEBIFODCTLYOKLLRJLFPVKC'
   ]
}
"""
```