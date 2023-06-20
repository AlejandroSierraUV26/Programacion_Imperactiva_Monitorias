import customtkinter as ctk
import tkinter as tk

lista = []

def insertar_persona():
    nombre = campotexto1.get()
    edad   = campotexto2.get()
    persona = []
    persona.append(nombre)
    persona.append(edad)
    lista.append(persona)
    print(lista)
    

    
    


# ctk.set_appearance_mode("light")

ventana = ctk.CTk()
ventana.geometry("500x500")

texto1 = ctk.CTkLabel(master = ventana, text = "Nombre : ", font=("Arial",15))
texto1.place(relx = 0.3, rely = 0.38 ,anchor = tk.CENTER)

campotexto1 = ctk.CTkEntry(master = ventana)
campotexto1.place(relx = 0.3, rely = 0.45, anchor = tk.CENTER)

texto2 = ctk.CTkLabel(master = ventana, text = "Edad : ", font=("Arial",15))
texto2.place(relx = 0.6, rely = 0.38 ,anchor = tk.CENTER)

campotexto2 = ctk.CTkEntry(master = ventana)
campotexto2.place(relx = 0.6, rely = 0.45, anchor = tk.CENTER)


boton1 = ctk.CTkButton(master = ventana, text = "Enviar", command = insertar_persona)
boton1.place(relx = 0.45, rely = 0.6, anchor = tk.CENTER)


ventana.mainloop()