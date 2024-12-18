## Let's see some more advanced examples of how to use the library.

### Get the tick info from the CORE server
Here's a simple example of how to use QubiPy. For example, If you want to get the tick info from the CORE server :

```python
from qubipy.core import core_client

CORE = QubiPy_Core()
tick_info = CORE.get_tick_info()

print(f"Tick info: {tick_info}")

# {'tick': 17650910, 'durationInSeconds': 6, 'epoch': 138, 'numberOfAlignedVotes': 0, 'numberOfMisalignedVotes': 0, 'initialTickOfEpoch': 17560000}
```

### Get the balance from a wallet address
```python
from qubipy.rpc import rpc_client

RPC = QubiPy_RPC()
wallet_balance = RPC.get_balance('IJFDMOBGBPKVJFFUVFOXYJSFVQYAKRIBPRHXNPRXLALSKYDVLNNSUPBAQJFC')

print(wallet_balance)

# {'id': 'IJFDMOBGBPKVJFFUVFOXYJSFVQYAKRIBPRHXNPRXLALSKYDVLNNSUPBAQJFC', 'balance': '80000000', 'validForTick': 17664386, 'latestIncomingTransferTick': 17664378, 'latestOutgoingTransferTick': 17664378, 'incomingAmount': '33073556140', 'outgoingAmount': '32993556140', 'numberOfIncomingTransfers': 828072, 'numberOfOutgoingTransfers': 18265}
```

### Get transaction
```python
from qubipy.rpc import rpc_client

RPC = QubiPy_RPC()
transaction_info = RPC.get_transaction('rlinciclnsqteajcanbecoedphdftskhikawqvedkfzbmiclqqnpgoagsbpb')

print(transaction_info)

# {'sourceId': 'FGKEMNSAUKDCXFPJPHHSNXOLPRECNPJXPIVJRGKFODFFVKWLSOGAJEQAXFIJ', 'destId': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFXIB', 'amount': '1000000', 'tickNumber': 17767809, 'inputType': 2, 'inputSize': 64, 'inputHex': '72c56a241b10e5c982bffa7368e7280a046785e1fb659610df3c03f4508d420f716c692b637564618b025950bc2b53a778644261ade91a22c85ef752da7ee162', 'signatureHex': '8ecb184c3da2dc9ee673189590846f3dea8877ad72eb04dec0be1e36791436c5b9254fd7dbe2c44352a20bed3b01973d8974320cf4a8f99c45eb662410f81300', 'txId': 'rlinciclnsqteajcanbecoedphdftskhikawqvedkfzbmiclqqnpgoagsbpb'}
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