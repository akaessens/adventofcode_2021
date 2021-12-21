import numpy as np
import re

size = 100000
yoff = int(size/2)

with open("input.txt", "r") as file:
    line = file.read()
    print(line)
    target = list(map(int, re.findall(r'-*\d+', line)))

data = np.zeros((size, size), dtype=np.uint8)

data[target[2]+yoff:target[3]+yoff+1, target[0]:target[1]+1] = 1


def aim(velo):
    max_y = 0
    pos = [yoff, 0]
    print("velo", velo)
    while not data[pos[0], pos[1]]:  # while not in target

        pos[0] += velo[0]  # y
        pos[1] += velo[1]  # x

        max_y = max(pos[0]-yoff, max_y)

        velo[0] -= 1  # gravity
        velo[1] = max(velo[1]-1, 0)  # drag
        #print ("step", step, "pos y =", pos[0]-yoff, "x =", pos[1], "velo", velo)

        if pos[0] < 0 or pos[1] < 0 or pos[1] > size-1 or pos[0] > size-1:
            print("out of bounds")
            return 0

    print("Hit target at y =", pos[0]-yoff, "x =", pos[1])
    return max_y


max_velo_y = [0, 0, 0]
for xvelo in range(1, 20):
    for yvelo in range(1, 500):
        max_y = aim([yvelo, xvelo])

        if max_y > max_velo_y[2]:
            max_velo_y = [yvelo, xvelo, max_y]

print("max_velo_y", max_velo_y)
