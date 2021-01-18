import math
import sys
import time

### TRI PAR FUSION

def merge_sort(list):
    print("Série :", list)
    start_time = time.time()
    nb_comparaison = len(list)*math.log2(len(list))
    list = tri(list)
    end_time = time.time()
    print("Résultat :", list)
    print("Nb de comparaison : {:.0f}".format(nb_comparaison))
    print("Temps (sec) : {:01.2f}".format((round((end_time - start_time)))))


def tri(list):
    list_lengh = len(list)
    if list_lengh < 2:
        return list
    else:
        list_splited = list_lengh // 2
        return fusion(tri(list[:list_splited]), tri(list[list_splited:]))


def str_to_list(str):
    list_int = list(map(float, str.split(';')))
    return list_int


def fusion(list1, list2):
    i1, i2, n1, n2 = 0, 0, len(list1), len(list2)
    result=[]
    while i1 < n1 and i2 < n2:
        if list1[i1] < list2[i2]:
            result.append(list1[i1])
            i1 += 1
        else:
            result.append(list2[i2])
            i2 += 1
    if i1 == n1:
        result.extend(list2[i2:])
    else:
        result.extend(list1[i1:])
    return result


merge_sort(str_to_list(sys.argv[1]))


