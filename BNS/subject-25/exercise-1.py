def recherche_min(tab):
    """
    >>> recherche_min([5])
    0
    >>> recherche_min([2, 4, 1])
    2
    >>> recherche_min([5, 3, 2, 2, 4])
    2
    >>> recherche_min([-1, -2, -3, -3])
    2
    """
    min_index = 0
    for i in range(1, len(tab)):
        if tab[i] < tab[min_index]:
            min_index = i
    return min_index

if __name__ == '__main__':
    import doctest
    doctest.testmod()