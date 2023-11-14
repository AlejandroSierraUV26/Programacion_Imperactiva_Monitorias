import tkinter as tk
import numpy 

def sumar_numeros():
    numero1 = int(entrada1.get()) 
    numero2 = int(entrada2.get())
    
    resultado = numero1 + numero2
    
    resultado1.configure(text = f"{resultado}", font = ("Arial",12))
    

ventana = tk.Tk() 
ventana.geometry("500x500")
ventana.title("Calculadora")
ventana.resizable(False,False)

texto1 = tk.Label(ventana, text = "Calculadora en Python", font = ("Arial",15))
texto1.grid(row = 0 , column = 0, padx = 10, pady = 10)

texto2 = tk.Label(ventana, text = "Ingrese el primer numero :")
texto2.grid(row = 1 , column = 0)

entrada1 = tk.Entry(ventana)
entrada1.grid(row = 2 , column = 0)


texto3 = tk.Label(ventana, text = "Ingrese el segundo numero : ")
texto3.grid(row = 1 , column = 2)


entrada2 = tk.Entry(ventana)
entrada2.grid(row = 2 , column = 2)

boton1 = tk.Button(ventana, text = "Sumar numeros" , command = sumar_numeros)
boton1.grid(row = 3 , column = 0)

resultado1 = tk.Label(ventana, text = "")
resultado1.grid(row = 4 , column = 1, pady = 50)

ventana.mainloop()



