"""R-4.1 Describe a recursive algorithm for finding the maximum element in a sequence, S,
of n elements. What is your running time and space usage?"""


def max_recur(S, n, max=0):
    if n < 0:  # when n = -1
        return max
    elif S[n] > max:
        max = S[n]
    return max_recur(S, n - 1, max)


print(max_recur([5, 3, 4], 2, 0))

"""R-4.2 Draw the recursion trace for the computation of power(2,5), using the
traditional function implemented in Code Fragment 4.11"""


def power(x, n):
    """Compute the value x n for integer n."""
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


"""R-4.6 Describe a recursive function for computing the nth Harmonic number,
Hn = ∑ni=1 1/i."""


def Hn(n, sum=0):
    if n < 1:
        return 'Harmonic number with given n is {0:.2f}'.format(sum)
    else:
        sum += 1 / n
        return Hn(n - 1, sum)


print(Hn(4))

"""R-4.7 Describe a recursive function for converting a string of digits into the integer it represents. 
For example, '13531' represents the integer 13,531."""


def str_to_int(data, n, i=0):
    c = int(data[n])
    if n < 0:
        return c
    else:
        return c * 10 ** (i) + str_to_int(data, n - 1, i + 1)


A = '13531'
print(str_to_int(A, len(A) - 1, 0))
print(type(str_to_int(A, len(A) - 1, 0)))

"""R-4.8 Isabel has an interesting way of summing up the values in a sequence A of
n integers, where n is a power of two. She creates a new sequence B of half
the size of A and sets B[i] = A[2i]+A[2i+1], for i = 0,1,...,(n/2)−1. If
B has size 1, then she outputs B[0]. Otherwise, she replaces A with B, and
repeats the process. What is the running time of her algorithm?"""


