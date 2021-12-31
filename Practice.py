def add_it_up(n):
    total = 0
    try:
        for num in range(0,n+1):
            total += num
            num += 1
    except TypeError:
        return 0
    return total

print(add_it_up(6))

import matplotlib as plt
def get_products_of_all_ints_except_at_index(n):
    result = []
    for i in range(0,len(n)):
        mul = 1
        for j in n:
            mul = mul * j
        div = mul // n[i]
        result.append(div)
    return result

n = [1,7,3,4]
result = get_products_of_all_ints_except_at_index(n)


def average(n):
    A = [0] * len(n)
    total = 0
    for i in range(0,len(n)-1):
        total += n[i]
        A[i] = total / (i+1)
    return A

n = [3.1,5.6,4.3,8.1,2.7]

print(average(n))


