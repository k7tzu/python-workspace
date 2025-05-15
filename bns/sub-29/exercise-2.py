def trouver_intrus(tab, g, d):
    """
    >>> trouver_intrus([3, 3, 3, 9, 9, 9, 1, 1, 1, 7, 2, 2, 2, 4, 4, 4, 8, 8, 8], 0, 18)
    7
    >>> trouver_intrus([8, 5, 5, 5, 9, 9, 9, 18, 18, 18, 3, 3, 3], 0, 12)
    8
    >>> trouver_intrus([5, 5, 5, 1, 1, 1, 0, 0, 0, 6, 6, 6, 3, 8, 8, 8], 0, 15)
    3
    """
    if g == d:
        return tab[g]
    else:
        nombre_de_triplets = (d - g) // 3
        indice = g + 3 * (nombre_de_triplets // 2)
        if tab[indice] != tab[indice + 1]:
            return trouver_intrus(tab, g, indice)
        else:
            return trouver_intrus(tab, indice + 3, d)
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()