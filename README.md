[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Version: 1.0](https://img.shields.io/badge/Version-1.0-brightgreen)
# Blockmail
Blockmail enables sending on-chain messages using Python and the web3 library. Supports multiple blockchain networks, including Binance Smart Chain (BSC), Ethereum (ETH), Crypto.org (CRO), Fantom (FTM), Avalanche (AVAX), Polygon (POLY), and Milkomeda (MADA).

## Table of Contents

+ [Features](#features)
+ [Usage](#usage)
+ [Notes](#notes)

## Features <a name = "features"></a>
- Sends messages on-chain to a specified address
- Supports including a transaction value along with the message
- Utilizes web3.py library to interact with the Ethereum blockchain
- Supports BSC/ETH/CRO/FTM/AVAX/POLY/mADA and their respective testnets
- Provides a link to view the transaction on a blockchain explorer

## Usage <a name = "usage"></a>
1. Install dependencies: web3, configparser
2. Fill the config.ini file [Example values provided inside]:
```[addresses]
source_address = <your_address>
source_privkey = <your_private_key>
chain = <network_ticker> (e.g. ETH, BSC)
recv_address = <message_receiver_address>

[content]
message = <message_to_send>
tx_value = <value_denominated_in_ether>
```
3. Run the script and it will output a link to view the transaction on a blockchain explorer.

## Notes <a name = "notes"></a>
Script can be easily modified to support additional blockchain networks by adding them to the NETWORKS dictionary. In case you want to test the program on the testnet just comment out NETWORKS dictionary and uncomment the same variable from "TESTNETS" section.
