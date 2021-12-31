#R-1.1
def is_multiple(n,m):
    if (n % m) == 0:
        return True
    else:
        return False

#print(is_multiple(9,3))

#R-1.2
def is_even(k):
    if k&1 == 0:
        return True
    else:
        return False
#print(is_even(4))

#R-1.3

def minmax(data):
    if len(data) > 0:
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp
        min = data[0]
        max = data[len(data)-1]
    return min,max
def minmax2(data):
    min = data[0]
    max = data[0]
    for i in data:
        if i < min:
            min = i
        elif i > max:
            max = i
    return min, max
n= [12,3,5,16]
#print(minmax2(n))

#R-1.5
def sum_square(n):
    k = [i*i for i in range(0,n)]
    return sum(k)

#print(sum_square(3))

#R-1.6
def sum_square_odd(n):
    sum =0
    for i in range(0,n):
        if i % 2 != 0:
           sum += i*i
    return sum

#print(sum_square_odd(4))

#R-1.7
def sum_of_srt_odd(n):
    return sum([i*i for i in range(n) if i%2 != 0])

#print(sum_of_srt_odd(4))

#R-1.8
def negative_int(s):
    n = len(s)
    for k in range(-n,0): #k = -7,-6,....,-1
        print(s[k])

    for j in range(-n,0): #j = 0,1,2,3,...,6
        print(s[j+n])


#negative_int('python ')

#R-1.9
#50,60,70,80
#print([i for i in range(50,81,+10)])

#R-1.10
#8,6,4,2,0,-2,-4,-6,-8
#print([i for i in range(8,-9,-2)])

#C-1.13
def reverse_list(list):
    n = len(list)
    i = 0
    while i < n-1:
        list[i], list[n-1] = list[n-1], list[i]
        i += 1
        n -= 1
    return list


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(reverse_list(my_list))

#C-1.15
def distinct_number(S):
    a = {}
    for i in S:
        if i in a:
            return False
        else:
            a[i] = 1
    return True

# print(distinct_number([1,2,4,8]))

#C-1.16
def scale(data,factor):
    for j in range(0,len(data)):
        data[j] *= factor
    return data

#print(scale([1,2,3,4],2))

def rearrange(S,k,start,end):
    if len(n) % 2 ==0:
        if start == end:
            return S
        else:
            if ((S[start] <= k) and (S[end-1] > k)): #if both start value and end value meet condition
                return rearrange(S,k,start+1,end-1)
            elif S[start] <=k: #if both start and end are less than k
                return rearrange(S,k,start+1,end) #keep end value to compare, move forward from start value
            elif S[end-1] > k: #if both start and end are bigger than k
                return rearrange(S,k,start,end-1) #keep start value to compare, move backward from end value
            else: #if start > and end <= k
                S[start],S[end-1] = S[end-1],S[start] #swap them
                return rearrange(S,k,start+1,end-1)

# S = [7,2,8,9,5]
# print(rearrange(S,6,0,len(S)))

def power2(x, n):
    """Computer the value x**n for integer n"""
    result = 1
    for i in range(0,n//2):
        result *= x**2
    if n % 2 != 0:
        result *= x
    return result

# print(pow(2,3))
# print(power2(2,3))


def pair_of_sum(S,k,start,end):
    if start >= end-1:
        return 'end'
    sum = S[start] + S[end-1]
    if sum == k:
        print(S[start], S[end-1])
        return pair_of_sum(S,k,start+1,end-1)
    elif sum < k:
        return pair_of_sum(S,k,start+1,end)
    elif sum > k:
        return pair_of_sum(S,k,start,end-1)


S = [5,6,7,9,10,11,14,20,26,36]
print(pair_of_sum(S,21,0,len(S)))
