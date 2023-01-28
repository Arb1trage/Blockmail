################################# NETWORKS ################################

NETWORKS = {
    'BSC': {'rpc': 'https://bsc-dataseed.binance.org/', 'chain_id': 56, 'explorer': 'https://bscscan.com/tx/', 'ticker': 'BNB'},
    'ETH': {'rpc': 'https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161', 'chain_id': 1, 'explorer': 'https://etherscan.io/tx/', 'ticker': 'ETH'},  
    'CRO': {'rpc': 'https://evm-cronos.crypto.org/', 'chain_id': 25, 'explorer': 'https://cronoscan.com/tx/', 'ticker': 'CRO'},
    'FTM': {'rpc': 'https://rpc.fantom.network', 'chain_id': 250, 'explorer': 'https://cronoscan.com/tx/', 'ticker': 'FTM'},
    'AVAX': {'rpc': 'https://api.avax.network/ext/bc/C/rpc', 'chain_id': 43114, 'explorer': 'https://snowtrace.io/tx/', 'ticker': 'AVAX'},
    'POLY': {'rpc': 'https://polygon-rpc.com', 'chain_id': 137, 'explorer': 'https://polygonscan.com/tx/', 'ticker': 'MATIC'},
    'MADA': {'rpc': 'https://rpc-mainnet-cardano-evm.c1.milkomeda.com/', 'chain_id': 2001, 'explorer': 'https://explorer-mainnet-cardano-evm.c1.milkomeda.com/tx/', 'ticker': 'mADA'}
}

# TESTNETS
# NETWORKS = {
#     'BSC': {'rpc': 'https://data-seed-prebsc-1-s1.binance.org:8545', 'chain_id': 97, 'explorer': 'https://testnet.bscscan.com/tx/', 'ticker': 'BNB'},
#     'ETH': {'rpc': 'https://goerli.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161', 'chain_id': 5, 'explorer': 'https://goerli.etherscan.io/tx/', 'ticker': 'ETH'},  
#     'CRO': {'rpc': 'https://cronos-testnet-3.crypto.org:8545/', 'chain_id': 338, 'explorer': 'https://cronos.org/explorer/testnet3/tx/', 'ticker': 'CRO'},
#     'FTM': {'rpc': 'https://rpc.testnet.fantom.network', 'chain_id': 4002, 'explorer': 'https://testnet.ftmscan.com/tx/', 'ticker': 'FTM'},
#     'AVAX': {'rpc': 'https://api.avax-test.network/ext/bc/C/rpc', 'chain_id': 43113, 'explorer': 'https://testnet.snowtrace.io/tx/', 'ticker': 'AVAX'},
#     'POLY': {'rpc': 'https://matic-mumbai.chainstacklabs.com', 'chain_id': 80001, 'explorer': 'https://mumbai.polygonscan.com/tx/', 'ticker': 'MATIC'},          
#     'MADA': {'rpc': 'https://rpc-devnet-cardano-evm.c1.milkomeda.com/', 'chain_id': 200101, 'explorer': 'https://explorer-devnet-cardano-evm.c1.milkomeda.com/tx/', 'ticker': 'mADA'}   
# }

############################################################################
from web3 import Web3
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")
source_address = config["addresses"]["source_address"]
source_privkey = config["addresses"]["source_privkey"]
chain = config["addresses"]["chain"]
recv_address = config["addresses"]["recv_address"]
message = config["content"]["message"]
tx_value = float(config["content"]["tx_value"])
web3 = Web3(Web3.HTTPProvider(NETWORKS[chain]['rpc']))

#Validate the config
try:
    if chain.upper() in NETWORKS.keys():
        pass
    else:
        raise ValueError
except (ValueError):
    print("Invalid chain name. Please check the config file.")
    exit()  
    
try:
    if tx_value >= 0:
        pass
    else:
        raise ValueError
except (TypeError, ValueError):
    print("Error: Value must be non-negative and denominated in 'ether' units.")
    exit()

print('Blockmail by Arb1trage - Version 1.0')
raw_tx = {
    'from': source_address,
    'to': recv_address,
    'value': web3.toWei(tx_value, 'ether'),
    'data': message.encode("utf-8").hex(),
    'gasPrice': web3.eth.gas_price,
    'nonce': web3.eth.get_transaction_count(source_address),
    'chainId': web3.eth.chain_id
}

raw_tx['gas'] = web3.eth.estimateGas(raw_tx)
signed_tx = web3.eth.account.sign_transaction(raw_tx, source_privkey)
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
tx_link = f"{NETWORKS[chain]['explorer']}{web3.toHex(tx_hash)}"

print(f"View transaction on chain explorer: {tx_link}")