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
    pos = [yoff, 0]
    print("velo", velo)
    while not data[pos[0], pos[1]]:  # while not in target

        pos[0] += velo[0]  # y
        pos[1] += velo[1]  # x

        velo[0] -= 1  # gravity
        velo[1] = max(velo[1]-1, 0)  # drag
        #print ("step", step, "pos y =", pos[0]-yoff, "x =", pos[1], "velo", velo)

        if pos[0] < 0 or pos[1] < 0 or pos[1] > size-1 or pos[0] > size-1:
            print("out of bounds")
            return False

    print("Hit target at y =", pos[0]-yoff, "x =", pos[1])
    return True


velos = []
for xvelo in range(-500, 500):
    for yvelo in range(-500, 500):
        if (aim([yvelo, xvelo])):
            velos.append((yvelo, xvelo))

print("len", len(velos))
