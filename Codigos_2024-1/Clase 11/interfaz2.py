import tkinter as tk


def desactivar_ventana():
    ventana.deiconify()
    

def inicializar_ventana():
    ventana = tk.Tk()

    ventana.title("Mi primera ventana")
    ventana.geometry("800x600")

    etiqueta = tk.Label(ventana, text="Hola mundo")

    etiqueta.pack()


    boton = tk.Button(ventana, text="Presioname", command=lambda : print("Sapo Camilo"))
    boton.pack()


    ventana.mainloop()
