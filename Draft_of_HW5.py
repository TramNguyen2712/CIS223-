def find_repeated_int(A):
    if len(A) < 2:
        raise IndexError
    else:
        B = [0] * (len(A))
        for i in range(0, len(A)):
            if A[i] in B:
                print("The integer is repeated in array is {0:3d}".format(A[i]))
                B[i] = A[i]
            else:
                B[i] = A[i]
        print(B)


# A = [1,2,3,4,5,5,6]
# print(find_repeated_int(A))
# print(-sum(set(A))+sum(A))

S = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]
# total = 0
# for list in S:
#     for val in list:
#         total += val
# print(total)

# total = sum([sum(val for val in list) for list in S])
# print(total)

import ctypes
import time


class DynamicArray(object):
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    # Create a low-level array of pointers that are treated as objects by the interpreter
    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def __len__(self):
        return self._n

    def __getitem__(self, index):
        if not 0 <= index < self._n:
            raise IndexError('invalid index')
        return self._A[index]

    def __setitem__(self, index, value):
        if not 0 <= index < self._n:
            raise IndexError('invalid index')
        self._A[index] = value

    # Grow the array dynamically
    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def append(self, obj):
        if self._n == self._capacity:  # dynamic array is full
            self._resize(2 * self._capacity)  # can be tweaked to fit the actual growth of lists
        self._A[self._n] = obj
        self._n += 1

    def insert(self, k, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)

        for j in range(self._n, k, -1):
            self._A[j] = self._A[j - 1]

        self._A[k] = obj
        self._n += 1

    def remove_at_index(self, k):
        if 0 <= k <= self._n:
            for i in range(k, self._n - 1):
                self._A[i] = self._A[i + 1]
            self._n -= 1
        else:
            return "IndexError"


