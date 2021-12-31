# More examples of recursion
import random

# Example 1: Adding elements in a sequence
# Recursion: Add n-1 integers to n; repeat for n-1

def linear_sum(S, n):
    """Assumes user calls function with n=len(S)"""
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]


S = [random.randint(1, 100) for i in range(11)]
print(linear_sum(S, len(S)))
# print(sum(S))

# Analysis:
# If you create the execution tree you see that each recursive call reduces n by 1
# Each call is O(1) and there are n + 1 function calls at O(1)
# Thus, O(n)


# Example 2: Reversing a sequence (in-place)
# Say the sequence is S = [6, 3, 7, 1, 4]

# Idea: Swap the first and last elements and repeat for sequence without the endpoints
# We need to keep track of indices such that we can differentiate between the even and odd length cases for any given
# sequence S

# If S is even, then we stop when start == end - 1
# If S is odd, then we stop when start == end

# def swap(a, b):
#     temp = b
#     b = a
#     a = temp


def reverse(S, start, end):
    """Assumes function is called with start=0, end=len(S) to reverse entire sequence."""
    if start < end - 1:
        S[start], S[end-1] = S[end-1], S[start]   # Python swap
        reverse(S, start + 1, end - 1)



print(S)
reverse(S, 0, len(S))
print(S)

# Analysis:
# see execution tree
# Each case when S is even or odd, the complexity is floor(n/2), which is simply O(n)

# Example 3: Computing n powers of x


def power1(x, n):
    if n == 0:
        return 1
    else:
        return x * power1(x, n-1)

# Analysis: O(n)


def power2(x, n):
    if n == 0:
        return 1
    else:
        partial = power2(x, n//2)    # single recursive call
        result = partial * partial   # avoids making a second recursive call to power2()
        if n%2:   # if the result of n%2 is 1, it is interpreted as True
            result *= x
        return result


p1 = power1(5, 4)
p2 = power2(5, 4)
print(p1, p2)













