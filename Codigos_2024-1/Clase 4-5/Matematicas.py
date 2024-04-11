# # import math


# # def factorizar(a,b,c):
# #     discriminante = b**2 - 4*a*c
# #     if discriminante < 0:
# #         return "No tiene solucion en los reales"
# #     elif discriminante == 0:
# #         x = -b/(2*a)
# #         if a == 1:
# #             return f"(x-{x})"    
# #         return f"{a}(x-{x})"
# #     else:
# #         x1 = (-b + math.sqrt(discriminante))/(2*a)
# #         x2 = (-b - math.sqrt(discriminante))/(2*a)
# #         # tener en cuenta los signos
# #         if a == 1:
# #             if x1 < 0:
# #                 return f"(x+{-x1})(x+{-x2})"
# #             elif x2 < 0:
# #                 return f"(x-{x1})(x-{x2})"
        

# # a = 1
# # b = 1
# # c = 0

# # print(factorizar(a,b,c))


# import math  #Para valor exacto en la raiz
# #Pedimos valores
# def prueba(a,b,c):

#     dis = (b**2) - (4*a*c)

#     if dis > 0:
#         x1 = (-b + math.sqrt(dis)) / (2*a)
#         x2 = (-b - math.sqrt(dis)) / (2*a)
#         print(f"Las soluciones son: {x1} y {x2}")
#         if x1 < 0:
#             x1 *= -1
#             return(f"Factorizados: (x + {x1}), (x - {x2})")
#         elif x2 < 0:
#             x2 *= -1
#             return(f"Factorizados: (x - {x1}), (x + {x2})")
#         else:
#             return(f"Factorizados: (x - {x1}),(x - {x2})")

#     elif dis == 0:
#         x = -b / (2*a)
#         return(f"{x}")

#     else:
#         return("No solución")
    
    
# # generar las pruebas para a,b,c en la funcion de todos los valores de 0 a 5

# for i in range(1,6):
#     for j in range(1,6):
#         for k in range(0,6):
#             print(f"Para a = {i}, b = {j}, c = {k} : {prueba(i,j,k)}")




def funcion(a,b,c):
    import math  #Invocamos libreria para valor exacto en la raiz

    #Pedimos valores

    #Calculamos la discriminante
    dis = (b**2) - (4*a*c) 


    #Si es mayor que cero tiene dos soluciones
    if dis > 0:
        #Calculamos y redondeamos
        x1 = round((-b + math.sqrt(dis)) / (2*a),3)
        x2 = round((-b - math.sqrt(dis)) / (2*a),3)
        print(f"Las soluciones son: {x1} y {x2}")

        if x1 < 0 and x2 < 0:
            x1 *= -1
            x2 *= -1
            return(f"Factorizados: (x + {x1}), (x + {x2})")

        elif x2 < 0:
            x2 *= -1
            return(f"Factorizados: (x - {x1}), (x + {x2})")

        elif x1 < 0:
            x1 *= -1
            return(f"Factorizados: (x + {x1}), (x - {x2})")  

        else:
            return(f"Factorizados: (x - {x1}),(x - {x2})")

    #Si es cero calculamos el resto
    elif dis == 0:
        x = -b / (2*a)
        return(f"{x}")

    #Si es negativo
    else:
        return("No tiene solución en los números reales")
        
# generar las pruebas para a,b,c en la funcion de todos los valores de 0 a 5

for i in range(1,6):
    for j in range(1,6):
        for k in range(0,6):
            print(f"Para a = {i}, b = {j}, c = {k} : {funcion(i,j,k)}")
            
