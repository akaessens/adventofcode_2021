import numpy as np
from collections import Counter

inputfile = open('input.txt', 'r')
lines = inputfile.readlines()

polymer = lines[0].strip()

ins = []

for line in lines[2:]:
    split = line.strip().split(" -> ")
    split.append(split[0][0] + split[1].lower() + split[0][1])

    ins.append(split)

print(polymer)

steps = 10
for step in range(1,steps+1):

    oldpolymer = ""
    while oldpolymer != polymer: # needed for cases like BBB -> BnBnB
        oldpolymer = polymer
        for i in ins:
            polymer = polymer.replace(i[0], i[2])

    polymer = polymer.upper()
    print("step", step, "length", len(polymer))

counter = Counter(polymer)

most_common = counter.most_common()

print(most_common[0][1] - most_common[-1][1])