def run(list):
    count = 1
    max_count = 1

    for i in range(len(list) - 1):
        if list[i] == list[i + 1]:
            count += 1
        else:
            count = 1

        if count > max_count:
            max_count = count

    return (max_count)


List = [1, 5, 5, 3, 1, 2, 2, 2, 2, 3, 6, 5, 5, 6]
print(run(List))


def run1(list):
    a = {}
    max_count = 0
    for i in list:
        if i in a:
            a[i] = a[i] + 1
        else:
            a[i] = 1

        if a[i] > max_count:
            max_count = a[i]

    return max_count


print(run1(List))
