def selection(tab):
    for i in range(len(tab)):
        min_index = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[min_index]:
                min_index = j
        tab[i], tab[min_index] = tab[min_index], tab[i]
    return tab

tab = [64, 25, 12, 22, 11]
print(selection(tab))