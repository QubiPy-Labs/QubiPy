# QubiPy, a Python Library for the QUBIC RPC API
Currently, QubiPy is in a very early development phase, so please take this into consideration before using the library.

Please visit [Change log](CHANGELOG.md) to see all changes.

![v0.2.3](https://img.shields.io/badge/beta_version-0.2.3-green)

###  Important notice
QubiPy is in beta phase and may change considerably until the stable version. Keep this in mind when using the library.

### Documentation
To learn more about QubiPy and its complete use, please visit our official [documentation](https://qubipy.readthedocs.io/en/latest/).

### Requirements
To install the necessary dependencies, run this command in the console :
```
$ pip install -r requirements.txt
```

### How to use
You have two ways to use QubiPy, one is by [PyPi](https://pypi.org/project/QubiPy/) or by cloning the project from the official repository.

To use the module, it is necessary to import some classes before :
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

### Notes
This library is using `crypto.dll` which is a C extension of Qubic key utility functions and bind it to Python. To build this `crypto.dll`, this repository was used: [https://github.com/serendipity-seeker/key-utils-binding](https://github.com/serendipity-seeker/key-utils-binding).

