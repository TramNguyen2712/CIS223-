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
    #print array
    def __str__(self):
        array = ""
        for i in range(self._n):
            array += str(self._A[i]) + ","
        array = array[:-1] # remove "," at the end of array after for loop
        return "[" + array + "]"
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

    def remove(self, obj):
        pass

    def pop(self):  # only implement pop from end of array
        # IDEA to remove the last element; at index len(self._n) - 1
        # It is similar to append but instead of growing the list, you check
        # the current capacity and make a decision as to how much empty space
        # to keep.

        # for instance if you are using 1/4 of the capacity, then shrink capacity by 1/2
        pass

    def pop(self, idx=-1):
        # IDEA to remove element at index idx
        # Other than considering the capacity you should also make sure
        # that list elements are next to each other, without gaps in between
        # which means shifting elements back to fill any empty locations
        pass


"""In Code Fragment 5.1, we perform an experiment to compare the length of
a Python list to its underlying memory usage. Determining the sequence
of array sizes requires a manual inspection of the output of that program.
Redesign the experiment so that the program outputs only those values of
k at which the existing capacity is exhausted. For example, on a system
consistent with the results of Code Fragment 5.2, your program should
output that the sequence of array capacities are 0, 4, 8, 16, 25, ...."""

import sys

data = []
n = 50
pre = 0
for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)  # size in bytes
    if b > pre and a > 0:  # except a = -1 when subtract a with 1
        print("When the length reaches at {0:3d}, the size in bytes will grow by {1:4d} bytes".format(a - 1, b - pre))
    pre = b
    data.append(None)

"""Our DynamicArray class, as given in Code Fragment 5.3, does not support
use of negative indices with getitem . Update that method to better
match the semantics of a Python list"""

import ctypes


class DynamicArray1(DynamicArray):
    def __init__(self):
        super().__init__()

    def __getitem__(self, index):
        """Update the method __getitem__ to get negative indices
        Return entry at index k(using standard interpretation if negative)."""
        if index < 0:  # Code Fragment 2.6
            index += len(self)
        if not 0 <= index < self._n:
            raise IndexError('invalid index')
        return self._A[index]


"""Our implementation of insert for the DynamicArray class, as given in
Code Fragment 5.5, has the following inefficiency. In the case when a resize occurs, the resize operation takes time 
to copy all the elements from an old array to a new array, and then the subsequent loop in the body of
insert shifts many of those elements. Give an improved implementation
of the insert method, so that, in the case of a resize, the elements are
shifted into their final position during that operation, thereby avoiding the
subsequent shifting."""


class DynamicArray2(DynamicArray):
    def __init__(self):
        super().__init__()

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def insert1(self, k, obj):
        """Insert value at index k, shifting subsequent values rightward."""
        if self._n == self._capacity:
            """To avoid subsequent shifting, inserting value during the resize operation is occurring """
            B = self._make_array(2 * self._capacity)  # same as resize operation
            for i in range(0,k):  # 0<= i < k
                # copy all elements from old arrays to a new array
                B[i] = self._A[i]
            B[k] = obj  # At k index, insert the obj value
            for j in range(k, self._n):  # from k to the last index, shifts many of those elements
                B[j + 1] = self._A[j]
            self._A = B
            self._capacity = 2 * self._capacity

        else:
            for j in range(self._n, k, -1):  # if array is not full
                self._A[j] = self._A[j - 1]

            self._A[k] = obj
        self._n += 1

if __name__ == "__main__":
    print('Answer for R-5.6')
    A = DynamicArray2()
    A.append(1)
    A.append(2)
    print('Array A:')
    print(A)
    print('Array A after the insert method:')
    A.insert1(1,3)
    print(A)
    print()


"""Let A be an array of size n ≥ 2 containing integers from 1 to n−1, inclusive, 
with exactly one repeated. Describe a fast algorithm for finding the integer in A that is repeated"""


def find_repeated_int(A):
    if len(A) < 2:
        raise IndexError
    else:
        B = [0] * (len(A)) #Create the new array with same length of old array
        for i in range(0, len(A)): #copy all element from array A to array B
            if A[i] in B: #if the element from A already exits in B, print it out
                print("The integer is repeated in array is {0:3d}".format(A[i]))
                B[i] = A[i]
            else:
                B[i] = A[i]
if __name__ == "__main__":
    print('Answer for R-5.7 ')
    A = [1, 2, 3, 4, 5, 5, 6]
    find_repeated_int(A)
    print()
# The time of complexity is O(n)

"""Describe how the built-in sum function can be combined with Python’s
comprehension syntax to compute the sum of all numbers in an n×n data
set, represented as a list of lists"""
S = [[6, 2, 8], [1, 4, 7], [10, 7, 11]]
# total = 0
# for lists in S:
#     for val in lists:
#         total += val
# print(total)
if __name__ == "__main__":
    print('Answer for R-5.12 ')
    total = sum([sum(val for val in lists) for lists in S])
    print(total)
    print()

