"""
Diseñe un algoritmo que imprima en pantalla el conjunto de 
los multiplos enteros (x) digitado por el usuario.
"""

def multiplos(numero):
    for i in range(0,numero+1):
        for j in range(0,numero+1):
            if i*j == numero:
                print(i,j)

"""
Diseñe un algoritmo que imprima en pantalla el conjunto de los divisiores de un
entero (x) digitado por el usuario.
"""

def divisores(numero):
    for i in range(1,numero+1):
        if numero%i == 0:
            print(i)
        
        
"""
Diseñe un algoritmo que calcule e imprima las tablas de multiplicar del 1 al 9.

"""


# for i in range(1,10):
#     print("===========")
#     for j in range(1,10):
#         print(i,"x",j,"=",i*j)

"""
Diseñe un algoritmo que imprima las siguientes series para n terminos:

1. 4 8 12 16 20 24 28 32 36 40 44

2. 1 4 9 16 25 36 49 64 81

3. 2 -4 6 -8 10 -12

4. 1 2 4 8 16 32 64 128 256 512 1024


"""
# n = 6

# for i in range(1,n+1):
#     print(i*4, end=" ")
# print()
# for i in range(1,n+1):
#     print(i**2, end=" ")
# print()
# for i in range(1,n+1):
#     print(i*2*(-1)**(i+1), end=" ")
# print()
# for i in range(1,n+1):
#     print(2**i, end=" ")



"""
Diseñe un algoritmo que imprima los primeros 10 numeros de la serie de Fibonacci.


"""

def fibonnaci(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonnaci(numero-1) + fibonnaci(numero-2)

# print(fibonnaci(10))

# a,b = 0,1
# i = 0
# while(i<10):
#     i+=1
#     a,b = b,a+b
#     print(b)


"""
Diseñe un algoritmo que permita calcular si un numero es primo o no, recuerde que los numeros primos son 
aquellos que solo son divisibles por una unidad y por ellos mismos.


"""



def es_primo(numero):
    contador = 0
    for i in range(2,numero):
        if numero % i == 0:
            contador+=1
    if contador>=1:
        return False
    return True

#print("Es primo" if es_primo(13) else "No es primo")

"""

Diseñe un algoritmo que capture 10 numeros determine si son primos, si estan dentro de los numeros de 
fibonnaci, en caso de no ser primos y no estar en la serie de fibonnaci, imprima el numero, con sus 
divisores y multiplos.


Suerte!
"""

def funcion_potente(numero):
    # 0 1 1 2 3 5 8 13 21 34
    if es_primo(numero):
        if numero in [fibonnaci(i) for i in range(10)]:
            print(f"El numero es primo {numero} y esta en la serie de fibonnaci")
        else:
            print(f"El numero es primo {numero} y no esta en la serie de fibonnaci")
    else:
        print(f"El numero no es primo {numero}")
        print("Divisores")
        divisores(numero)
        print("Multiplos")
        multiplos(numero)
        
for i in range(1,10,2):
    funcion_potente(i)