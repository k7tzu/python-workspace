def ecriture_binaire_entier_positif(n):
    if n == 0:
        return '0' 
    bin_n = '' 
    while n != 0 : 
        bin_n = str(n % 2) + bin_n 
        n = n //2
    return bin_n
 
print(ecriture_binaire_entier_positif(0))
print(ecriture_binaire_entier_positif(2))
print(ecriture_binaire_entier_positif(105))

def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i] 
    tab[i] = tab[j] 
    tab[j] = temp 

def tri_bulles(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri à bulles.'''
    n = len(tab)
    for i in range(n-1, -1, -1): 
        for j in range(i): 
            if tab[j] > tab[j+1]: 
                echange(tab, j, j+1) 


tab = []
tri_bulles(tab)
print(tab)
tab2 = [9, 3, 7, 2, 3, 1, 6]
tri_bulles(tab2)
print(tab2)
tab3 = [9, 7, 4, 3]
tri_bulles(tab3)
print(tab3)