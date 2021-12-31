# Plot all 1, logn, n, nlogn, n**2, n**3, 2**n

import numpy as np
import matplotlib.pyplot as plt

# n = 100
# n_ = [i for i in range(2, n)]
#
#
# # Constant function
# x = [1 for i in n_]
# plt.plot(n_, x)
#
# # Log of n, base 2
# log2 = [np.log2(i) for i in n_]
# plt.plot(n_, log2)
#
# # Linear function
# linear = [i for i in n_]
# plt.plot(n_, linear)
#
# # n-log-n
# nlogn = [i*np.log2(i) for i in n_]
# plt.plot(n_, nlogn)
#
# # quatratic
# nsquare = [i**2 for i in n_]
# plt.plot(n_, nsquare)
#
# # cubic
# ncube = [i**3 for i in n_]
# plt.plot(n_, ncube)
#
# # exponential base 2
# exponential = [2**i for i in n_]
# plt.plot(n_, exponential)

# Constant
const = lambda x: 1

# Log
log = lambda x: np.log2(x)

# Line
line = lambda x: x

# nLogn
nlogn = lambda x: x * np.log2(x)

# polynomial
poly2 = lambda x: x ** 2
poly3 = lambda x: x ** 3

# exponential
expo = lambda x: 2 ** x


# Plot all functions
def plot_functions(fl, n):
    """
    To plot functions in the same plot.
    :param fl: list of functions
    :param n: number of elements to evaluate all functions
    :return: None
    """
    x = [i for i in range(2, n)]
    for func in fl:
        y = [func(i) for i in range(2, n)]
        plt.plot(x, y)


fList = [const, log, line, nlogn, poly2, poly3, expo]
plot_functions(fList, 100)

plt.legend(['y=1', 'y=log(n)', 'y=n', 'y=nlog(n)', 'y=' + r'$n^{2}}$', 'y=' + r'$n^{3}$', \
    'y=' + r'$2^{n}$'], loc='upper left')

plt.xscale('log')
plt.yscale('log')


plt.show()






