"""
Ejercicio 1. 

Pedir al usuario que ingrese dos numeros, uno entero y uno decimal, 
verificar que no tengan errores de ningun tipo y mostrar la 
division de ambos. 

Decimal numerador y entero denominador.

"""

print("Se va a dividir el primer numero por el segundo....")
while(True):
    print("")
    try: 
        numero_entero = int(input("Ingrese un numero entero : "))
        numero_decimal = float(input("Ingrese un numero decimal : "))
        print("")
        print(numero_entero/numero_decimal)
        break
    except ValueError: 
        print("Por favor ingrese valores numericos")
    except ZeroDivisionError:
        print("No es posible la division por 0")
print("Programa finalizado con exito")
