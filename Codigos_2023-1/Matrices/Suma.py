import tkinter as tk

def sumar_numeros():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2
        label_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        label_resultado.config(text="Error: Ingrese números válidos")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Suma de dos números")

# Crear los elementos de la interfaz
label_num1 = tk.Label(ventana, text="Número 1:")
label_num1.pack()

entry_num1 = tk.Entry(ventana)
entry_num1.pack()

label_num2 = tk.Label(ventana, text="Número 2:")
label_num2.pack()

entry_num2 = tk.Entry(ventana)
entry_num2.pack()

boton_sumar = tk.Button(ventana, text="Sumar", command=sumar_numeros)
boton_sumar.pack()

label_resultado = tk.Label(ventana, text="")
label_resultado.pack()

# Iniciar el bucle de eventos
ventana.mainloop()