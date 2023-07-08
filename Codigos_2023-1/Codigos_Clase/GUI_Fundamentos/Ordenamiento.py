import customtkinter 
import tkinter

customtkinter.set_appearance_mode("System")
#Opciones light, dark, default
customtkinter.set_default_color_theme("blue")
#Opciones dark-blue, green, blue default

app = customtkinter.CTk()

app.title("GUI 1")
ancho_pantalla = app.winfo_screenwidth()
alto_pantalla = app.winfo_screenheight()
ancho_ventana = 600
alto_ventana = 300
x_pos = int((ancho_pantalla - ancho_ventana) / 2)  # Centrar horizontalmente
y_pos = int((alto_pantalla - alto_ventana) / 2)  # Centrar verticalmente
app.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

lista = []
def open_popup():
    popup = customtkinter.CTkToplevel()
    popup.title("Ventana emergente")
    popup.geometry("300x1000")
    
    for i in range(0, len(lista)):
        label = customtkinter.CTkLabel(popup, text=f"Nombre : {lista[i][0]} Identificacion : {lista[i][1]} \n")
        label.pack(pady=20)
    close_button = customtkinter.CTkButton(popup, text="Cerrar", command=popup.destroy)
    close_button.pack()
    
    popup.mainloop()

def funcionBoton():
    persona = []
    nombre = campo1.get()
    identificacion = campo2.get()
    persona.append(nombre)
    persona.append(identificacion)
    lista.append(persona)
    print(lista)
    
    
texto1 = customtkinter.CTkLabel(master=app, text = "Nombre", font=("Arial",20))
texto2 = customtkinter.CTkLabel(master=app, text = "Identificacion", font=("Arial",20))

texto3 = customtkinter.CTkLabel(master=app, text = "", font=("Arial",20))

campo1 = customtkinter.CTkEntry(master=app)
campo2 = customtkinter.CTkEntry(master=app)

button = customtkinter.CTkButton(master=app, text = "Boton" ,command=funcionBoton)

button_ver = customtkinter.CTkButton(master=app, text = "Ver", command=open_popup)

texto1.place(relx=0.3333, rely=0.3, anchor=tkinter.CENTER)
texto2.place(relx=0.6666, rely=0.3, anchor=tkinter.CENTER)

campo1.place(relx=0.3333, rely=0.5, anchor=tkinter.CENTER)
campo2.place(relx=0.6666, rely=0.5, anchor=tkinter.CENTER)


button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
button_ver.place(relx=0.8, rely=0.8, anchor=tkinter.CENTER)

app.mainloop()