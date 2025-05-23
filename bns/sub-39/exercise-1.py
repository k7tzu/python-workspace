def moyenne(tab):
    """
    >>> moyenne([5,3,8])
    5.333333333333333
    >>> moyenne([1,2,3,4,5,6,7,8,9,10])
    5.5
    >>> moyenne([])
    'Le tableau passé en paramètre est vide.'
    """
    if len(tab) == 0:
        return 'Le tableau passé en paramètre est vide.'
    valeurs = 0
    for v in tab:
        valeurs += v
    return valeurs / len(tab)

if __name__ == '__main__':
    import doctest
    doctest.testmod()