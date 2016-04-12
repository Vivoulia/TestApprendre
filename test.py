import math

"""FORMULE DE GEOMETRIE DE BASE SUR DES RECTANGLE"""

def air(a, b):
    return a*b

def perimetre(a, b):
    return a+b

def diagonale(a, b):
    diagonale = math.sqrt(a*a + b*b)
    return diagonale
    

rectangle = (1, 1)
a, b = rectangle
print(air(a, b))
print(diagonale(a, b))


