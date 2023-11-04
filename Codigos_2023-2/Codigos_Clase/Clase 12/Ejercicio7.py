def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
def factorial2(n):
    resultado = 1
    for i in range(1,n+1):
        resultado *= i
    return resultado

if __name__ == "__main__":
    n = int(input("Ingrese el numero a calcular : "))
    print("Por recursividad ", factorial(n))
    print("Por bucle for : ", factorial2(n))