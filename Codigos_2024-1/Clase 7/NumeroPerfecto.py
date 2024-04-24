
def generar_perfecto(numero):
    acom = 0
    for i in range(1,numero):
        if numero % i == 0:
            acom += i
    if numero == acom:
        print(f"El numero {numero} es perfecto")


for i in range(1,1000):        
    generar_perfecto(i)


"""
Un numero perfecto es un numero entero positivo que es igual a la 
suma de sus divisores propios positivos, excluyendo el mismo numero. 
Por ejemplo, 6 es un numero perfecto porque 1 + 2 + 3 = 6.


¿Cuantos numeros perfectos existen desde el 1 hasta el 1000?

A. 3    
B. 4
# C. 5
# D. 6
# E. 7

# """
# # for numero in range(1,10_000):
# #     acom = 0
# #     for i in range(1,numero):
# #         if numero % i == 0:
# #             acom+=i

# #     if acom == numero:
# #         print(f"El numero {numero} es perfecto")




# """
# Determinar si un numero es narcisista:

# Un numero narcisista es un numero que es igual a la suma de sus 
# digitos elevados a la potencia de la cantidad de digitos que tiene 
# el numero.

# Ejemplo:

# 153 --> 1^3 + 5^3 + 3^3 = 153

# 370 --> 3^3 + 7^3 + 0^3 = 370

# 371 --> 3^3 + 7^3 + 1^3 = 371

# 407 --> 4^3 + 0^3 + 7^3 = 407



# """
# numero = 153
# num = numero
# c  = num // 100
# num = num % 100
# d = num // 10
# num = num % 10
# u = num

# resultado = c**3 + d**3 + u**3

# if resultado == numero:
#     print(f"El numero {numero} es narcisista")
# else:
#     print(f"El numero {numero} no es narcisista")
    
    
# def descomponer_numero(numero):
#     numero = str(numero)
#     return [int(i) for i in numero]
# def narcisista(numero):
#     copiar_numero = numero
#     numero = descomponer_numero(numero)
#     resultado = 0
#     for i in numero:
#         resultado+=i**len(numero)
#     if resultado == copiar_numero:
#         return f"El numero {copiar_numero} es narcisista"
#     else:
#         return f"El numero {copiar_numero} no es narcisista"
    
    
# print(narcisista(153))

