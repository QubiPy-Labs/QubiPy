# Change Log
## v0.2.2-alpha - November X, 2024
* Added unit tests for the RPC Client
* Added fixtures
* Added new method : tick data
* Added new utils method to check bytes format
* Added new exception to handle bytes error
* Added new exception for the SC method
* Updated requirements.txt

## v0.2.1-alpha - November 4th, 2024
* A security patch has been added to prevent creating a transaction with an invalid tick, i.e. less than the current tick.

## v0.2.0-alpha - October 27th, 2024
* QX Support added
* Qubic key util library implemented
* Build transaction feature added
* Broadcast transaction feature added
* Query SC feature added
* Code refactorized