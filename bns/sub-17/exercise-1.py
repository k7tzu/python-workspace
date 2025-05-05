class Noeud:
    def __init__(self, etiquette, gauche, droit):
        self.v = etiquette
        self.gauche = gauche
        self.droit = droit

a = Noeud(1, Noeud(4, None, None),
             Noeud(0, None,
                      Noeud(7, None, None)))

def taille(a):
    """
    >>> taille(a)
    4
    >>> taille(None)
    0
    """
    if a is None:
        return 0
    return 1 + taille(a.gauche) + taille(a.droit)

def hauteur(a):
    """
    >>> hauteur(a)
    2
    >>> hauteur(None)
    -1
    """
    if a is None:
        return -1
    return 1 + max(hauteur(a.gauche), hauteur(a.droit))

if __name__ == '__main__':
    import doctest
    doctest.testmod()