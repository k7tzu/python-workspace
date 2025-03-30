def recherche(tab, n):
    ind_debut = 0
    ind_fin = len(tab)-1
    while ind_debut <= ind_fin:
        m = (ind_debut + ind_fin)//2
        if tab[m]: == n:
            return m
        elif tab[m] < n :
            ind_debut = m + 1
        else:
            ind_fin = m - 1
    return None

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    '''Renvoie la position de la lettre dans l'alphabet'''
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    '''Renvoie le message codé par la méthode de César
    pour le decalage donné'''
    resultat = ''
    for c in message: 
        if 'A' <= c and c <= 'Z':
            indice = (c) % 26 
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = c 
    return resultat



