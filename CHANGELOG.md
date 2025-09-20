# Change Log

## v0.4.1-beta - September 20, 2025
* Improved macOS compatibility: The cryptography library detection has been updated to differentiate between Apple Silicon (arm64) and Intel (x86_64) chips. The library module now automatically selects the correct version (crypto_silicon.dylib or crypto_intel.dylib), resolving potential compatibility issues on newer machines.

## v0.4.0-beta - May 25, 2025
* Added new endpoint method:
    * `get_monero_mining_stats()`: Returns a dictionary containing various statistics related to Monero mining, such as pool and network hashrates, network difficulty, block height, and other relevant pool/miner data.
    * Since the reward for each block of monero is `0.6 XMR`, we have added a small formula that allows us to calculate approximate rewards.
* Some internal libraries have been updated to fix known vulnerabilities.
* Since the : `/block-height` endpoint is going to be removed, a message has been added to the `get_block_height()` method to warn that it is recommended to use the  `get_tick_info()` method instead to ensure maximum compatibility.
* Donation addresses have been added to help cover operational costs, spend more time on new features, bug fixes and full documentation, ensuring that QubiPy remains a robust tool for everyone. More information in our [README](https://github.com/QubiPy-Labs/QubiPy/blob/main/README.md) and our [online documentation](https://qubipy.readthedocs.io/en/latest/about/#community-and-support).

## v0.3.0-beta - May 7, 2025
* Added new endpoints methods : 
    * get_assets_issuances(): Returns a list of issued assets.
    * get_assets_issuances_by_index() : Returns an asset issuance by universe index
    * get_ownerships_assets(): Returns a list of asset owners. Asset name and issuer are required. Issuer defaults to zero address.
    * get_ownerships_assets_by_index(): Returns an asset ownership by universe index.
    * get_assets_possessions(): Returns a list of asset possessors. Asset name and issuer are required. Issuer defaults to zero address.
    * get_assets_possessions_by_index(): Returns an asset possession by universe index.
    * get_assets_owners_per_asset(): Returns the asset owners per asset
* Added a function to check the input index and validate before making the query.
* Added more information to the response returned by the get_rich_list method, such as epoch, tick and more.
* Added new exceptions to handle new errors.
* Fixed get_rich_list method test.

## v0.2.6-beta - December 26, 2024
* Added a check function to verify and validate the wallet ID before making a call to the Qubic network
* Optimized network calls by preventing invalid requests
* Added input validation to enhance security and reliability
* Refactored transaction bytes validation for better data integrity
* Added empty bytes check for transaction data validation

## v0.2.5-beta - December 22, 2024
* Added new advanced code examples
* Reorganized documentation structure
* Formatted responses for better readability in the documentation
* Fixed some imports on the documentation

## v0.2.4-beta - December 21, 2024
* Enhanced github documention & online documentation
* Fixed some links in the documentation

## v0.2.3-beta - December 19, 2024
* Included dll, dylib and so files in package distribution to avoid bugs

## v0.2.2-beta - December 19, 2024
* Added unit tests for the RPC Client
* Added fixtures
* Added new method : tick data
* Added new utils method to check bytes format
* Added new exception to handle bytes error
* Added new exception for the SC method
* Updated requirements.txt
* Created requirements-doc.txt
* Fixed bugs
* Added documentation


## v0.2.1-alpha - November 4th, 2024
* A security patch has been added to prevent creating a transaction with an invalid tick, i.e. less than the current tick.

## v0.2.0-alpha - October 27th, 2024
* QX Support added
* Qubic key util library implemented
* Build transaction feature added
* Broadcast transaction feature added
* Query SC feature added
* Code refactorized