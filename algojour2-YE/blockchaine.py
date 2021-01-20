import block
import crud_file
from datetime import datetime


class Blockchaine:
    def __init__(self, nbr_zero):
        file = crud_file.File()
        existing_file = file.read()
        if "" == existing_file or "Aucun élément dans la liste." in existing_file:
            self.blockchaines = []
            self.nbr_zero = nbr_zero
        else:
            lines = existing_file.split("\n")
            self.nbr_zero = int(lines[0])
            #i commence à 3 car les première ligne du fichier ne nous intéresse pas pour créer le Block
            i = 3
            self.blockchaines = []
            while i < len(lines):
                #Avec 8 le nombre de paramètre pour la classe block
                one_block = lines[i:i+8]
                index = one_block[0].split(": ")[1]
                previous_hash = one_block[1].split(": ")[1]
                data = one_block[2].split(": ")[1]
                signature = one_block[3].split(": ")[1]
                preuve_travail = one_block[4].split(": ")[1]
                creation_date = one_block[5].split(": ")[1]
                main_hash = one_block[6].split(": ")[1]
                nounce = one_block[7].split(": ")[1]
                new_block = block.Block(previous_hash, data, signature, preuve_travail, creation_date, main_hash, index,
                                        nounce)
                self.blockchaines.append(new_block)
                i += 10

    def add_block(self, data, signature):
        if not self.blockchaines:
            new_block = block.Block("NONE", data, signature, "", datetime.now(), "", 0, 0)
        else:
            previous_hash = self.blockchaines[len(self.blockchaines) - 1].hash
            new_block = block.Block(previous_hash, data, signature, "", datetime.now(), "", len(self.blockchaines), 0)
        new_block = new_block.create_hash(self.nbr_zero)
        self.blockchaines.append(new_block)
    
    def replace_blockchaine(self, new_blockchaines):
        if new_blockchaines.is_blockchaine_valid():
            self.blockchaines = new_blockchaines.blockchaines
        else :
            print("ERREUR : la nouvelle blockchaine n'est pas valide")

    def delete_all(self):
        if not self.blockchaines:
            print("Aucun élément à supprimer de la blockchaine")
        else:
            self.blockchaines = []
            print("Tous les éléments ont été supprimés de la blockchaine")
    
    def delete_one(self, index):
        if not self.blockchaines:
            print("Aucun élément à supprimer de la blockchaine")
        else:
            del self.blockchaines[index]
            for i in range(len(self.blockchaines)):
                self.blockchaines[i].index = i
            print("Le block " + str(index) + " a été supprimé de la blockchaine")

    def is_format_all_hash_valid(self):
        is_valid = True
        for i in range(len(self.blockchaines)):
            if i == 0:
                is_valid = is_valid and self.blockchaines[i].is_format_hash_ok(self.blockchaines[i].hash, self.nbr_zero)
            else:
                is_valid = is_valid and self.blockchaines[i].is_format_hash_ok(self.blockchaines[i].previous_hash,
                                                                               self.nbr_zero)
                is_valid = is_valid and self.blockchaines[i].is_format_hash_ok(self.blockchaines[i].hash, self.nbr_zero)
        return is_valid

    def is_all_hash_equal_previous_hash(self):
        is_valid = True
        for i in range(1, len(self.blockchaines)):
            is_valid = is_valid and self.blockchaines[i-1].hash == self.blockchaines[i].previous_hash
        return is_valid

    def is_blockchaine_valid(self):
        is_valid = self.is_format_all_hash_valid()
        is_valid = is_valid and self.is_all_hash_equal_previous_hash()
        is_valid = is_valid and self.blockchaines[0].previous_hash == "NONE"
        return is_valid

    def afficher(self):
        if not self.blockchaines:
            return "Aucun block dans la liste."
        result = "Blockchaine vérifiée : " + str(self.is_blockchaine_valid()) + "\n"
        for i in range(len(self.blockchaines)):
            result += "Block n° "
            result += str(i)
            result += " : [\n" 
            result += str(self.blockchaines[i])
            result += "\n]\n" 
        return result

    def afficher_one_block(self, index):
        if not self.blockchaines or len(self.blockchaines) < index:
            return "Le block à la position " + str(index) + " n'existe pas."
        result = "Block n° "
        result += str(index)
        result += " : [\n" 
        result += str(self.blockchaines[index])
        result += "\n]\n" 
        return result

    def afficher_last_block(self):
        if not self.blockchaines:
            return "Aucun block dans la liste."
        index = len(self.blockchaines) - 1 
        result = "Block n° "
        result += str(index)
        result += " : [\n" 
        result += str(self.blockchaines[index])
        result += "\n]\n" 
        return result
