import numpy
import random
from colorama import Fore

"""
Generar 100 personas aleatorias con las siguientes características:

- Nombre: String de longitud aleatoria entre 5 y 10 caracteres
- Numero: Tiene que tener 5 digitos
- Lugar de compra:


Existen 2 ganadores:

- Quienes tengan los 5 numeros
- Quienes tengan los 4 primeros numeros

"""
# Generar 100 nombres aleatorios



def generar_persona():
    persona = {}
    persona["nombre"] = random.choice(nombre)
    persona["numero"] = random.randint(10000, 99999)
    persona["lugar"] = random.choice(lugares)
    return persona
def comprobar_4digitos(numero_ganador, numero_persona):
    numero_ganador = str(numero_ganador)
    numero_persona = str(numero_persona)
    numero_ganador = numero_ganador[0:4]
    numero_persona = numero_persona[0:4]
    if numero_ganador == numero_persona:
        return True
    else:
        return False
def comprobar_5digitos(numero_ganador, numero_persona):
    if numero_ganador == numero_persona:
        return True
    else:
        return False

def mostrar_persona(persona):
    print("Nombre: ", persona["nombre"])
    print("Numero: ", persona["numero"])
    print("Lugar: ", persona["lugar"])
    print("\n")
    
def mostrar_ganadores(ganadores):
    for persona in ganadores:
        mostrar_persona(persona)
        
def lista_vacia(lista):
    if len(lista) == 0:
        return True
    return False
lugares = ["Cali", "Tuluá", "Buga", "Caicedonia", "Cartago"]
nombre = ["Juan", "Pedro", "Maria", "Luisa", "Andres", "Carlos", "Sofia", "Camila", "Laura", "Valentina"]
numero_ganador = random.randint(10000, 99999)

print(Fore.YELLOW)
print(f"----------------------{numero_ganador}----------------------")
print(Fore.RESET)
ganadores5=[]
ganadores4=[]
for i in range(99999):
    persona = generar_persona()
    if comprobar_5digitos(numero_ganador, persona["numero"]):
        ganadores5.append(persona)
    elif comprobar_4digitos(numero_ganador, persona["numero"]):
        ganadores4.append(persona)        
print(Fore.MAGENTA)
print("--------------Ganadores de 5 digitos--------------")
print(Fore.RESET)
if lista_vacia(ganadores5):
    print(Fore.RED + "No hay ganadores de 5 digitos")
    print(Fore.RESET)
mostrar_ganadores(ganadores5)

print(Fore.MAGENTA)
print("--------------Ganadores de 4 digitos--------------")
print(Fore.RESET)
if lista_vacia(ganadores4):
    print(Fore.GREEN + "No hay ganadores de 5 digitos")
    print(Fore.RESET)
mostrar_ganadores(ganadores4)



