import numpy as np
import heapq

inputfile = open('input.txt', 'r')
lines = inputfile.readlines()

xlen = 100
ylen = 100
data = np.zeros((ylen, xlen), dtype=np.uint32)


for x, line in enumerate(lines):
    for y, char in enumerate(line):
        if char == "\n":
            continue
        data[x, y] = int(char)

print(data)

for i in range (4):
    data = np.append(data, data[-ylen:,:]+1, 0)
    data = np.append(data, data[:,-xlen:]+1, 1)

xlen = data.shape[1]
ylen = data.shape[0]

for y in range (ylen):
    for x in range(xlen):

        if data[y,x] > 9:
            data[y,x] = data[y,x] % 9


def get_adjacent_indices(i, j, m, n):
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i-1, j))
    if i+1 < m:
        adjacent_indices.append((i+1, j))
    if j > 0:
        adjacent_indices.append((i, j-1))
    if j+1 < n:
        adjacent_indices.append((i, j+1))
    return adjacent_indices

def heuristic(pos):
    # definitively underestimating: 1.0 * (...) -> takes too long
    # hopefully underestimating:    1.5 * (...) -> works
    # def. not underestimating:     2.0 * (...) -> incorrect with test input
    return 1.5 * (xlen+ylen-2-pos[0]-pos[1])

def treeSearch():

    # init
    startState = ( heuristic((0,0)), 0, 0, 0)
    fringe = [startState]
    heapq.heapify(fringe) # faster than sorting manually
    visited = set()  # set of already visited states to avoid loops

    while (fringe):

        state = heapq.heappop(fringe)  # get next element
        visited.add(state[2:4])

        if state[2:4] == (ylen-1, xlen-1):
            return state

        for child in get_adjacent_indices(state[2], state[3], xlen, ylen):
            if (child[0], child[1]) not in visited:
                cost = state[1] + data[child[0], child[1]]
                heur = heuristic(child)
                new_state = ( heur + cost, cost, child[0], child[1] )

                heapq.heappush(fringe, new_state )

        print("state", state)
        #print ("fringe ", fringe)
        print("visited ", len(visited))

    print("Failure, no path found !")
    return []


path = treeSearch()

print(path)
