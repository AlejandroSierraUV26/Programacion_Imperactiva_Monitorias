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
Prueba tu código con los datos que se ha proporcionado

"""

def piramide(bloques):
    altura = 0
    while bloques > 0:
        altura += 1
        bloques -= altura
    if bloques < 0:
        altura -= 1
    return altura    

if __name__ == "__main__":
    bloques = int(input("Ingrese la cantidad de bloques : "))
    print(f"La altura de la piramide es : {piramide(bloques)}")