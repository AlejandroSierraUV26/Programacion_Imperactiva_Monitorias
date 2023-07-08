def conjetura(n):
    secuencia = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3) + 1
        secuencia.append(n)
    return secuencia


numero = int(input("Ingresa un número entero positivo: "))
secuencia= conjetura(numero)
print("Secuencia de Collatz para el número", numero, ":")
print(secuencia)
