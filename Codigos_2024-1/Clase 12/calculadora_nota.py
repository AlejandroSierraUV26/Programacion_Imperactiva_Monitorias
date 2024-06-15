# Realizar una calculadora de notas finales, con una interfaz sencilla

import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

def calcular_nota():
    try:
        notas = [float(nota.get()) for nota in notas_entries]
        creditos = [float(credito.get()) for credito in creditos_entries]
        nota_final = sum([notas[i] * creditos[i] for i in range(cantidad_asignaturas.get())]) / sum(creditos)
        nota_final_label.configure(text=f"Nota final: {nota_final}")
        
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido")
    
def ingresar_correcto_numero():
    try:
        cantidad_asignaturas = int(cantidad_asignaturas_entry.get())
        if cantidad_asignaturas <= 0:
            messagebox.showerror("Error", "Ingrese un número positivo")
        else:
            construir_interfaz()
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido")
def construir_interfaz():
    espacio = 2
    for i in range(int(cantidad_asignaturas_entry.get())):
        campo = ctk.CTkFrame(root)
        espacio += 2
        
        nombre_asignatura_label = tk.Label(campo, text=f"Asignatura {i+1}:", background="white", foreground="black")
        nombre_asignatura_label.grid(row=0 + espacio, column=0)
        
        nota1_label = ctk.CTkLabel(campo, text=f"Nota {i+1}:")
        nota1_label.grid(row=1 + espacio, column=0)
        


        nota1_entry = ctk.CTkEntry(campo)
        nota1_entry.grid(row=1 + espacio, column=1)
        notas_entries.append(nota1_entry)

        credito1_label = ctk.CTkLabel(campo, text=f"Créditos {i+1}:")
        credito1_label.grid(row=2 + espacio, column=0)

        credito1_entry = ctk.CTkEntry(campo)
        credito1_entry.grid(row=2 + espacio, column=1)
        creditos_entries.append(credito1_entry)
        
        campo_texto = ctk.CTkLabel(campo, text="")
        campo_texto.grid(row=3 + espacio, column=0)

        campo.pack()
    calcular_button = ctk.CTkButton(root, text="Calcular", command=calcular_nota)
    calcular_button.pack()
    global nota_final_label
    nota_final_label = ctk.CTkLabel(root, text="")
    nota_final_label.pack()

# root = ctk.CTk()
# root.title("Calculadora de notas")
# root.geometry("500x500")

# notas_entries = []
# creditos_entries = []


# texto = ctk.CTkLabel(root, text="Ingrese las notas y créditos de las asignaturas")
# texto.pack()

# cantidad_asignaturas = ctk.CTkLabel(root, text="Ingrese la cantidad de asignaturas")
# cantidad_asignaturas.pack()

# cantidad_asignaturas_entry = ctk.CTkEntry(root)
# cantidad_asignaturas_entry.pack()
# cantidad_asignaturas_button = ctk.CTkButton(root, text="Ingresar", command=ingresar_correcto_numero)
# cantidad_asignaturas_button.pack()










corredores = [["Alejandro", 120, 150, 167, 120, 1000], ["Sierra", 10, 10, 67, 20, 1020], ["Yop", 1220, 120, 137, 121, 140]]

menor = sum(corredores[0][1:])
posicion = 0
for i in range(len(corredores)):
    suma = sum(corredores[i][1:])
    print(suma)
    if suma < menor:
        menor = suma
        posicion = i
print(corredores[posicion][0])

    
    
    
    






















