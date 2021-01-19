import block

class BlockChaine:
    def __init__(self):
        self.blockchaine = []

    def addBlock(self, nbrZero, data):
        if not self.blockchaine:
            newBlock = block.Block("NONE", data, "Crée par", "preuveTravail")
        else:
            previousHash = self.blockchaine[len(self.blockchaine)-1].hash
            newBlock = block.Block(previousHash, data, "Crée par", "preuveTravail")
        newBlock = newBlock.createHash(nbrZero)
        self.blockchaine.append(newBlock)
    

    def __str__(self):
        result = ""
        if not self.blockchaine:
            return "Aucun élément dans la liste."
        for i in range(len(self.blockchaine)):
            result += "Element n° "
            result += str(i)
            result += " : [\n" 
            result += str(self.blockchaine[i]) 
            result += "\n]\n" 
        return result


blockchaine = BlockChaine()
print("***** TESTE SANS AJOUT ********")
print(blockchaine)
print("***** TESTE AJOUT ********")
blockchaine.addBlock(2, "Genesis block")
blockchaine.addBlock(2, "First block")
blockchaine.addBlock(2, "Second block")
print(blockchaine)

