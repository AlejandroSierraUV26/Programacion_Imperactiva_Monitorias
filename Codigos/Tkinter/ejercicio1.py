"""
Realizar un formulario sencillo que pida el nombre y la identificacion del usuario
y que la almacene en una matrix 

Que tenga un boton que me muestre los usuarios existentes, y que dentro de esa ventana tenga para 
volver al formulario principal.




"""

import customtkinter as ctk

def button_clicked():
    print("¡Botón clicado!")

root = ctk.tkinter.Tk()

custom_button = ctk.CTkButton(root, text="Mi botón", command=button_clicked)
custom_button.pack()

disable_button = ctk.CTkButton(root, text="Deshabilitar", command=custom_button.disable)
disable_button.pack()

enable_button = ctk.CTkButton(root, text="Habilitar", command=custom_button.enable)
enable_button.pack()

root.mainloop()
