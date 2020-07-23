"""
problem_5.py - BlockChain
build a link list to store basic blockchain data
the data in this example is just a random integer
"""

import hashlib
import time


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = str(self.data).encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def __str__(self):
        return ('Timestamp: {}\nData: {}\nPrevious Hash: {}\nHash: {}'.format(self.timestamp, self.data, self.previous_hash, self.hash))

class Blockchain:

    def __init__(self):
        self.current_block = None

    def add_block(self, value):
        timestamp = time.gmtime()
        data = value
        previous_hash = self.current_block.hash if self.current_block else 0
        self.current_block = Block(timestamp, data, previous_hash)

blockchain = Blockchain()

blockchain.add_block('1) First String')
print(blockchain.current_block)

blockchain = Blockchain()
blockchain.add_block('2) Second String to')
print(blockchain.current_block)

blockchain = Blockchain()
blockchain.add_block('3) Third String to encode')
print(blockchain.current_block)

blockchain = Blockchain()
blockchain.add_block('4) Forth String to encode in block')
print(blockchain.current_block)

# Edge Cases:
blockchain = Blockchain()
blockchain.add_block('')
print(blockchain.current_block)
