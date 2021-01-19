import block
import crud_file
from datetime import datetime


class Blockchaine:
    def __init__(self, nbr_zero):
        file = crud_file.File()
        existing_file = file.read()
        if "Aucun élément dans la liste." in existing_file:
            self.blockchaines = []
            self.nbr_zero = nbr_zero
        else:
            lines = existing_file.split("\n")
            self.nbr_zero = int(lines[0])
            for i in range(1, len(lines)):
                previous_hash = lines[0]
                data = lines[0]
                signature = lines[0]
                preuve_travail = lines[0]
                creation_date = lines[0]
                main_hash = lines[0]
                index = lines[0]
                nounce = lines[0]
                new_block = block.Block(previous_hash, data, signature, preuve_travail, creation_date, main_hash,
                                        index, nounce)
                self.blockchaines.append(new_block)
                self.blockchaines = []

    def add_block(self, data, signature):
        if not self.blockchaines:
            new_block = block.Block("NONE", data, signature, "", datetime.now(), "", 0, 0)
        else:
            previous_hash = self.blockchaines[len(self.blockchaines) - 1].hash
            new_block = block.Block(previous_hash, data, signature, "", datetime.now(), "", len(self.blockchaines), 0)
        new_block = new_block.create_hash(self.nbr_zero)
        self.blockchaines.append(new_block)

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
        return is_valid

    def afficher(self):
        if not self.blockchaines:
            return "Aucun élément dans la liste."
        result = "Blockchaine vérifiée : " + str(self.is_blockchaine_valid()) + "\n"
        for i in range(len(self.blockchaines)):
            result += "Block n° "
            result += str(i)
            result += " : [\n" 
            result += str(self.blockchaines[i])
            result += "\n]\n" 
        return result

    @staticmethod
    def menu():
        affichage = "******************* MENU *******************"
        affichage += "\n Taper a pour afficher la blockchaine."
        affichage += "\n Taper s pour sauvegarder."
        affichage += "\n Taper x pour ajouter un block."
        affichage += "\n Taper m pour afficher le menu."
        affichage += "\n Taper q pour quitter."
        affichage += "\n*****************************************"
        return affichage

    def choix(self):
        choix = ""
        while choix != "q":
            choix = input("Taper votre choix : ")
            if choix == "a":
                print(blockchaine.afficher())
            elif choix == "s":
                file = crud_file.File()
                file.save(blockchaine, self.nbr_zero)
            elif choix == "x":
                data = input("Taper votre donnée : ")
                signature = input("Taper votre signature : ")
                blockchaine.add_block(data, "Crée par " + signature)
            elif choix == "m":
                print(blockchaine.menu())
            elif choix == "q":
                print("Au revoir !")
            else:
                print("Choix incorrect")
                blockchaine.menu()


blockchaine = Blockchaine(2)
print(blockchaine.menu())
blockchaine.choix()
