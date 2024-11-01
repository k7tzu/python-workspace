print("Sarah on top <3")

def ajoute_dictionnaires(d1, d2):
    result = {}
    for key in d1:
        if key in d2:
            result[key] = d1[key] + d2[key]
        else:
            result[key] = d1[key]
    for key in d2:
        if key not in result:
            result[key] = d2[key]
    return result

print(ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}))