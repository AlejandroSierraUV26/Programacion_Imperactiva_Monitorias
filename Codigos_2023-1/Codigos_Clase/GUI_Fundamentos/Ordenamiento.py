import tkinter as tk
from tkinter import messagebox

def validar_credenciales(usuario, contrasena):
    # Aquí deberías realizar la lógica para validar las credenciales.
    # Esto es solo un ejemplo simple.
    return usuario == "usuario" and contrasena == "contrasena"

def iniciar_sesion():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    if validar_credenciales(usuario, contrasena):
        messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso")
        # Puedes agregar aquí la lógica para abrir la siguiente ventana o realizar otras acciones después del inicio de sesión
    else:
        messagebox.showerror("Error", "Credenciales incorrectas")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Inicio de Sesión")

# Crear widgets (etiquetas, entradas, botones)
label_usuario = tk.Label(ventana, text="Usuario:")
label_contrasena = tk.Label(ventana, text="Contraseña:")
entry_usuario = tk.Entry(ventana)
entry_contrasena = tk.Entry(ventana, show="*")  # La opción show="*" oculta las contraseñas
boton_iniciar_sesion = tk.Button(ventana, text="Iniciar Sesión", command=iniciar_sesion)

# Colocar widgets en la ventana
label_usuario.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
label_contrasena.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
entry_usuario.grid(row=0, column=1, padx=10, pady=5)
entry_contrasena.grid(row=1, column=1, padx=10, pady=5)
boton_iniciar_sesion.grid(row=2, column=0, columnspan=2, pady=10)

# Obtener el tamaño de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Obtener las dimensiones de la ventana
ancho_ventana = 300  # Ajusta según sea necesario
alto_ventana = 150  # Ajusta según sea necesario

# Calcular las coordenadas para centrar la ventana
x_pos = (ancho_pantalla - ancho_ventana) // 2
y_pos = (alto_pantalla - alto_ventana) // 2

# Establecer la geometría de la ventana para centrarla
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

# Iniciar el bucle principal
ventana.mainloop()
