from implementation import *

def taille_arbre(arbre):
    if arbre is None:
        return 0
    return 1 + taille_arbre(arbre.left) + taille_arbre(arbre.right)

def hauteur_arbre(arbre):
    if arbre is None:
        return 0
    return 1 + max(hauteur_arbre(arbre.left), hauteur_arbre(arbre.right))

print(taille_arbre(a))
print(hauteur_arbre(a))