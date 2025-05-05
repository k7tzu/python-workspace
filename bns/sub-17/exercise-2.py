def ajoute(indice, element, tab):
    """
    >>> ajoute(1, 4, [7, 8, 9])
    [7, 4, 8, 9]
    >>> ajoute(3, 4, [7, 8, 9])
    [7, 8, 9, 4]
    >>> ajoute(0, 4, [7, 8, 9])
    [4, 7, 8, 9]
    """
    nbre_elts = len(tab)
    tab_ins = [0] * (nbre_elts + 1)
    for i in range(indice):
        tab_ins[i] = tab[i]
    tab_ins[indice] = element
    for i in range(indice + 1, nbre_elts + 1):
        tab_ins[i] = tab[i-1]
    return tab_ins

if __name__ == '__main__':
    import doctest
    doctest.testmod()