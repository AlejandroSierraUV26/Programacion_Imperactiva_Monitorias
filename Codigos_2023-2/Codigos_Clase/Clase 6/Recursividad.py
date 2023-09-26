# def Sumatoria(num):
#     if num == 1:
#         return 1
#     else: 
#         return num + Sumatoria(num-1)
# def factorial(num):
#     if num == 0:
#         return 1
#     else: 
#         return num * factorial(num-1)

# def Collazt(num):
#     print(num)
#     if num == 1:
#         return 1
#     else:
#         if num % 2 == 0:
#             return Collazt(num//2)
#         else:
#             return Collazt(num*3+1)


def Suma(num):
    if num == 1:
        return 1 
    else:
        return num + Suma(num-1)

def factorial(num):
    if num == 1:
        return 1 
    else:
        return num * factorial(num-1)

if __name__ == '__main__':
    print("Suma : ",Suma(10))
    print("Factorial : ",factorial(5))




def ConvertirBinario(numero):
    if numero == 1:
        return "1"
    elif numero == 0:
        return "0"
    else: 
        return ConvertirBinario(numero//2) + str(numero%2)

print("Converting", ConvertirBinario(19))






def Collazt(numero):
    print(int(numero))
    if numero == 1:
        return 1
    elif numero%2 == 0:
        return Collazt(numero/2)
    else:
        return Collazt(numero*3 + 1)



# print(Collazt(24))




"""
Una casa de cambio vende 3 tipos de divisas diferentes 
dólares $3080, euros $ 3469, libras $4030). 
La empresa necesita desarrollar
un programa que dé 2 opciones a los clientes: 
1. Consulta deprecios de las divisas, y 
2. el valor de la conversión del peso colombiano 
a la divisa. 

"""

        