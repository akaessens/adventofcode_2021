import numpy as np
from treelib import Node, Tree
import math

with open("input.txt") as file:
    lines = file.readlines()

class Value(object):
    def __init__(self, val):
        self.val = val

node_idx = 0
tree = Tree()

def create_tree(tree, number, parent_node):
    global node_idx
    name = node_idx
    if type(number) == int:
        tree.create_node(name, name, parent = parent_node, data=Value(number))
        node_idx += 1
    elif type(number) == list:
        tree.create_node(name, name, parent = parent_node, data=Value(number))
        node_idx += 1
        for nr in number:
            create_tree(tree, nr, name)
    
    return number

def get_prev_leaf(left_child, tree):
    leaves = tree.leaves()
    for node_id in reversed(range(0, left_child.identifier)):
        node = tree.get_node(node_id)
        if node in leaves:
            return node

    return None

def get_next_leaf(right_child, tree):
    leaves = tree.leaves()
    for node_id in range(right_child.identifier+1, len(tree.nodes)):
        node = tree.get_node(node_id)
        if node in leaves:
            return node

    return None

def update_after_explode(tree):

    new_node_id = 0
    for node_id in list(tree.expand_tree(mode=Tree.DEPTH)):
        node = tree.get_node(node_id)
        node.tag = new_node_id
        tree.update_node(node_id, identifier=new_node_id)

        new_node_id += 1
    pass

    for node_id in reversed(list(tree.expand_tree(mode=Tree.ZIGZAG))):
        children = tree.children(node_id)

        node = tree.get_node(node_id)
        if len(children) == 2: 
            node.data.val = [children[0].data.val, children[1].data.val]

def update_after_split(tree):

    new_node_id = len(tree.nodes)-1
    for node_id in reversed(list(tree.expand_tree(mode=Tree.DEPTH))):
        node = tree.get_node(node_id)
        node.tag = new_node_id
        tree.update_node(node_id, identifier=new_node_id)

        new_node_id -= 1
    pass

    for node_id in reversed(list(tree.expand_tree(mode=Tree.ZIGZAG))):
        children = tree.children(node_id)

        node = tree.get_node(node_id)
        if len(children) == 2: 
            node.data.val = [children[0].data.val, children[1].data.val]
    
def explode(tree):
    for i in range(len(tree)):
        node = tree.get_node(i)
        depth = tree.depth(node)

        if depth == 4 and node not in tree.leaves():
            #print ("node", node, "depth", depth)
            children = tree.children(node.identifier)

            # explode children calues to neighboring leaves
            prev_leaf = get_prev_leaf(children[0], tree)
            next_leaf = get_next_leaf(children[1], tree)
            if prev_leaf:
                prev_leaf.data.val = prev_leaf.data.val + children[0].data.val
            
            if next_leaf:
                next_leaf.data.val = next_leaf.data.val + children[1].data.val

            # remove children and set data to 0
            node.data.val = 0
            tree.remove_node(children[0].identifier)
            tree.remove_node(children[1].identifier)

            update_after_explode(tree)
            #print("after explode", tree.get_node(0).data.val)
            return True

    return False

def split(tree):
    for i in range(len(tree)):
        node = tree.get_node(i)
        val = node.data.val
        if type(val) == int and val  >= 10:
            tree.create_node(-2, -2, data=Value(math.floor(val/2)), parent = node) # left one
            tree.create_node(-1, -1, data=Value(math.ceil(val/2)), parent = node) # right one

            update_after_split(tree)
            #print("after split", tree.get_node(0).data.val)
            return True

    return False

def reduc(tree):
    more = True

    while more:
        more = explode(tree)
        if (more):
            continue
        more = split(tree)
        
def add(tree, number):
    
    root = tree.get_node(0)
    root_children = tree.children(root.identifier)
    # insert below root
    tree.create_node(-1, -1, data=Value(root.data.val), parent = 0)

    for child in root_children:
        tree.move_node(child.identifier, -1)

    update_after_split(tree)
    global node_idx
    node_idx = len(tree)
    create_tree(tree, number, tree.get_node(0).identifier)
    update_after_split(tree)

def magnitude(node):

    magn = 0
    children = tree.children(node.identifier)

    if (children):
        left = children[0].data.val
        if type(left) == int:
            magn += left * 3
        else:
            magn += 3 * magnitude(children[0])

        right = children[1].data.val
        if type(right) == int:
            magn += right * 2
        else:
            magn += 2 * magnitude(children[1])

    return magn
        

mags = []
for line1 in lines:
    for line2 in lines:
        if line1 == line2:
            continue

        number = eval("[" + line1 + "," + line2 + "]")
        create_tree(tree, number, None)
        reduc(tree)

        mags.append(magnitude(tree.get_node(0)))
        del tree
        node_idx = 0
        tree = Tree()


print("Magnitude max ", max(mags))