import numpy as np
def evaluacion_docente(preguntas):
    n = int(input("Ingrese el numero de estudiantes : "))
    notas = np.zeros(3)
    for i in range(n):
        print(f"Estudiante {i+1}")
        for j in range(3):
            print(preguntas[j])
            notas[j] += float(input(" : "))/n
            notas[j] = round(notas[j],2)
    return notas
        
preguntas = np.array([
"El docente explic ́o claramente los temas" ,
"El docente dio las calificaciones a tiempo" ,
"El docente fue respetuoso con los estudiantes"
])
print(evaluacion_docente(preguntas))