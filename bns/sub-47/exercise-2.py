def echange(tab, i, j):
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp

def tri_selection(tab):
    N = len(tab)
    for k in range(N):
        imin = k
        for i in range(k+1, N):
            if tab[i] < tab[imin]:
                imin = i
        echange(tab, k, imin)

tab = [41, 55, 21, 18, 12, 6, 25]
tri_selection(tab)
print(tab)