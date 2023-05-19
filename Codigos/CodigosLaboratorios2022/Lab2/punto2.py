"""
Autores: Alejandro Sierra Betancourt / Tina Maria Torres Tascon
Codigo Estudiante: 2259559-3743      / 2259729-3743
Fecha: 07/04/2022
Laboratorio 2
Descripcion: Fundamentos de programación. Punto 2 
"""

#Funcion para identificar que materia selecciona
def materia(nombre_materia):
    if nombre_materia == 1:
        return "Matematicas"
    elif nombre_materia == 2:
        return "Fisica"
    elif nombre_materia == 3:
        return "Quimica"
    else: 
        print("Valor ingresado invalido")
#Función nota de las 3 materia
def nota_definitiva(nombre_materia, nota_parcial, nota1, nota2, nota3):
    if nombre_materia == 1:
        nota_final = (nota_parcial*0.9) + (((nota1 + nota2 + nota3)/3)*0.1)
        return nota_final
    elif nombre_materia == 2:
        nota_final = (nota_parcial*0.8) + (((nota1 + nota2 + nota3)/3)*0.2)
        return nota_final
    elif nombre_materia == 3:
        nota_final = (nota_parcial*0.85) + (((nota1 + nota2 + nota3)/3)*0.15)
        return nota_final
    else: 
        print("Valor ingresado invalido")


for i in range(1,4):
    #Recoleccion de variables por parte del usuario
    nombre_materia = int(input("Estas son las opciones \n 1. Matematicas \n 2. Fisica \n 3. Quimica \n Ingrese el numero de la asignatura :"))
    print("==========================================================================================")
    nota_parcial = float(input("Ingrese su nota del parcial: "))
    nota1 = float(input("Ingrese su nota de la tarea 1 : "))
    nota2 = float(input("Ingrese su nota de la tarea 2 : "))
    nota3 = float(input("Ingrese su nota de la tarea 3 : "))
    #Salida de los datos
    print(f"Ingreso de notas para : {nombre_materia} \n La nota definitiva en {materia(nombre_materia)} es {round(nota_definitiva(nombre_materia, nota_parcial, nota1, nota2, nota3),2)}")
    if nota_definitiva(nombre_materia, nota_parcial, nota1, nota2, nota3)>=3.0:
        print("¡gana la materia!")
    else:
        print("¡perdio la materia!")
    print("==========================================================================================")




