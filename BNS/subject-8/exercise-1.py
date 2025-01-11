def delta(liste):
    """
    >>> delta([1000, 800, 802, 1000, 1003])
    [1000, -200, 2, 198, 3]
    >>> delta([42])
    [42]
    """
    result = [liste[0]]
    for i in range(1, len(liste)):
        result.append(liste[i] - liste[i - 1])
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()