def sum_Isabel(data, n):
    """suming up value in q sequence A with n integer (n is a power of two)"""
    # n = 2,4,8,...
    if len(data) == 1:
        return data[0]
    else:
        B = []
        for i in range(0, (n // 2)):
            B.append(data[2 * i] + data[2 * i + 1])
        print(B)
        return sum_Isabel(B, n // 2)


A = [2, 4, 8, 10]
print(sum_Isabel(A, len(A)))

"""C-4.9 Write a short recursive Python function that finds the minimum 
and maximum values in a sequence without using any loops."""


def min_max(S, n, max=0, min=1000):
    if n < 1:
        return 'Min: {0} and Max: {1}'.format(min, max)
    else:
        max1 = (S[n] > max) * S[n] + (max > S[n]) * max
        min1 = (S[n] < min) * S[n] + (min < S[n]) * min
        return min_max(S, n - 1, max1, min1)


print(min_max([4, 3, 7], 2))

"""C-4.10 Describe a recursive algorithm to compute the integer part of the base-two
logarithm of n using only addition and integer division."""


def compute_log(base, number):
    while number > 1:
        "Real logarithms are only defined for x > 0"
        if number <= base:
            return 1
        elif number == 1:
            return 0
        else:
            return compute_log(base, number / base) + 1


print(compute_log(2, 5))

"""C-4.11 Describe an efficient recursive function for solving the element uniqueness problem, 
which runs in time that is at most O(n2) in the worst case without using sorting"""


def ele_uniquess(S, n, i=0, j=1):
    # IDEA: i is index of left element and j is index of right element in array
    # if indexes are out of size of array then array is unique
    if i >= n and j >= n:
        return True
    # if right index has reached maximum limit increase the left by 1 and
    # pass the right index one more than left index
    elif j >= n:
        return ele_uniquess(S, n, i + 1, i + 2)
    # both indexes are valid and if elements are equal at those indexes means
    # array is not unique
    elif S[i] == S[j]:
        return False
    return ele_uniquess(S, n, i, j + 1)  # recurse by increasing j by 1


print(ele_uniquess([1, 3, 2, 4, 5], 4, 0, 1))

"""C-4.12 Give a recursive algorithm to compute the product of two positive integers,
m and n, using only addition and subtraction"""


def product_of_two(m, n):
    if n == 0:
        return 0
    else:
        return m + product_of_two(m, n - 1)


print(product_of_two(3, 3))

"""C-4.14: Towers of Hanoi"""


def Towers_of_Hanoi(n, source, des, temp):
    if n == 1:
        print('Move disc from {0} to {1}'.format(source, des))  # Base Case
    else:
        Towers_of_Hanoi(n - 1, source, temp, des)  # move n-1 from source to temp
        print('Move disc from {0} to {1}'.format(source, des))
        Towers_of_Hanoi(n - 1, temp, des, source)  # move n-1 from temp to des


Towers_of_Hanoi(3, 'source', 'dest', 'temp')

"""C-4.15 Write a recursive function that will output all the subsets of a set of n
elements (without repeating any subsets)."""


def subsets(S, subset, i=0):
    if i >= len(S):
        # when the process ends, print out the subsets of n element
        print(list(subset))
    else:
        # add the element in the current subset and recur
        subset.append(S[i])
        subsets(S, subset, i + 1)
        # backtrack: remove the last element from the current subset and recur
        subset.pop()
        subsets(S, subset, i + 1)


print(subsets([1, 2, 3], [], 0))
print()
# Complexity: O(2**n)

"""C-4.16 Write a short recursive Python function that takes a character string s and
outputs its reverse. For example, the reverse of pots&pans would be
snap&stop ."""


def reverse_string(data, start, end):
    if start >= end - 1:
        return data[start]
    else:
        return data[end] + reverse_string(data, start + 1, end - 1) + data[start]


print(reverse_string('pots&pans', 0, 8))

"""C-4.17 Write a short recursive Python function that determines if a string s is a
palindrome, that is, it is equal to its reverse. For example, racecar and
gohangasalamiimalasagnahog are palindromes."""


def palindrome(S):
    if len(S) == 0:
        return True
    else:
        if S[len(S) - 1] == S[0]:
            return palindrome(S[1:len(S) - 1])
        return False


print(palindrome('racecar'))

"""C-4.18 Use recursion to write a Python function for determining if a string s has
more vowels than consonants"""


def vowel_consonants(S,i=0, vowel=0, con=0):
    if i >= len(S):
        if vowel > con:
            return True
        return False
    else:
        if (S[i] == 'a' or S[i] == 'e' or S[i] == 'i' or S[i] == 'o' or S[i] == 'u' or
                S[i] == 'A' or S[i] == 'E' or S[i] == 'I' or S[i] == 'O' or S[i] == 'U'):
            vowel += 1
        else:
            con += 1
        return vowel_consonants(S,i+1, vowel, con)


print(vowel_consonants('aaat'))

"""C-4.19 Write a short recursive Python function that rearranges a sequence of integer values 
so that all the even values appear before all the odd values."""

def rearrange(S,start,end):
    if start > end-1:
        return S
    else:
        if S[start] % 2 == 0 and S[end] % 2 != 0:
            return rearrange(S,start+1,end-1)
        elif S[start] % 2 == 0:
            return rearrange(S,start+1,end)
        elif S[end] % 2 !=0:
            return rearrange(S,start,end-1)
        else:
            temp = S[start]
            S[start] = S[end]
            S[end] = temp
            return rearrange(S,start+1,end-1)
S = [1,2,3,4,5,6]
print(rearrange(S,0,len(S)-1))

"""C-4.21 Suppose you are given an n-element sequence, S, containing distinct integers that are listed in increasing order. 
Given a number k, describe a recursive algorithm to find two integers in S that sum to k, if such a pair
exists. What is the running time of your algorithm?"""

def pair_number(S,k,start,end):
    if start > end-1:
        return 'end'
    else:
        if (S[start] + S[end]) > k :
            return pair_number(S,k,start,end-1)
        elif (S[start]+S[end]) < k :
            return pair_number(S,k,start+1,end)
        else:
            print('{0}, {1}'.format(S[start],S[end]))
            return pair_number(S,k,start+1,end-1)
S = [1,2,3,4,5,6,7,8]
print(pair_number(S,8,0,len(S)-1))

"""Implement a recursive function with signature find(path, filename) that
reports all entries of the file system rooted at the given path having the
given file name."""
from os import listdir
from os.path import isdir,join,isfile

def find(path,filename):
    if isdir(path):
        for file in listdir(path):
            if isfile(join(path,file)):
                if file == filename:
                    print(file)
            else:
                find(join(path,file), filename)

path = "C:\\Users\\tramn"
filename = "test.txt"

find(path,filename)





