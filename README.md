# Blockmail
Blockmail enables sending on-chain messages using Python and the web3 library.

## Features
- Sends messages on-chain to a specified address
- Supports including a transaction value along with the message
- Utilizes web3.py library to interact with the Ethereum blockchain
- Provides a link to view the transaction on a blockchain explorer

## Usage
1. Install dependencies: web3, configparser
2. Fill the config.ini file [Example values provided inside]:
```[addresses]
source_address = <your_address>
source_privkey = <your_private_key>
chain = <network_name> (e.g. mainnet, ropsten)
recv_address = <destination_address>

[content]
message = <message_to_send>
tx_value = <value_in_ether>```
3. Run the script and it will output a link to view the transaction on a blockchain explorer.
