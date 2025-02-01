def inverse_chaine(chaine):
    '''
    Retourne la chaine inversée

    >>> inverse_chaine('bac')
    'cab'
    '''
    resultat = ""
    for caractere in chaine:
        resultat = caractere + resultat
    return resultat

def est_palindrome(chaine):
    '''
    Renvoie un booléen indiquant si la chaine ch
    est un palindrome

    >>> est_palindrome('NSI')
    False
    >>> est_palindrome('ISN-NSI')
    True
    '''
    inverse = inverse_chaine(chaine)
    return chaine == inverse

def est_nbre_palindrome(nbre):
    """
    >>> est_nbre_palindrome(214312)
    False
    >>> est_nbre_palindrome(213312)
    True
    """
    chaine = str(nbre)
    return est_palindrome(chaine)

if __name__ == "__main__":
    import doctest
    doctest.testmod()