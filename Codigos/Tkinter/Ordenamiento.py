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

def funcionBoton():
    nombre = campo1.get()
    print(f"Nombre {nombre}")
    texto3.configure(text =nombre)
    texto3.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
    
texto1 = customtkinter.CTkLabel(master=app, text = "Nombre", font=("Arial",20))
texto2 = customtkinter.CTkLabel(master=app, text = "Identificacion", font=("Arial",20))

texto3 = customtkinter.CTkLabel(master=app, text = "", font=("Arial",20))

campo1 = customtkinter.CTkEntry(master=app)
campo2 = customtkinter.CTkEntry(master=app)

button = customtkinter.CTkButton(master=app, text = "Boton" ,command=funcionBoton)

button_ver = customtkinter.CTkButton(master=app, text = "Ver")

texto1.place(relx=0.3333, rely=0.3, anchor=tkinter.CENTER)
texto2.place(relx=0.6666, rely=0.3, anchor=tkinter.CENTER)

campo1.place(relx=0.3333, rely=0.5, anchor=tkinter.CENTER)
campo2.place(relx=0.6666, rely=0.5, anchor=tkinter.CENTER)


button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
button_ver.place(relx=0.8, rely=0.8, anchor=tkinter.CENTER)

app.mainloop()