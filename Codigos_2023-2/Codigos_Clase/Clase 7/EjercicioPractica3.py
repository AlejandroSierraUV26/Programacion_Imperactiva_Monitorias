"""
Imprimir la palabra esternocleidomastoideo, letra por letra.

>>> e s t e r n o c l e i d o m a s t o i d e o 

>>> e
>>> s
>>> t
>>> e
>>> r
>>> n
>>> o
>>> c
>>> l
>>> e
>>> i
>>> d
>>> o
>>> m
>>> a
>>> s
>>> t
>>> o
>>> i
>>> d
>>> e
>>> o
"""

# len(palabra) ==> Numero de elementos 
palabra = "esternocleidomastoideo"
numero = len(palabra)

print(numero)


for i in range(0, numero-1):
    print(palabra[i])
    