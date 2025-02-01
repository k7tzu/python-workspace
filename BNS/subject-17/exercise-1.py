def nb_repetitions(elt, tab):
    """
    >>> nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5])
    3
    >>> nb_repetitions('A', ['B', 'A', 'B', 'A', 'R'])
    2
    >>> nb_repetitions(12, [1, '!', 7, 21, 36, 44])
    0
    """
    counter = 0
    for value in tab:
        if value == elt:
            counter += 1
    return counter

if __name__ == "__main__":
    import doctest
    doctest.testmod()