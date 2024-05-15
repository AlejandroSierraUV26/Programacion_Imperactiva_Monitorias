import random
def generar_nombres():
    nombres = ["Alejandro", "Juan", "Pedro", "Maria", "Luis", "Carlos", "Andres", "Sofia", "Camila", "Laura"]
    apellidos = ["Sierra","Gomez", "Perez", "Rodriguez", "Gonzalez", "Hernandez", "Sanchez", "Torres", "Ramirez", "Diaz", "Lopez"]

    nombre_completo = random.choice(nombres) + " " + random.choice(apellidos)
    return nombre_completo


balotas_ganadoras = [30,33,28,1]
super_balota = 5

for i in range(1_000_000):
    balotas = (random.sample(range(1,43),4))
    super_balota = random.randint(1,15)
    nombre = generar_nombres()
    if balotas == balotas_ganadoras:
        print(i)
        print(f"La persona {nombre} ha ganado el baloto!")
        print(f"Balotas ganadoras: {balotas} Superbalota: {super_balota}")
        break
    
    
    


