def somme_max(tab):
    """
    >>> somme_max([1, 2, 3, 4, 5])
    15
    >>> somme_max([1, 2, -3, 4, 5])
    9
    >>> somme_max([1, 2, -2, 4, 5])
    10
    >>> somme_max([1, -2, 3, 10, -4, 7, 2, -5])
    18
    """
    n = len(tab)
    sommes_max = [0]*n
    sommes_max[0] = tab[0]
    # on calcule la plus grande somme se terminant en i
    for i in range(1,n):
        if sommes_max[i-1] + tab[i] > tab[i]:
            sommes_max[i] = sommes_max[i-1] + tab[i]
        else:
            sommes_max[i] = tab[i]
    # on en déduit la plus grande somme de celles-ci
    maximum = 0
    for i in range(1, n):
        if sommes_max[i] > sommes_max[maximum]:
            maximum = i
    return sommes_max[maximum]

if __name__ == '__main__':
    import doctest
    doctest.testmod()