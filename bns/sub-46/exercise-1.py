def compte_occurrences(x, tab):
    """
    >>> compte_occurrences(5, [])
    0
    >>> compte_occurrences(5, [-2, 3, 1, 5, 3, 7, 4])
    1
    >>> compte_occurrences('a', ['a','b','c','a','d','e','a'])
    3
    """
    counter = 0
    for v in tab:
        if v == x:
            counter += 1
    return counter

if __name__ == '__main__':
    import doctest
    doctest.testmod()