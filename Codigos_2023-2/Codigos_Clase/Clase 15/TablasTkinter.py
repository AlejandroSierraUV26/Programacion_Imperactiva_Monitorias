import tkinter as tk
from tkinter import ttk

def agregar_elemento():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    # Agregar el elemento al Treeview
    tree.insert('', 'end', text=str(len(tree.get_children()) + 1), values=(nombre, edad))
    # Limpiar las entradas después de agregar el elemento
    entry_nombre.delete(0, 'end')
    entry_edad.delete(0, 'end')

def eliminar_elemento():
    # Obtener el índice seleccionado
    seleccion = tree.focus()
    if seleccion:
        tree.delete(seleccion)

root = tk.Tk()
tree = ttk.Treeview(root)
tree['columns'] = ('Name', 'Age')

tree.column('#0', width=50)
tree.column('Name', width=100)
tree.column('Age', width=50)

tree.heading('#0', text='ID')
tree.heading('Name', text='Name')
tree.heading('Age', text='Age')

tree.pack()

# Entradas para el nombre y la edad
label_nombre = tk.Label(root, text='Nombre:')
label_nombre.pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

label_edad = tk.Label(root, text='Edad:')
label_edad.pack()
entry_edad = tk.Entry(root)
entry_edad.pack()

agregar_button = tk.Button(root, text='Agregar', command=agregar_elemento)
agregar_button.pack()

eliminar_button = tk.Button(root, text='Eliminar', command=eliminar_elemento)
eliminar_button.pack()

root.mainloop()
