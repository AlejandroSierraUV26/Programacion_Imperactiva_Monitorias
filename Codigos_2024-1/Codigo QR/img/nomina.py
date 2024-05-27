import numpy as np
from tabulate import tabulate 

valor_hora = 10_000
personas = []
nomina = []


numero_empleados = int(input("Ingrese el número de empleados: "))
total_semanas = int(input("Ingrese el número de semanas: "))
for i in range(numero_empleados):
    empleado = []
    nombre = input(f"Enter the name of the employee N° {i+1} : ")
    empleado.append(nombre)
    saldo = 0
    nomina_persona = []
    for j in range(total_semanas):
        horas_trabajadas = int(input("Enter the total of hours worked : "))
        saldo += horas_trabajadas*valor_hora
        nomina_persona.append(horas_trabajadas*valor_hora)
        empleado.append(horas_trabajadas)
    empleado.append(saldo)
    personas.append(empleado)
    nomina.append(nomina_persona)

nomina_semanal = []
for i in range(0,len(nomina)):
    acom = 0
    for j in range(0,len(nomina[i])):
        acom += nomina[i][j]
        print(f"Posicion ({i} , {j}) = {nomina[i][j]}")
    nomina_semanal.append(acom)
        


personas = np.array(personas)
nomina = np.array(nomina)



print(tabulate(personas))        
print(tabulate(nomina))
print(nomina_semanal)
    
    
    

