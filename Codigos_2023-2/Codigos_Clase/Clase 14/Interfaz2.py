import tkinter as tk
from PIL import Image, ImageTk
import numpy 

def sumar_numeros():
    numero1 = int(entrada1.get()) 
    numero2 = int(entrada2.get())
    
    resultado = numero1 + numero2
    
    resultado1.configure(text = f"El resultado es {resultado}", font = ("Arial",20))
    
def restar_numeros():
    numero1 = int(entrada1.get()) 
    numero2 = int(entrada2.get())
    
    resultado = numero1 - numero2
    
    resultado1.configure(text = f"El resultado es {resultado}", font = ("Arial",20))

def dividir_numeros():
    numero1 = int(entrada1.get()) 
    numero2 = int(entrada2.get())
    
    resultado = numero1 / numero2
    
    resultado1.configure(text = f"El resultado es {resultado}", font = ("Arial",20))

def multiplicar_numeros():
    numero1 = int(entrada1.get()) 
    numero2 = int(entrada2.get())
    
    resultado = numero1 * numero2
    
    resultado1.configure(text = f"El resultado es {resultado}", font = ("Arial",20))
    

ventana = tk.Tk() 
ventana.geometry("510x500")
ventana.title("Calculadora")
ventana.resizable(False,False)

campo1 = tk.Frame(ventana, background="red")
campo1.grid(row = 0, column = 0)


texto1 = tk.Label(campo1, text = "Calculadora en Python", font = ("Arial",15))
texto1.grid(row = 0 , column = 0, padx = 10, pady = 10)

texto2 = tk.Label(campo1, text = "Ingrese el primer numero :")
texto2.grid(row = 1 , column = 0)

entrada1 = tk.Entry(campo1)
entrada1.grid(row = 2 , column = 0)


texto3 = tk.Label(campo1, text = "Ingrese el segundo numero : ")
texto3.grid(row = 1 , column = 2)


entrada2 = tk.Entry(campo1)
entrada2.grid(row = 2 , column = 2)

campo2 = tk.Frame(ventana, background="blue")
campo2.grid(row = 1, column = 0, padx = 5, pady = 5)

boton1 = tk.Button(campo2, text = "(+)Sumar numeros" , command = sumar_numeros)
boton1.grid(row = 3 , column = 0, padx = 5, pady = 5)

boton1 = tk.Button(campo2, text = "(-)Restar numeros" , command = restar_numeros)
boton1.grid(row = 3 , column = 1, padx = 5, pady = 5)

boton1 = tk.Button(campo2, text = "(*)Dividir numeros" , command = dividir_numeros)
boton1.grid(row = 3 , column = 2, padx = 5, pady = 5)

boton1 = tk.Button(campo2, text = "(/)Multiplicar numeros" , command = multiplicar_numeros)
boton1.grid(row = 3 , column = 3, padx = 5, pady = 5)


campo3 = tk.Frame(ventana)
campo3.grid(row = 3, column = 0)
resultado1 = tk.Label(campo3, text = "")
resultado1.grid(row = 4 , column = 1, pady = 50)



ventana.mainloop()



