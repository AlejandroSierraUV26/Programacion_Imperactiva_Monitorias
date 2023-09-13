"""
Pedir el nombre del estudiante y sus 3 notas del
semestre para calcular el promedio final.

Mostrarlo por pantalla

"""

nombre = str(input("Ingrese su nombre: "))

nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))

promedio = float((nota1+nota2+nota3)/3)

print(f"{nombre} su promedio es : {promedio}")
