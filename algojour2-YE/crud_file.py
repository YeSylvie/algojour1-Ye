class File:
    def __init__(self):
        self.name = "blockchaine"

    def save(self, blockchaine, nbr_zero):
        f = open(self.name + ".txt", "w")
        f.write(str(nbr_zero) + "\n")
        f.write(blockchaine.afficher())
        f.close()
        print("Sauvegarde réussie ! ")

    def read(self):
        try:
            f = open(self.name + ".txt", "r")
            existing_blockchaine = f.read()
            f.close()
            return existing_blockchaine
        except IOError:
            return ""
