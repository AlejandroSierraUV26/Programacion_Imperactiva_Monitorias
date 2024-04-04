"""
Calculadora simple: Crea un programa que pida al usuario dos números y realice las cuatro operaciones básicas 
(+, -, *, /) con esos números. El usuario debe elegir desde el inicio cual operación hacer, puede ser con un
menú que le pida un número de opción. Ej: 1. Suma, 2. Resta…
"""

# print("------------Calculadora en python------------")

# num1 = float(input("Ingrese el primer numero : "))
# num2 = float(input("Ingrese el segundo numero : "))


# print("Opciones disponibles : ")
# print("1. Suma (+) \n2. Resta (-) \n3. Multiplicacion(*) \n4. Division (/)")
# opcion = int(input("Ingrese la opcion que requiera :"))
# resultado = 0

# while False:
#     if opcion == 1:
#         resultado = num1 + num2
#         break
#     elif opcion == 2: 
#         resultado = num1 - num2
#         break
#     elif opcion == 3:
#         resultado = num1 * num2
#         break
#     elif opcion == 4:
#         resultado = num1 / num2
#         break
#     else:
#         print("¡Opcion Incorrecta!")
#         opcion = int(input("Ingrese la opcion nuevamente : "))
        
# print("El resultado es ", resultado)
    


"""

Contador de números pares e impares: Escribe un programa que solicite al usuario un número entero positivo y 
luego cuente y muestre la cantidad de números pares e impares entre 1 y el número ingresado.

Tabla de multiplicar: Solicita al usuario un número y muestra la tabla de multiplicar de ese número del 1 al 10.

Suma de los primeros n números naturales: Pide al usuario un número entero positivo 'n' y muestra la suma de los primeros 
'n' números naturales.

Factorial de un número: Pide al usuario un número entero positivo y calcula su factorial.

Verificación de números primos: Pide al usuario un número entero positivo y muestra si es primo o no.

Contador de dígitos: Pide al usuario un número entero positivo y cuenta y muestra la cantidad de dígitos en ese número.

Contador de unidades, decenas y centenas: Pide al usuario un número entero positivo y cuenta y muestra la cantidad de 
unidades, decenas y centenas que este tiene. Ejemplo: 456 tiene 4 centenas, 5 decenas y 6 unidades.


"""

# while True:
#     numero = int(input("Ingrese un numero de 3 digitos :"))
#     if numero >= 100 and numero <1000:
#         break
#     else: 
#         print("¡Ingrese el valor nuevamente!")

# centenas = numero // 100
# numero = numero % 100
# deceneas = numero // 10
# numero = numero % 10
# unidades = numero 


# print(f"{centenas} Centenas , {deceneas} Decenas , {unidades} Unidades")



numero = int(input("Ingrese un numero cualquiera : "))
print(numero)

while numero != 1:
    if numero % 2 == 0:
        numero = numero / 2
    else:
        numero =(3 * numero)+ 1 
    print(numero)
print("Funciono")















