def nbr_occurences(chaine):
    """
    >>> nbr_occurences('Hello World!')
    {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'W': 1, 'r': 1, 'd': 1, '!': 1}
    """
    dico = {}
    for c in chaine:
        if c not in dico:
            dico[c] = 1
        else:
            dico[c] += 1
    return dico

if __name__ == '__main__':
    import doctest
    doctest.testmod()