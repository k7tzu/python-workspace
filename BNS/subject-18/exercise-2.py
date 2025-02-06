def chercher(tab, x, i, j):
    '''Renvoie l'indice de x dans tab, si x est dans tab,
    None sinon.
    On suppose que tab est trié dans l'ordre croissant.

    >>> chercher([1, 5, 6, 6, 9, 12], 7, 0, 10)
    >>> chercher([1, 5, 6, 6, 9, 12], 7, 0, 5)
    >>> chercher([1, 5, 6, 6, 9, 12], 9, 0, 5)
    4
    >>> chercher([1, 5, 6, 6, 9, 12], 6, 0, 5)
    2
    '''
    if i > j:
        return None
    m = (i + j) // 2
    if tab[m] < x:
        return chercher(tab, x, m+1, j)
    elif tab[m] > x:
        return chercher(tab, x, i, m-1)
    else:
        return m
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()