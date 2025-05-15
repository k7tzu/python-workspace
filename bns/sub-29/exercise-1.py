def selection_enclos(animaux, num_enclos):
    """
    >>> selection_enclos(animaux, 5)
    [{'nom': 'Titine', 'espece': 'chat', 'age': 2, 'enclos': 5}, {'nom': 'Mirza', 'espece': 'chat', 'age': 6, 'enclos': 5}]
    >>> selection_enclos(animaux, 2)
    [{'nom': 'Medor', 'espece': 'chien', 'age': 5, 'enclos': 2}]
    >>> selection_enclos(animaux, 7)
    []
    """
    result = []
    for dico in animaux:
        if dico['enclos'] == num_enclos:
            result.append(dico)
    return result

animaux = [ {'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2},
            {'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},
            {'nom':'Tom', 'espece':'chat', 'age':7, 'enclos':4},
            {'nom':'Belle', 'espece':'chien', 'age':6, 'enclos':3},
            {'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]


if __name__ == '__main__':
    import doctest
    doctest.testmod()