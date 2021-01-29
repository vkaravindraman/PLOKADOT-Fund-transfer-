# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 11:45:35 2021

@author: ARAVIND RAMAN V K
"""

import requests
import json



from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException


substrate = SubstrateInterface(
    url="https://polkascan.io/polkadot/block/3550597")

print(substrate.get_block_header)
print(substrate.get_runtime_events)
print(substrate.block_hash)
print(substrate.get_block_hash)

url = 'https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Frococo-rpc.polkadot.io#/explorer/query'
response = requests.get(url)
print(response.ok)
print(response.text)
print(dir(response))
print(response.json)



