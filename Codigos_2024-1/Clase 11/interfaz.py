import tkinter as tk
import main
def presionar():
    print("Presionaste el botón")

def funcion_rara(x,y):
    return x + y
def desactivar_ventana():
    ventana.deiconify()
def ventana_con_parametros(parametro):
    ventana2 = tk.Tk()
    ventana2.geometry("400x400")
    label = tk.Label(ventana2, text=parametro)
    label.pack()
    ventana2.mainloop()
    
def inicializar_ventana():
    global ventana
    ventana = tk.Tk()
    ventana.title("Mi primera ventana")
    ventana.geometry("800x600")

    etiqueta = tk.Label(ventana, text="Hola mundo")
    etiqueta.pack()
    boton = tk.Button(ventana, text="Presionar", command=devolver_main)
    boton.pack()

    ventana.mainloop()
def devolver_main():
    ventana.withdraw()
    main.principal()


valores = [1,2,3,4,5]