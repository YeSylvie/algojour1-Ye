from math import *
import sys

def string_to_list(string): 
    list1=[] 
    list1[:0]=string 
    return list1 
    
def string_to_ascii(word):
    return ord(word)

def calcul_matrice_len(nbr_code_ascii):
    trouve = False
    while not trouve:
        if int(str(sqrt(nbr_code_ascii)).split(".")[1]) == 0:
            trouve = True
            return int(str(sqrt(nbr_code_ascii)).split(".")[0])
        nbr_code_ascii +=1

def create_matrice_carre(col_size, line_size, asci_codes):
    matrice = []
    liste = []
    element = 0
    for i in range(line_size): 
        liste = []
        j = 0
        for j in range(col_size):
            if element >= len(asci_codes):   
                liste.append(0)
            else:
                liste.append(asci_codes[element])
                element += 1
        matrice.append(liste)
    return matrice

def create_matrice(col_size, asci_codes):
    matrice = []
    liste = []
    element = 0
    while element < len(asci_codes):
        liste = []
        j = 0
        for j in range(col_size):
            if element >= len(asci_codes):   
                liste.append(0)
            else:
                liste.append(asci_codes[element])
                element += 1
        matrice.append(liste)
    return matrice

def construct_ascii_liste(char):
    char_list = string_to_list(char)
    asci_codes = []
    for i in range(len(char_list)):
        asci_codes.append(string_to_ascii(char_list[i]))
    return asci_codes
    
def transform_to_matrice_carre(char):
    asci_codes = construct_ascii_liste(char)
    matrice_len = calcul_matrice_len(len(asci_codes))
    return create_matrice_carre(matrice_len, matrice_len, asci_codes)

def transform_to_matrice(char, col_size):
    asci_codes = construct_ascii_liste(char)
    return create_matrice(col_size, asci_codes)

def main(arg1, arg2):
    matrice_carre = transform_to_matrice_carre(arg2)
    autre_matrice = transform_to_matrice(arg1, len(matrice_carre))
    show_matrice(matrice_carre)
    show_matrice(autre_matrice)
    # matrice_factor(autre_matrice, matrice_carre)

def show_matrice(matrice):
    col_size= len(matrice[0])
    line_size = len(matrice)
    print("Matrice : \n")
    for i in range(line_size): 
        for j in range(col_size):
            print("\t" + str(matrice[i][j]), end='')
        print("\n")
        
# def matrice_factor(matrice1, matrice2):
#     # matrice1 * matrice2
#     nbr_col1 = len(matrice1[0]) 
#     nbr_line2 = len(matrice2)
#     if nbr_line1 != nbr_col2:
#         print("ERREUR : impossible de faire la multiplication de ces deux matrices : Nbr colonne matrice 1 != nbr ligne matrice 2")
#     else:
#         for i in range(nbr_line2): 
#             valeur = 0

#             for j in range(nbr_col1):
#                 valeur =+ matrice2[i][j]*matrice1[i][j]
#             values_new_matrice.append
#         show_matrice(create_matrice(nbr_col2, values_new_matrice))

main(sys.argv[1], sys.argv[2])
# main("Just because I don't care doesn't mean I understand.", "Homer S")