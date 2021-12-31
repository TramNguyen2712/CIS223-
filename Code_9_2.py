# # We compare running times of two functions to find the best in terms of running time
# import time
# import matplotlib.pyplot as plt
#
# def factors1(n):
#     return [i for i in range(1, n+1) if not n % i]
#
#
# def factors2(n):
#     factors = []
#     k = 1
#     while k * k < n:   # only need to check up to sqrt(n)
#         if not n % k:
#             factors.append(k)
#             factors.append(n//k)
#         k += 1
#     if k * k == n:
#         factors.append(k)
#
#
# # We run 100 integers through each function and obtain the total running time results which we then plot
# x = [i for i in range(10000, 60000, 500)]
# # print(len(x))
#
# times1 = []
# times2 = []
# for j in x:
#     # Test factors1() .. fix this code so we take averages for each input
#     avg_time = []
#     for k in range(100):
#         start_time = time.time()    # current time of the machine's clock in milliseconds
#         factors1(j)
#         end_time = time.time()
#         avg_time.append(end_time - start_time)
#     times1.append(sum(avg_time)/len(avg_time))
#
#     start_time = time.time()  # current time of the machine's clock in milliseconds
#     factors2(j)
#     end_time = time.time()
#     times2.append(end_time - start_time)
#
# print(times1)
# print(times2)
#
#
# # Plot times vs input size
# plt.scatter(x, times1, color="red")
# plt.scatter(x, times2, color="blue")
# plt.ylabel("Running Time (ms)")
# plt.xlabel("Input Size (n)")
# plt.ylim(-.01, .01)
# plt.show()


# Experimental Analysis
# Caveats:
#   1. Comparing algorithms requires that we use the same hardware and software environments
#   2. Can only test limited number of inputs (thus not a proof)
#   3. Algorithms must be fully implemented. (This is problem since it may require time to implement, perhaps only to
#      perhaps find it is not good enough)


# Logarithm expression inside the ceiling function
def log_ceiling(n, b):
    n_ = n
    counter = 0
    while True:
        x = n_/b
        counter += 1
        if x <= 1:
            break
        else:
            n_ = x 
    return counter


print(log_ceiling(81, 6))   # 3
print(log_ceiling(12, 2))   # 4
print(log_ceiling(27, 3))





