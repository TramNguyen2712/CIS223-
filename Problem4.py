def prim_num(n):
    list = []
    for i in range(1,n):
        count = 0
        for j in range(1,i):
            if i % j == 0:
                count += 1
        if count == 1:
            list.append(i)
    return list

print(prim_num(50))