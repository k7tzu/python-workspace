def recherche(elt, tab):
    """
    >>> recherche(1, [2, 3, 4]) # renvoie None
    >>> recherche(1, [10, 12, 1, 56])
    2
    >>> recherche(1, [1, 0, 42, 7])
    0
    >>> recherche(1, [1, 50, 1])
    2
    >>> recherche(1, [8, 1, 10, 1, 7, 1, 8])
    5
    """
    index = None
    for i in range(len(tab)):
        if tab[i] == elt:
            index = i
    return index

if __name__ == '__main__':
    import doctest
    doctest.testmod()