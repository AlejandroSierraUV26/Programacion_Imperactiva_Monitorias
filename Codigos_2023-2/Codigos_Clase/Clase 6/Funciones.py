# """
# Sumatorias == > 1+2+3+4+5+6+....+100
# n(n+1)/2

# """
# """
# Factorial ->


# Factorial 5 

# 1*2*3*4*5 = 120



# """
# def factorial(numero):
#     if numero == 1:
#         print(numero, end= " = ")
#         return 1
#     else:
#         print(numero, end= " * ")
#         return factorial(numero-1) * numero
    
# # print(factorial(5))









# # Numero  = 10
# def MultiplicacionExpresion(numero):
#     # Caso base
#     if numero == 1:
#         return "1"
#     # Caso Recursivo 
#     else:
#         return f"{MultiplicacionExpresion(numero - 1)} * {numero}"
# def Factorial(numero):
#     # Caso base
#     if numero == 1:
#         return 1
#     # Caso Recursivo 
#     else:
#         resultado = Factorial(numero - 1)
#         return numero * resultado


# if __name__ == '__main__':
#     print(f"{MultiplicacionExpresion(7)} = {Factorial(7)}")





# # # 10 * 9 * 8 * 7 

# # # 1 * 2 * 3 * 4 * 5 * 6



# def Collazt(num):
#     if num == 1:
#         return 1
#     else:
#         if(num%2 == 0):
#             return Collazt(num/2)            
#         else:
#             return Collazt(num*3+1)
    
# print(Collazt(120))
# print(Collazt(20))
# print(Collazt(10))
            
            
    
def ConvertirBinario(numero):
    if numero == 0:
        return "0"
    elif numero == 1:
        return "1"
    else:
        return ConvertirBinario(numero//2) + str(numero%2)
    
print(ConvertirBinario(35))
