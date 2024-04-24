"""
Ejercicio 1:
Se tiene una empresa que necesita descontar de su nomina
los impuestos de sus empleados, para ello se necesita
calcular el salario neto de cada empleado.

Se tiene la siguiente tabla de impuestos:

    - Si el salario es menor a 10,000, no se le descuenta nada.
    - Si el salario es mayor a 10,000 y menor a 20,000, se le descuenta el 10%.
    - Si el salario es mayor a 20,000 y menor a 30,000, se le descuenta el 15%.
    - Si el salario es mayor a 30,000, se le descuenta el 20%.


Asi mismo tambien debe pagar el seguro social, el cual es el 5% del salario.

Se necesita un programa que reciba el salario de un empleado

y calcule el salario neto del empleado.

Ejemplo:

    Salario: 15000
    Impuesto: 10%
    Seguro Social: 5%
    Salario Neto: 13500



Ejercicio 2:

Mostar los numeros primos gemelos:

Los numeros primos gemelos son aquellos numeros primos que
estan separados por dos unidades, por ejemplo 11 y 13.

Se necesita un programa que muestre los numeros primos gemelos
hasta un numero dado.

Ejemplo:

    Numero: 20
    Numeros primos gemelos: (3, 5), (11, 17)
     


Ejercicio 3:
Mostar los primeros n numeros primos.

Se necesita un programa que muestre los primeros n numeros primos.

Ejemplo:
    
        Numero: 5
        Numeros primos: 2, 3, 5, 7, 11


Ejercicio 4:

Se tiene un numero superior a dos cifras, su tarea es sumar sus digitos e indicar cual es su valor final, debe ser de una cifra


Ejemplo:
    
        Numero: 1234
        (1+2+3+4) = 10
        (1 + 0) = 1
        Valor final: 1 

        Numero: 99991
        (9+9+9+9+1) = 37
        (3+7) = 10
        (1+0) = 1
        
        
"""

# Ejercicio 2:


def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def numeros_primos_gemelos(numero):
    # No listas
    for i in range(2, numero):
        if es_primo(i) and es_primo(i + 2):
            print(f"({i}, {i + 2})")
    

numeros_primos_gemelos(20)



    
    
    
    
    
    
    