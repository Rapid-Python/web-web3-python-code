# Python 

Version: 3.9.7

# Web3 
Web 3 (also known as Web 3.0 and sometimes stylized as web3) is an idea for a new iteration of the World Wide Web based on blockchain technology, which incorporates concepts such as decentralization and token-based economics.

## Documentation
[Web3](https://web3py.readthedocs.io/en/stable/)

## Installation 
Create the virtual env

```python -m venv venv```


Activate the virtual env

```
source venv/bin/activate
pip install -r requirements.txt
```

1.interact_with_contract.py - This code is used to interact with external contracts from etherscan.io(example - omisego )
2.get_any_ether_balance - This code is used to check balance of any ether address.
3.send_receive_ether - This code is used to send ether from one account to another in ganache(local blockchain).
4.uniswap_events- This code is used to call functions from uniswap exchange.

## Initializing .env
See the inputs from .env.example and replace your credentials. Rename .env.example with .env 

## Run python files 
```bash
python filename.py
```