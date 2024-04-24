"""
Escucha esta historia: Un niño y su padre, un programador de computadoras, juegan con bloques de madera.
Están construyendo una pirámide.
Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide, es plana. La pirámide se
apila de acuerdo con un principio simple: cada capa inferior contiene un bloque más que la capa superior.
La figura ilustra la regla utilizada por los constructores:
Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la
altura de la pirámide que se puede construir utilizando estos bloques.
Nota: La altura se mide por el número de capas completas: si los constructores no tienen la cantidad
suficiente de bloques y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.
Prueba tu código con los datos que se ha proporcionado.
Entrada de muestra: 6
Producto esperado: La altura de la pirámide es: 3
print(piramide(6)) # 3
print(piramide(20)) # 5
print(piramide(100)) # 13
print(piramide(2)) # 1
print(piramide(1)) # 1
"""

def piramide(bloques):
    altura = 0
    bloques_restantes = bloques
    while bloques_restantes >= 0:
        altura += 1
        bloques_restantes -= altura
    return altura - 1


print(piramide(6)) # 3
print(piramide(20)) # 5
print(piramide(100)) # 13
print(piramide(2)) # 1