def Sequence(n):
    a = 1
    for i in range(1,n):
        yield a
        a = a * 2 + 1


print(list(Sequence(20)))

result = [(2**k + k + 1) for k in range(0,20)]
print(result)