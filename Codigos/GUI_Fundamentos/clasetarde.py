import tkinter as tk

def saludar():
    nombre = campo_texto.get()
    etiqueta2.config(text =nombre)


ventana = tk.Tk()

ventana.title("GUI 1")

ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
ancho_ventana = 400
alto_ventana = 300
x_pos = int((ancho_pantalla - ancho_ventana) / 2)  # Centrar horizontalmente
y_pos = int((alto_pantalla - alto_ventana) / 2)  # Centrar verticalmente
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")





ventana.title("Aplicacion Fundamentos")
ventana.resizable(False, False)
color_pastel_azul = "#AED6F1"  # Código hexadecimal para el tono pastel azul
ventana.configure(bg=color_pastel_azul)

etiqueta = tk.Label(ventana, text = "Ingrese su nombre: ")
etiqueta.configure(bg=color_pastel_azul)
etiqueta.config(font=("Arial",14))

etiqueta2 = tk.Label(ventana, text = "")
etiqueta2.configure(bg=color_pastel_azul)
etiqueta2.config(font=("Arial",14))

campo_texto = tk.Entry(ventana)

boton1 = tk.Button(ventana, text = "Presioname")

boton1.config(command=saludar)


etiqueta.pack()
campo_texto.pack()
boton1.pack()
etiqueta2.pack()


ventana.mainloop()

