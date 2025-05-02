def moyenne(notes):
    """
    >>> moyenne([(15.0,2),(9.0,1),(12.0,3)])
    12.5
    """
    res = 0
    co = 0
    for note in notes:
        res += (note[0] * note[1])
        co += note[1]
    return res / co

if __name__ == '__main__':
    import doctest
    doctest.testmod()