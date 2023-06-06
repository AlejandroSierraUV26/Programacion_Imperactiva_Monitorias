import random

nombres = ["Alejandro","Maria","Karen","Daniel","John","Juan","Sebastian","Camila"]
apellidos = ["Sierra","Valencia","Rodriguez","Gomez","Lopez","Muñoz","Garcia","Torres"]

for i in range(30):
    numero_nombre = random.randint(0, len(nombres)-1)
    numero_apellido = random.randint(0, len(apellidos)-1)
    print(f"Persona {i+1}\n")
    print(nombres[numero_nombre] + " " + apellidos[numero_apellido])

