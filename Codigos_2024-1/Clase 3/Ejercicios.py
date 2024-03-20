"""
Ejercicios para practicar el uso de las funciones en Python.
3174031895

1. Crear una funcion que reciba un numero entero y retorne el factorial de ese numero.
Ejemplo: factorial(5) -> 120

2. Crear una funcion que reciba un numero entero y retorne True si es par, False si es impar.
Ejemplo: es_par(5) -> False

3. Realizar una funcion que reciba un precio y retorne el precio con el IVA incluido.
Ejemplo: precio_con_iva(100, 19) -> 119

4. Crear una funcion que reciba un numero entero y retorne el numero invertido.
Ejemplo: invertir_numero(1234) -> 4321

5. Realizar una funcion que reciba un numero representado como el grado farenheit 
y retorne el valor en grados celsius.
Ejemplo: farenheit_a_celsius(32) -> 0
Formula  ===>                           Celcius = (Farenheit - 32) * 5/9

6. Verificar si un numero de 4 digitos es capicua.
(Se lee igual de derecha a izquierda que de izquierda a derecha)
Ejemplo: es_capicua(1234) -> False
Ejemplo: es_capicua(1221) -> True
Ejemplo: es_capicua(12321) -> True

7. Crear una funcion que reciba un numero entero 
y retorne el numero en binario.
Ejemplo: decimal_a_binario(10) -> 1010
Ejemplo: decimal_a_binario(5) -> 101
Ejemplo: decimal_a_binario(100) -> 1100100

Pista:
 
Bucle While
Concatenacion
Modulo




"""
numero = int(input("Ingrese el numero factorial a averiguar : "))

def factorial(numero):
    if numero == 0:
        return 1
    else: 
        return numero * factorial(numero - 1)

print(factorial(5))
def Es_par(numero): 
    if numero % 2 == 0:
        return True
    else:
        return False


def aplicar_iva(precio_neto, iva):
    return precio_neto + precio_neto* iva 


def invertido(numero):
    numero = str(numero)
    numero_invertido = numero[::-1]
    return int(numero) == int(numero_invertido)       

def farenheit_a_celsius(grados_farenheit):
    grados_celsius = (grados_farenheit - 32) * 5/9
    return grados_celsius
    
def Es_capicua(numero):
    return str(numero) == str(numero)[::-1]

def decimal_a_binario(numero):
    if numero == 0:
        return '0'
    binario = ''
    while numero > 0:
        binario = str(numero % 2) + binario
        numero //=2
    return binario

print(decimal_a_binario(10))


