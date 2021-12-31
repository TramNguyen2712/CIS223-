import random
# R-1.4
"""Write a short Python function that
takes a positive integer n and returns the sum of the squares of all the positive integer
smaller than n"""
def sum_of_sqrt(n):
    sum = 0
    #n is positive integer
    if n > 0:
        #sum of the square of the n-1
        for i in range(n):
            sum = sum + (i * i)
        #and then do the same with n-2
        return sum

print('Answer R-1.4')
print(sum_of_sqrt(4))

# R-1.11
"""Demonstrate how to use Python's list comprehension syntax to produce the list
[1,2,4,8,16,32,64,128,256]"""
#get the sequence of 2**k where k from 0 to 9
print('Answer R-1.11')
result = [pow(2, k) for k in range(0, 9,+1)]
print(result)


# R-1.12
"""Python's random module includes a function choice(data) that returns a random element from a non-empty sequence. 
The random module includes a more basic function randrange, with parameterization similar to the built-in range function
,that return a random choice from the given range. Using only the randrange function, 
implement your own version of the choice function."""
def choice(data):
    #the sequence cannot be empty
    if len(data) > 0:
        #get the random index from data
        n = random.randrange(0,len(data)-1)
        #return random element
        return data[n]
    else:
        #if len(data) = 0, print this message
        print('Sequence is empty')
        return 0
print('Answer R-1.12')
print(choice('name'))

#C-1.14
"""Write a short Python function that takes a sequence of integer values and determines
if there is a distinct pair of numbers in the sequence whose product is odd."""
def product_odd(data):
    #loop for each element
    for i in range(0,len(data)):
        #loop for each element
        for j in range(i+1,len(data)):
            #check if their product is odd or even
            if ((data[i] * data[j]) % 2 != 0):
                #if the remainder of their product and 2 is different from 0
                #returning true
                return True
    #if not, returning false
    return False
print('Answer C-1.14')
print(product_odd([2,4,5]))

#C-1.19
"""Demonstrate how to use python's list comprehension syntax to produce
the list [ a , b , c ,..., z ],without typing  characters literally."""
#chr(k): return a one-character string with the given Unicode code
# Unicode code point of a is 97
# Unicode code point of z is 122
# Python's list comprehension syntax
#Way 1:
lis = [chr(k) for k in range(97,123)]
#Way 2:
lis = [chr(k) for k in range(ord('a'),ord('z')+1)]
print('Answer C-1.19')
print(lis)

#C-1.21
"""Write a Python program that repeatedly reads lines from standard input until an EOFError is raised, 
and then outputs those lines in reverse order (a user can indicate end of input by typing ctrl-D)."""
def reserve_line():
    #function for reserving the standard input
    n = [] #create an empty list
    done = False
    try:
        while not done: #repeatly reads line
            line_input = input('Enter the line input to reverse, Ctrl-D to stop ')
            #add the input into the list
            n.append(line_input)
    except (EOFError): #when user clicks crl-d to stop
        done = True
    #reserving the line
    for i in range(len(n)-1,-1,-1):
        print(n[i])
print('Answer C-1.21')
reserve_line()

#C-1.22
"""Write a short Python program that takes two arrays a and b length n storing int values, 
and returns the dot product of a and b. That is , it returns an array c of the length n 
such that c[i] = a[i].b[i], for i = 0,....,n-1"""
def dot_product(a,b):
    #a and b have the same length (n)
    if len(a) == len(b):
        c = []
        #i = 0,....n-1
        for i in range(0,len(a)):
            #add the dot product of a and b to array c
            c.append(a[i]*b[i])
        #output
        return c
    else:
        #print the error message if the both are not match in length
        print('a and b must have the same length')
a = [1,2,3]
b = [2,3,4]
result = dot_product(a,b)
print('Answer C-1.22')
print(result)

#C-1.23
"""Give an example of a Python code fragment that attempts to write an element to a list based on an index 
that may be out of bounds. If that index is out of bounds, the program should catch the exception that results, 
and print the following error message: “Don’t try buffer overflow attacks in Python!”"""

def write_elem(list,index,elem):
    try:
        #write an element to a list bassed on an index
        list[index] = elem
        return list
    except IndexError:
        #if index >= the length of list, print the error message
        print('Don’t try buffer overflow attacks in Python!')
print('Answer C-1.23')
n = [0,1,2,3,4]
print(write_elem(n,5,4))

#C-1.27
"""In Section 1.8, we provided three different implementations of a generator that computes factors of a given integer. 
The third of those implementation, from page 41, was the most efficient, but we noted that it did not yield the factors 
in increasing order. Modify the generator so that it reports factors in increasing order, 
while maintaining its general performance advantages"""

#write again the third of those implement
def factors(n):
    k = 1
    while k * k < n: #while k < sqrt(n)
        if n % k == 0:
            yield k
        k += 1
    if k*k == n: #specical case if n is perfect quare
        yield k
   #after yield k
    k -= 1 #go back to yield n // k
    while k > 0: #in case k = 0
        if n % k == 0:
            yield n // k
        k -= 1
X = factors(100)
print('Answer C-1.27')
print(list(X))

#C-1.28
"""For the special case of p = 2, this results in the traditional Euclidean norm, 
which represents the length of the vector. 
For example, the Euclidean norm of a two-dimensional vector with coordinates (4,3) has a Euclidean norm of 
√(4^2 +3^2) = √(16+9) =√25 = 5. 
Give an implementation of a function named norm such that norm(v, p) returns the p-norm value of v and norm(v) 
returns the Euclidean norm of v"""

def norm(v,p=2): #generator norm function
    #assume v is a list of numbers
    sum = 0
    for k in v:
        sum = sum + k**p #sum of two-dimensional vector to the power of p
    return sum ** (1/p) # the Euclidean norm of v

print('Answer C-1.28')
v = [4,3]
print(norm(v,2))

#P-1.36
"""Write a Python program that inputs a list of words, separated by white space, and outputs how many time each word appears in list.
You need not worry about efficiency at this point, however, as this topic is something that will be addressed later in this book"""

def count_word(data):
    n = data.split() #split input string by white space into list
    a = {} #create empty dictionary
    for i in n:
        if i in a: #if the word appears more than one time
            a[i] = a[i] + 1 #dictionary element will increase by 1
        else: #if the word just appears once in list
            a[i] = 1 #element equals 1
    return a  #print result
list_words = 'a b c t a t b'
print('Answer P-1.36')
print(count_word(list_words))

























