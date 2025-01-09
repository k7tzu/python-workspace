def correspond(mot, mot_a_trous):
    """
    >>> correspond('INFORMATIQUE', 'INFO*MA*IQUE')
    True
    >>> correspond('AUTOMATIQUE', 'INFO*MA*IQUE')
    False
    >>> correspond('STOP', 'S*')
    False
    >>> correspond('AUTO', '*UT*')
    True
    """
    if len(mot) != len(mot_a_trous):
        return False
    for i in range(len(mot)):
        if mot[i] != mot_a_trous[i] and mot_a_trous[i] != "*":
            return False
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()