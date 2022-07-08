import random
array = []
size = 5

for x in range(size):
    arr = []
    for y in range(size):
        arr.append(random.randint(0, 3))
    array.append(arr)
    
print("Початкова матриця:")
for i in range(size):
    print(*[array[i][j] for j in range(5)])
                
for i in range(size):
    print(*[array[i][j] for j in range(5)])

def CSR(array_lst):
    aelem = []
    jptr = []
    iptr = [0]
    counter_y = 0
    size_ = len(array_lst)
    # aelem and jptr
    for i in range(size_):
        for n in range(size_):
            if array_lst[i][n] != 0:
                aelem.append(array[i][n])
                jptr.append(n)
                counter_y += 1
        iptr.append(counter_y)
    print("\naelem\n", aelem, "\n-----")
    print("jptr\n", jptr, "\n-----")
    print("iptr\n", iptr)
    return aelem, jptr, iptr
a = CSR(array)
def return_matrix(aelem, jptr, iptr):
    size_matrix = len(iptr) - 1
    matrix = []
    for z in range(size_matrix):
        mat = []
        for t in range(size_matrix):
            mat.append(0)
        matrix.append(mat)
    index_1 = 0
    for z in range(size_matrix):
        counter = 0
        for w in range(size_matrix):
            if counter < iptr[z + 1] - iptr[z]:
                if w == jptr[index_1]:
                    matrix[z][w] = aelem[index_1]
                    index_1 += 1
                    counter += 1

    # print("\nend matrix:\n", matrix)
    return matrix

print("\nПоновлена матриця:\n", return_matrix(a[0], a[1], a[2]))

print("\nПеревірка на рівність матриць: ", array == return_matrix(a[0], a[1], a[2]))
