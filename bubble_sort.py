import sys
import time

### TRI A BULLE

def bubble_sort(list):
    print("Série :", list)
    start_time = time.time()
    list_lengh = len(list)
    nb_comparaison = 0
    nb_iteration = 0
    for i in range(list_lengh):
        nb_iteration = nb_iteration + 1
        for j in range(list_lengh-i-1):
            nb_comparaison = nb_comparaison + 1
            nb_iteration = nb_iteration + 1
            if list[j] > list[j+1]:
                tmp = list[j]
                list[j] = list[j+1]
                list[j + 1] = tmp
    end_time = time.time()
    print("Résultat :", list)
    print("Nb de comparaison :", nb_comparaison)
    print("Nb d'itération:", nb_iteration)
    print("Temps (sec) : {:01.2f}".format((round((end_time - start_time)))))


def str_to_list(str):
    list_int = list(map(float, str.split(';')))
    return list_int


bubble_sort(str_to_list(sys.argv[1]))






