def renverse(mot):
    """
    >>> renverse('')
    ''
    >>> renverse('abc')
    'cba'
    >>> renverse('informatique')
    'euqitamrofni'
    """
    result = ''
    for i in range(len(mot)):
        result = mot[i] + result
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()