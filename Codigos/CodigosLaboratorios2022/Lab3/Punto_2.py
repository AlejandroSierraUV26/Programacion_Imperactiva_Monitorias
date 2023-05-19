"""
punto #2
laboratorio 4

integrantes:

Alejandro Sierra Betancourt-2259559
Tina María Torres-2259729
Edgar Rueda Colonia-2259606
Kevin Steven Ramírez-2259371

profesor: Carlos Delgado
3743

"""
import numpy as np 
from tabulate import tabulate
def datosMatriz(n):
    matriz = np.zeros((n,5))
    return matriz
def asignacionPresupuesto(n,presupuesto):
    arreglo = datosMatriz(n)
    for i in range(0,arreglo.shape[0]): 
        print(f"--------Proyecto {i+1}--------")
        print("Zonas destinadas: \n Pacífica 1 \n Atlántica 2 \n Centro 3 \n Oriental 4")
        print("Actividad Productiva: \n Agricultura 1 \n Ganadería 2 \n Pecuaria 3 \n Avícola 4")
        arreglo[i][0]= i+1
        zona = int(input("Seleccione la zona: "))
        arreglo[i][1]= zona
        actividad = int(input("Ingrese la actividad productiva: "))
        arreglo[i][2]= actividad
        hectareas = int(input("Ingrese la cantidad de hectareas: "))
        arreglo[i][3]= hectareas
        personas = int(input("Ingrese la cantidad de personas: "))
        arreglo[i][4]= personas
    arreglo = np.insert(arreglo, [5], 0, axis=1)
    i = 0
    for i in range(0,arreglo.shape[0]):
        if arreglo[i][1] == 1:
            presupuesto_zona = presupuesto*25/100
        if arreglo[i][1] == 2:
            presupuesto_zona = presupuesto*20/100
        if arreglo[i][1] == 3:
            presupuesto_zona = presupuesto*35/100
        if arreglo[i][1] == 4:
            presupuesto_zona = presupuesto*20/100
        if arreglo[i][2] == 1:
            if arreglo[i][4] <= 5:
                arreglo[i][5] = presupuesto_zona* 0.6/100 * arreglo[i][3] + (presupuesto_zona* 0.6/100 * arreglo[i][3]) * 4/100
            elif arreglo[i][4] > 5:
                arreglo[i][5] = presupuesto_zona* 0.6/100 * arreglo[i][3] + (presupuesto_zona* 0.6/100 * arreglo[i][3]) * 6/100
        if arreglo[i][2] == 2:
            if arreglo[i][4] <= 5:
                arreglo[i][5] = presupuesto_zona* 0.5/100 * arreglo[i][3] + (presupuesto_zona* 0.5/100 * arreglo[i][3]) * 4/100
            elif arreglo[i][4] > 5:
                arreglo[i][5] = presupuesto_zona* 0.5/100 * arreglo[i][3] + (presupuesto_zona* 0.5/100 * arreglo[i][3]) * 6/100
        if arreglo[i][2] == 3 or 4:
            if arreglo[i][4] <= 5:
                arreglo[i][5] = presupuesto_zona*2/100 + (presupuesto_zona*2/100 ) * 4/100
            elif arreglo[i][4] > 5:
                arreglo[i][5] = presupuesto_zona*2/100 + (presupuesto_zona*2/100 ) * 6/100
    return arreglo
def proyectosAvalados(n,presupuesto):
    arreglo = asignacionPresupuesto(n,presupuesto)
    presupuesto_final = np.zeros((n))
    valor = 0
    valor_acomulativo = 0
    acomulativo = np.zeros((4))
    arreglo = np.insert(arreglo, [6], 0, axis=1)
    for i in range(0,arreglo.shape[0]):
        valor = arreglo[i][5] + valor
        presupuesto_final[i] = valor
        presupuesto = presupuesto - presupuesto_final[i]
        if presupuesto > 0: 
            arreglo[i][6] = 1
        else: 
            arreglo[i][6] = 2
        if arreglo[i][1] == 1:
            valor_acomulativo = valor_acomulativo + arreglo[i][5]
            acomulativo[0] = valor_acomulativo  
        if arreglo[i][1] == 2:
            valor_acomulativo = valor_acomulativo + arreglo[i][5]
            acomulativo[1] = valor_acomulativo 
        if arreglo[i][1] == 3:
            valor_acomulativo = valor_acomulativo + arreglo[i][5] 
            acomulativo[2] = valor_acomulativo
        if arreglo[i][1] == 4:
            valor_acomulativo = valor_acomulativo + arreglo[i][5]
            acomulativo[3] = valor_acomulativo
    
    #Se cambia de tipo int a str todos los valores
    arreglo = arreglo.astype(str)
    #print(type(arreglo[1][0]))
    for i in range(0, arreglo.shape[0]):
        if arreglo[i][1] == "1.0":
            arreglo[i][1] = "Pacifica"
        if arreglo[i][1] == "2.0":
            arreglo[i][1] = "Atlatica"
        if arreglo[i][1] == "3.0":
            arreglo[i][1] = "Centro"
        if arreglo[i][1] == "4.0":
            arreglo[i][1] = "Oriental"
        if arreglo[i][2] == "1.0":
            arreglo[i][2] = "Agricultura"
        if arreglo[i][2] == "2.0":
            arreglo[i][2] = "Ganaderia"
        if arreglo[i][2] == "3.0":
            arreglo[i][2] = "Pecuaria"
        if arreglo[i][2] == "4.0":
            arreglo[i][2] = "Avicola"
        if arreglo[i][6] == "1.0":
            arreglo[i][6] = "Aprobado"
        if arreglo[i][6] == "2.0":
            arreglo[i][6] = "Falta de presupuesto"
    print((tabulate(arreglo, headers=["Orden de llegada", "Zona", "Actividad productiva","Cantidad de Hectareas","Cantidad de personas","Valor presupuesto","Estado"],tablefmt='fancy_grid')))
    zona = np.array(["Pacifica","Atlantica","Centro","Oriental"])
    nueva_lista = np.array([])
    for i in range(0,4):
        texto = (f"\nTotal avalado para la zona {(zona[i])} es {acomulativo[i]}")
        nueva_lista = np.append(nueva_lista, texto)
    return nueva_lista
n = int(input("Ingrese el total de proyectos ha presentar: "))
presupuesto = float(input("Ingrese el valor del presupuesto a cada proyecto: "))
print(*proyectosAvalados(n,presupuesto))