img=[[20, 34, 254, 145, 6], [23, 124, 237, 225, 69],
     [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]

def nombre_lignes(image):
    """
    >>> nombre_lignes(img)
    4
    """
    return len(image)

def nombre_colonnes(image):
    """
    >>> nombre_colonnes(img)
    5
    """
    return len(image[0])

def negatif(image):
    """
    >>> negatif(img)
    [[235, 221, 1, 110, 249], [232, 131, 18, 30, 186], [58, 81, 48, 230, 168], [0, 255, 231, 58, 66]]
    """
    nouvelle_image = [[0 for k in range(nombre_colonnes(image))]
        for i in range(nombre_lignes(image))]
    
    for i in range(nombre_lignes(image)):
        for j in range(nombre_colonnes(image)):
            nouvelle_image[i][j] = 255 - image[i][j]
    return nouvelle_image

def binaire(image, seuil):
    """
    >>> binaire(img,120)
    [[0, 0, 255, 255, 0], [0, 255, 255, 255, 0], [255, 255, 255, 0, 0], [255, 0, 0, 255, 255]]
    """
    nouvelle_image = [[0] * nombre_colonnes(image)
                       for i in range(nombre_lignes(image))]
    
    for i in range(nombre_lignes(image)):
        for j in range(nombre_colonnes(image)):
            if image[i][j] < seuil:
                nouvelle_image[i][j] = 0
            else:
                nouvelle_image[i][j] = 255
    return nouvelle_image

if __name__ == '__main__':
    import doctest
    doctest.testmod()