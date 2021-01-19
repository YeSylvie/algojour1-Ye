import block


class Blockchaine:
    def __init__(self):
        self.blockchaines = []

    def add_block(self, nbr_zero, data):
        if not self.blockchaines:
            new_block = block.Block("NONE", data, "Crée par", "preuveTravail")
        else:
            previous_hash = self.blockchaines[len(self.blockchaines) - 1].hash
            new_block = block.Block(previous_hash, data, "Crée par", "preuveTravail")
        new_block = new_block.create_hash(nbr_zero)
        self.blockchaines.append(new_block)

    def __str__(self):
        result = ""
        if not self.blockchaines:
            return "Aucun élément dans la liste."
        for i in range(len(self.blockchaines)):
            result += "Block n° "
            result += str(i)
            result += " : [\n" 
            result += str(self.blockchaines[i])
            result += "\n]\n" 
        return result


blockchaine = Blockchaine()
print("***** TESTE SANS AJOUT ********")
print(blockchaine)
print("***** TESTE AJOUT ********")
blockchaine.add_block(2, "Genesis block")
blockchaine.add_block(2, "First block")
blockchaine.add_block(2, "Second block")
print(blockchaine)
