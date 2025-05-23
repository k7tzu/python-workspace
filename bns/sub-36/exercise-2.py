class Noeud:
    def __init__(self, etiquette):
        self.etiquette = etiquette
        self.gauche = None
        self.droit = None

    def inserer(self, cle):
        """
        >>> arbre.gauche.etiquette
        3
        >>> arbre.droit.etiquette
        9
        >>> arbre.gauche.gauche.etiquette
        1
        >>> arbre.gauche.droit.etiquette
        6
        """
        if cle < self.etiquette:
            if self.gauche != None:
                self.gauche.inserer(cle)
            else:
                self.gauche = Noeud(cle)
        else:
            if self.droit != None:
                self.droit.inserer(cle)
            else:
                self.droit = Noeud(cle)

arbre = Noeud(7)
for cle in (3, 9, 1, 6):
    arbre.inserer(cle)

if __name__ == '__main__':
    import doctest
    doctest.testmod()