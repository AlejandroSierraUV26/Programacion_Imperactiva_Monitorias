"""
Juego de la multiplicacion y division 
El juego consiste en generar dos numeros aleatorios
y generar la operacion aleatoria entre multiplicar o dividir

Si la operacion es multiplicar o dividir el usuario debe ingresar el resultado de la multiplicacion
si responde correctamente se le suma 1 punto
si la respuesta es incorrecta se le resta 1 punto

En la ultima operacion debera realizar una division y multiplicacion 
al mismo tiempo, mas compleja.

El juego termina cuando el usuario responde incorrectamente 3 veces
o cuando el usuario llega a 10 puntos
"""






import random

puntos = 0

while puntos < 10:
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    operacion = random.choice(["multiplicar","dividir"])
    
    if operacion == "multiplicar":
        resultado = num1 * num2
        respuesta = int(input(f"Cuanto es {num1} x {num2} : "))
    else:
        resultado = num1 / num2
        respuesta = int(input(f"Cuanto es {num1} / {num2} : "))
        
    if respuesta == resultado:
        puntos += 1
        print(f"Correcto! tienes {puntos} puntos")
    else:
        puntos -= 1
        print(f"Incorrecto! tienes {puntos} puntos")
        if puntos < 0:
            break
print("Fin del juego")
# Prueba final

num1 = random.randint(1,10)
num2 = random.randint(1,10)
num3 = random.randint(1,10)
num4 = random.randint(1,10)

resultado = (num1 * num2) / (num3 * num4)
print(f"Cuanto es {num1} x {num2} / {num3} x {num4} : ")
respuesta = int(input("Ingrese la respuesta : "))

puntos += 10 if respuesta == resultado else -5

print(f"Tu puntaje final es {puntos}")

