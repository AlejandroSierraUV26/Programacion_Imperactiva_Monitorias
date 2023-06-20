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

def mostrar_personas():
    ventana2 = ctk.CTkToplevel()
    ventana2.title("Ventana emergente")
    ventana2.geometry("300x1000")
    for i in range(0, len(lista)):
        label = ctk.CTkLabel(master = ventana2, text=f"Nombre : {lista[i][0]} Edad : {lista[i][1]} \n")
        label.pack(pady=20)
    close_button = ctk.CTkButton(master = ventana2, text="Cerrar", command=ventana2.destroy)
    close_button.pack()
    
    
    ventana2.mainloop()



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
boton1.place(relx = 0.3, rely = 0.65, anchor = tk.CENTER)

boton2 = ctk.CTkButton(master = ventana, text = "Mostrar", command = mostrar_personas)
boton2.place(relx = 0.6, rely = 0.65, anchor = tk.CENTER)

ventana.mainloop()