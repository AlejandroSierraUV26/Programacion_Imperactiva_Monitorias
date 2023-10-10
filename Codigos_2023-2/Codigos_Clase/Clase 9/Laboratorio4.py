"""
Autor : Alejandro Sierra

Fecha de creacion: 2023-10-10

"""

def calcularDefinitiva(parcial,examen,tarea1,tarea2,participacion):
    parcial = 20/100 * parcial
    examen = 40/100 * examen
    tareas = 20/100 * ((tarea1+tarea2)/2)
    participacion = 20/100 * participacion
    
    return (parcial,examen,participacion,tareas)
    
    
def calcularClasificacion(nota, materia):
    if materia == "Fundamentos":
        if nota >= 0 and nota < 2.0:
            return "Malo"
        elif nota >= 2.0 and nota < 3.0:
            return "Deficiente"
        elif nota >= 3.0 and nota < 3.8:
            return "Regular"
        elif nota >= 3.8 and nota < 4.5:
            return "Bueno"
        elif nota >= 4.5 and nota < 5:
            return "Excelente"
        else: 
            return "Parametros Incorrectos"
    elif materia == "CalculoI":
        if nota >= 0 and nota < 2.0:
            return "Malo"
        elif nota >= 2.0 and nota < 3.0:
            return "Deficiente"
        elif nota >= 3.0 and nota < 3.5:
            return "Regular"
        elif nota >= 3.5 and nota < 4.5:
            return "Bueno"
        elif nota >= 4.5 and nota < 5:
            return "Excelente"
        else: 
            return "Parametros Incorrectos"
    elif materia == "Ingles":
        if nota >= 0 and nota < 3.0:
            return "Deficiente"
        elif nota >= 3.0 and nota < 4:
            return "Regular"
        elif nota >= 4 and nota < 4.5:
            return "Bueno"
        elif nota >= 4.5 and nota < 5:
            return "Excelente"
        else: 
            return "Parametros Incorrectos"
    elif materia == "Deporte":
        if nota >= 0 and nota < 3.0:
            return "Malo"
        elif nota >= 3.0 and nota < 4:
            return "Regular"
        elif nota >= 4.0 and nota < 5:
            return "Bueno"
        else: 
            return "Parametros Incorrectos"
    

materias = ["Fundamentos","CalculoI","Ingles","Deporte"]

nombre = input("Ingrese su nombre : ")
for i in range(0,4):

    print("=" * 30)
    parcial = 4.1
    tarea1 = 3.0
    tarea2 = 4.2
    examen_final = 4.6
    participacion = 3.6 
    parcial,examen_final,participacion,tareas = calcularDefinitiva(parcial,examen_final,tarea1,tarea2,participacion)
    promedio = parcial + examen_final +participacion + tareas

    nombre_asignatura = materias[i]
    print("Nombre Alumno : ", nombre)
    print("Nombre Asignatura : ", nombre_asignatura)
    print("Clasificacion : ", calcularClasificacion(promedio,nombre_asignatura))
        

        
        
"""
0.72
0.82
1,84
0.72
"""



