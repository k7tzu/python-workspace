from implementation import *

def recherche_arbre(arbre, valeur):
    if arbre is None:
        return False
    if arbre.data == valeur:
        return True
    return recherche_arbre(arbre.left, valeur) or recherche_arbre(arbre.right, valeur)

print(recherche_arbre(a, 3))