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

for iy, ix in np.ndindex((ylen, xlen)):
    top = data[iy-1, ix]
    below = data[iy+1, ix]
    right = data[iy, ix+1]
    left = data[iy, ix-1]
    value = data[iy, ix]
    if value < top and value < below and value < left and value < right:
        pos.append([iy, ix])

print(data)

basins = []


def bfs(data, start):  # function for BFS
    visited = [start]
    queue = [start]

    while queue:          # Creating loop to visit each node
        curr = queue.pop(0)

        iy = curr[0]
        ix = curr[1]
        
        top = [iy-1, ix]
        below = [iy+1, ix]
        right = [iy, ix+1]
        left = [iy, ix-1]

        for n in [top, below, right, left]:
            if n not in visited and data[n[0], n[1]] != 9:
                visited.append(n)
                queue.append(n)
    
    return visited


for p in pos:
    print(p, data[p[0], p[1]])

    visited = bfs(data, p)

    basins.append(len(visited))

basins.sort()
print(basins[-3:], np.prod(basins[-3:]))