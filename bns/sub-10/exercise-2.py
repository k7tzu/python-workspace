alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    """
    >>> cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4)
    'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'
    >>> cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5)
    'BONJOUR A TOUS. VIVE LA MATIERE NSI !'
    """
    resultat = ''
    for c in message:
        if 'A' <= c and c <= 'Z':
            indice = (position_alphabet(c) + decalage) % 26
            resultat = resultat + alphabet[indice]
        else:
            resultat = resultat + c
    return resultat

if __name__ == '__main__':
    import doctest
    doctest.testmod()