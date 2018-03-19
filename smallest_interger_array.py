def findSmallestInt(arr):
    smallest = arr[0]
    for x in arr:
        if x < smallest:
            smallest = x

    return smallest


def findSmallestInt2(arr):
    return min(arr)


x = findSmallestInt2([3, 4, 5, 6, 1, 9])


print(x)
