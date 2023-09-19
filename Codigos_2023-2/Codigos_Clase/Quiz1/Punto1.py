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


nombre = input("Ingrese su nombre: ")

salario = float(input("Ingrese su salario : "))

año = float(input("Ingrese su año de vinculacion : "))

bonificacion = 0

if ((salario > 1_500_000) and (año >1995)):
    bonificacion = 6/100
elif((salario < 550_000) or (año == 1995)):
    bonificacion = 3/100
else: 
    bonificacion = 4/100
    
pago_salud = 4/100

salario = salario + (bonificacion * salario) - (pago_salud * salario)


print(f"La persona {nombre} recibira un sueldo de {salario}")

    

