# File System
# Determine the cumulative disk space usage of a path in the os directory

import os

# os.path.getsize(path) --- immediate disk usage
# os.path.isdir(path)    --- returns true if path is a directory
# os.listdir(path)      -- return immediate subnodes as string
# os.path.join(path, filename) --- uses operating system operator to generate a new path

def disk_usage(_path):
    """Return the number of bytes used by a directory path and its sub-nodes"""
    total = os.path.getsize(_path)

    if os.path.isdir(_path):
        for sub_node in os.listdir(_path):
            sub_path = os.path.join(_path, sub_node)
            total += disk_usage(sub_path)

    return total

if __name__ == "__main__":
    _path = "C:\\Users\\Guarionex Salivia\\Documents"
    t = disk_usage(_path)
    print(t)

# Analysis:
# Each sub_node will be called once at each iteration of the for loop, thure there are exactly n recursive calls
# we will see the results of tree traversals in chapter 8
# if the number of operations at each node is O(1) and there are n visits, one for each node then
# complexity is O(n)





