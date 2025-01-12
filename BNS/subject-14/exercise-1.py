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

    min_value = tab[0]
    max_value = tab[0]
    for i in range(len(tab)):
        if tab[i] < min_value:
            min_value = tab[i]
        
        if tab[i] > max_value:
            max_value = tab[i]
    result['min'] = min_value
    result['max'] = max_value
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()