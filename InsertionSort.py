# Algorithm
# Input: Array A of comparable elements
# Output: A with elements in non-decreasing order
# for k from 1 to n-1 do
#    Insert A[k] at its proper location within A[0], A[1], A[k-1]
#       # we will implement the insertion by repeatedly checking if A[k] < A[k-1] and swap them

def insertion_sort(A):
    """Sort list of comparable elements into non-decreasing order."""

    for k in range(1, len(A)):   # k represents indices; notice we skipped 0
        current = A[k]
        j = k
        while j > 0 and A[j-1] > current:   # if previous element is larger, move it to the right
            A[j] = A[j-1]                   # actual movement of the element to the right
            j -= 1
        A[j] = current                      # insert element in correct position


if __name__ == "__main__":
    from random import randint
    S = [randint(0, 100) for i in range(10)]
    print(S)
    insertion_sort(S)
    print(S)

# Analysis:
# The worst-case scenario occurs when the list is in descending order
# we will have to shift n-1 element to the right in the inner loop....
# we have the following pattern 1 + 2 + 3 + ... = n(n-1)/2
# Thus O(n**2)
