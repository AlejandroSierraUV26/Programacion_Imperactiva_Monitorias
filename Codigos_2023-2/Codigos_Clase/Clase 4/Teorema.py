"""
Realiza la conjetura de Collazt con recursividad


La conjetura de Collatz, también conocida como conjetura 3x + 1 o conjetura de Ulam (entre otros nombres),
es una conjetura matemática que afirmaba lo siguiente:

Dado un número entero cualquiera, si es par se divide entre 2 y si es impar se multiplica por 3 y se le suma 1.

Esta operación se repite sucesivamente con el resultado de la operación anterior hasta llegar a 1.

Por ejemplo, para el número 6, la secuencia sería la siguiente:

6, 3, 10, 5, 16, 8, 4, 2, 1

Para el número 13, la secuencia sería la siguiente:

13, 40, 20, 10, 5, 16, 8, 4, 2, 1

Se puede observar que, para el número 6, la secuencia contiene 9 términos y, para el número 13, 10 términos.

Se pide crear una función recursiva que reciba un número entero positivo y devuelva la longitud de la secuencia de Collatz de dicho número.

Por ejemplo, para el número 6, la función debe devolver el valor 9 y, para el número 13, la función debe devolver el valor 10.

Nota: La función debe validar que el número recibido sea entero positivo, en caso contrario debe devolver el valor -1.


"""

def collazt(numero):
    if numero == 1: return 1
    elif numero % 2 == 0: return collazt(numero/2)
    else: return collazt((numero*3)+1)

print(collazt(6))