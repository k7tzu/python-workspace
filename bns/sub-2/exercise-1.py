def max_et_indice(tab):
    """
    >>> max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8])
    (9, 3)
    >>> max_et_indice([-2])
    (-2, 0)
    >>> max_et_indice([-1, -1, 3, 3, 3])
    (3, 2)
    >>> max_et_indice([1, 1, 1, 1])
    (1, 0)
    """
    max_value = tab[0]
    max_index = 0
    for i in range(len(tab)):
        if tab[i] > max_value:
            max_value = tab[i]
            max_index = i
    return (max_value, max_index)

if __name__ == '__main__':
    import doctest
    doctest.testmod()