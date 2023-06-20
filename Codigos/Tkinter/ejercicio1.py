"""
Realizar un formulario sencillo que pida el nombre y la identificacion del usuario
y que la almacene en una matrix 

Que tenga un boton que me muestre los usuarios existentes, y que dentro de esa ventana tenga para 
volver al formulario principal.




"""

import customtkinter 

def button_clicked():
    print("¡Botón clicado!")

root = customtkinter.CTk()

custom_button = customtkinter.CTkButton(master = root, text="Mi botón", command=button_clicked)
custom_button.pack()

disable_button = customtkinter.CTkButton(master = root, text="Deshabilitar", command=custom_button.disable)
disable_button.pack()

enable_button = customtkinter.CTkButton(master = root, text="Habilitar", command=custom_button.enable)
enable_button.pack()

root.mainloop()
