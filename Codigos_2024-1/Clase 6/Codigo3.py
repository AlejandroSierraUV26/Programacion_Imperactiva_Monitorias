"""
Realizar una funcion que cada que es llamada
imprima un mensaje que diga "Hola Mundo"
"""

def hola_mundo(contador):
    if contador == 0:
        return "Termine"
    else:
        print("Hola Mundo")
        return hola_mundo(contador-1)
print(hola_mundo(10))
# What is the output of this code?

# A) Hola Mundo
# B) Hola Mundo Hola Mundo
# C) Hola Mundo Hola Mundo Hola Mundo
# D) Hola Mundo Hola Mundo Hola Mundo Hola Mundo
# E) Hola Mundo Hola Mundo Hola Mundo Hola Mundo Hola Mundo
# F) None