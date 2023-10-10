# # FILEPATH: multiplication_tables.py

# Multiplication tables from 1 to 10
for i in range(1, 11):
    print(f"Multiplication table of {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print()




import random
import time


for i in range(0,3):
    numero = random.randint(1,21)
    time.sleep(3)
    print("Persona :", numero)
def secuencia(numero):
    if numero == 5:
        return 1
    else: 
        return 20 + secuencia(numero-1)
    
print(secuencia(20))
