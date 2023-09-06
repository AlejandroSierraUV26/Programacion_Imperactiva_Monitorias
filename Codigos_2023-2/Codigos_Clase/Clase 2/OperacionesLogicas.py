"""
Operadores logicos

 And 20==20 and 10!=10 -> False // 
 Or 20 > 10 or 10!=10 or 1<2
 Negative !
 


"""

# a = 20

# b = 10

# print(a==a and a!=b and a!=b and a!=b and a!=b and a!=b)

# print((20<10) or (10!=10) or not (1<2))



"""
Ejercicio Operadores Logicos


    1. n pertenece al rango [-10,30]
    
    2. n no es menor o igual que 40
    
    3. n es diferente de 30 o mayor que 100
    
    


"""

#Ejemplo 1

n = int(input("Ingrese un numero : "))

resultado = n >= -10 and n <= 30
print("Punto 1")
print(resultado)
# Ejemplo 2
resultado = not(n<=40)
print("Punto 2")
print(resultado)
# Ejemplo 3
resultado = (n !=30) or (n>100)
print("Punto 3")
print(resultado)