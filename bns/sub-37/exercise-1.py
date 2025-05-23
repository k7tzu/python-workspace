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
    result = 0
    power = len(tab) - 1
    for bit in tab:
        if bit == True:
            result += 2 ** power
        power -= 1
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()