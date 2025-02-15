def ecriture_binaire_entier_positif(n):
    """
    >>> ecriture_binaire_entier_positif(0)
    '0'
    >>> ecriture_binaire_entier_positif(2)
    '10'
    >>> ecriture_binaire_entier_positif(105)
    '1101001'
    """
    if n == 0:
        return '0'
    result = ''
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()