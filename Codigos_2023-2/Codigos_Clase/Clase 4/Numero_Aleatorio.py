import random 
numero_aletorio = random.randint(1, 10)

"""
Tiene 3 posibilidades de adivinarlo

Si pierdes mas de 3 numeros.
"""
#! Se realiza la toma del valor numero por entrada.
numero = int(input("Adivina un numero del 1 al 10: "))

if(numero == numero_aletorio):
    print("GANASTE!!!")
else:
    print("No adivinaste el numero")
    print("Te quedan dos vidas")
    numero = int(input("Adivina un numero del 1 al 10: "))
    if(numero ==numero_aletorio):
        print("GANASTE!!!")
    else:
        print("No adivinaste el numero")
        print("Te quedan una vidas")
        numero = int(input("Adivina un numero del 1 al 10: "))
        if(numero == numero_aletorio):
            print("GANASTE!!!")
        else:
            print("No adivinaste el numero")
print("El numero era : ", numero_aletorio)    