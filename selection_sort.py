import sys
import time

### TRI PAR SELECTION

def selection_sort(list):
    print("Série :", list)
    start_time = time.time()
    list_lengh = len(list)
    nb_comparaison = 0
    nb_iteration = 0
    for i in range(list_lengh):
        index_min = i
        nb_iteration = nb_iteration + 1
        for j in range(i+1, list_lengh):
            nb_comparaison = nb_comparaison + 1
            nb_iteration = nb_iteration + 1
            if list[j] < list[index_min]:
                index_min = j
        tmp = list[index_min]
        list[index_min] = list[i]
        list[i] = tmp
    end_time = time.time()
    print("===> Première méthode :")
    print("Résultat :", list)
    print("Nb de comparaison :", nb_comparaison)
    print("Nb d'itération:", nb_iteration)
    print("Temps (sec) : {:01.2f}".format((round((end_time - start_time)))))


def str_to_list(str):
    list_int = list(map(float, str.split(';')))
    return list_int

selection_sort(str_to_list(sys.argv[1]))

def selection_sort_bis(list):
    start_time = time.time()
    list_lengh = len(list)
    nb_comparaison = 0
    nb_iteration = 0
    result = []
    for i in range(list_lengh):
        index_min = list.index(min(list))
        result.append(list[index_min])
        del list[index_min]
    end_time = time.time()
    print("===> Deuxième méthode :")
    print("Résultat :", result)
    print("Nb de comparaison :", nb_comparaison)
    print("Nb d'itération:", nb_iteration)
    print("Temps (sec) : {:01.5f}".format((round((end_time - start_time)))))

def str_to_list(str):
    list_int = list(map(float, str.split(';')))
    return list_int

selection_sort_bis(str_to_list(sys.argv[1]))
