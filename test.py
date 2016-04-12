import math

"""FORMULE DE GEOMETRIE DE BASE SUR DES RECTANGLE"""

def RectAir(a, b):
    return a*b

def RectPerimetre(a, b):
    return (a+b)*2

def RectDiagonale(a, b):
    diagonale = math.sqrt(a*a + b*b)
    return diagonale

<<<<<<< HEAD
def RectSePresenter(a, b):
    print("je suis un rectangle de longueur: ", a, "et de largeur: ", b)
=======
"""FORMULE DE GEOMETRIE DE BASE SUR DES CARRES"""

def CarrAir(a):
    return a*a

def CarrPerimetre(a):
    return a*4

def CarrDiagonale(a):
    diagonale = math.sqrt(a*a)
    return diagonale
>>>>>>> refs/remotes/origin/carré


rectangle = (1, 1)
a, b = rectangle
RectSePresenter(a, b)
print(RectAir(a, b))
print(RectDiagonale(a, b))

carre = 1
a = carre
print(CarrAir(a))
print(CarrDiagonale(a))

