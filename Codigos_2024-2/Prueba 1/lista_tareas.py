import tkinter as tk
from tkinter import messagebox, simpledialog

# Funciones principales
def agregar_tarea():
    tarea = simpledialog.askstring("Agregar tarea", "Ingrese la tarea:")
    if tarea:
        tareas.append({"tarea": tarea, "realizada": False})
        actualizar_lista_tareas()
        guardar_tareas()

def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        indice = seleccion[0]
        tarea_eliminada = tareas.pop(indice)
        messagebox.showinfo("Eliminar tarea", f"Tarea '{tarea_eliminada['tarea']}' eliminada.")
        actualizar_lista_tareas()
        guardar_tareas()
    else:
        messagebox.showwarning("Eliminar tarea", "Seleccione una tarea para eliminar.")

def marcar_tarea_realizada():
    seleccion = lista_tareas.curselection()
    if seleccion:
        indice = seleccion[0]
        tareas[indice]["realizada"] = True
        messagebox.showinfo("Marcar tarea", f"Tarea '{tareas[indice]['tarea']}' marcada como realizada.")
        actualizar_lista_tareas()
        guardar_tareas()
    else:
        messagebox.showwarning("Marcar tarea", "Seleccione una tarea para marcar como realizada.")

def actualizar_lista_tareas():
    lista_tareas.delete(0, tk.END)
    for tarea_dic in tareas:
        estado = "Realizada" if tarea_dic["realizada"] else "Pendiente"
        lista_tareas.insert(tk.END, f"{tarea_dic['tarea']} - {estado}")

def guardar_tareas():
    with open("tareas.txt", "w") as archivo:
        for tarea_dic in tareas:
            archivo.write(f"{tarea_dic['tarea']},{tarea_dic['realizada']}\n")

def cargar_tareas():
    global tareas
    tareas = []
    try:
        with open("tareas.txt", "r") as archivo:
            for linea in archivo:
                tarea, realizada = linea.strip().split(",")
                tareas.append({"tarea": tarea, "realizada": realizada == "True"})
        actualizar_lista_tareas()
        messagebox.showinfo("Cargar tareas", "Tareas cargadas exitosamente.")
    except FileNotFoundError:
        messagebox.showwarning("Cargar tareas", "No se encontró el archivo de tareas.")

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Gestor de Tareas")

# Centrando la ventana en la pantalla
ancho_ventana = 500
alto_ventana = 400
pantalla_ancho = ventana.winfo_screenwidth()
pantalla_alto = ventana.winfo_screenheight()
pos_x = (pantalla_ancho // 2) - (ancho_ventana // 2)
pos_y = (pantalla_alto // 2) - (alto_ventana // 2)
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

# Estilo
font_estilo = ("Arial", 12)

frame_lista = tk.Frame(ventana)
frame_lista.pack(pady=20)

scrollbar = tk.Scrollbar(frame_lista)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lista_tareas = tk.Listbox(frame_lista, height=10, width=50, font=font_estilo, yscrollcommand=scrollbar.set)
lista_tareas.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.config(command=lista_tareas.yview)

# Botones de acciones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=20)

btn_agregar = tk.Button(frame_botones, text="Agregar tarea", width=15, font=font_estilo, command=agregar_tarea)
btn_agregar.grid(row=0, column=0, padx=10, pady=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar tarea", width=15, font=font_estilo, command=eliminar_tarea)
btn_eliminar.grid(row=0, column=1, padx=10, pady=5)

btn_marcar = tk.Button(frame_botones, text="Marcar como realizada", width=20, font=font_estilo, command=marcar_tarea_realizada)
btn_marcar.grid(row=0, column=2, padx=10, pady=5)

btn_guardar = tk.Button(frame_botones, text="Guardar tareas", width=15, font=font_estilo, command=guardar_tareas)
btn_guardar.grid(row=1, column=0, padx=10, pady=5)

btn_cargar = tk.Button(frame_botones, text="Cargar tareas", width=15, font=font_estilo, command=cargar_tareas)
btn_cargar.grid(row=1, column=1, padx=10, pady=5)

btn_salir = tk.Button(frame_botones, text="Salir", width=15, font=font_estilo, command=ventana.quit)
btn_salir.grid(row=1, column=2, padx=10, pady=5)

# Variables globales
tareas = []

# Cargar las tareas al iniciar la aplicación
cargar_tareas()

# Iniciar la interfaz gráfica
ventana.mainloop()
