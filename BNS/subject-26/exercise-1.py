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
    for key, value in d1.items():
        d[key] = value

    for key, value in d2.items():
        if key in d:
            d[key] += value
        else:
            d[key] = value
    return d

if __name__ == "__main__":
    import doctest
    doctest.testmod()