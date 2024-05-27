import customtkinter as ctk

def saludar():
    nombre = entry.get()
    label.configure(text=f"Hola {nombre}")
    
def sumar():
    num1 = int(entry.get())
    num2 = int(entry2.get())
    resultado = num1 + num2
    label.configure(text=f"El resultado es: {resultado}")
    
def restar():
    num1 = int(entry.get())
    num2 = int(entry2.get())
    resultado = num1 - num2
    label.configure(text=f"El resultado es: {resultado}")

def multiplicar():
    num1 = int(entry.get())
    num2 = int(entry2.get())
    resultado = num1 * num2
    label.configure(text=f"El resultado es: {resultado}")

def dividir():
    num1 = int(entry.get())
    num2 = int(entry2.get())
    resultado = num1 / num2
    label.configure(text=f"El resultado es: {resultado}")


root = ctk.CTk()

root.geometry("800x500")
root.resizable(0,0)
root.title("Interfaz gráfica con tkinter")

espacio1 = ctk.CTkFrame(root)


espacio3 = ctk.CTkFrame(espacio1, height=100)

entry = ctk.CTkEntry(espacio3, width=60)
entry2 = ctk.CTkEntry(espacio3, width=60)

boton1 = ctk.CTkButton(espacio1, text= "Sumar", command = sumar)
boton2 = ctk.CTkButton(espacio1, text= "Restar", command = restar)
boton3 = ctk.CTkButton(espacio1, text= "Multiplicar", command = multiplicar)
boton4 = ctk.CTkButton(espacio1, text= "Dividir", command = dividir)
entry.grid(row=0, column=0,padx=10)
entry2.grid(row=0, column=1,padx=10)
espacio3.pack()
boton1.pack(pady = 10)
boton2.pack(pady = 10)
boton3.pack(pady = 10)
boton4.pack(pady = 10)




espacio1.pack(expand=True, fill='both', side='top', padx=10, pady=10)
espacio2 = ctk.CTkFrame(root)
label = ctk.CTkLabel(espacio2, text="Hola mundo")
label.pack()
espacio2.pack(expand=True, fill='both', side='top', padx=10, pady=10)


root.mainloop()

