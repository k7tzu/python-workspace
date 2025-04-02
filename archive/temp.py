class Graphe:
    def __init__(self, liste_sommets):
        self.liste_sommets = []
        self.adjacents = {}
        
    def ajoute_arete(self, sommetA, sommetB):
        if sommetA not in self.liste_sommets:
            self.liste_sommets.append(sommetA)
            self.adjacents[sommetA] = []
        if sommetB not in self.liste_sommets:
            self.liste_sommets.append(sommetB)
            self.adjacents[sommetB] = []
        self.adjacents[sommetA].append(sommetB)
        self.adjacents[sommetB].append(sommetA)
        
    def voisins(self, sommet):
        return self.adjacents.get(sommet, [])
        
g = Graphe(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
g.ajoute_arete('A', 'B')
g.ajoute_arete('A', 'C')
g.ajoute_arete('B', 'D')
g.ajoute_arete('D', 'C')
g.ajoute_arete('B', 'E')
g.ajoute_arete('D', 'E')
g.ajoute_arete('E', 'F')
g.ajoute_arete('E', 'G')
g.ajoute_arete('F', 'G')
g.ajoute_arete('G', 'H')

def DFSrec(g, traites, actuel):
    traites.append(actuel)
    for voisin in g.voisins(actuel):
        if voisin not in traites:
            DFSrec(g, traites, voisin)
    return traites

print(DFSrec(g, [], 'A'))
