def a_doublon(tab):
    """
    >>> a_doublon([])
    False
    >>> a_doublon([1])
    False
    >>> a_doublon([1, 2, 4, 6, 6])
    True
    >>> a_doublon([2, 5, 7, 7, 7, 9])
    True
    >>> a_doublon([0, 2, 3])
    False
    """
    for i in range(len(tab)-1):
        if tab[i] == tab[i+1]:
            return True
    return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()