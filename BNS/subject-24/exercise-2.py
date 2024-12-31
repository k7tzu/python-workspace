def somme_max(tab):
    n = len(tab)
    sommes_max = [0] * n
    sommes_max[0] = tab[0]
    # on calcule la plus grande somme se terminant en i
    for i in range(1, n):
        if sommes_max[i - 1] + tab[i] > tab[i]:
            sommes_max[i] = sommes_max[i - 1] + tab[i]
        else:
            sommes_max[i] = tab[i]
    # on en déduit la plus grande somme de celles-ci
    maximum = sommes_max[0]
    for i in range(1, n):
        if sommes_max[i] > maximum:
            maximum = sommes_max[i]
    return maximum
