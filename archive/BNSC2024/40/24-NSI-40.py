def selection_enclos(animaux, num_enclos):
    table = []
    for animal in animaux:
        if animal['enclos'] == num_enclos:
            table.append(animal)
    return table

def trouver_intrus(tab, g, d):
    if g == d:
        return tab[g]
    else:
        nombre_de_triplets = (d - g) // 3
        indice = g + 3 * (nombre_de_triplets // 2)
        if tab[indice] != tab[indice + 1] :
            return trouver_intrus(tab, g, indice)
        else:
            return trouver_intrus(tab, indice + 3, d)


