def arithmetic_sequence_elements(a, r, n):
    l = list()
    l.append(a)
    for x in range(0, n-1):
        l.append(l[x]+r)
    return ', '.join(str(x) for x in l)




print(arithmetic_sequence_elements(1,2,5))