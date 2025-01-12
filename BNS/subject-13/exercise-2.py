def insere(tab, a):
    """
    Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le
    nouveau tableau.

    >>> insere([1, 2, 4, 5], 3)
    [1, 2, 3, 4, 5]
    >>> insere([1, 2, 7, 12, 14, 25], 30)
    [1, 2, 7, 12, 14, 25, 30]
    >>> insere([2, 3, 4], 1)
    [1, 2, 3, 4]
    >>> insere([], 1)
    [1]
    """
    tab_a = [ a ] + tab

    i = 0
    while i < len(tab) and a > tab[i]:
        tab_a[i] = tab[i]
        tab_a[i+1] = a
        i = i + 1
    return tab_a

if __name__ == "__main__":
    import doctest
    doctest.testmod()