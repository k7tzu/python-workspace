def detection_cycle(g:Graphe, en_cours:list, termines:list, depart:str) -> bool:
    if depart in  ... :
        return False
    elif depart in ... :
        return True
    else:
        ... .append(depart)
        for voisin in g.voisins(depart):
            if ... :
                return True
        ... .append(depart)
        return False

def detection_cycle(g: Graphe, en_cours: list, termines: list, depart: str) -> bool:
    if depart in termines:
        return False
    elif depart in en_cours:
        return True
    else:
        en_cours.append(depart)
        for voisin in g.voisins(depart):
            if detection_cycle(g, en_cours, termines, voisin):
                return True
        en_cours.remove(depart)
        termines.append(depart)
        return False
