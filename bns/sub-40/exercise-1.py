def recherche_indices_classement(elt, tab):
    r1 = []
    r2 = []
    r3 = []
    for value in tab:
        if value < elt:
            r1.append(value)
        elif value == elt:
            r2.append(value)
        else:
            r3.append(value)
    return (r1, r2, r3)

print(recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0]))