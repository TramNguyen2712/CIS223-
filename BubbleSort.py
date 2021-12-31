# Array based implementation of bubble sort
# IDEA: Compare consecutive elements from left to right and swap elements if right element is smaller that left element
# the largest element "bubbles" to the right with first case, then second largest, etc

from SelectionSort import swap


def bubble_sort(L):
    for i in range(len(L) - 1):  # total number of passes over the lst to guarantee its sort
        # iterate over all pairs until just before the last sorted element
        for j in range(len(L) - i - 1):
            # compare consecutive elements and swap if necessary
            if L[j] > L[j + 1]:
                swap(L, j, j + 1)
        print(L)

# Analysis:
# We observe that if list is in descending order (worst case) all elements need to relocate
# so we incur in n-1 + n-2 + n-3 +.....+1 -> O(n**2)

L = [12,15,36,31,11,17,9,13,23,25]
bubble_sort(L)
print(L)
