# "ALGORITHMS AND DATABASE STRUCTURE"



with open('notas.txt', 'r') as archivo:
    archivo = archivo.read()
    archivo = archivo.split("\n")
    alumnos = []

    for elem in archivo:
        elem = elem.split(",")
        alumnos.append(elem)
    for i in range(len(alumnos)):
        alumnos[i][1] = float(alumnos[i][1])
    print(alumnos)

cantidad_inscritos = len(alumnos)

aprobados = [alumno for alumno in alumnos if alumno[1] >= 3.0]
desaprobados = [alumno for alumno in alumnos if alumno[1] < 3.0]
habilitacion = [alumno for alumno in alumnos if 0.0 <= alumno[1] < 3.0]


promedio_notas = sum([alumno[1] for alumno in alumnos]) / cantidad_inscritos


porcentaje_aprobados = (len(aprobados) / cantidad_inscritos) * 100


mejores_promedios = sorted(alumnos, key=lambda x: x[1], reverse=True)[:5]

notas_bajas = [alumno for alumno in alumnos if 0.0 <= alumno[1] <= 2.0]
persona_nota_baja = min(notas_bajas, key=lambda x: x[1], default=None)



print("Cantidad de alumnos inscritos:", cantidad_inscritos)
print("Cantidad de alumnos aprobados:", len(aprobados))
print("Cantidad de alumnos desaprobados:", len(desaprobados))
print("Promedio de notas de los alumnos:", promedio_notas)
print("Número de personas que deben hacer habilitación (nota menor a 3):", len(habilitacion))
print("Porcentaje de alumnos aprobados:", porcentaje_aprobados, "%")
print("Estímulo académico (5 mejores promedios):")
for i, (nombre, nota) in enumerate(mejores_promedios, start=1):
    print(f"  {i}. {nombre} , {nota}")
if persona_nota_baja:
    print("Nombre de la persona con la nota más baja (0.0 a 2.0):", persona_nota_baja[0], "-", persona_nota_baja[1])
else:
    print("No hay notas en el rango de 0.0 a 2.0")
















# aprobados = [alumno for alumno in alumnos if alumno[1] >= 3.0]
# desaprobados = [alumno for alumno in alumnos if alumno[1] < 3.0]
# habilitacion = [alumno for alumno in alumnos if 0.0 <= alumno[1] < 3.0]


# promedio_notas = sum([alumno[1] for alumno in alumnos]) / alumnos


# porcentaje_aprobados = (len(aprobados) / alumnos) * 100


# mejores_promedios = sorted(alumnos, key=lambda x: x[1], reverse=True)[:5]

# notas_bajas = [alumno for alumno in alumnos if 0.0 <= alumno[1] <= 2.0]
# persona_nota_baja = min(notas_bajas, key=lambda x: x[1], default=None)
