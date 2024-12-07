def taille(arbre, lettre):
    if arbre[lettre][0] == '' and arbre[lettre][1] == '':
        return 1
    
    gauche = taille(arbre, arbre[lettre][0]) if arbre[lettre][0] != '' else 0
    droit = taille(arbre, arbre[lettre][1]) if arbre[lettre][1] != '' else 0

    return 1 + gauche + droit

a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], \
     'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], 'H':['','']}
print(taille(a, 'F'))
print(taille(a, 'B'))
print(taille(a, 'I'))