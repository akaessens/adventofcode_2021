import numpy as np

inputfile = open('input.txt', 'r')
lines = inputfile.readlines()

xlen = 100
ylen = 100
data = np.zeros((ylen+1, xlen+1), dtype=np.uint)


for x, line in enumerate(lines):
    for y, char in enumerate(line):
        if char == "\n":
            continue
        data[x, y] = int(char)

# padding
data[ylen, :] = 9
data[:, xlen] = 9

pos = []

for iy, ix in np.ndindex((ylen,xlen)):
    top = data[iy-1, ix]
    below = data[iy+1, ix]
    right = data[iy, ix+1]
    left = data[iy, ix-1]
    value = data[iy, ix]
    if value < top and value < below and value < left and value < right:
        pos.append([iy, ix])

print(data)

sum_risk = 0
for p in pos:
    print (p, data[p[0], p[1]])
    sum_risk += data[p[0], p[1]] + 1

print ("Sum", sum_risk)