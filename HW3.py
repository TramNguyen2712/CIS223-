# •Problem R-3.2 page 141
"""The number of operations executed by algorithms A and B is 8nlog n and
2n2, respectively. Determine n0 such that A is better than B for n ≥ n0"""
# Answer in PDF FILE

# •Problem R-3.3 page 141
"""The number of operations executed by algorithms A and B is 40n2 and
2n3, respectively. Determine n0 such that A is better than B for n ≥ n0"""
# Answer in PDF FILE

# •Problem R-3.6 page 141
"""What is the sum of all the even numbers from 0 to 2n, for any positive
integer n?"""
# Answer in PDF FILE
# •Problem R-3.9 page 141
"""Show that if d(n) is O(f(n)), then ad(n) is O(f(n)), for any constant
a > 0."""
# Answer in PDF FILE

# •Problem R-3.15 page 142
"""Show that f(n) is O(g(n)) if and only if g(n) is Ω(f(n))"""
# Answer in PDF FILE

# •Problem R-3.21 page 142
"""Show that nlog n is Ω(n)."""
# Answer in PDF FILE

# •Problem R-3.26 page 142
"""Give a big-Oh characterization, in terms of n, of the running time of the
example4 function shown in Code Fragment 3.10"""


def example4(S):
    """Return the sum of the prefix sums of sequence S."""
    n = len(S)
    prefix = 0
    total = 0
    for j in range(n):
        prefix += S[j]
        total += prefix
    return total


# Analysis
# For the line 26, the loop runs from 0 to n, so running time is n
# So, the time complexity is O(n)


# •Problem R-3.27 page 142
"""Give a big-Oh characterization, in terms of n, of the running time of the
example5 function shown in Code Fragment 3.10."""


def example5(A, B):  # assume that A and B have equal length
    """Return the number of elements in B equal to the sum of prefix sums in A."""
    n = len(A)
    count = 0
    for i in range(n):  # loop from 0 to n-1
        total = 0
        for j in range(n):  # loop from 0 to n-1
            for k in range(1 + j):  # loop from 0 to j
                total += A[k]
        if B[i] == total:
            count += 1
    return count


# Analysis
# Line 43, the loop runs from 0 to n-1, so running time is n
# Line 45, the inner loop runs from 0 to n-1, so running time is n*n
# Line 46, the inner loop runs from 0 to j. For example, if j = 1, the loop will run 1 time.
# That also means if j = n, it will runs n times
# Therefore, j also equals n, and running time is n*n*n
# So, the time complexity is O(n*3)

# •Problem C-3.36 page 144
"""Describe an efficient algorithm for finding the ten largest elements in a
sequence of size n. What is the running time of your algorithm?"""


def ten_largest_elem(n):
    for i in range(0, len(n)):
        for j in range(i, len(n)):
            if n[i] < n[j]:
                temp = n[i]
                n[i] = n[j]
                n[j] = temp
    return n[:10]


n = [6, 7, 5, 4, 3, 8, 9, 2, 10, 12, 1]
print(ten_largest_elem(n))

# Analysis
# For line 64, running time is n
# For line 65, running time is n*n
# From line 66 to 70 is O(1)
# So, the time complexity is O(n^2)

# •Problem C-3.38 page 144
"""Show that ∑n i=1 i2 is O(n3)."""
# Answer in PDF FILE
