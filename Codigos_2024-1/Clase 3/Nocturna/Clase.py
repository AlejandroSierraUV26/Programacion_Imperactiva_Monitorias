# """"
# Autor: Alejandro Sierra
# Fecha: 20-03-2024



# # Calcular el factorial de un numero:

# # 5! = 5 * 4 * 3 * 2 * 1 
# # 5! = 120



# # """
# # # resultado = 1
# # # numero = int(input("Ingrese el valor a calcular :"))
# # # for i in range(1,numero+1):
# # #     resultado = resultado * i
# # # print(resultado)
    



# # # # for i in range(0,10,2):
# # # #     print(i)
    
# # # i = 10
# # # while i <= 10:
# # #     print(i)
# # #     i+=1 
# # # else: 
# # #     print("El valor de i es mayor que 10")
    
    
    





# # # a,b = 0,1
# # # while b < 40:
# # #     print(b)
# # #     a,b = b, a+b
# # # print(b)
    
# # # a,b = 0,1 
# # # print()
# # # for i in range(9):
# # #     print(b)
# # #     a,b = b, a+b
# # # print(b)















# # a, b = 0, 1
# # num = int(input("Ingrese hasta que elemento desea conocer :"))

# # for i in range(num):
# #     print(b)
# #     a,b = b,a+b
    
# # a, b = 0, 1
# # while b<=55:
# #     print(b)
# #     a,b = b,a+b

# # i = 0
# # a,b = 0,1
# # while i<10:
# #     print(b)
# #     a,b = b,a+b
# #     i+=1

# num_primo = int(input("Ingrese el numero para verificar si es primo : "))
# contador = 0
# for i in range(2,num_primo):
#     if num_primo % i == 0:
#         contador += 1

# if contador == 0:
#     print("El numero es primo")
# else:
#     print("El numero no es primo")
    
    
    
    
    
    
    
    
# num = int(input("Ingrese el numero para verificar si es primo : "))

# contador = 0

# for i in range(2,num):
#     if num % i == 0:
#         contador += 1

# if contador > 0:
#     print("No es primo")
# else:
#     print("Es primo")        
    
    
    
    


# for i in range(0,100):
#     if i % 2 == 0:
#         if i % 3 == 0:
#             continue
#         print(i)
#         if i == 50:
#             break
        
        
i = 0
while i<50:
    if i % 3 == 0 or i % 5 == 0:
        if i % 2 == 0:
            i+=1
            continue
        print(i)
    i+=1
    
    
    
    
    
    
    
    
    


    

    
    
    