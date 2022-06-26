import os
import json
from web3 import Web3
import asyncio
from dotenv import load_dotenv

load_dotenv()


infura_url = os.getenv('INFURA_URL')
web3 = Web3(Web3.HTTPProvider(infura_url))


uniswap_router = os.getenv('UNISWAP_ROUTER')
uniswap_factory = os.getenv('UNISWAP_FACTORY')
uniswap_factory_abi = json.loads(os.getenv('UNISWAP_FACTORY_ABI'))
contract = web3.eth.contract(address=uniswap_factory, abi=uniswap_factory_abi)
allPairsLength = contract.functions.allPairsLength().call()


def handle_event(event):
    print(Web3.toJSON(event))


async def log_loop(event_filter, poll_interval):
    while True:
        for PairCreated in event_filter.get_new_entries():
            handle_event(PairCreated)
        await asyncio.sleep(poll_interval)


def main():
    event_filter = contract.events.PairCreated.createFilter(fromBlock='latest')
    block_filter = web3.eth.filter('latest')
    # tx_filter = web3.eth.filter('pending')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                log_loop(event_filter, 2),
                log_loop(block_filter, 2)))
    finally:
        # close loop to free up system resources
        loop.close()


if __name__ == "__main__":
    print('Connection established' + ' = ', web3.isConnected())
    print('AllPairsLength' + ' = ', allPairsLength)
    main()
