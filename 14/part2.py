import numpy as np
from collections import Counter
import math

inputfile = open('input.txt', 'r')
lines = inputfile.readlines()

polymer = lines[0].strip()
ins = []
for line in lines[2:]:
    split = line.strip().split(" -> ")
    ins.append(split)

print(polymer)


# init counter
count_pair = dict()
count_char = dict()

for i in ins:
    count_char[i[1]] = 0

    count_pair[i[0]] = 0
    for char in range(len(polymer) - 1 ):
        if polymer[char:char+2] == i[0]:
            count_pair[i[0]] += 1

#print ("Step 0", count_pair)

steps = 40
for step in range(1,steps+1):
    count_after = count_pair.copy()

    for i in ins:
        num = count_pair[i[0]]
        count_after[i[0]] -= num

        fst = i[0][0] + i[1]
        snd = i[1] + i[0][1]

        count_after[fst] += num
        count_after[snd] += num

    count_pair = count_after
    #print("Step", step, count_pair)

for pair in count_pair:
    num = count_pair[pair]
    fst = pair[0]
    snd = pair[1]

    count_char[fst] += num/2
    count_char[snd] += num/2

counter = Counter(count_char)

most_common = counter.most_common()

print(math.ceil(most_common[0][1] - most_common[-1][1]))
