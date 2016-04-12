import math

"""FORMULE DE GEOMETRIE DE BASE SUR DES RECTANGLE"""

def RectAir(a, b):
    return a*b

def RectPerimetre(a, b):
    return a+b

def RectDiagonale(a, b):
    diagonale = math.sqrt(a*a + b*b)
    return diagonale


"""SI TU VOIS CE COM C'EST QUE SA MARCHE"""

rectangle = (1, 1)
a, b = rectangle
print(RectAir(a, b))
print(RectDiagonale(a, b))


