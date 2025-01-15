def binaire(a):
    '''convertit un nombre entier a en sa representation
    binaire sous forme de chaine de caractères.

    >>> binaire(83)
    '1010011'
    >>> binaire(6)
    '110'
    >>> binaire(127)
    '1111111'
    >>> binaire(0)
    '0'
    '''
    if a == 0:
        return '0'
    bin_a = ''
    while a != 0:
        bin_a = str(a % 2) + bin_a
        a //= 2
    return bin_a

if __name__ == "__main__":
    import doctest
    doctest.testmod()