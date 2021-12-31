# Lists are Dynamic Arrays
# Lists are initialized with more space than necessary
# List grows as necessary by adding "chunks" of memory at a time
# to add a "chunk" of memory, a new area in memory with the desired new allocation
# is selected and a copy of the array is then stored in the new area of memory

import sys

data = []
n = 50
for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)     # size in bytes
    data.append(None)
    print("Length: {0:3d}, Size in bytes: {1:4d}".format(a, b))

# When the list goes from 56 -> 88 bytes it grows 32 bytes
# In a 64-bit machine, each memory address has 8 bytes. So the next allocation
# should be capable of storing 4 more elements.
# That is why we see 4 printouts at 88 bytes

# When the list goes from 88 -> 120 bytes it grows by 32 bytes
# it grows 32 bytes again, which means 4 more elements can be stored before growing again

# From 120 -> 184 bytes it grows by 64 bytes
# we can now store 8 more elements at 8 bytes each

# From 184 -> 256 we see a jump of 72 bytes
# now we can store 9 elements at 9 bytes each

# From 256 -> 336 we see a jump of 80 bytes

# From 336 -> 424 ..... etc

# More or less; after the first few appends, list grow by 8 bytes + however many bytes you allocated
# in the previous growth step

