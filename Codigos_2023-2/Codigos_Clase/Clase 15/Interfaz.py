import tkinter as tk

def ocultar_ventana():
    ventana1.withdraw()  # Oculta la ventana actual
    ventana2.deiconify()  # Muestra la ventana actual
    

def mostrar_ventana():
    ventana2.withdraw()  # Oculta la ventana actual
    ventana1.deiconify()  # Muestra la ventana actual
        
ventana1 = tk.Tk()
ventana1.title("Inicio")
ancho_pantalla = ventana1.winfo_screenwidth()
alto_pantalla = ventana1.winfo_screenheight()
ancho_ventana = 400
alto_ventana = 300
x_pos = int((ancho_pantalla - ancho_ventana) / 2)  # Centrar horizontalmente
y_pos = int((alto_pantalla - alto_ventana) / 2)  # Centrar verticalmente
ventana1.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")


boton1 = tk.Button(ventana1, text="Cambiar de Ventana", command=ocultar_ventana)
boton1.pack()


ventana2 = tk.Tk()
ventana2.title("Registro")
ventana2.withdraw()
ancho_pantalla = ventana2.winfo_screenwidth()
alto_pantalla = ventana2.winfo_screenheight()
ancho_ventana = 400
alto_ventana = 300
x_pos = int((ancho_pantalla - ancho_ventana) / 2)  # Centrar horizontalmente
y_pos = int((alto_pantalla - alto_ventana) / 2)  # Centrar verticalmente
ventana2.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")


boton2 = tk.Button(ventana2, text="Cambiar de Ventana", command=mostrar_ventana)
boton2.pack()

ventana1.mainloop()
ventana2.mainloop()    


