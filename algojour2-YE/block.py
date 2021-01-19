import random
import string
from hashlib import sha256
from datetime import datetime


class Block:
    def __init__(self, previousHash, data, signature, preuveTravail):
        self.previousHash = previousHash
        self.data = data
        self.signature = signature
        self.preuveTravail = preuveTravail
        self.creationDate = datetime.now()
        self.hash = ""
    

    @staticmethod
    def isFormatHashOk(hashBlock, nbrZero):
        zeroChaine = ""
        for i in range(nbrZero):
            zeroChaine += "0"
        return hashBlock.startswith(zeroChaine)

    
    @staticmethod
    def mineur(preuveTravail):
        letters = string.ascii_letters
        result_str = ''.join(random.choice(letters) for i in range(2))
        return preuveTravail + result_str


           
    def createHash(block, nbrZero):
        newPreuveTravail = block.preuveTravail
        bloc = str(block.previousHash) + str(block.data) + str(block.signature) + str(newPreuveTravail) + str(block.creationDate) 
        hashBlock = sha256(bloc.encode('utf-8')).hexdigest()
        while not block.isFormatHashOk(hashBlock, nbrZero):
            newPreuveTravail = block.mineur(block.preuveTravail)
            bloc = str(block.previousHash) + str(block.data) + str(block.signature) + str(newPreuveTravail) + str(block.creationDate) 
            hashBlock = sha256(bloc.encode('utf-8')).hexdigest()
        block.hash = hashBlock
        block.preuveTravail = newPreuveTravail
        return(block)


    def __str__(self):
        return "\tPrivous Hash : " + (self.previousHash) \
        + "\n\tData : " + (self.data) \
        + "\n\tSignature : " + (self.signature) \
        + "\n\tPreuve de travail : " + (self.preuveTravail) \
        + "\n\tCreation Date : " + str(self.creationDate) \
        + "\n\tHash : " + (self.hash)


# block = Block("None", "DATA", "Mineur", "Preuve")
# block = block.createHash(2)
# print(block)




