import tkinter as tk

def suma():
    numero1 = int(entrada_texto1.get())
    numero2 = int(entrada_texto2.get())
    mensaje3.configure(text = f"{numero1} + {numero2} = {numero1+numero2}")
    
# ----------------------------------------------------------------

# * Pagina Principal

ventana_principal = tk.Tk()



ventana_principal.title("GUI 1")
ventana_principal.geometry("500x500")
ventana_principal.resizable(False,False)


# ----------------------------------------------------------------

# *  Elementos 
campo = tk.Frame(ventana_principal)
campo.grid(row = 0, column = 1, padx=80, pady=10)
mensaje1 = tk.Label(campo, text = "Numero 1: ")
mensaje1.configure(font = ("0rial", 20), fg = "black")
mensaje1.grid(padx=5, pady=10, row = 0, column = 0)

mensaje2 = tk.Label(campo, text = "Numero 2: ")
mensaje2.configure(font = ("Arial", 20), fg = "black")
mensaje2.grid(padx=5, pady=10, row = 0, column = 2)

entrada_texto1 = tk.Entry(campo)
entrada_texto1.configure(font = ("Arial", 12), fg = "black")
entrada_texto1.grid(row =1, column = 0)

entrada_texto2 = tk.Entry(campo)
entrada_texto2.configure(font = ("Arial", 12), fg = "black")
entrada_texto2.grid(row = 1, column = 2)


campo2 = tk.Frame(ventana_principal)
campo2.grid(row = 1, column = 1, padx=80, pady=10)
boton1 = tk.Button(campo2, text = "Suma")
boton1.configure(font = ("Arial", 20), fg = "black", command=suma)
boton1.grid(padx=5, pady=50, row =2, column = 1)

mensaje3 = tk.Label(campo2, text = "...")
mensaje3.configure(font = ("Arial", 20), fg = "black")
mensaje3.grid(padx=5, pady=10, row = 3, column = 1)



# ----------------------------------------------------------------


ventana_principal.mainloop()

