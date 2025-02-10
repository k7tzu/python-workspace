# Answer for Q1 is --> [4, 2, 5, 8]
# Answer for Q2.1 is --> 4
# Answer for Q2.2 is --> 1
# Answer for Q3 is --> [8, 4, 2, 5]

def creer_pile_vide():
    return []

def est_vide(p):
    return p == []

def empiler(p, x):
    p.append(x)

def depiler(p):
    assert not est_vide(p)
    return p.pop()

P = creer_pile_vide()
empiler(P, 8)
empiler(P, 5)
empiler(P, 2)
empiler(P, 4)

def hauteur_pile(P):
    Q = creer_pile_vide()
    n = 0
    while not(est_vide(P)):
        n += 1
        x = depiler(P)
        empiler(Q, x)
    while not est_vide(Q):
        x = depiler(Q)
        empiler(P, x)
    return n

print(hauteur_pile(P)) 

def max_pile(P, i):
    Q = creer_pile_vide()
    max_value = None
    max_position = 0

    for position in range(1, i + 1):
        if est_vide(P):
            break
        
        x = depiler(P)
        empiler(Q, x)

        if max_value is None or x > max_value:
            max_value = x
            max_position = position

    while not est_vide(Q):
        empiler(P, depiler(Q))

    return max_position

print(max_pile(P, 2))

def retourner(P, j):
    Q = creer_pile_vide()
    R = creer_pile_vide()

    for _ in range(j):
        empiler(Q, depiler(P))

    while not est_vide(Q):
        empiler(R, depiler(Q))
    
    while not est_vide(R):
        empiler(P, depiler(R))

retourner(P, 3)
print(P)

def tri_crepes(P):
    n = hauteur_pile(P)  # Get the height of the stack

    for i in range(n, 1, -1):  # We sort from the bottom to the top
        max_pos = max_pile(P, i)  # Step 1: Find the max position in the first `i` elements

        if max_pos != i:  # If the max is not already in the correct place
            retourner(P, max_pos)  # Step 2: Bring the max element to the top
            retourner(P, i)  # Step 3: Move it to its correct position
