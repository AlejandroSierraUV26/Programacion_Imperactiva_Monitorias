import tkinter as tk
from tkinter import messagebox

def saludar():
    numero1 = int(campo1.get())
    numero2 = int(campo2.get())
    messagebox.showinfo("Mensaje", f"{numero1} x {numero2}  = {numero1*numero2}")

ventana_principal = tk.Tk()

ventana_principal.title("GUI 1")
# ventana_principal.geometry("600x400")
ancho_pantalla = ventana_principal.winfo_screenwidth()
alto_pantalla = ventana_principal.winfo_screenheight()
ancho_ventana = 400
alto_ventana = 300
x_pos = int((ancho_pantalla - ancho_ventana) / 2)  # Centrar horizontalmente
y_pos = int((alto_pantalla - alto_ventana) / 2)  # Centrar verticalmente
ventana_principal.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")


ventana_principal.resizable(False,False)








mensaje1 = tk.Label(ventana_principal, text = "Numero 1 ")
mensaje1.configure(bg="white")
mensaje1.config(font=("Arial", 20), fg = "black")


mensaje2 = tk.Label(ventana_principal, text = "Numero 2 ")
mensaje2.configure(bg="white")
mensaje2.config(font=("Arial", 20), fg = "black")


campo1 = tk.Entry(ventana_principal)

campo2 = tk.Entry(ventana_principal)





botton1 = tk.Button(ventana_principal, text = "Multiplicar")
botton2 = tk.Button(ventana_principal, text = "Sumar")
botton3 = tk.Button(ventana_principal, text = "Restar")

botton1.config(command = saludar)
botton2.config(command = saludar)
botton3.config(command = saludar)








mensaje1.pack()

campo1.pack()

mensaje2.pack()


campo2.pack()


botton1.pack()



ventana_principal.mainloop()