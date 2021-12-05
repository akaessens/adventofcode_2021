import numpy as np
import re
inputfile = open('testinput.txt', 'r')
lines = inputfile.readlines()

line_map = np.zeros((10,10))

for line in lines:
    num = list(map(int, re.findall('\d+', line)))
    
    x1 = min([num[0], num[2]])
    y1 = min([num[1], num[3]])
    x2 = max([num[0], num[2]])
    y2 = max([num[1], num[3]])

    if x1 != x2 and y1 != y2:  # ignore those lines
        continue

    line_map[y1:y2+1, x1:x2+1] += 1
    
count = np.count_nonzero(line_map >= 2)

print("count", count)

inputfile.close()