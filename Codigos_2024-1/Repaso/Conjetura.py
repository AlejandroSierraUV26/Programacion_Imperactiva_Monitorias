def secuencia_collazt(n):
    secuencia = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1 
        secuencia.append(n)
    return secuencia



numero = int(input("Ingrese un numero : "))
print(secuencia_collazt(numero))




"""
Secuencia : 
            a   b 
0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34 , 55 

Cual es el valor de x y de y

"""

a = 0
b = 1

while b<=55:
    print(b)
    a_anterior = a
    a = b
    b = a_anterior + b 

    
    

