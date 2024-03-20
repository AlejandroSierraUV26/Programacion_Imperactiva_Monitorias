"""
Se requiere de un programa que lee la cedula, salario
año vinculacion
calcular su salario neto.

Si gana 1.200.000 y trabaja despues de 1995
se le adicciona un 6% de su salario

Si gana menos de 550.000 o entreo a trabajar 
en 1995 
se le adicciona 3% de su salario

En cualquier caso se adicciona 4%

Cada empleado debe cumplir con el pago de su salario

Paga 4 % cada mes







"""
#! Entrada de datos
def leer_datos():    
    nombre = input("Ingrese su nombre: ")

    salario = float(input("Ingrese su salario : "))

    año = float(input("Ingrese su año de vinculacion : "))
    
    return(nombre, salario, año)

#? Proceso 
def definir_salario(nombre,salario,año):
    bonificacion = 0
    if ((salario > 1_500_000) and (año >1995)):
        bonificacion = 6/100
    elif((salario < 550_000) or (año == 1995)):
        bonificacion = 3/100
    else: 
        bonificacion = 4/100
        
    pago_salud = 4/100

    salario = salario + (bonificacion * salario) - (pago_salud * salario)
    return salario

#! Salida de datos
def imprimir_resultados(nombre,salario):
    print(f"El empleado {nombre} tiene un salario neto de {salario}")

if __name__ == "__main__":
    nombres = ["Juan", "Pedro", "Maria", "Luisa"] 
    salarios = [1_200_000, 1_500_000, 1_000_000, 2_000_000]
    años = [1995, 1996, 1997, 1998]
    for i in range(len(nombres)):
        nombre = nombres[i]
        salario = salarios[i]
        año = años[i]
        salario = definir_salario(nombre, salario, año)
        imprimir_resultados(nombre, salario)



    

