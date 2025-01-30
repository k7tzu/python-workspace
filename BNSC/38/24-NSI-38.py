def indices_maxi(tab):
    val_max = tab[0]
    ind_max = []
    for i in range(len(tab)):
        if tab[i] > val_max:
            val_max = tab[i]
            ind_max = [i]
        elif tab[i] == val_max:
            ind_max.append(i)
    return (val_max, ind_max)
print(indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
print(indices_maxi([7]))


def renverse(pile):
    pile_inverse = [] 
    while pile != []:
        pile_inverse.append(pile.pop()) 
    return pile_inverse 


def positifs(pile):
    pile_positifs = [] 
    while pile != []:
        elt = pile.pop() 
        if elt >= 0: 
            pile_positifs.append(elt)
    return renverse(pile_positifs) 


