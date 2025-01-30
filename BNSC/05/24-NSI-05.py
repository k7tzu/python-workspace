def est_un_ordre(tab):
    '''
    Renvoie True si tab est de longueur n et contient tous les
    entiers de 1 à n, False sinon
    '''
    n = len(tab)
    vus = []
    for x in tab:
        if x < 1 or x > n or x in vus:
            return False
        vus.append(x)
    return True


def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de point de rupture de ordre qui représente
    un ordre de gènes de chromosome
    '''
    # on vérifie que ordre est un ordre de gènes
    assert est_un_ordre(ordre) == True, "ce n'est pas un ordre"
    n = len(ordre)
    nb = 0
    if ordre[0] != 1: # le premier n'est pas 1
        nb = nb + 1
    i = 0
    while i < len(ordre)-1:
        if ordre[i+1] - ordre[i] not in [-1, 1]: # l'écart n'est pas 1
            nb = nb + 1
        i = i + 1
    if ordre[i] != n: # le dernier n'est pas n
        nb = nb + 1
    return nb


def max_et_indice(tab):
    indice=0
    maxi=tab[0]
    for i in range (len(tab)):
        if tab[i]>maxi:
            indice=i
            maxi=tab[i]
    return maxi,indice
