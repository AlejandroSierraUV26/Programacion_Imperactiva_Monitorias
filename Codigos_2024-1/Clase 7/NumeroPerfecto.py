"""
Un numero perfecto es un numero entero positivo que es igual a la 
suma de sus divisores propios positivos, excluyendo el mismo numero. 
Por ejemplo, 6 es un numero perfecto porque 1 + 2 + 3 = 6.


¿Cuantos numeros perfectos existen desde el 1 hasta el 1000?

A. 3    
B. 4
C. 5
D. 6
E. 7

"""
for numero in range(1,10_000):
    acom = 0
    for i in range(1,numero):
        if numero % i == 0:
            acom+=i

    if acom == numero:
        print(f"El numero {numero} es perfecto")



