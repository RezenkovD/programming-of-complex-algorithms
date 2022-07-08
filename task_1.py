import random

size = 10

array = []

for x in range(size):
    arr = []
    for j in range(size):
        arr.append(random.randint(10, 99))
    array.append(arr)

for x in range(size):
    print(array[x])

for z in range(size):
    for i in range(1, int(len(array)/2)):
        for y in range(len(array) - 1, len(array) - 1- i, -1):
            if array[i][y] > array[i][y - 1]:
                array[i][y], array[i][y - 1] = array[i][y - 1], array[i][y]

    for v in range(int(len(array) / 2), len(array) - 1):
        for p in range(v + 1, len(array)):
            if array[v][p] > array[v][p - 1]:
                array[v][p], array[v][p - 1] = array[v][p - 1], array[v][p]

print('\n')
for x in range(size):
    print(array[x])