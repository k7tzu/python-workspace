def multiplication(n1, n2):
    """
    >>> multiplication(3, 5)
    15
    >>> multiplication(-4, -8)
    32
    >>> multiplication(-2, 6)
    -12
    >>> multiplication(-2, 0)
    0
    """
    result = 0
    if n1 < 0:
        return -multiplication(-n1, n2)
    if n2 < 0:
        return -multiplication(n1, -n2)
    for _ in range(n2):
        result += n1
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()