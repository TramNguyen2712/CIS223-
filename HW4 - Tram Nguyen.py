"""R-4.1 Describe a recursive algorithm for finding the maximum element in a sequence, S, of n elements.
What is your running time and space usage?"""

def max_elem(S,n,max=0):
    if n < 0:
        return max #when n reached the beginning of sequence, return the maximun value
    elif S[n] > max: #compare element with max
        max = S[n]  #if element is bigger than max, let it is the maximun element
    return max_elem(S,n-1,max)


S = [5,3,7,8,3,-12]
print('Answer R-4.1: maximum element in S = [5,3,7,8,3,-12] is')
print(max_elem(S,len(S)-1,0))
print()

#Analysis
#Each call is O(1) and there are n + 1 function calls at O(1)
#Running time is O(n)
#Each of these call is compared to previous number and takes up actual memory
#Space Usage is O(n) space also

"""R-4.3 Draw the recursion trace for the computation of power(2,18), using the
repeated squaring algorithm, as implemented in Code Fragment 4.12."""

# def power1(x, n):
#  """Compute the value x n for integer n."""
#  if n == 0:
#     return 1
#  else:
#     partial = power1(x, n // 2) # rely on truncated division
#     result = partial*partial
#     if n % 2 == 1: # if n odd, include extra factor of x
#         result *= x
#     return result

def power(x,n):
    """Computer the value x**n for integer n"""
    if n == 0:
        return 1
    elif n == 1: #if n is odd, extra the factor of x
        return x
    else:
        return x**2 * power(x,n-2)
print('Answer R-4.3: power(2,18) is')
print(power(2,18))
print()

"""R-4.6 Describe a recursive function for computing the nth Harmonic number, Hn = ∑ni=1 1/i"""

def harmonic(n):
    if n == 1:
        return 1
    else:
        return 1/n + harmonic(n-1)
print('Answer R-4.3: Harmonic number of n = 8 is')
print(format(harmonic(8),'.4f'))
print()

#Describe:
#n-th Harmonic number is the sum of 1,1/2,1/3,.....,1/(n-1),1/n

"""R-4.7 Describe a recursive function for converting a string of digits into the integer it represents. 
For example, '13531' represents the integer 13,531"""

def convert(data):
    if len(data) == 1:
        return int(data[0])
    else:
        c = int(data[0])
        return c * power(10,len(data)-1) + convert(data[1:len(data)])

n ='13531'
print("Answer R-4.7: Convert '13531' to integer 13,531")
print(convert(n))
print(type(convert(n)))
print()

"""C-4.12 Give a recursive algorithm to compute the product of two positive integers,
m and n, using only addition and subtraction."""

def product(m,n):
    "Compute the value of m * n"
    if n == 1: #except m * 0
        return m
    else:
        # for example: 2 * 3 = 2 + 2 + 2
        # run recursive
        return m + product(m,n-1)

print('Answer C-4.12: product(2,3) is')
print(product(2,3))
print()

"""C-4.16 Write a short recursive Python function that takes a character string s and
outputs its reverse. For example, the reverse of pots&pans would be
snap&stop ."""
def reverse(S):
    if len(S) == 1: #if S[0] = '&', return it
        return S[0]
    else:
        return S[len(S)-1] + reverse(S[1:len(S)-1]) + S[0]
S ='pots&pans'
print('Answer C-4.16: reverse of pots&pans ')
print(reverse(S))
print()
#Analysis
#Executive tree in pdf file

"""C-4.20 Given an unsorted sequence, S, of integers and an integer k, describe a
recursive algorithm for rearranging the elements in S so that all elements
less than or equal to k come before any elements larger than k. What is
the running time of your algorithm on a sequence of n values?"""

def rearrange(S,k,start,end):
    """Rearrange all elements in S with start = 0 and end = len(S) """
    if start == end: # if there is nothing to compare with k
        return S # return S that is rearranged
    else:
        if ((S[start] <= k) and (S[end-1] > k)): # if both start value and end value meet condition
            return rearrange(S,k,start+1,end-1)
        elif S[start] <=k: # if both start and end are less than k
            return rearrange(S,k,start+1,end) # keep end value to compare, move forward from start value
        elif S[end-1] > k: # if both start and end are bigger than k
            return rearrange(S,k,start,end-1) # keep start value to compare, move backward from end value
        else: # if start > and end <= k
            S[start],S[end-1] = S[end-1],S[start] # swap them
            return rearrange(S,k,start+1,end-1)
S = [-7,2,8,9,5]
print('Answer C-4.12: The S after rearrange with k = 6')
print(rearrange(S,6,0,len(S)))
print()
#Analysis
#Executive tree in pdf file
#Each case when element in S is smaller or bigger , the running time is O(n)
"""C-4.21 Suppose you are given an n-element sequence, S, containing distinct integers that are listed in increasing order. Given a number k, describe a
recursive algorithm to find two integers in S that sum to k, if such a pair
exists. What is the running time of your algorithm?"""

def pair_of_sum(S,k,start,end):
    if start >= end-1:
        return 'end'
    sum = S[start] + S[end-1]
    if sum == k:
        print(S[start], S[end-1])
        return pair_of_sum(S,k,start+1,end-1)
    elif sum < k:
        return pair_of_sum(S,k,start+1,end)
    elif sum > k:
        return pair_of_sum(S,k,start,end-1)

print('Answer C-4.21: pair(s) of two integers in S that sum to k = 21 if exits')
S = [5,6,7,9,10,11,14,20,26,36]
print(pair_of_sum(S,62,0,len(S)))
print()
#Analysis
#Each case for sum of two interger is bigger, smaller or equal to k, the running time is O(n)

"""C-4.22 Develop a nonrecursive implementation of the version of power from
Code Fragment 4.12 that uses repeated squaring"""

def power2(x, n):
    """Computer the value x**n for integer n"""
    result = 1
    for i in range(0,n//2):
        result *= x**2
    if n % 2 != 0:  # if n odd, include extra factor of x
        result *= x
    return result

print('Answer C-4.12: power(2,5) is')
print(power2(2,5))
print()




















