# Element Uniqueness

def uniqueness1(S):
    """Returns True if all elements in S are distinct"""
    tracker = []
    for element in S:
        if element not in tracker:
            tracker.append(element)
        else:
            return False
    return True

x = [1, 2, 3, 4, 5]
y = [1, 1, 2, 3, 4, 5]
print(uniqueness1(x), uniqueness1(y))

# Analysis:
# For loop will execute at O(n) in the case where all elements are unique


def uniqueness2(S):
    for j in range(len(S)):
        for k in range(j+1, len(S)):
            if S[j] == S[k]:
                return False
    return True

# Analysis:
# O(n^2)... pattern is run n times, at each inner iteration we have 1 + 2 + 3 + ... + (n-1)

def uniqueness3(S):
    temp = sorted(S)    # gives us an ascending order version of S
    for j in range(1, len(temp)):
        if temp[j-1] == temp[j]:
            return False
    return True


# Analysis:
# O(n) comparisons
# However, the sorting mechanism takes O(nlogn) steps
# Thus O(nlogn) time complexity


# x = [i for i in range(100)]
# a_slice = x[10:20]    # takes memory


# Recursion
# what is recursion? an iterating mechanism
# how do you do recursion? a function that call itself

# Modern languages suspend invocation of a function until the recursive call completes
# An execution stack is created for each recursive call; also called activation records
# Examples: Factorial function -> n!
#           English Ruler      -> fractal structure
#           Binary search      -> data lookup
#           File systems       -> exploration of nested files


# Factorial function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Complexity O(n)















