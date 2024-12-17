from implementation import *

def nb_feuilles(arbre):
    if arbre is None:
        return 0
    if arbre.left is None and arbre.right is None:
        return 1
    return nb_feuilles(arbre.left) + nb_feuilles(arbre.right)

print(nb_feuilles(a))