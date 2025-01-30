def recherche_min(tab):
    indice_min = 0
    for i in range(len(tab)):
        if tab[i] < tab[indice_min]:
            indice_min = i
    return indice_min

print(recherche_min([5]))
print(recherche_min([2, 4, 1]))
print(recherche_min([5, 3, 2, 2, 4]))
print(recherche_min([-1, -2, -3, -3]))

def separe(tab):
    '''Separe les 0 et les 1 dans le tableau tab'''
    gauche = 0
    droite = len(tab) - 1 
    while gauche < droite:
        if tab[gauche] == 0 :
            gauche = gauche + 1 
        else :
            tab[gauche] = tab[droite] 
            tab[droite] = 1 
            droite = droite - 1 
    return tab

