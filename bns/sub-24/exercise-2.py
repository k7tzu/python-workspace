class Noeud:
    def __init__(self, etiquette, gauche, droit):
        self.etiquette = etiquette
        self.gauche = gauche
        self.droit = droit
    
def parcours(arbre, liste):
    if arbre != None:
        parcours(arbre.gauche, liste)
        liste.append(arbre.etiquette)
        parcours(arbre.droit, liste)
    return liste

def insere(arbre, cle):
    if arbre == None:
        return Noeud(cle, None, None)
    else:
        if cle < arbre.etiquette:
            arbre.gauche = insere(arbre.gauche, cle)
        else:
            arbre.droit = insere(arbre.droit, cle)
        return arbre
    
a = Noeud(5, Noeud(2, None, Noeud(3, None, None)), Noeud(7, None, None))
a = insere(a, 1)
a = insere(a, 4)
a = insere(a, 6)
a = insere(a, 8)

print(parcours(a, []))