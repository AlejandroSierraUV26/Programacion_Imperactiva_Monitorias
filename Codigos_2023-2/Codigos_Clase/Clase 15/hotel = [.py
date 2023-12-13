def comprobarHabitacion(hotel,habitacion):
    for i in range(0,len(hotel)):
        for j in range(0,len(hotel)):
            if hotel[i][j][0] == habitacion:
                if hotel[i][j][1] == 0:
                    print("La habitacion esta disponible")
                    return True
                else:
                    return False
    return False
hotel = [
        [["A1",0],["A2",0],["A3",0],["A4",0]],
        [["B1",0],["B2",0],["B3",0],["B4",0]],
        [["C1",0],["C2",0],["C3",0],["C4",0]],
        [["D1",0],["D2",0],["D3",0],["D4",0]]
        ]
# Las disponibles.
for i in range(0,len(hotel)):
    for j in range(0,len(hotel)):
        if hotel[i][j][1] == 0:
            print(hotel[i][j][0], end="-")
    print()
    

numero_habitacion = str(input("Ingrese el numero de la habitacion :"))

if comprobarHabitacion(hotel,numero_habitacion):
    for i in range(0,len(hotel)):
        for j in range(0,len(hotel)):
            if hotel[i][j][0] == numero_habitacion:
                hotel[i][j][1] = 1
print(f"Su habitacion {numero_habitacion} fue reserveda con exito")

# Muestra las ocupadas 
for i in range(0,len(hotel)):
    for j in range(0,len(hotel)):
        if hotel[i][j][1] == 1:
            print(hotel[i][j][0], end="-")
    print()



        