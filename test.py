import math

"""FORMULE DE GEOMETRIE DE BASE SUR DES RECTANGLE"""

def RectAir(a, b):
    return a*b

def RectPerimetre(a, b):
    return (a+b)*2

def RectDiagonale(a, b):
    diagonale = math.sqrt(a*a + b*b)
    return diagonale

def RectSePresenter(a, b):
    print("je suis un rectangle de longueur: ", a, "et de largeur: ", b)


rectangle = (1, 1)
a, b = rectangle
RectSePresenter(a, b)
print(RectAir(a, b))
print(RectDiagonale(a, b))


