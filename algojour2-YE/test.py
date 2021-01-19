zeroChaine = ""
for i in range(7):
    zeroChaine += "0"
print(zeroChaine)
hashBlock = "09090909"
b = hashBlock.startswith(zeroChaine)
print(b)