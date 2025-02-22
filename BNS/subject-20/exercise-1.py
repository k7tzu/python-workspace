from random import randint as rn

def lancer(n):
    result = []
    for _ in range(n):
        result.append(rn(1, 6))
    return result

def paire_6(tab):
    counter = 0
    for val in tab:
        if val == 6:
            counter += 1
    if counter >= 2:
        return True
    return False

lancer1 = lancer(5)
print(lancer1)
print(paire_6(lancer1))