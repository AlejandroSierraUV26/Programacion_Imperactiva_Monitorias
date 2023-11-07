maximo = int(input("Ingrese el valor máximo de la secuencia de Fibonacci: "))
a, b = 0, 1
while a < maximo:
    a, b = b, a + b
    print(a, end = " ")
