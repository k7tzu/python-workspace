def ajoute_dictionnaires(d1, d2):
    """
    >>> ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11})
    {1: 5, 2: 16, 3: 11}
    >>> ajoute_dictionnaires({}, {2: 9, 3: 11})
    {2: 9, 3: 11}
    >>> ajoute_dictionnaires({1: 5, 2: 7}, {})
    {1: 5, 2: 7}
    """
    d = {}
    for key in d1:
        d[key] = d1[key]
    for key in d2:
        if key in d:
            d[key] += d2[key]
        else:
            d[key] = d2[key]
    return d

if __name__ == '__main__':
    import doctest
    doctest.testmod()