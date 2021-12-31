# Three-way set disjointness
# Determine if A intersection B intersetion C is empty

from time import time
from matplotlib import pyplot as plt

def disjoint1(A, B, C):
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False

    return True


def disjoint2(A, B, C):
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if a == c:
                        return False

    return True


def plot_functions(func):
    y = []

    x = [i for i in range(100)]

    for i in x:
        start = time() #record the starting time
        A = set(range(1, i, 1))
        B = set(range(2, i, 1))
        C = set(range(3, i, 1))
        result = func(A, B, C)
        run_time = time() - start #compute the elapsed time
        y.append(run_time) #save the executive time
    #plotting the time vs input size
    plt.plot(x, y,'o')

plot_functions(disjoint1)
plot_functions(disjoint2)
# naming the x axis
plt.xlabel('Data Size')
# naming the y axis
plt.ylabel('Time(sec)')
# naming the title
plt.title('Comparing The Running Time Between 2 Functions')
plt.legend(['y=disjoint1', 'y=disjoint2'], loc='upper left')



plt.show()



























