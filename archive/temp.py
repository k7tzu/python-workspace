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

# Recherche du plus court chemin
def recherche_chemin(g, depart, arrivee):
    '''
    Parcours en largeur du graphe g en partant du sommet depart,
    qui s'arrête dès que le sommet arrivee est atteint.
    Renvoie alors le chemin du depart vers arrivee.
    '''
    traites = []
    decouverts = [depart]
    en_attente = [depart]
    parent = {}
    while en_attente != [] :
        sommet = en_attente.pop(0)
        voisins = g.voisins(sommet)
        for voisin in voisins:
            if voisin not in decouverts:
                decouverts.append(voisin)
                en_attente.append(voisin)
                parent[voisin] = sommet
                if voisin == arrivee:
                    return remonte_chemin(depart, arrivee, parent)
        traites.append(sommet)
    return "non trouvé"  


def remonte_chemin(depart, arrivee, parent):
    sommet = arrivee
    chemin = arrivee
    while sommet != depart:
        sommet = parent[sommet]
        chemin = sommet + chemin
    return chemin

print(recherche_chemin(g, 'E', 'H'))
