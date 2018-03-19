def find_it(seq):
    repetitions = {}
    for x in seq:
        if x in repetitions:
            repetitions[x] += 1
        else:
            repetitions[x] = 1

    for key, value in repetitions.items():
        if value % 2 != 0:
            return key


def find_it_alt(seq):
    for x in seq:
        if seq.count(x) % 2 != 0:
            return x


mymap = {}
mymap[1] = "uno"
mymap[2] = "dos"
mymap[3] = "tres"


if 1 in mymap:
    print("Yes")
else:
    print("No")

print(mymap)


for x, y in mymap.items():
    print("Key: {0} - Value: {1}".format(x, y))
