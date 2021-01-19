import blockchaine
import crud_file

class Main:
        
    @staticmethod
    def menu():
        affichage = "******************* MENU *******************"
        affichage += "\n Taper c pour créer une blockchaine."
        affichage += "\n Taper a pour afficher la blockchaine."
        affichage += "\n Taper s pour sauvegarder."
        affichage += "\n Taper x pour ajouter un block."
        affichage += "\n Taper m pour afficher le menu."
        affichage += "\n Taper q pour quitter."
        affichage += "\n*****************************************"
        print(affichage)

    def choix(self):
        choix = ""
        my_blockchaine = blockchaine.Blockchaine(0)
        is_blockchaine_created = len(my_blockchaine.blockchaines) >= 0
        while choix != "q":
            choix = input("Taper votre choix : ")
            if choix == "c":
                nbr_zero = input("Taper le nombre de zéro voulu pour le hash : ")
                my_blockchaine = blockchaine.Blockchaine(2)
                is_blockchaine_created = True
            if choix == "a":
                if is_blockchaine_created:
                    print(my_blockchaine.afficher())
                else:
                    print("Créer dans un premier temps votre blockchaine")
            elif choix == "s":
                if is_blockchaine_created:
                    file = crud_file.File()
                    file.save(my_blockchaine, 2)
                else:
                    print("Créer dans un premier temps votre blockchaine")
            elif choix == "x":
                if is_blockchaine_created:
                    data = input("Taper votre donnée : ")
                    signature = input("Taper votre signature : ")
                    my_blockchaine.add_block(data, "Crée par " + signature)
                else:
                    print("Créer dans un premier temps votre blockchaine")
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
