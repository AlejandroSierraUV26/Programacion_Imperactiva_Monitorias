import random
import time

import tkinter as tk 


nombres = ["Gladis", "Juan Diego", "Samuel", "Johan", "Alberto", "Gladis", "Juan Diego", "Samuel", "Johan", "Alberto", "Gladis", "Juan Diego", "Samuel", "Johan", "Alberto", "Gladis", "Juan Diego", "Samuel", "Johan", "Alberto", "Gladis", "Juan Diego", "Samuel", "Johan", "Alberto", "Gladis", "Juan Diego", "Samuel", "Johan", "Alberto", "Gladis", "Juan Diego", "Samuel", "Johan", "Alberto", "Gladis", "Juan Diego", "Samuel", "Johan", "Alberto", "Gladis", "Juan Diego", "Samuel", "Johan", "Alberto", "Gladis", "Juan Diego", "Samuel", "Johan", "Alberto", "Gladis", "Juan Diego", "Samuel", "Johan", "Alberto", "Gladis", "Juan Diego", "Samuel", "Johan", "Alberto", "Gladis", "Juan Diego", "Samuel", "Johan", "Alberto"]


def choose_name():
    return random.choice(nombres)

def construir_interfaz():
    ventana = tk.Tk()
    ventana.title("Elegir nombre")
    # Centrar la ventana con respecto a la pantalla
    
    ancho_ventana = 400
    alto_ventana = 200
    
    x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2
    
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x_ventana}+{y_ventana}")
    

    label = tk.Label(ventana, text="El nombre elegido es:", font=("Arial", 20))
    label.pack()

    nombre = tk.Label(ventana, text="", font=("Arial", 30))
    nombre.pack()
    
    contador = tk.Label(ventana, text="", font=("Arial", 30))
    contador.pack()

    for i in range(10):
        nombre_elegido = choose_name()
        nombre.config(text=nombre_elegido, fg="green")
        contador.config(text=f"Contador: {i+1}")

        ventana.update()
        ventana.after(500)
    
    ventana.mainloop()
    
construir_interfaz()


