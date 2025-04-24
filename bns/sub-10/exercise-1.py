def recherche(tab, n):
    """
    >>> recherche([2, 3, 4, 5, 6], 5)
    3
    >>> recherche([2, 3, 4, 6, 7], 5) # renvoie None
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if n == tab[m]:
            return m
        elif n > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return None

if __name__ == '__main__':
    import doctest
    doctest.testmod()