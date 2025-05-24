def binaire(a):
    """
    >>> binaire(0)
    '0'
    >>> binaire(77)
    '1001101'
    """
    if a == 0:
        return '0'
    bin_a = ''
    while a != 0:
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a

if __name__ == '__main__':
    import doctest
    doctest.testmod()