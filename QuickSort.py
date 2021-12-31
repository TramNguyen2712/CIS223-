# Array based implementation
# IDEA: select the last element as the pivot, organize the remaining elements
# so that all smaller elements than the pivot are to the left of the pivot
# larger elements than the pivot are to the right of the pivot

def quick_sort(S, start, end):
    if start >= end:
        return
    else:
        pivot = S[end]
        first = start
        current = first


        while current <  end:
            if S[current] >= pivot:
                current += 1
            elif S[current] < pivot:
                #swap current with first
                S[first], S[current] = S[current], S[first] # A Python swap
                # update index of current and index of first
                current += 1
                first += 1
            print(L)
        # Put pivot in the final (correct) location by swapping with first

        S[first], S[end] = S[end], S[first]

        # Recur over left and right portions of the list
        quick_sort(S, start, first-1)
        quick_sort(S,first+1,end)


L= [12,15,36,31,11,17,9,13,23,25]
quick_sort(L,0,len(L)-1)
print(L)

# Analysis:
# If the element chosen as the pivot is about the middle element, there are n-k comparison on each iteration
# The recursion produces a tree structure, the height of the tree is a logn, thus we suspect thus to be an O(nlogn)

# If the pivot is the largest element or smallest element, then we obtain the linear tree with height n, thus O(n**2)

# If we selected the pivot at random, rather than just selecting the last element, the probability of getting an element
# that is about the middle is larger. As a result, we could prove that a randomized version of quick_sort is O(nlogn)

# HINT: I could ask you in the final exam to show experimentally that randomized quick_sort is better than quick-sort

