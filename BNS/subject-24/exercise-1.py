from queue import Queue

def parcours_largeur(arbre):
    if arbre is None:
        return []
    
    file = Queue()
    file.put(arbre)
    result = []

    while not file.empty():
        current = file.get()
        if current is not None:
            g, x, d = current
            result.append(x)
            file.put(g)
            file.put(d)
    return result

arbre = (
    ((None, 1, None), 2, (None, 3, None)),
    4,
    ((None, 5, None), 6, (None, 7, None))
)
print(parcours_largeur(arbre))