import tkinter as tk
from tkinter import messagebox


#TODO: Funciones aplicadas a botones

def saludar():
    nombre = campo.get()
    messagebox.showinfo("Mensaje", f"Hola {nombre}")
def cambiar_ventana_Segundaria():
    ventana.withdraw()
    ventana2.deiconify()
def cambiar_ventana_Principal():
    ventana2.withdraw()
    ventana.deiconify()
    



#? Seccion aplicada solo a la ventana

#* Inicializar la ventana
ventana = tk.Tk()
ventana2 = tk.Tk()
ventana2.withdraw()


#* Titulo
ventana.title("Primer Ventana")
ventana2.title("Segunda Ventana")


#* Tamaño
# ventana.geometry("500x300")
# ventana2.geometry("500x300")

#* Tamaño Centrado 

ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
ancho_ventana = 400
alto_ventana = 300
x_pos = int((ancho_pantalla - ancho_ventana) / 2)  # Centrar horizontalmente
y_pos = int((alto_pantalla - alto_ventana) / 2)  # Centrar verticalmente
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")
ventana2.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

#* Definir color de fondo
ventana.configure(bg="white")
ventana2.configure(bg="white")

#* Disponibilidad de minimizar y maximizar
ventana.resizable(False, False)
ventana2.resizable(False, False)



#? Herramientas de la ventana 

#* Etiquetas o labels

etiqueta = tk.Label(ventana, text = "Hola Bienvenido")

etiqueta.configure(bg="white")

etiqueta.config(font=("Arial", 20), fg = "red")

# * Campo de tex
campo = tk.Entry(ventana, text = "Ingrese su nombre ")



campo.configure(bg="white")



#! Despues de añadir algo se debe poner el nombre .pack()
#! Indica la posicion, predeterminada una bajo la otra

etiqueta.pack()
campo.pack()



boton = tk.Button(ventana, text = "Saludar")
boton2 = tk.Button(ventana, text = "Cambiar Ventana")
boton3 = tk.Button(ventana2, text = "Regresar")

#! Despues de añadir algo se debe poner el nombre .pack()
boton.pack()
boton2.pack(side = "bottom")
boton3.pack()

#? Comando que ejecuta al presionar

boton.config(command = saludar)
boton2.config(command = cambiar_ventana_Segundaria)
boton3.config(command = cambiar_ventana_Principal)



#TODO: Ciclo que permite la ejecucion del codigo hasta cerrarlo, en este caso
#TODO: La x de la ventan.
ventana.mainloop()

