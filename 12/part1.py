import numpy as np

inputfile = open('input.txt', 'r')
lines = inputfile.readlines()

connections = []
paths = []

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


def search(node, visited, path):

    path.append(node)

    if node == "end":
        paths.append(path)
        return

    if node.islower():
        visited.add(node)

    neighbors = get_neighbors(node)

    for neighbor in neighbors:

        if neighbor not in visited:
            #print ("node", node, "neighbor", neighbor, "path", path, "visited", visited)
            search(neighbor, visited.copy(), path.copy())


search("start", set(), [])

print("len paths", len(paths))
#print(paths)
