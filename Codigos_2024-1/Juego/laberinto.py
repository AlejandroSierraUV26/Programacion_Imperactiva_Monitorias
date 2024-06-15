"""
Crear un codigo que realice aleatoriamente un laberinto de 10x10, donde se pueda mover un jugador con las teclas de direccion y que se pueda salir del laberinto.



"""

import tkinter as tk
import random
from tkinter import messagebox

def crear_laberinto():
    laberinto = [[0]*10 for _ in range(10)]
    # Crear un camino desde el inicio hasta el final
    
    # Agregar paredes de forma aleatoria
    for i in range(10):
        for j in range(10):
            if (i, j) not in [(k, k) for k in range(10)] and random.randint(0, 1) == 1:
                laberinto[i][j] = 1
                
    # En esta parte genera el camino correcto
    for i in range(10):
        laberinto[i][i] = 0
        if i < 9:
            laberinto[i+1][i] = 0
    return laberinto

def mover_jugador(event):
    global jugador
    if event.keysym == "Right":
        if jugador[1] < 9 and laberinto[jugador[0]][jugador[1] + 1] == 0:
            jugador = (jugador[0], jugador[1] + 1)
    elif event.keysym == "Left":
        if jugador[1] > 0 and laberinto[jugador[0]][jugador[1] - 1] == 0:
            jugador = (jugador[0], jugador[1] - 1)
    elif event.keysym == "Up":
        if jugador[0] > 0 and laberinto[jugador[0] - 1][jugador[1]] == 0:
            jugador = (jugador[0] - 1, jugador[1])
    elif event.keysym == "Down":
        if jugador[0] < 9 and laberinto[jugador[0] + 1][jugador[1]] == 0:
            jugador = (jugador[0] + 1, jugador[1])
    dibujar_laberinto()
    if jugador == (9, 9):
        messagebox.showinfo("Ganaste", "Felicidades, has ganado")
        root.destroy()
    
    
def dibujar_laberinto():
    canvas.delete("all")
    for i in range(10):
        for j in range(10):
            if laberinto[i][j] == 1:
                canvas.create_rectangle(j*50, i*50, j*50 + 50, i*50 + 50, fill="black")
    canvas.create_rectangle(jugador[1]*50, jugador[0]*50, jugador[1]*50 + 50, jugador[0]*50 + 50, fill="red")
    canvas.create_rectangle(9*50, 9*50, 9*50 + 50, 9*50 + 50, fill="green")
    
laberinto = crear_laberinto()
jugador = (0, 0)

root = tk.Tk()
root.title("Laberinto")
root.geometry("500x500")

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

dibujar_laberinto()

root.bind("<Key>", mover_jugador)

root.mainloop()

  