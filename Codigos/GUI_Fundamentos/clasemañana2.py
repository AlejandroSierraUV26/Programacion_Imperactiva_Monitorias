import tkinter
import customtkinter
def saludar():
    nombre = campotexto.get()
    texto2.configure(text = f"Hola {nombre}")
    texto2.place(relx = 0.2, rely = 0.8, anchor = tkinter.CENTER)


ventana = customtkinter.CTk()


ventana.title("GUI 1")
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
ancho_ventana = 600
alto_ventana = 300
x_pos = int((ancho_pantalla - ancho_ventana) / 2)  # Centrar horizontalmente
y_pos = int((alto_pantalla - alto_ventana) / 2)  # Centrar verticalmente
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")



texto = customtkinter.CTkLabel(master = ventana, text = "Nombre", font =("Arial",20))

texto2 = customtkinter.CTkLabel(master = ventana, text = "", font =("Arial",20))

texto.place(relx = 0.1, rely = 0.5, anchor= tkinter.CENTER)

campotexto = customtkinter.CTkEntry(master = ventana)

campotexto.place(relx = 0.3, rely = 0.5, anchor= tkinter.CENTER)

boton = customtkinter.CTkButton(master = ventana , command=saludar, text = "Saludar")

boton.place(relx = 0.2, rely = 0.6, anchor = tkinter.CENTER)

ventana.mainloop()