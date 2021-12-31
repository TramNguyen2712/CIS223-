# random 3x3 matrix fo integers less than 20
import random

def matrix_builder(n):
    matrix_n_n = [[random.randrange(1, 20) for i in range(n)] for j in range(n)]   # list comprehension
    return matrix_n_n

print(matrix_builder(10))


#print(matrix_3_3[0][0])

# # ITERATORS and GENERATORS

# Iterable - object that produces an iterator iter(obj)
# Iterator - object that manages iteration next(i) -- this is in essence what a for loop does

X = iter([x for x in range(10)])
print(X)

print(next(X))
for i in X:
    print(i)

# GENERATOR - a procedure to generate a collection
# Want to build a generator for the fibonacci sequence
# for example, want to generate the first 5 fibonacci numbers -> {1, 1, 2, 3, 5}


def fibonacci(n):
    a = 0
    b = 1
    i = 0
    while i < n:
        future = a + b
        a = b
        b = future
        yield a
        i += 1

X = fibonacci(5)
print(list(X))

# Generate the factors (divisors) of a number
# IDEA: For an integer n, check all integers k <= n, if n%k == 0, then k is a divisor (factor)

# IDEA 2: If we know that an element k is a factor (divisor) then n//k is also a divisor.
# This simplifies the previous idea (algorithm) by allowing us to check only number up to sqrt(n)

def factors(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n//k
        k += 1
    if k * k == n:
        yield k  # in this case k = n//k


X = factors(10)
print(list(X))


# Generate positive even numbers
def evens():
    even = 0
    while True:
        yield even
        even += 2

even = evens()
print("EVENS: " + str(next(even)))
print("EVENS: " + str(next(even)))
print("EVENS: " + str(next(even)))
print("EVENS: " + str(next(even)))
print("EVENS: " + str(next(even)))
print(even)






















