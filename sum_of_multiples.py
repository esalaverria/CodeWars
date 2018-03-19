def sum_mul(n, m):
    sum = 0
    if m > 0 and n > 0:
        for x in range(2, m):
            if x % n == 0:
                sum += x
    else:
        return "INVALID"

    return sum

print(sum_mul(0, 0))

for x in range(3,13,3):
    print(x)

l = range(3,13,3)
print(l)