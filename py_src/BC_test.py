import pprint
import json
import time

import web3
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
from web3.middleware import construct_sign_and_send_raw_middleware

# web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8543'))
# print("Connected to node:", web3.isConnected())
#
# web3.middleware_onion.inject(geth_poa_middleware, layer=0)
# print("Version:", web3.clientVersion)
#
# abi = json.loads('[{"constant": true,"inputs": [{"name": "","type": "address"}],"name": "Admins","outputs": [{"name": "","type": "uint256"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": true,"inputs": [{"name": "","type": "uint256"}],"name": "EventLog","outputs": [{"name": "eventString","type": "string"},{"name": "date","type": "uint256"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": false,"inputs": [{"name": "adminName","type":      "address"},{"name": "linuxUID","type": "uint256"}],"name": "addAdmin","outputs": [],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": false,"inputs": [{"name": "eventString","type": "string"},{"name": "linuxID","type": "uint256"},{"name": "date","type": "uint256"}],"name": "addEvent","outputs": [],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": true,"inputs": [],"name": "getEvent","outputs": [{"name": "","type":   "string"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": true,"inputs": [{"name": "startDate","type": "uint256"},{"name": "endDate","type": "uint256"}],"name": "triggerEventsBetween","outputs": [{"name": "","type": "string"}],"payable": false,"stateMutability": "view","type": "function"}]')
#
# address = "0xBf1424C613dCCde74Bc996BDA939Bdaeaec52CF3"
#
# contract = web3.eth.contract(address=address, abi=abi)
#
# PASSWORD = "12345678"
# SECONDS_UNLOCKED = 5999999999
# print("Account unlocked:", web3.parity.personal.unlock_account(web3.eth.coinbase, PASSWORD, SECONDS_UNLOCKED))

# with open('./../../../devnet1/node1/keystore/UTC--2020-08-09T16-13-40.036177602Z--cabfe27af17d6d10f484b9251a43f8df9bc8381d') as keyfile:
#     encrypted_key = keyfile.read()
#     private_key = web3.eth.account.decrypt(encrypted_key, PASSWORD)

# web3.middleware_onion.add(construct_sign_and_send_raw_middleware(private_key)) #Automates signing when using sendTransaction() or ContractFunctions

# tx = contract.functions.addEvent("test string", 1000, 1596993230492753924).buildTransaction({'nonce': web3.eth.getTransactionCount(web3.eth.coinbase)})
# signed_tx = web3.eth.account.signTransaction(tx, private_key=private_key)
# web3.eth.sendRawTransaction(signed_tx.rawTransaction)

#using random linuxID and time to complete test transaction
# gas_estimate = contract.functions.addEvent("test string A", 1000, 1596993230492753924).estimateGas()
# print("Gas estimate to complete transaction:", gas_estimate)
#
# if gas_estimate < 100000:
#     print("Sending transaction to add event\n")
#     tx_hash = contract.functions.addEvent("test string A", 1000, 1596993230492753924).transact({'from': web3.eth.coinbase})
#     receipt = web3.eth.waitForTransactionReceipt(tx_hash)
#     print("Transaction receipt mined:")
#     pprint.pprint(dict(receipt))
#     print("\nWas transaction successful?")
#     pprint.pprint(receipt["status"])
# else:
#     print("Gas cost exceeds 100000")
#
# latestPush = contract.functions.getEvent().call()
# print(latestPush)

# http connection info for port the blockchain is on
LOCALHOST = 'http://127.0.0.1:7545'
# json representation of the abi
ABI = json.load(open("../trfle/build/ABI.json"))
# address of the smartcontract
ADDRESS = "0xad3C26dbC9AD5F08Cd6420D0C6AAb4eFDF10689d"
# password of the account
PASSWORD = "12345678"
# seconds to unlock the account for
SECONDS_UNLOCKED = 5999999999


class blockchain:
    def __init__(self):
        # Connects to the blockchain's port
        self.w3 = Web3(Web3.HTTPProvider(LOCALHOST))
        print("Connected to node:", self.w3.is_connected(True))

        # Adds middleware for POA blockchain
        # Wont let me call funcitons without it, still not sure what it is or why I need it
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        print("Version:", self.w3.client_version)

        # Creates the contract object to access the smartcontract
        self.contract = self.w3.eth.contract(address=ADDRESS, abi=ABI)

        #self.contract.functions.addAuthorizedUsers(self.w3.eth.accounts).call({'from': '0x2223FF4a875626e51dE9300cD5cB0eE400a49Bf2'})

    # Stores the string event_info in the blockchain with linuxID and time
    def add_event(self, event_info):
        start = time.time()
        gas_estimate = self.contract.functions.selector(event_info).estimate_gas()
        print("Gas estimate to complete transaction:", gas_estimate)
        print(self.contract.functions.selector(event_info).call())
        end = time.time()
        print('time: ' + str(end - start))
        # if gas_estimate < 1000000:
        #     print("Sending transaction to add event\n")
        #     tx_hash = self.contract.functions.selector(event_info).call()
        #     receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        #     print("Transaction receipt mined:")
        #     pprint.pprint(dict(receipt))
        #     print("\n Was transaction successful?")
        #     pprint.pprint(receipt["status"])
        # else:
        #     print("Gas cost exceeds 1000000")

    # def get_commit(self, commit_hash):
    #     tx_hash = self.contract.functions.getCommit(commit_hash).call({'from': "0x2223FF4a875626e51dE9300cD5cB0eE400a49Bf2"})
    #     receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
    #     print('TX receipt')
    #     pprint.pprint(dict(receipt))


    # def get_latest(self):
    #     latest = self.contract.functions.getLatestHash().call({'from': self.w3.eth.accounts[2]})
    #     return latest


b = blockchain()
print(b.w3.eth.accounts)
#print('latest hash: ' + b.get_latest())
b.add_event([1,1,1,1,1,1,1,1,1,1,50,50,1])
b.add_event([1,1,1,1,1,1,1,1,1,1,50,50,1])
b.add_event([1,1,1,1,1,1,1,1,1,1,50,50,1])
b.add_event([1,1,1,1,1,1,1,1,1,1,50,50,1])
b.add_event([1,1,1,1,1,1,1,1,1,1,50,50,1])
b.add_event([1,1,1,1,1,1,1,1,1,1,50,50,1])
b.add_event([1,1,1,1,1,1,1,1,1,1,50,50,1])
b.add_event([1,1,1,1,1,1,1,1,1,1,50,50,1])
b.add_event([1,1,1,1,1,1,1,1,1,1,50,50,1])
b.add_event([1,1,1,1,1,1,1,1,1,1,50,50,1])
# b.get_commit('test1')