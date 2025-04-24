arbre = ( ( (None, 1, None), 2, (None, 3, None) ), 4, ( (None, 5, None), 6, (None, 7, None) ) )

def parcours_largeur(arbre):
    """
    >>> parcours_largeur(arbre)
    [4, 2, 6, 1, 3, 5, 7]
    """
    if arbre is None:
        return []
    result = []
    file = [arbre]
    while file:
        noeud = file.pop(0)
        gauche, x, droite = noeud
        result.append(x)
        if gauche is not None:
            file.append(gauche)
        if droite is not None:
            file.append(droite)
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()