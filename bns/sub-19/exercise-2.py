def separe(tab):
    """
    >>> separe([1, 0, 1, 0, 1, 0, 1, 0])
    [0, 0, 0, 0, 1, 1, 1, 1]
    >>> separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0])
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    """
    gauche = 0
    droite = len(tab) - 1
    while gauche < droite:
        if tab[gauche] == 0:
            gauche += 1
        else:
            tab[gauche] = tab[droite]
            tab[droite] = 1
            droite -=1
    return tab

if __name__ == '__main__':
    import doctest
    doctest.testmod()