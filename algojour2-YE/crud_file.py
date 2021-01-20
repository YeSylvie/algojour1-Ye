import os


class File:
    def __init__(self):
        self.name = "blockchaine"

    def save(self, blockchaine, nbr_zero):
        if os.path.exists(self.name+".txt"):
            os.remove(self.name+".txt")
        f = open(self.name+".txt", "w+")
        f.write(str(nbr_zero) + "\n")
        f.write(blockchaine.afficher())
        f.close()
        print("Sauvegarde réussie ! ")

    def read(self):
        try:
            f = open(self.name+".txt")
            existing_blockchaine = f.read()
            f.close()
            return existing_blockchaine
        except IOError:
            print("Erreur lors de la lecture")
            return ""
