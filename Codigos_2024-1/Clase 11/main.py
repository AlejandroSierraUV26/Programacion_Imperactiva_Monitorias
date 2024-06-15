import interfaz
import interfaz2
import tkinter as tk

def cambiar_ventana1():
    ventana_principal.withdraw()
    interfaz.inicializar_ventana()

def cambiar_ventana2():
    ventana_principal.withdraw()
    interfaz2.inicializar_ventana()
def desactivar_ventana():
    ventana_principal.withdraw()
    
def principal():
    global ventana_principal
    ventana_principal = tk.Tk()
    ventana_principal.title("Ventana principal")
    ventana_principal.geometry("800x600")
    interfaz.funcion_rara(1,2)

    boton = tk.Button(ventana_principal, text="Abrir ventana", command=cambiar_ventana1)
    boton.pack()
    boton_sumar = tk.Button(ventana_principal, text="Sumar", command=lambda: (desactivar_ventana(), interfaz.ventana_con_parametros("Camilo Carechimba")))
    boton_sumar.pack()

    boton2 = tk.Button(ventana_principal, text="Abrir ventana 2", command=cambiar_ventana2)
    boton2.pack()

    ventana_principal.mainloop()


if __name__ == "__main__":
    print(interfaz.valores)
    
    

