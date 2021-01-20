import blockchaine
import crud_file


class Main:
        
    @staticmethod
    def menu():
        affichage = "******************* MENU *******************"
        affichage += "\n Taper a pour afficher la blockchaine."
        affichage += "\n Taper s pour sauvegarder."
        affichage += "\n Taper x pour ajouter un block."
        affichage += "\n Taper d pour vider la blockchaine."
        affichage += "\n Taper r pour supprimer un block de la blockchaine."
        affichage += "\n Taper m pour afficher le menu."
        affichage += "\n Taper q pour quitter."
        affichage += "\n*****************************************"
        print(affichage)

    @staticmethod
    def choix():
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
            elif choix == "d":
                delete = input("Etes-vous sure de vouloir supprimer la blockchaine (oui/non) : ")
                if delete == "oui":
                    my_blockchaine.delete_all()
                else:
                    print("Vous avez annulé la suppression de la blockchaine")
            elif choix == "r":
                index = input("Quel block voulez-vous supprimer (rentrer l'index) : ")
                print("Le block a supprimé est : \n" + str(my_blockchaine.blockchaines[int(index)]))
                delete = input("Etes-vous sure de vouloir supprimer ce block (oui/non) : ")
                if delete == "oui":
                    my_blockchaine.delete_one(int(index))
                else:
                    print("Vous avez annulé la suppression du block suivant :\n" + str(my_blockchaine.blockchaines[int(index)]))
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
