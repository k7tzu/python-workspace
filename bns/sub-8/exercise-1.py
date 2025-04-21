def maximum_tableau(tab):
    """
    >>> maximum_tableau([98, 12, 104, 23, 131, 9])
    131
    >>> maximum_tableau([-27, 24, -3, 15])
    24
    """
    result = 0
    for val in tab:
        if val > result:
            result = val
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()