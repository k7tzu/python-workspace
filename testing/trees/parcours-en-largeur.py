from implementation import *
from queue import Queue

def BFS(arbre):
    if arbre is None:
        return []
    
    file = Queue()
    file.put(arbre)
    result = []

    while not file.empty():
        current = file.get()
        if current:
            result.append(current.data)
            file.put(current.left)
            file.put(current.right)

    return result

print(BFS(a))