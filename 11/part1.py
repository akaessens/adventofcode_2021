import numpy as np

inputfile = open('input.txt', 'r')
lines = inputfile.readlines()

xlen = 10
ylen = 10
data = np.zeros((ylen, xlen), dtype=np.uint)


for x, line in enumerate(lines):
    for y, char in enumerate(line):
        if char == "\n":
            continue
        data[x, y] = int(char)




def get_adjacent_indices(i, j, m, n):
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i-1,j))
    if i+1 < m:
        adjacent_indices.append((i+1,j))
    if j > 0:
        adjacent_indices.append((i,j-1))
    if j+1 < n:
        adjacent_indices.append((i,j+1))
    if i > 0 and j > 0:
        adjacent_indices.append((i-1,j-1))
    if i > 0 and j+1 < n:
        adjacent_indices.append((i-1,j+1))
    if i+1 < m and j+1 < n:
        adjacent_indices.append((i+1,j+1))
    if i+1 < m and j > 0:
        adjacent_indices.append((i+1,j-1))
    
    return adjacent_indices

print (data)

flash_counter = 0

for step in range(1,101):
    flashing = set()
    # init new flashing
    new_flashing = set()
    for iy, ix in np.ndindex(data.shape):
        data[iy, ix] += 1
        if data[iy, ix] > 9:
            new_flashing.add((iy, ix))


    while len(new_flashing) > 0:
        flashing.update(new_flashing)
        this_run_flashing = new_flashing.copy()
        new_flashing.clear()
        for fl in this_run_flashing:
            adj = get_adjacent_indices(fl[0], fl[1], ylen, xlen)
            for ad in adj:
                data[ad[0], ad[1]] += 1
                if data[ad[0], ad[1]] > 9:
                    new_flashing.add((ad[0], ad[1]))
                pass

        new_flashing -= flashing
        pass

    for iy, ix in np.ndindex(data.shape):
        if data[iy, ix] > 9:
            data[iy, ix] = 0

    print("STEP", step)
    print (data)

    flash_counter += len(flashing)

print("flash_counter", flash_counter)

