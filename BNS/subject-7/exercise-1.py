def gb_vers_entier(tab):
    """
    >>> gb_vers_entier([])
    0
    >>> gb_vers_entier([True])
    1
    >>> gb_vers_entier([True, False, True, False, False, True, True])
    83
    >>> gb_vers_entier([True, False, False, False, False, False, True, False])
    130
    """
    entier = 0
    puissance = len(tab) - 1
    for bit in tab:
        if bit:
            entier += 2 ** puissance
        puissance -= 1
    return entier

if __name__ == "__main__":
    import doctest
    doctest.testmod()
