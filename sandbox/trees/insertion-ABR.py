from implementation import *

def insertion(arbre, valeur):
    if arbre is None:
        return Arbre(valeur)
    else:
        v = arbre.data
        if valeur <= v:
            arbre.left = insertion(arbre.left, valeur)
        else:
            arbre.right = insertion(arbre.right, valeur)
        return arbre