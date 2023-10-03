import random
import time
def numero_aleatorio():
    numero = random.randint(1, 8)
    return numero
    


for i in range(0,3):
    time.sleep(2)
    print(numero_aleatorio())