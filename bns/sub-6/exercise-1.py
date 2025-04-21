def liste_puissances(a, n):
    """
    >>> liste_puissances(3, 5)
    [3, 9, 27, 81, 243]
    >>> liste_puissances(-2, 4)
    [-2, 4, -8, 16]
    """
    result = [a]
    for _ in range(n-1):
        result.append(result[-1] * a)
    return result

def liste_puissances_borne(a, borne):
    """
    >>> liste_puissances_borne(2, 16)
    [2, 4, 8]
    >>> liste_puissances_borne(2, 17)
    [2, 4, 8, 16]
    >>> liste_puissances_borne(5, 5)
    []
    """
    result = []
    x = a
    while x < borne:
        result.append(x)
        x = x * a
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()