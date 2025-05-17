def occurrences(caractere, chaine):
    """
    >>> occurrences('e', "sciences")
    2
    >>> occurrences('i',"mississippi")
    4
    >>> occurrences('a',"mississippi")
    0
    """
    counter = 0
    for char in chaine:
        if char == caractere:
            counter += 1
    return counter


if __name__ == '__main__':
    import doctest
    doctest.testmod()