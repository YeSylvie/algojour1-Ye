import math
import sys
import time

### TRI RAPIDE


def quick_sort(list):
    print("Série :", list)
    start_time = time.time()
    nb_comparaison = len(list)*math.log2(len(list))
    result = trirapide(list)
    end_time = time.time()
    print("Résultat :", result)
    print("Nb de comparaison : {:.0f}".format(nb_comparaison))
    print("Temps (sec) : {:01.2f}".format((round((end_time - start_time)))))


def str_to_list(str):
    list_int = list(map(float, str.split(';')))
    return list_int


def trirapide(list):
    if not list:
        return []
    else:
        list_lengh = len(list)
        plus_petits_list = []
        plus_grands_list = []
        for k in range(1, list_lengh):
            if list[k] <= list[0]:
                plus_petits_list.append(list[k])
            else:
                plus_grands_list.append(list[k])
        list = trirapide(plus_petits_list) + [list[0]] + trirapide(plus_grands_list)
        return list


quick_sort(str_to_list(sys.argv[1]))





