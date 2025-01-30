def insertion_abr(a, cle): 
    if a is None:
        return (None, cle, None)
    elif cle > a[1]:
        return (a[0], a[1], insertion_abr(a[2], cle))
    elif cle < a[1]:
        return (insertion_abr(a[0], cle), a[1], a[2])
    return a

def empaqueter(liste_masses, c):
    n = len(liste_masses)
    nb_boites = 0
    boites = [ 0 for _ in range(n) ]
    for masse in liste_masses: 
        i = 0
        while i < nb_boites and boites[i] + masse > c: 
            i = i + 1
        if i == nb_boites:
            nb_boites = nb_boites + 1
        boites[i] = boites[i] + masse 
    return nb_boites


