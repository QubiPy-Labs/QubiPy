# QubiPy, a Python Library for the QUBIC RPC API
Currently, QubiPy is in a very early development phase, so please take this into consideration before using the library.

Visit [Change log](CHANGELOG.md)

![v0.2.2](https://img.shields.io/badge/alpha_version-0.2.2-red)

###  IMPORTANT NOTICE
At the moment and as QubiPy is still in a very early stage of development, a PyPi package is not provided. The only alternative right now is to clone the repository in your personal environment and use it.

### Requirements
```
Python 3
requests
```
To install the necessary dependencies, run this command in the console :
```
$ pip install -r requirements.txt
```

### How to use
Clone the repository and run your script from the root path to avoid import issues.

To use the module, it is necessary to import some modules before :
```python
from qubipy.rpc import rpc_client
from qubipy.core import core_client
```

Let's request tick info from the RPC for example :

```python
RPC = rpc_client.QubiPy_RPC()
print(RPC.get_tick_info())
```
Response :
```python
$ {
  "tick": 16660254,
  "duration": 1,
  "epoch": 131,
  "initialTick": 16640000
}
```
Let's request the entity info from the core :
```python
CORE = core_client.QubiPy_Core()
print(CORE.get_entity_info('PEKBRHZQKMGCQBTAHXHZRXQRLBACJIHAGWHMPIJTZBWIJVTIWQOVMGJDTPFO'))
```
Reponse :
```python
$ {
  "entity": {
    "id": "PEKBRHZQKMGCQBTAHXHZRXQRLBACJIHAGWHMPIJTZBWIJVTIWQOVMGJDTPFO",
    "incomingAmount": "113653127220",
    "outgoingAmount": "80838490981",
    "numberOfIncomingTransfers": 824156,
    "numberOfOutgoingTransfers": 422,
    "latestIncomingTransferTick": 16613012,
    "latestOutgoingTransferTick": 16613029
  },
  "validForTick": 16660147,
  "spectrumIndex": 7434551,
  "siblingIds": [
    "GIDNABDPPDFPECDPYUQZEBZONVJAXCTRQXRGHCLPNAOMEAHMULYQBQQEZRBE",
    "WUTXDWZRYSBHOEHBZSVCWIRXSAPAZFMZSJFHOGDTIAYOPAIKGUNGIOLEVFVO",
    "NZUUNSQJEAXQAACZVEGHEHDNQRLDZRHXDJKCJLCXODFQQJTHGCMIRZDFAXBD",
    "HFSHRQUTQONGFDTXKPPAGHEMJSHBLTWVQKZMKVGYYEDSTPBIRBTMHSRCUKUO",
    "PGXXITTPEGARXGSHDTBVFYRVBXFHZBXPIQQNBQKJHEGXZGDTTCYGITFGSKBG",
    "EFEDDOBGUVASHBTCYRCUZOXQTLUDMKMCEYFHDLETIFAUDPLYOZYQUPEBAXGC",
    "DNYAQMGQRFCUMBUCEIFRNYSCYUXDWNWTTLFQQFDCEBVCTOWGLVXLCNBESPJE",
    "MSWZOKQKAWZUECKOEWOPMNUBSQSDAHTHYIFMSYRRKBZSJJLHLECBOUUDNNHO",
    "RGHPZOHWBHKIICUGBENRQPKDJHJDLIFKETGMKMPMTAJGRTPIOKCPETRDPBME",
    "CADVHWJMDNOJJGPDAVPYOUNDPWEABLSDLPGHCWJWGDFTYIVFBAZIBTDBQKVL",
    "AEMCJNNWDXBRSFEZVXAHFDPLNBJHMMMDBLKPVETCQFCZFJWEVEEXANUBUMCM",
    "BTOZFRHDVNYUVAMHNBBZJTNMCVZBORRPFNQIZZPRDEMHIFPWTFSARQVBMATC",
    "SHWFJGOAMBUIJDDSKCWAMOIWBNJHUUDHRDDHRBORSDCCSJLSSCDGXOKCVWMB",
    "XTOYTMZTUTPPVGBWYCVIFDVMLLWFIMXRZKOGUHJLADMIKLZTIPQJPLKCGVUB",
    "ZVBYCOZKUMZRTBIAYVWUTWUGYNQEPASOMENYCCERUDCYFHKMIQDLCVNCZCVA",
    "GHGNSBIOBLCIRGBBEKQZOSTKXJGHXWUYVNLRCTSBUENITLCSDIBNSDBBITQL",
    "PKFLHUYXWAELGGXBXTRRASNCQZSEDURLIUXKEDHTYFAIASIPPTSBVYMCQTWB",
    "OCOVEQIPGTUPIBAYGYDOSAWXWIGBKDBVKIFARQSHWAUUYSYVLKZITMZCMHCI",
    "NAPHRLGCLNNKVERLZDIGIFADQSLAZYUULTBAGCDYEEDSBFZGCCLXZXDGSBKK",
    "IGIZMDVOTFEJTFXHXURCUXNOSCDFJJJHTTTSRGABECNPKMJFZQTTEKOBSDFH",
    "OHEMQVDLSQLQQAVHTYOKFPZUOHIBNBWJITCHETOBUAAPWWFSYACPPSMEHSEE",
    "LPJMDKCKOOYGBFAEXDRZCALQUIIALWMHFSAEJUUBKBQXRPDYCXEXKMYDDJIO",
    "HGDFFPYTXOKSMGYMXPFEPLCQXXLDRULLJEIAYOVZBFABJIYZHVNSLRAENXUG",
    "ZQLSECAGXOUHNEFFBATFQIBYAYYDECSPKVHNGGJIPEGNSIUWNORASTNAUFYL"
  ]
}

```
You can build a transaction and brodcast it :

```python
from qubipy.tx.utils import create_tx
from qubipy.rpc.rpc_client import QubiPy_RPC

seed = "........................."
destination_id = "........................."
amount = 1000

rpc = QubiPy_RPC()
tick = rpc.get_latest_tick()

# Build transaction
tx, signed_tx, signature, tx_hash = create_tx(seed, destination_id, amount, tick + 5)

# Broadcast Transaction
tx_broadcasted = rpc.broadcast_transaction(signed_tx)

print(f"Transaction will be executed at tick: {tick+5}")
print(f"Transaction data: {tx_broadcasted}")
```
