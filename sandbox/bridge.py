import re

def creer_file():
    return []

def est_vide(f):
    return len(f) == 0

def enfiler(f, elt):
    f.append(elt)

def defiler(f):
    if not est_vide(f):
        return f.pop(0)
    return None  

def test_est_vide():
    f1 = ["bac", "nsi", "2023", "file"]
    print("5.a - est_vide(f1) :", est_vide(f1))  # False

def test_defiler():
    f1 = ["bac", "nsi", "2023", "file"]
    defiler(f1)
    print("5.b - f1 après defiler :", f1)  # ['nsi', '2023', 'file']

def test_enfiler():
    f2 = creer_file()
    for elt in ["castor", "python", "poule"]:
        enfiler(f2, elt)
    print("5.c - f2 après ajout :", f2)  # ['castor', 'python', 'poule']

def longueur(f):
    resultat = 0
    g = creer_file()
    
    while not est_vide(f):
        elt = defiler(f)
        resultat += 1
        enfiler(g, elt)  # Sauvegarde
    
    while not est_vide(g):
        enfiler(f, defiler(g))  # Restauration
    
    return resultat

def test_longueur():
    f = ["apple", "banana", "cherry"]
    print("6 - Longueur de f :", longueur(f))  # 3

def est_valide(mot):
    if len(mot) < 8:  
        return False  
    if not any(c.isupper() for c in mot):  
        return False  
    if not any(c.isdigit() for c in mot):  
        return False  
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", mot):  
        return False  
    return True  

def test_est_valide():
    mots = ["Test1234", "Password!", "Abc1@", "Secure@123"]
    for mot in mots:
        print(f"7 - {mot} est valide ? {est_valide(mot)}")

test_est_vide()
test_defiler()
test_enfiler()
test_longueur()
test_est_valide()
