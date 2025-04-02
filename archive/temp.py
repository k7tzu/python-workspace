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
    
    def est_connexe(self):
        depart = g.liste_sommets[0]
        parcours = BFS(g, depart)
        return len(g.liste_sommets) == len(parcours)
    
    def est_eulerien(self):
        total = 0
        for elt in g.liste_sommets:
            if len(g.voisins(elt)) % 2 == 1:
                total += 1
        return est_connexe(g) and (total == 0 or total == 2)
                
g1 = Graphe(['A', 'B', 'C', 'D', 'E'])
g1.ajoute_arete('A', 'B')
g1.ajoute_arete('A', 'C')
g1.ajoute_arete('A', 'E')
g1.ajoute_arete('A', 'D')
g1.ajoute_arete('C', 'E')
g1.ajoute_arete('E', 'D')


def BFS(g, depart):
        traites = []
        decouverts = [depart]
        en_attente = [depart]
        while en_attente != []:
            sommet = en_attente.pop(0)
            voisins = g.voisins(sommet)
            for voisin in voisins:
                if voisin not in decouverts:
                    decouverts.append(voisin)
                    en_attente.append(voisin)
            traites.append(sommet)
        return traites
    
print(BFS(g1, 'A'))
