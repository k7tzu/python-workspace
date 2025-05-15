def voisinage(n, ligne, colonne):
    voisins = []
    for dl in range(-1, 2):
        for dc in range(-1, 2):
            l = ligne + dl
            c = colonne + dc
            if (l, c) != (ligne, colonne) \
                    and 0 <= l < n and 0 <= c < n:
                voisins.append((l, c))
    return voisins

def incremente_voisins(grille, ligne, colonne):
    voisins = voisinage(len(grille), ligne, colonne)
    for l, c in voisins:
        if grille[l][c] != -1:
            grille[l][c] += 1

def genere_grille(bombes):
    n = len(bombes)
    grille = [[0 for colonne in range(n)] for ligne in range(n)]
    for ligne, colonne in bombes:
        grille[ligne][colonne] = -1
        incremente_voisins(grille, ligne, colonne)
    return grille

print(genere_grille([(1, 1), (2, 4), (3, 1), (3, 3), (4, 4)]))