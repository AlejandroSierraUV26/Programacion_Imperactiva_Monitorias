def calcular_suma(n):
    suma = 0
    for i in range(1,n+1):
        if i%2 != 0:
            suma += i
        
if __name__ == "__main__":
    n = int(input("Ingrese el limite para ver los numeros impares : "))
    print(f"La suma de los numeros impares de 1 hasta {n} es : {calcular_suma(n)}")