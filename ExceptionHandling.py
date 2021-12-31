# Handling Exceptions
# Check types and values
# Square root approximation is given by
def sqrt(n, terms=1000):
    if not isinstance(n, (int, float)):
        raise TypeError("n must be int or float!")
    elif n < 0:
        raise ValueError("n cannot be a negative number!")
    else:
        x = 1
        for i in range(terms):
            x = .5 * (x + n/x)
        return x


#Recursion example: Greatest Common Divisor
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# List comprehensions
# list comprehensions are a succinct way of executing an iteration (for)
# List: [expression _for_ value _in_ iterable _if_ condition]

# squares of numbers from 1 to n
n = 100
squares = [x**2 for x in range(n)]
print(squares)

squares2 = []
for i in range(n):
    squares2.append(i**2)
print(squares2)

# first 100 even numbers
evens_100 = [x for x in range(1, 201) if not x % 2]
print(len(evens_100), evens_100)

# factors of n
n = 120
factors = [i for i in range(1, n+1) if n % i == 0]
print(factors)


# random 3x3 matrix fo integers less than 20
import random
matrix_3_3 = [[random.randrange(1, 20) for i in range(3)] for j in range(3)]
print(matrix_3_3)

if __name__ == "__main__":
    number = 2
    print(sqrt(number))

    print(gcd(735, 252))

    print(gcd(252, 735))
