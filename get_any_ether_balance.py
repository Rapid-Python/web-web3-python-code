from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

infura_url = os.getenv('INFURA_URL1')
web3 = Web3(Web3.HTTPProvider(infura_url))
print('Connection established' + ' = ', web3.isConnected())

# latest block number
print('blockNumber' + ' = ', web3.eth.blockNumber)

# to get the balance from the account(random ether address)
ether_address = input("Enter the Ether Address" + ' = ')

# checksumaddress contains mix of capital and small letters
converted_toChecksumAddress = Web3.toChecksumAddress(ether_address)
balance = (web3.eth.getBalance(converted_toChecksumAddress))
# Random_address= "0x71C7656EC7ab88b098defB751B7401B5f6d8976F", you can use any ether address

print('Toatl balance in account' + ' = ', balance)
print('Concerted balance' + ' = ', web3.fromWei(balance, 'ether'))
