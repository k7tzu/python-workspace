def liste_puissances(a,n):
    puissances = [a]
    for i in range(n-1):
        puissances.append(puissances[-1] * a)
    return puissances

def liste_puissances_borne(a, borne):
    lst = []
    val = a
    while val < borne:
        lst.append(val)
        val = val * a
    return lst

dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
        "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
        "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
        "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
        "W": 23, "X": 24, "Y": 25, "Z": 26}


def codes_parfait(mot):
    # mot est une chaîne de caractères (en lettres majuscules)
    code_concatene = ""
    code_additionne = 0
    for c in mot:
        code_concatene = code_concatene + str(dico[c])
        code_additionne = code_additionne + dico[c]
    code_concatene = int(code_concatene)
    mot_est_parfait = code_concatene % code_additionne == 0
    return code_additionne, code_concatene, mot_est_parfait


