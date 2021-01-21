import random
import string
from hashlib import sha256


class Block:
    def __init__(self, previous_hash, data, signature, proof_of_work, creation_date, main_hash, index, nounce):
        self.previous_hash = previous_hash
        self.data = data
        self.signature = signature
        self.proof_of_work = proof_of_work
        self.creation_date = creation_date
        self.hash = main_hash
        self.index = index
        self.nounce = nounce

    @staticmethod
    def is_format_hash_ok(hash_block, nbr_zero):
        zero_chaine = ""
        for i in range(nbr_zero):
            zero_chaine += "0"
        return hash_block.startswith(zero_chaine)

    def generate_preuvre_travail(self):
        letters = string.ascii_letters
        result_str = ''.join(random.choice(letters) for i in range(8))
        return self.proof_of_work + result_str

    def create_hash(self, nbr_zero):
        new_preuve_travail = self.proof_of_work
        bloc = str(self.previous_hash) + str(self.data) + str(self.signature) + str(new_preuve_travail) \
            + str(self.creation_date)
        hash_block = sha256(bloc.encode('utf-8')).hexdigest()
        nounce = 0
        while not self.is_format_hash_ok(hash_block, nbr_zero):
            nounce += 1
            new_preuve_travail = self.generate_preuvre_travail()
            bloc = str(self.previous_hash) + str(self.data) + str(self.signature) + str(new_preuve_travail) \
                + str(self.creation_date)
            hash_block = sha256(bloc.encode('utf-8')).hexdigest()
        self.hash = hash_block
        self.nounce = nounce
        self.proof_of_work = new_preuve_travail
        return self

    def __str__(self):
        return "\tIndex : " + str(self.index) \
            + "\n\tPrevious Hash : " + self.previous_hash \
            + "\n\tData : " + self.data \
            + "\n\tSignature : " + self.signature \
            + "\n\tPreuve de travail : " + self.proof_of_work \
            + "\n\tCreation Date : " + str(self.creation_date) \
            + "\n\tHash : " + self.hash \
            + "\n\tNounce : " + str(self.nounce)
