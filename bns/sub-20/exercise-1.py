def min_et_max(tab):
    """
    >>> min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1])
    {'min': -2, 'max': 9}
    >>> min_et_max([0, 1, 2, 3])
    {'min': 0, 'max': 3}
    >>> min_et_max([3])
    {'min': 3, 'max': 3}
    >>> min_et_max([1, 3, 2, 1, 3])
    {'min': 1, 'max': 3}
    >>> min_et_max([-1, -1, -1, -1, -1])
    {'min': -1, 'max': -1}
    """
    result = {}
    result['min'] = tab[0]
    result['max'] = tab[0]
    for i in range(1, len(tab)):
        if tab[i] > result['max']:
            result['max'] = tab[i]
        if tab[i] < result['min']:
            result['min'] = tab[i]
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()