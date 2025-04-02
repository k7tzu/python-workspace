def detection_cycle(g:Graphe, en_cours:list, termines:list, depart:str) -> bool:
    if depart in termines:
        return False
    elif depart in en_cours:
        return True
    else:
        en_cours.append(depart)
        for voisin in g.voisins(depart):
            if detection_cycle(g, en_cours, termines, voisins):
                return True
        termines.append(depart)
        return False


class Graphe:
    def __init__(self, sommets, aretes):
        """
        sommets : liste des sommets du graphe.
        aretes : liste de tuples représentant les arêtes (u, v).
        """
        self.sommets = sommets
        self.adjacence = {s: [] for s in sommets}
        for u, v in aretes:
            self.adjacence[u].append(v)
            self.adjacence[v].append(u)  # Supposons un graphe non orienté

    def voisins(self, sommet):
        """Retourne la liste des voisins du sommet."""
        return self.adjacence[sommet]

    def est_connexe(self) -> bool:
        """Détermine si le graphe est connexe."""
        if not self.sommets:
            return True  # Un graphe vide est considéré comme connexe
        
        visite = set()
        pile = [self.sommets[0]]
        
        while pile:
            courant = pile.pop()
            if courant not in visite:
                visite.add(courant)
                for voisin in self.voisins(courant):
                    if voisin not in visite:
                        pile.append(voisin)
        
        return len(visite) == len(self.sommets)
