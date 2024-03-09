pip install web3
from web3 import Web3
import os
import random
from eth_account import Account

# Connect to Goerli network
web3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/your_infura_project_id'))

# Set your private key
private_key = 'Your_Private_Key'

# Set sender and receiver addresses
sender_address = 'Sender_Address'
receiver_address = 'Receiver_Address'

# Check if the connection is successful
if web3.isConnected():
    print("Connected to Goerli network")

    # Convert ETH to Wei
    def to_wei(eth):
        return web3.toWei(eth, 'ether')

    # Generate random amount under 0.0001 ETH
    def generate_random_amount():
        return random.uniform(0.0000000001, 0.0001)

    # Build and sign transaction
    def build_and_sign_transaction(sender, receiver, value, gas_price, gas_limit, nonce):
        transaction = {
            'to': receiver,
            'value': value,
            'gas': gas_limit,
            'gasPrice': gas_price,
            'nonce': nonce,
            'chainId': 5  # Goerli network ID
        }
        signed_txn = web3.eth.account.signTransaction(transaction, private_key)
        return signed_txn

    # Get sender's nonce
    sender_nonce = web3.eth.getTransactionCount(sender_address)

    # Get current gas price
    gas_price = web3.eth.gas_price

    # Generate random amount
    amount_eth = generate_random_amount()

    # Convert amount to Wei
    amount_wei = to_wei(amount_eth)

    # Build and sign transaction
    signed_txn = build_and_sign_transaction(sender_address, receiver_address, amount_wei, gas_price, 21000, sender_nonce)

    # Send transaction
    tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

    print(f"Transaction sent: https://goerli.etherscan.io/tx/{tx_hash.hex()}")
else:
    print("Failed to connect to Goerli network")
