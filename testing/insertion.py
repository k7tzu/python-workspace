def insertion(tab):
    if len(tab) <= 1:
        return tab, "Déjà trié."
    
    for i in range(1, len(tab)):
        key = tab[i]
        j = i - 1
        while j >= 0 and key < tab[j]:
            tab[j+1] = tab[j]
            j -= 1
        tab[j+1] = key
    return tab

arr = [12, 11, 13, 5, 6]
print(insertion(arr))