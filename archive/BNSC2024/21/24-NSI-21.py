def recherche_motif(motif, texte):
    sol = []
    i = 0
    while i <= len(texte) - len(motif):
        j = 0
        while j < len(motif) and motif[j] == texte[j+i]:
            j += 1
        if j == len(motif):
            sol.append(i)
        i += 1
    return sol

adj = [[1, 2], [0, 3], [0], [1], [5], [4]]
print(recherche_motif("ab",""))
print(recherche_motif("ab", "cdcdcdcd"))
print(recherche_motif("ab", "abracadabra"))
print(recherche_motif("ab", "abracadabraab"))

def parcours(adj, x, acc):
    '''Réalise un parcours en profondeur récursif
    du graphe donné par les listes d'adjacence adj
    depuis le sommet x en accumulant les sommets
    rencontrés dans acc'''
    if x not in acc:
        acc.append(x)
        for y in adj[x]:
            parcours(adj, y, acc)

def accessibles(adj, x):
    '''Renvoie la liste des sommets accessibles dans le
    graphe donné par les listes d'adjacence adj depuis
    le sommet x.'''
    acc = []
    parcours(adj, x, acc)
    return acc

print(accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 0))
print(accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 4))