import blockchaine
import crud_file

class Main:
        
    @staticmethod
    def menu():
        affichage = "******************* MENU *******************"
        affichage += "\n Taper a pour afficher la blockchaine."
        affichage += "\n Taper s pour sauvegarder."
        affichage += "\n Taper x pour ajouter un block."
        affichage += "\n Taper m pour afficher le menu."
        affichage += "\n Taper q pour quitter."
        affichage += "\n*****************************************"
        print(affichage)

    def choix(self):
        choix = ""
        my_blockchaine = blockchaine.Blockchaine(4)
        while choix != "q":
            choix = input("Taper votre choix : ")
            if choix == "a":
                print(my_blockchaine.afficher())
            elif choix == "s":
                file = crud_file.File()
                file.save(my_blockchaine, my_blockchaine.nbr_zero)
            elif choix == "x":
                data = input("Taper votre donnée : ")
                signature = input("Taper votre signature : ")
                my_blockchaine.add_block(data, "Crée par " + signature)
            elif choix == "m":
                main.menu()
            elif choix == "q":
                print("Au revoir !")
            else:
                print("Choix incorrect")
                main.menu()
                
main = Main()
main.menu()
main.choix()
