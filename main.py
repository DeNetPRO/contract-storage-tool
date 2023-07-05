from web3 import Web3
import json, time


# Testnet Address
w3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/polygon_mumbai'))
contract_storage_address = "0x9d304623C5fB154628bd4672c28114ED97bee77E"

# Mainnet Address
w3 = Web3(Web3.HTTPProvider('https://polygon-rpc.com'))
contract_storage_address = "0xB6b309Ae66A12d69259566220A2D0e35fE4bC556"


def to_checksum_address(address: str) -> str:
    w3 = Web3()
    return w3.to_checksum_address(address)

def getNetworkName(network_id):
	if network_id == 137:
		return "Polygon"
	if network_id == 80001:
		return "Mumbai-Testnet"
	return "Unknown"

abi = [{"inputs":[{"internalType":"bytes32","name":"contractName","type":"bytes32"},{"internalType":"uint256","name":"networkId","type":"uint256"}],"name":"getContractAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"contractString","type":"string"},{"internalType":"uint256","name":"networkId","type":"uint256"}],"name":"getContractAddressViaName","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"networkId","type":"uint256"}],"name":"getContractListOfNetwork","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getNetworkLists","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"nameString","type":"string"}],"name":"stringToContractName","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"pure","type":"function"}]

contract_address = to_checksum_address(contract_storage_address)
contract = w3.eth.contract(address=contract_address, abi=abi)

networks = contract.functions.getNetworkLists().call()

for network_id in networks:
	print("found network:", network_id)
	contract_names = contract.functions.getContractListOfNetwork(network_id).call()
	for contract_name in contract_names:
		print(
			"| ",
			getNetworkName(network_id), " | ",
			network_id, " | ",
			contract_name, " | ",
			end = ""
		)
		this_contract_address = contract.functions.getContractAddressViaName(
			contract_name,
			network_id
		).call()
		print(this_contract_address, end = " |\n")

	