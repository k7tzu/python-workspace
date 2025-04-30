def recherche(elt, tab):
    """
    >>> recherche(1, [2, 3, 4]) # renvoie None
    >>> recherche(1, [10, 12, 1, 56])
    2
    >>> recherche(50, [1, 50, 1])
    1
    >>> recherche(15, [8, 9, 10, 15])
    3
    """
    for i in range(len(tab)):
        if tab[i] == elt:
            return i
    return None

if __name__ == '__main__':
    import doctest
    doctest.testmod()