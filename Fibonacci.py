# Fibonacci sequence 1 1 2 3 5 8 ...
# F0 = 1
# F1 = 1
# Fn = Fn-1 + Fn-2

def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Horrible complexity > O(2^n)..... f(n) > 2 ** (n/2)
# Main issue is memory efficiency.

# Better implementation returns two values, keeping track of work already done

def fibonacci_alt(n):
    if n <= 1:
        return n, 0  # with the understanding that the sequence is indexed starting at 1...
    else:
        a, b = fibonacci_alt(n-1)
        return a+b, a


x = fibonacci_alt(4)
print(x[0] + x[1])
print(fibonacci(4))

# Extra problem: compare execution times between fibonacci() and fibonacci_alt() experimentally.





