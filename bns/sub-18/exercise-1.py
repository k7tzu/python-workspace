def moyenne(tab):
    """
    >>> moyenne([1])
    1.0
    >>> moyenne([1, 2, 3, 4, 5, 6, 7])
    4.0
    >>> moyenne([1, 2])
    1.5
    """
    add = 0
    for value in tab:
        add += value
    res = add / len(tab)
    return float(res)

if __name__ == '__main__':
    import doctest
    doctest.testmod()