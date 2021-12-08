# Manually spawning the fish is too slow, even when parallelized on all CPUs
# https://github.com/barrychocolate/Advent_of_code_2021/blob/main/day_6/day_6.ipynb
import numpy as np
from collections import Counter

fish = np.loadtxt("input.txt", dtype='int', delimiter=',')

days = 256
count = Counter(fish)

for day in range(days):
    mothers = count[0]
    count[0] = count[1]
    count[1] = count[2]
    count[2] = count[3]
    count[3] = count[4]
    count[4] = count[5]
    count[5] = count[6]
    count[6] = count[7]
    count[6] = count[6] + mothers
    count[7] = count[8]
    count[8] = mothers

# return the sum of all fish
print("Sum of", sum(count.values()))
