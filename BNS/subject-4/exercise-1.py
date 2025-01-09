def recherche(tab, n):
    """
    >>> recherche([5, 3],1) # renvoie None
    >>> recherche([2,4],2)
    0
    >>> recherche([2,3,5,2,4],2)
    3
    """
    index = None
    for i in range(len(tab)):
        if n == tab[i]:
            index = i
    return index

if __name__ == "__main__":
    import doctest
    doctest.testmod()