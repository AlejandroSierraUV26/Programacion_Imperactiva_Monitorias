import math

def raiz(x):
    return math.sqrt(x)
def log(x,b):
    return math.log(x,b)

def suma(a,b):
    return a + b
def cos(x):
    return math.cos(x)
def sen(x):
    return round(math.sin(x)

# print(raiz(25))
# print(log(64,2))
print(sen(45))
print(cos(0))

print("""
Realizar una calculadora cientifica pueden apoyarse de la libreria math
la idea es realizar por cada operacion  una funcion que reciba los parametros necesarios
y que regrese el resultado de la operacion

1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Potencia
6. Raiz cuadrada
7. Seno 
8. Coseno
9. Tangente
10. Logaritmo
11. Logaritmo en base 10
12. Factorial
13. e^x
14. Salir
""")
opcion = int(input("Ingrese la operacion que desea realizar : "))

# def suma(n1,n2):
#         return n1 + n2
# def resta(n1,n2):
#         return n1 - n2
# def multiplicacion(n1,n2):
#         return n1 * n2
# def division(n1,n2):
#         return n1 / n2
# def potencia(n1,n2):
#         return n1 ** n2
# opcion = int(input("Ingrese la operacion que desea realizar : "))
# match opcion:
#     case 1:
#         n1 = int(input("Ingrese el primer numero : "))
#         n2 = int(input("Ingrese el segundo numero : "))
#         print(suma(n1,n2))
#     case 2:
#         n1 = int(input("Ingrese el primer numero : "))
#         n2 = int(input("Ingrese el segundo numero : "))
#         print(resta(n1,n2))
#     case 3:
    
    