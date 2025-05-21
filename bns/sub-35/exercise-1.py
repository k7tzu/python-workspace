def max_dico(dico):
    """
    >>> max_dico({ 'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50 })
    ('Ada', 201)
    >>> max_dico({ 'Alan': 222, 'Ada': 201, 'Eve': 222, 'Tim': 50 })
    ('Alan', 222)
    """
    max_key = ''
    max_value = 0
    for key in dico:
        if dico[key] > max_value:
            max_value = dico[key]
            max_key = key
    return (max_key, max_value)

if __name__ == '__main__':
    import doctest
    doctest.testmod()