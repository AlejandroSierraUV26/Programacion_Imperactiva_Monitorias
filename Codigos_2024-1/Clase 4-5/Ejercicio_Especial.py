"""
Diseñe un algoritmo que capture 10 numeros, determine si son primos y 
si estan dentro de los numeros de fibonnaci, en caso de no ser primos 
y no estar en la serie de fibonnaci, imprima el numero, con sus 
divisores y multiplos.

Diseñar funciones para cada procedimiento.

"""
import random

def definir_numeros():
    while (True):
        numero1 = random.randint(1,10)
        numero2 = random.randint(1,10)
        if not(numero1 == 3 or numero2 == 3 or numero1 == 5 or numero2 == 5):
            break    
    return numero1,numero2
def juego():
    puntos = 0
    for i in range(1,10+1):
        print(f"Pregunta numero  {i}")
        num1, num2 = definir_numeros()
        respuesta1 = int(input(f"Cuanto da multiplicacion de {num1} * {num2} = "))
        if respuesta1 == num1 * num2:
            puntos += 1
        else:
            print("Vos sos pendejo")
            
    print(f"Su total de puntos es {puntos}")
    
if __name__ == "__main__":
    juego()
    
    
    
    
    
    
# i = 1
# while i<100:
#     if i % 7 == 0:
#         i+=1
#         continue
#     if i == 50:
#         break
#     print(i)
#     i+=1    

    
    
    
    
    
    
    
    
    
