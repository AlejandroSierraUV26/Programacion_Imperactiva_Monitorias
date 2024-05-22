import numpy as np

def verificar_fila(tablero, fila, numero):
    # Funcion para verificar que no esta el numero en la fila
    for i in range(9):
        if tablero[fila][i] == numero:
            return False
    return True

def verificar_columna(tablero, columna, numero):
    # Funcion para verificar que no esta el numero en la columna
    for i in range(9):
        if tablero[i][columna] == numero:
            return False
    return True

def poner_numero_aleatorio(tablero):
    # Funcion para poner los numeros iniciales
    fila = np.random.randint(0, 9)
    columna = np.random.randint(0, 9)
    numero = np.random.randint(1, 10)
    if verificar_fila(tablero, fila, numero) and verificar_columna(tablero, columna, numero) and verificar_cuadro(tablero, fila, columna, numero):
        tablero[fila][columna] = numero
    else:
        tablero = poner_numero_aleatorio(tablero)
    return tablero

def diseño_tablero(tablero):
    # Diseño para el tablero
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(tablero[i][j], end=" ")
        print()

def verificar_cuadro(tablero, fila, columna, numero):
    # Verificacion de cada cuadro vaya desde el 1 hasta el 9
    fila_inicio = fila - fila % 3
    columna_inicio = columna - columna % 3
    for i in range(fila_inicio, fila_inicio + 3):
        for j in range(columna_inicio, columna_inicio + 3):
            if tablero[i][j] == numero:
                return False
    return True

        
tablero = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0]]
tablero = np.array(tablero)
for i in range(50):
    tablero = poner_numero_aleatorio(tablero)
    
diseño_tablero(tablero)
while True:
    print("Ingrese la fila y columna donde desea ingresar un número")
    fila = int(input("Fila: "))
    if fila < 0 or fila > 8:
        print("Fila inválida")
        continue
    columna = int(input("Columna: "))
    if columna < 0 or columna > 8:
        print("Columna inválida")
        continue
    print("Ingrese el número que desea ingresar")
    numero = int(input("Número: "))
    
    if not verificar_fila(tablero, fila, numero):
        print("Número inválido en la fila")
        continue 
    if not verificar_columna(tablero, columna, numero):
        print("Número inválido en la columna")
        continue
    if not verificar_cuadro(tablero, fila, columna, numero):
        print("Número inválido en el cuadro")
        continue
    
    tablero[fila][columna] = numero
    diseño_tablero(tablero)
    continuar = input("Desea ingresar otro número? (s/n): ")
    if continuar == "n":
        break
    


