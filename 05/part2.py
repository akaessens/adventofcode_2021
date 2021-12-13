import numpy as np
import re
inputfile = open('input.txt', 'r')
lines = inputfile.readlines()

line_map = np.zeros((1000,1000))

for line in lines:
    num = list(map(int, re.findall('\d+', line)))
    
    x1 = num[0]
    y1 = num[1]
    x2 = num[2]
    y2 = num[3]

    if x1 != x2 and y1 != y2: # diagonal
        print("line" , x1, y1, x2, y2)
        if (x1 < x2):
            y_off = 0
            for x in range (x1,x2+1,1):
                print("x", x, "y", y1+y_off)
                line_map[y1+y_off, x] += 1

                if y2 < y1:
                    y_off -= 1
                else:
                    y_off += 1
        else:
            y_off = 0
            for x in range (x1,x2-1,-1):
                print("x", x, "y", y1+y_off)
                line_map[y1+y_off, x] += 1

                if y2 < y1:
                    y_off -= 1
                else:
                    y_off += 1


    else:
        x1 = min([num[0], num[2]])
        y1 = min([num[1], num[3]])
        x2 = max([num[0], num[2]])
        y2 = max([num[1], num[3]])
        line_map[y1:y2+1, x1:x2+1] += 1
    
count = np.count_nonzero(line_map >= 2)

print("count", count)

inputfile.close()