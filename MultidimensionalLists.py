# Consider storing data from two distinct values, such as rolling two dice and storing all
# possible results (Sample space)
# each die has six sides, so a 6x6 matrix would suffice to store the sample space
from random import randint

dice = list(range(1, 7))
two_dice_sample_space = [[(i, j) for i in dice] for j in dice]
for i in range(len(dice)):
    print(two_dice_sample_space[i])

# print(two_dice_sample_space[1][5][1])

for i in range(10):
    print(two_dice_sample_space[randint(0, 5)][randint(0, 5)])


