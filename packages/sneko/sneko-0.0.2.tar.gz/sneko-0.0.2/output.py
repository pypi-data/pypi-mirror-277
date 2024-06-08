CODE = """# @version ^0.3.0

greet: public(String[100])

@external
def __init__():
    self.greet = "Hello World"
"""
ABI = [
    {
        "stateMutability": "nonpayable",
        "type": "constructor",
        "inputs": [],
        "outputs": [],
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "greet",
        "inputs": [],
        "outputs": [{"name": "", "type": "string"}],
    },
]
BYTECODE = "3461004c57600b6040527f48656c6c6f20576f726c64000000000000000000000000000000000000000000606052604080515f556020810151600155506100836100506000396100836000f35b5f80fd5f3560e01c63cfae3217811861007b573461007f576020806040528060400160205f54015f81601f0160051c6005811161007f57801561004f57905b80548160051b85015260010181811861003b575b5050508051806020830101601f825f03163682375050601f19601f825160200101169050810190506040f35b5f5ffd5b5f80fd8418838000a16576797065728300030a0012"

# import asyncio
import boa
from web3 import Web3, EthereumTesterProvider

# from dotenv import load_dotenv

# load_dotenv()

x = boa.loads(CODE)
import pdb

pdb.set_trace()  # noqa

w3 = Web3(EthereumTesterProvider())
deploy = w3.eth.contract(abi=ABI, bytecode=BYTECODE).constructor().transact()
contract_address = w3.eth.get_transaction_receipt(deploy)["contractAddress"]
contract = w3.eth.contract(address=contract_address, abi=ABI)

# async def main():
#     async with AsyncWeb3(WebSocketProvider(os.getenv.get("RPC_URL"))) as w3:
#         print(w3.is_connected())
#         contract = w3.eth.contract(abi=ABI, bytecode=BYTECODE)
#         WETH_ADDRESS = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
#         transfer_event_topic = w3.keccak(text="Transfer(address,address,uint256)")
#         filter_params = {
#             "address": WETH_ADDRESS,
#             "topics": [transfer_event_topic],
#         }
#     subscription_id = await w3.eth.subscribe("logs", filter_params)
#     weth_contract = w3.eth.contract(address=WETH_ADDRESS, abi=WETH_ABI)
#     async for payload in w3.socket.process_subscriptions():
#         result = payload["result"]
#         from_addr = decode(["address"], result["topics"][1])[0]
#         to_addr = decode(["address"], result["topics"][2])[0]
#         amount = decode(["uint256"], result["data"])[0]
#         print(f"{w3.from_wei(amount, 'ether')} WETH from {from_addr} to {to_addr}")
#
# asyncio.run(main())
