def empaqueter(liste_masses, c):
    """
    >>> empaqueter([1, 2, 3, 4, 5], 10)
    2
    >>> empaqueter([1, 2, 3, 4, 5], 5)
    4
    >>> empaqueter([7, 6, 3, 4, 8, 5, 9, 2], 11)
    5
    """
    n = len(liste_masses)
    nb_boites = 0
    boites = [0 for _ in range(n)]
    for masse in liste_masses:
        i = 0
        while i < nb_boites and boites[i] + masse > c:
            i = i + 1
        if i == nb_boites:
            nb_boites += 1
        boites[i] = boites[i] + masse
    return nb_boites

if __name__ == '__main__':
    import doctest
    doctest.testmod()