"""Implement a pop method for the DynamicArray class, given in Code Fragment 5.3, that removes the last element of the array, 
and that shrinks the capacity, N, of the array by half any time the number of elements in the
array goes below N/4"""


class DynamicArray3(DynamicArray):
    def __init__(self):
        super().__init__()

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

    def pop(self):  # only implement pop from end of array
        # IDEA to remove the last element; at index len(self._n) - 1
        # It is similar to append but instead of growing the list, you check
        # the current capacity and make a decision as to how much empty space
        # to keep.

        # for instance if you are using 1/4 of the capacity, then shrink capacity by 1/2
        """remove the last element from the end of the array"""
        last_element = None

        if self._capacity > 0:
            last_element = self._A[self._n - 1]
            self._A[self._n - 1] = None
            self._n -= 1

            if self._n < self._capacity // 4:
                """shrinks the capacity, N, of the array by half any time 
                the number of elements in the array goes below N/4"""
                # for example, if there is an array having 1 element but using 4 memories,
                # we have to resize its capacity to half of its current the capacity
                # So, the array will consume less memories.
                self._resize(self._capacity // 2)

        return last_element

if __name__ == "__main__":
    print('Answer for C-5.16 ')
    S = DynamicArray3()
    S.append(1)
    S.append(2)
    S.append(3)
    print(S)
    print('S after pop method')
    S.pop()
    print(S)
    print()



# Why does the capacity divide by 4 instead of 2?
# Assume the array has the capacity is 2 and the size is 1, so the capacity will be 1 after this logic
# After this, if we have another append operation,we need to resize the array, and it takes O(n) to run

# However, in case of dividing by 4, if we have another append operation ,we just append the new element in the array
# which just takes O(1) to run

"""Perform experiments to evaluate the efficiency of the remove method of
Python’s list class, as we did for insert on page 205. Use known values so
that all removals occur either at the beginning, middle, or end of the list.
Report your results akin to Table 5.5"""

class DynamicArray4(DynamicArray):
    def __init__(self):

        super().__init__()

    def remove_at_index(self, k):
        if 0 <= k <= self._n:
            for i in range(k, self._n - 1):
                self._A[i] = self._A[i + 1]
            self._n -= 1
        else:
            return "IndexError"

if __name__ == "__main__":
    # Test implementation of remove(k, value) in DynamicArrays of varying sizes
    # by repeatedly remove elements in different areas of the DynamicArray

    def remove_test(array_list, location, num_operations=2000):
        file = open("results_remove_method_da.txt", "a")

        for array in array_list:
            if location == "end":
                l = len(array)
                start = time.time()
                for i in range(num_operations):
                    array.remove_at_index(len(array) - 1)

                # amortized analysis of time complexity
                average = (time.time() - start)/num_operations

                file.write("{0:<10},{1:^10},{2:>10e}\n".format(location, "N={0}".format(l), average))

            if location == "middle":
                l = len(array)
                start = time.time()
                for i in range(num_operations):
                    array.remove_at_index((len(array)-1)//2)

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
            array = DynamicArray4()

            for i in range(n):
                array.append(None)
            D.append(array)

        return D

    sizes = [100, 1000, 10000, 100000]

    # # test remove at end
    # array_list = create_arrays(sizes)
    # # print(array_list)
    # remove_test(array_list, 'end')
    #
    # # test remove at middle
    # array_list = create_arrays(sizes)
    # remove_test(array_list, 'middle')
    #
    # # test remove at beginning
    # array_list = create_arrays(sizes)
    # remove_test(array_list, 'start')

"""Write a Python program for a matrix class that can add and 
multiply two-dimensional arrays of numbers, assuming the dimensions agree appropriately for the operation."""


class Matrix():
    def __init__(self,matrix):
        self._matrix = matrix

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
            for k in range(len(self._matrix)):
                for i in range(len(other[0])):
                    for j in range(len(other)):  # Multiply the elements of each row of the first matrix by the elements of each column in the second matrix
                        mul[k][i] += self._matrix[k][j] * other[j][i]
            # print multiply result
            result = ""
            for i in range(len(mul)):
                for j in range(len(mul[0])):
                    result = result + str(mul[i][j]) + ' '
                result += '\n'
            return result
        else:
            print("The number of columns in the first matrix must equal to the number of rows in the second matrix")

if __name__ == "__main__":
    print('Answer of C-5.33')
    A = Matrix([[1, 2], [3, 4]])
    B = A + [[1, 2], [3, 4]]
    print('Adding two matrix')
    print(B)
    print('Multiply two matrix')
    print(A * [[2, 3, 4], [1, 2, 2]])









