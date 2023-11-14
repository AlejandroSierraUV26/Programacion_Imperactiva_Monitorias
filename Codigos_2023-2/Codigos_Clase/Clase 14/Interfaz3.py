import tkinter as tk 

def suma():
    numero1 = int(entrada1.get())
    numero2 = int(entrada2.get())
    operacion = numero1 + numero2	
    texto_resultado.configure(text = f"El resultado es {operacion}", font = ("Arial",20))
def resta():
    numero1 = int(entrada1.get())
    numero2 = int(entrada2.get())
    operacion = numero1 - numero2	
    texto_resultado.configure(text = f"El resultado es {operacion}", font = ("Arial",20))
def multiplicacion():
    numero1 = int(entrada1.get())
    numero2 = int(entrada2.get())
    operacion = numero1 * numero2	
    texto_resultado.configure(text = f"El resultado es {operacion}", font = ("Arial",20))
def division():
    numero1 = int(entrada1.get())
    numero2 = int(entrada2.get())
    operacion = numero1 / numero2	
    texto_resultado.configure(text = f"El resultado es {operacion}", font = ("Arial",20))

# ----------------------------------------------------------------
ventana1 = tk.Tk()

ventana1.geometry("1000x400")

ventana1.title("Calculadora")

ventana1.resizable(False,False)

# ----------------------------------------------------------------

campo1 = tk.Frame(ventana1, background="red")
campo1.grid(row = 0, column= 0)
texto1 = tk.Label(campo1, text = "Ingrese el primer numero : ")
texto1.grid(row = 0, column= 0)

entrada1 = tk.Entry(campo1)
entrada1.grid(row = 1, column= 0)

texto2 = tk.Label(campo1, text = "Ingrese el segundo numero : ")
texto2.grid(row = 0, column= 1)

entrada2 = tk.Entry(campo1)
entrada2.grid(row = 1, column= 1)


boton1 = tk.Button(campo1, text = "(+)", command = suma)
boton1.grid(row= 0, column= 2)

boton2 = tk.Button(campo1, text = "(-)", command = resta)
boton2.grid(row= 1, column= 2)

boton3 = tk.Button(campo1, text = "(x)", command = multiplicacion)
boton3.grid(row= 2, column= 2)

boton4 = tk.Button(campo1, text = "(/)", command = division)
boton4.grid(row= 3, column= 2)

texto_resultado = tk.Label(ventana1, text = "")
texto_resultado.grid(row = 0, column = 1, padx = 50, pady = 75)


ventana1.mainloop()