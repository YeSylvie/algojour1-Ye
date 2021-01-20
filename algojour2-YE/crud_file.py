import os

class File:
    def __init__(self):
        self.name = "blockchaine"

    def save(self, blockchaine, nbr_zero):
        if os.path.exists("texte.txt"):   
            os.chmod("texte.txt", 777)
        f = open("texte.txt", "w+")
        f.write(str(nbr_zero) + "\n")
        f.write(blockchaine.afficher())
        f.close()
        print("Sauvegarde réussie ! ")

    def read(self):
        try:
            f = open("texte.txt")
            existing_blockchaine = f.read()
            print(existing_blockchaine + "error")
            f.close()
            return existing_blockchaine
        except IOError:
            print("Erreur lors de la lecture")
            return "Hello"