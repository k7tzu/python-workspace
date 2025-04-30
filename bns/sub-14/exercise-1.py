from random import randint #means no doctest :sad:

def lancer(n):
    result = []
    for i in range(n):
        result.append(randint(1, 6))
    return result

def paire_6(tab):
    counter = 0
    for v in tab:
        if v == 6:
            counter += 1
    return counter >= 2

lancer1 = lancer(5)
print(lancer1)
print(paire_6(lancer1))