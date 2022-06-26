from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

# take port url from ganache
ganache_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))
print('Connection established' + ' = ', web3.isConnected())
print('blockNumber' + ' = ', web3.eth.blockNumber)

account1 = input("Enter Sender's Address" + ' = ')
account2 = input("Enter Receiver's Address" + ' = ')
# account1= "0x136ed42522249411C7Abefb83464DDF37Eee8a69"
# account2= "0xc164bD10b646E743C0D4b4BFbBA2909cf489B4a7"

# private key of account 1 from ganache
private_key = os.getenv('PRIVATE_KEY')

# get the nance
# build a transaction
nonce = web3.eth.getTransactionCount(account1)
tx = {
    'nonce': nonce,
    'to': account1,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}
# sign transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key)
txhash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(txhash)
print(web3.toHex(txhash))
