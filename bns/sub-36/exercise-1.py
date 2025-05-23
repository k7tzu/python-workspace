def nombre_de_mots(phrase):
    """
    >>> nombre_de_mots('Cet exercice est simple.')
    4
    >>> nombre_de_mots('Le point d exclamation est séparé !')
    6
    >>> nombre_de_mots('Combien de mots y a t il dans cette phrase ?')
    10
    >>> nombre_de_mots('Fin.')
    1
    """
    counter = 0
    for char in phrase:
        if char == ' ' or char == '.':
            counter += 1
    return counter

if __name__ == '__main__':
    import doctest
    doctest.testmod()