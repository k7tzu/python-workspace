# -- Imports

from implementation import *
from queue import Queue

# -- Exercise 1

def level_order_traversal(tree):
    if tree is None:
        return []
    
    file = Queue()
    file.put(tree)
    result = []

    while not file.empty():
        current = file.get()
        if current:
            result.append(current.data)
            file.put(current.left)
            file.put(current.right)
        return result
    
# -- Exercise 2

def insert_bst(tree, value):
    if tree is None:
        return Tree(value)
    else:
        v = tree.data
        if value <= v:
            tree.left = insert_bst(tree.left, value)
        else:
            tree.right = insert_bst(tree.right, value)
        return tree