import random

tablero = [["","",""],
           ["","",""],
           ["","",""]]


def imprimir_tablero():
    for fila in tablero:
        print(fila)
def pedir_datos():
    fila = int(input("Ingrese la fila: "))
    columna = int(input("Ingrese la columna: "))
    return fila,columna
def verificar_elemento(fila,columna):
    if tablero[fila][columna] == "":
        return True
    else:
        return False  
def ingresar_elemento(fila,columna,jugador):
    tablero[fila][columna] = jugador
def verificar_ganador(jugador):
    #* Verificar filas
    for fila in tablero:
        if fila[0] == jugador and fila[1] == jugador and fila[2] == jugador:
            return True
    #* Verificar columnas
    for i in range(0,3):
        if tablero[0][i] == jugador and tablero[1][i] == jugador and tablero[2][i] == jugador:
            return True
    #* Verificar diagonales
    if tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador:
        return True
    if tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == jugador:
        return True
    return False  
def poner_ficha(jugador):
    fila,columna = pedir_datos()
    if verificar_elemento(fila,columna):
        ingresar_elemento(fila,columna,jugador)
    else:
        print("Casilla ocupada")
        poner_ficha(jugador)
        
def reiniciar_tablero():
    for i in range(0,3):
        for j in range(0,3):
            tablero[i][j] = ""
    return tablero
def jugar():
    intercarlar = 0
    while True:
        jugador1 = str(input("Ingrese su simbolo :"))
        jugador2 = str(input("Ingrese su simbolo :"))
        if jugador1 == jugador2:
            print("Los simbolos deben ser diferentes")
            return "Juego Terminado"
        turno = 0 + intercarlar
        while True:
            imprimir_tablero()
            if turno % 2 == 0:
                print("Turno jugador 1")
                poner_ficha(jugador1)
                if verificar_ganador(jugador1):
                    imprimir_tablero()
                    print("Gano el jugador 1")
                    intercarlar = 1
                    x
                    break
            else:
                print("Turno jugador 2")
                poner_ficha(jugador2)
                if verificar_ganador(jugador2):
                    imprimir_tablero()
                    print("Gano el jugador 2")
                    intercarlar = 1
                    break
            turno += 1
            if turno == 9:
                print("Empate")
                break
        
        
        
if __name__ == "__main__":
    jugar()
            