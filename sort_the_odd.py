def sort_array(source_array):
    odds = list()
    ordered_list = list()
    for x in source_array:
        if x % 2 != 0:
            odds.append(x)

    odds.sort()
    i = 0
    for x in source_array:
        if x % 2 == 0:
            ordered_list.append(x)
        else:
            ordered_list.append(odds[i])
            i += 1

    return ordered_list


l = []
print(sort_array(l))
