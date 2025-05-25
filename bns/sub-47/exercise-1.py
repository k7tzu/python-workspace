def taille(arbre, lettre):
    """
    >>> taille(a, 'F')
    9
    >>> taille(a, 'B')
    5
    >>> taille(a, 'I')
    2
    """
    if lettre == '':
        return 0
    return 1 + taille(arbre, arbre[lettre][0]) + taille(arbre, arbre[lettre][1])

a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], \
     'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], \
     'H':['','']}

if __name__ == '__main__':
    import doctest
    doctest.testmod()