import numpy as np
from collections import Counter

inputfile = open('input.txt', 'r')
lines = inputfile.readlines()

connections = []
paths = set()

for line in lines:
    nodes = line.strip().split("-")
    connections.append((nodes[0], nodes[1]))

#print(connections)

def get_neighbors(node):
    neighbors = []
    for conn in connections:
        if node == conn[0]:
            neighbors.append(conn[1])
        elif node == conn[1]:
            neighbors.append(conn[0])
    return neighbors

def search(node, visited, path, small_cave_available):

    path.append(node)

    if node == "end":
        paths.add("-".join(path))
        print (path)
        return

    second_option = False
    if node.islower():
        if node == "start":
            visited.add(node)
        elif small_cave_available == True:
            visited_small = visited.copy()
            second_option = True
            visited.add(node)
        else:
            visited.add(node)

    neighbors = get_neighbors(node)

    for neighbor in neighbors:
        if neighbor not in visited:
            #print ("node", node, "neighbor", neighbor, "path", path, "visited", visited)
            search(neighbor, visited.copy(), path.copy(), small_cave_available)

            if second_option:
                search(neighbor, visited_small.copy(), path.copy(), False)


search("start", set(), [], True)

print("len paths", len(paths))
