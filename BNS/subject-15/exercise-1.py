def moyenne(tab):
    """
    >>> moyenne([1.0])
    1.0
    >>> moyenne([1.0, 2.0, 4.0])
    2.3333333333333335
    """
    #return sum(tab) / len(tab)
    somme = 0
    for v in tab:
        somme += v
    return somme / len(tab)

if __name__ == "__main__":
    import doctest
    doctest.testmod()