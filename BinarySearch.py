# Binary search
# Find an element in a sorted list

def binary_search(data, v, low, high):
    """Return True if v is between data[low] and data[high] including the endpoints."""
    if low > high:
        return False
    else:
        mid = (low + high)//2   # middle index
        if v == data[mid]:
            return True
        elif v < data[mid]:
            return binary_search(data, v, low, mid-1)   # recur on bottom half
        else:
            return binary_search(data, v, mid+1, high)  # recur on top half

# Analysis:
# O(logn)

from random import randint
data = sorted([randint(1, 10000) for i in range(100)])
print(data)
result = binary_search(data, 1234, 0, len(data) - 1)
print(result)

