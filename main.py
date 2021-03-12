#blockchain consisnts of block
#blocks consists of transaction
#blocks are connected through hashing
#unique digital fingerprint -trainsaction +previous blocks fingerprints

#Python hashlib hashing function takes variable length of bytes and converts it into a fixed length sequence. 
#This is a one way function. That means, you hash a message, you get a fixed length sequence. 
#But you cannot get the original message from those fixed length sequence.
# this will be the array of blocks
#hash=hashlib.sha256("secret message".encode()).hexdigest()
#secret message is the data given as input so that it produces hash in hexa so now hash has the unique hexa code for secret message
#which will be considered as unique fingerprints for different input
#print(hash)
from block import block
blockchain=[]
genesis_block=block("Chancellor on the brink...",["Santoshi send 1BTC to Manasa"],
                            ["dog sent 5BTC to cat"],
                            ["dolly sent 6BTC to molly"])
second_block=block(genesis_block.block_hash,["abc sent 6Btc to xyz"])
third_block=block(genesis_block.block_hash,["gth sent 8BTC to jkl"])

print("block_hash:Genesis_block")
print(genesis_block.block_hash)

print("block_hash:second_block")
print(second_block.block_hash)

print("block_hash:third_block")
print(third_block.block_hash)



