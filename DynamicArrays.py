# Implementing a Dynamic Array
# How to grow an array? You actually can't, but we can create a new array of larger capacity and migrate
# the elements

# Algorithm:
# If an element e is added to an Array A but A is full:
# 1. Allocate B with larger capacity (managed by some function)
# 2. Set B[i] = A[i] for all i
# 3. Insert the element e in A

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
        if self._n == self._capacity:       # dynamic array is full
            self._resize(2*self._capacity)  # can be tweaked to fit the actual growth of lists
        self._A[self._n] = obj
        self._n += 1

    def insert(self, k, obj):
        if self._n == self._capacity:
            self._resize(2*self._capacity)

        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1]

        self._A[k] = obj
        self._n += 1

    def remove(self, obj):
        pass

    def pop(self):   # only implement pop from end of array
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
    






if __name__ == "__main__":
    # Amortized Analysis of Dynamic Arrays

    # What is the running time of operation on dynamic arrays?

    # Amortization analysis - total amount of time spent per step is proportional to total time

    # - We can "overcharge" some operations to "pay" for more expensive operation later
    # - This may not happen at running time, it is just a way to analyze the total running time

    ##### INSERT

    # Test implementation of insert(k, value) in DynamicArrays of varying sizes
    # by repeatedly inserting elements in different areas of the DynamicArray

    def insert_test(array_list, location, num_operations=2000):
        file = open("results_insert_method_da.txt", "a")

        for array in array_list:
            if location == "end":
                l = len(array)
                start = time.time()
                for i in range(num_operations):
                    array.insert(len(array) - 1, None)

                # amortized analysis of time complexity
                average = (time.time() - start)/num_operations

                file.write("{0:<10},{1:^10},{2:>10e}\n".format(location, "N={0}".format(l), average))

            if location == "middle":
                l = len(array)
                start = time.time()
                for i in range(num_operations):
                    array.insert(len(array)//2, None)

                # amortized analysis of time complexity
                average = (time.time() - start) / num_operations

                file.write("{0:<10},{1:^10},{2:>10e}\n".format(location, "N={0}".format(l), average))

            if location == "start":
                l = len(array)
                start = time.time()
                for i in range(num_operations):
                    array.insert(0, None)

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
    #array_list = create_arrays(sizes)
    # print(array_list)
    #insert_test(array_list, 'end')

    # test insert at middle
    #array_list = create_arrays(sizes)
    #insert_test(array_list, 'middle')

    # test insert at beginning
    array_list = create_arrays(sizes)
    insert_test(array_list, "start")











