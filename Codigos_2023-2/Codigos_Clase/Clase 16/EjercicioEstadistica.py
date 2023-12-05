habitaciones = [
    [["A1",1],["A2",0],["A3",0],["A4",0],["A5",0]],
    [["B1",0],["B2",1],["B3",0],["B4",0],["B5",0]],
    [["C1",0],["C2",0],["C3",1],["C4",0],["C5",0]],
    [["D1",0],["D2",0],["D3",0],["D4",1],["D5",0]],
    [["E1",0],["E2",0],["E3",0],["E4",0],["E5",1]]
]
def comprobar_estado(habitaciones,numero_habitacion):
    for i in range(len(habitaciones)):
        for j in range(len(habitaciones[i])):
            if habitaciones[i][j][0] == numero_habitacion:
                if habitaciones[i][j][1] == 0:
                    return True
                else:
                    return False
    return False
print("Habitaciones Disponibles")
for i in range(len(habitaciones)):
    for j in range(len(habitaciones[i])):
        if habitaciones[i][j][1] == 0:
            print(habitaciones[i][j][0], end="-")
    print()
print("--------------------------------")
print("Seleccione una habitacion : ")
numero_habitacion = str(input("Ingrese la habitacion que desea : "))
if comprobar_estado(habitaciones,numero_habitacion):
    print("La habitacion esta disponible")
    for i in range(len(habitaciones)):
        for j in range(len(habitaciones[i])):
            if habitaciones[i][j][0] == numero_habitacion:
                habitaciones[i][j][1] = 1
print("Habitaciones Ocupadas")
for i in range(len(habitaciones)):
    for j in range(len(habitaciones[i])):
        if habitaciones[i][j][1] == 1:
            print(habitaciones[i][j][0], end="-")
    print()
print("--------------------------------")