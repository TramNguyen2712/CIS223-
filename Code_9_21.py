# Prefix Average
# for S = 1, 2, 3, ..., n
# A[j] = S[0] + ... + S[j] / (j + 1)

def prefix_average1(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += S[i]         # accumulates the total of the prefix
        A[j] = total/(j+1)
    return A

# Analysis
# Line 6: O(1)
# Line 7: O(n) .. since list grows one step up to n steps.. think of n append() statements
# Lines 8-10: O(n^2) nested for loops contribute n*(1 + 2 + 3 + ... +n), n + 2n + 3n + .. + n*n steps.
# Line 12: O(1)
# Thus complexity is O(n^2)


def prefix_average2(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        A[j] = sum(S[:j+1])/(j+1)
    return A

# Analysis
# We replaced the inner for loop with sum(S[:j+1])
# The evaluation of sum() takes O(j+1) steps for each j, thus 1 + 2 + 3 + ... + n are added for each j in the for loop
# We are still at O(n^2)

def prefix_average3(S):
    n = len(S)
    A = [0] * n
    total = 0
    for j in range(n):
        total += S[j]
        A[j] = total/(j+1)
    return A


# Analysis
# For loop executes n times since lines 40 and 41 are O(1)
# Thus total running time is O(n)


if __name__ == "__main__":
    print(prefix_average1([1.3, 2.1, 5.7, 3.2, 4.8]))


