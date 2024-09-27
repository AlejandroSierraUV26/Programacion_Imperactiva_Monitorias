import random

nombres = ["Alejandro", "Pepe", "Mia", "Lulu", "Luna", "Abel", "Sofai", "Roberta"]
def generar_personas():
    nombre = random.choice(nombres) # Elige un elemento aleatorio de la lista
    edad = random.randint(10,25) # Elige una edad entre ese rango
    genero_persona = random.randint(0,1) # Elige el genero
    
    return nombre, edad, genero_persona
def verificar_informacion():
    global genero
    nombre, edad, genero = generar_personas()
    print(nombre, edad, genero)
    if genero == 0:
        print("Usted es un hombre")
    else: 
        print("Usted es una mujer")
def contar_generos():
    acc_hombres = 0
    acc_mujeres = 0
    for i in range(10):
        verificar_informacion()
        if genero == 0:
            acc_hombres += 1
        else: 
            acc_mujeres += 1
    print(f"total de hombres : {acc_hombres}")
    print(f"total de mujeres : {acc_mujeres}")
contar_generos()



