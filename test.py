import math

"""FORMULE DE GEOMETRIE DE BASE SUR DES RECTANGLE"""

def RectAir(a, b):
    return a*b

def RectPerimetre(a, b):
    return a+b

def RectDiagonale(a, b):
    diagonale = math.sqrt(a*a + b*b)
    return diagonale

"""FORMULE DE GEOMETRIE DE BASE SUR DES CARRES"""

def CarrAir(a):
    return a*a

def CarrPerimetre(a):
    return a*4

def CarrDiagonale(a):
    diagonale = math.sqrt(a*a)
    return diagonale


rectangle = (1, 1)
a, b = rectangle
print(RectAir(a, b))
print(RectDiagonale(a, b))

carre = 1
a = carre
print(CarrAir(a))
print(CarrDiagonale(a))

