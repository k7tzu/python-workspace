def moyenne(tab):
    """
    >>> moyenne([5,3,8])
    5.333333333333333
    >>> moyenne([1,2,3,4,5,6,7,8,9,10])
    5.5
    >>> moyenne([])
    """
    value = 0
    if len(tab) != 0:
        for v in tab:
            value += v
        return value / len(tab)
    return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()