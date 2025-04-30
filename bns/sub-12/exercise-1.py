def fusion(tab1, tab2):
    """
    >>> fusion([3, 5], [2, 5])
    [2, 3, 5, 5]
    >>> fusion([-2, 4], [-3, 5, 10])
    [-3, -2, 4, 5, 10]
    >>> fusion([4], [2, 6])
    [2, 4, 6]
    >>> fusion([], [])
    []
    >>> fusion([1, 2, 3], [])
    [1, 2, 3]
    """
    tab = []
    while tab1 and tab2:
        if tab1[0] < tab2[0]:
            tab.append(tab1.pop(0))
        else:
            tab.append(tab2.pop(0))
    return tab + tab1 + tab2

if __name__ == '__main__':
    import doctest
    doctest.testmod()