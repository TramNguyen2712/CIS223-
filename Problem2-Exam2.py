def sum_up(A, n):
    """suming up value in q sequence A with n integer (n is a power of two)"""
    """The sequence must have the length that is a power of two such as 2,4,8,16,32..."""
    if len(A) == 1: #When the recursive process ends, and the sequence has only 1 element
        return 'The sum of all elements in sequence A is {0}'.format(A[0])
    else:
        B = [] #create the sequence B with length that is half the size of A
        for i in range(0, (n // 2)):
            B.append(A[2 * i] + A[(2 * i) + 1]) #B[i] = A[2i]+A[2i+1]
        print(B)
        return sum_up(B, n // 2) # recur to sum


A = [2, 4, 8, 10, 20, 21, 5, 6]
print(sum_up(A, len(A)))

#Analysis:
#The for loop and each recursive call will run n/2 times,
#So running time of complexity is O(n/2) that is also O(n)