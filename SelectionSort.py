# Array base implementation of selction sort
# IDEA: find the smallest element of unsorted portion of list L and swap with current element
# start the current element at the beginning of the list, and move iteratively to the right after sacnning the
# entire list each time

def swap(L,i,j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp

def selection_sort(L):
    # iterarate to the list elements
    for i in range(len(L)):
        _min = i
        # iterate through the rest of the list to find the minimum element index
        for j in range(i+1, len(L)):
            if L[j] < L[_min]:
                _min = j

        swap (L,_min,i)

# Analysis: In the worst-case we iterate over all elements and repeat process at each iteration
# Finding the minimal element will take n times the first time, then n-1 times, then n-2 times.....
# Thus O(n**2)

L = [1,4,5,6,4,7,8,9,4,6]
selection_sort(L)
print(L)

