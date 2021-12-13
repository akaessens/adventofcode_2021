import numpy as np

with open('input.txt', 'r') as inputfile:
    lines = inputfile.readlines()

counter = np.zeros(10, dtype = int)

for line in lines:
    in_out = line.split("|")
    out = in_out[1]
    for number in out.split():
         
        if len(number) == 2:
            counter[1] += 1
        elif len(number) == 3:
            counter[7] += 1
        elif len(number) == 4:
            counter[4] += 1
        elif len(number) == 7:
            counter[8] += 1

print ("Sum of 1,3,7,8:", sum (counter))