if __name__ == "__main__":
    ##### INSERT
    # Test implementation of remove(k, value) in DynamicArrays of varying sizes
    # by repeatedly remove elements in different areas of the DynamicArray

    def remove_test(array_list, location, num_operations=2000):
        file = open("results_remove_method1_da1.txt", "a")

        for array in array_list:
            if location == "end":
                l = len(array)
                start = time.time()
                for i in range(num_operations):
                    array.remove_at_index(len(array) - 1)

                # amortized analysis of time complexity
                average = (time.time() - start) / num_operations

                file.write("{0:<10},{1:^10},{2:>10e}\n".format(location, "N={0}".format(l), average))

            if location == "middle":
                l = len(array)
                start = time.time()
                for i in range(num_operations):
                    array.remove_at_index((len(array) - 1) // 2)

                # amortized analysis of time complexity
                average = (time.time() - start) / num_operations

                file.write("{0:<10},{1:^10},{2:>10e}\n".format(location, "N={0}".format(l), average))

            if location == "start":
                l = len(array)
                start = time.time()
                for i in range(num_operations):
                    array.remove_at_index(0)

                # amortized analysis of time complexity
                average = (time.time() - start) / num_operations

                file.write("{0:<10},{1:^10},{2:>10e}\n".format(location, "N={0}".format(l), average))

        file.close()


    # Helper function to create list of lists of different sizes
    def create_arrays(sizes):
        D = []
        for n in sizes:
            array = DynamicArray()

            for i in range(n):
                array.append(None)
            D.append(array)

        return D


    sizes = [100, 1000, 10000, 100000]

    # test insert at end
    # array_list = create_arrays(sizes)
    # print(array_list)
    # insert_test(array_list, 'end')

    # test insert at middle
    # array_list = create_arrays(sizes)
    # insert_test(array_list, 'middle')

    # test insert at beginning
    # array_list = create_arrays(sizes)
    # print(array_list)
    # remove_test(array_list, "middle")


def cal_twoD_matrix():
    rows = int(input('Enter the row number: '))
    columns = int(input('Enter the column number: '))
    a = [[0] * columns for j in range(rows)]
    b = [[0] * columns for j in range(rows)]
    for i in range(rows):
        for j in range(len(a[0])):
            a[i][j] = int(
                input('Enter the number of the column {0:3d} and the row {1:3d} of the 1st matrix '.format(i, j)))
    print(a)
    for i in range(rows):
        for j in range(len(b[0])):
            b[i][j] = int(
                input('Enter the number of the column {0:3d} and the row {1:3d} of the 2nd matrix '.format(i, j)))
    print(b)
    print()
    print('Total of two matrices')
    # add two matrix
    total = [[0] * columns for j in range(rows)]
    for i in range(len(a)):
        for j in range(len(a[0])): # Adding the elements of each row of the first matrix by the elements of each row in the second matrix
            total[i][j] = a[i][j] + b[i][j]
    # print total result
    for i in range(len(total)):
        for j in range(len(total[0])):
            print(total[i][j], end=' ')
        print()
    print()
    print('Multiply of two matrices')
    mul = [[0] * len(a[0]) for j in range(len(b))]
    if len(a[0]) == len(b):
        for i in range(len(b)):
            for j in range(len(a[0])):
                for k in range(len(a[
                                       0])):  # Multiply the elements of each row of the first matrix by the elements of each column in the second matrix
                    mul[i][j] += a[i][k] * b[k][j]
    else:
        raise IndexError("the number of columns in the first matrix equals the number of rows in the second matrix")
    # print multiply result
    for i in range(len(mul)):
        for j in range(len(mul[0])):
            print(mul[i][j], end=' ')
        print()


#cal_twoD_matrix()

def add_matric(a,b):
    total = [[0] * len(a[0]) for j in range(len(a))]
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        for i in range(len(a)):
            for j in range(len(a[0])):  # Adding the elements of each row of the first matrix by the elements of each row in the second matrix
                total[i][j] = a[i][j] + b[i][j]
    # print total result
        for i in range(len(total)):
            for j in range(len(total[0])):
                print(total[i][j], end=' ')
            print()
        print()
    else:
        print('Two matrices must have same dimension')

def multiple_matric(a,b):
    mul = [[0] * len(a[0]) for j in range(len(b))]
    if len(a[0]) == len(b):
        for i in range(len(b)):
            for j in range(len(a[0])):
                for k in range(len(a[0])):  # Multiply the elements of each row of the first matrix by the elements of each column in the second matrix
                    mul[i][j] += a[i][k] * b[k][j]
        # print multiply result
        for i in range(len(mul)):
            for j in range(len(mul[0])):
                print(mul[i][j], end=' ')
            print()
    else:
        print("The number of columns in the first matrix must equal to the number of rows in the second matrix")


a = [[1,2],[3,4]]
b = [[1,2],[3,4]]
c = [[1,2,3]]
add_matric(a,b)
multiple_matric(a,b)

class Matrix():
    def __init__(self,matrix):
        self._row = len(matrix)
        self._column = len(matrix[0])
        self._matrix = matrix

    def __len__(self):
        return self._row

    def get_column(self):
        return self._column

    def get_row(self):
        return self._row

    def __add__(self, other):
        total = [[0] * len(self._matrix[0]) for j in range(len(self._matrix))]
        if len(self._matrix) == len(other) and len(self._matrix[0]) == len(other[0]):
            for i in range(len(self._matrix)):
                for j in range(len(self._matrix[0])):  # Adding the elements of each row of the first matrix by the elements of each row in the second matrix
                    total[i][j] = self._matrix[i][j] + other[i][j]

            #print total result
            result = ""
            for i in range(len(total)):
                for j in range(len(total[0])):
                    result = result + str(total[i][j]) + ' '
                result += '\n'
            return result
        else:
            print('Two matrices must have same dimension')

    def __mul__(self, other):
        mul = [[0] * len(other[0]) for j in range(len(self._matrix))]
        if len(self._matrix[0]) == len(other):
            for i in range(len(self._matrix)):
                for j in range(len(other[0])):
                    for k in range(len(other)):  # Multiply the elements of each row of the first matrix by the elements of each column in the second matrix
                        mul[i][j] += self._matrix[i][k] * other[k][j]
            # print multiply result
            result = ""
            for i in range(len(mul)):
                for j in range(len(mul[0])):
                    result = result + str(mul[i][j]) + ' '
                result += '\n'
            return result
        else:
            print("The number of columns in the first matrix must equal to the number of rows in the second matrix")


A = Matrix([[1,2],[3,4]])
B = A+[[1,2],[3,4]]
print(B)
print(A * [[2,3,4],[1,2,2]])




