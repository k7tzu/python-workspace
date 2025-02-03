import re

# Création et gestion des files
def creer_file():
    return []

def est_vide(f):
    return len(f) == 0

def enfiler(f, elt):
    f.append(elt)

def defiler(f):
    if not est_vide(f):
        return f.pop(0)
    return None  # Renvoie None si la file est vide

# 5.a Vérification si une file est vide
def test_est_vide():
    f1 = ["bac", "nsi", "2023", "file"]
    print("5.a - est_vide(f1) :", est_vide(f1))  # False

# 5.b Évolution de la file après un défilement
def test_defiler():
    f1 = ["bac", "nsi", "2023", "file"]
    defiler(f1)
    print("5.b - f1 après defiler :", f1)  # ['nsi', '2023', 'file']

# 5.c Ajout d'éléments dans une nouvelle file
def test_enfiler():
    f2 = creer_file()
    for elt in ["castor", "python", "poule"]:
        enfiler(f2, elt)
    print("5.c - f2 après ajout :", f2)  # ['castor', 'python', 'poule']

# 6. Fonction longueur
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

# 7. Fonction est_valide
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

# Exécution des tests
test_est_vide()
test_defiler()
test_enfiler()
test_longueur()
test_est_valide()
