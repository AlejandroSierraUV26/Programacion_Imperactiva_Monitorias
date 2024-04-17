# # while True:
# #     try:
# #         edad = int(input("Ingrese su edad : "))
# #         print(edad)
# #         break
# #     except Exception:
# #         print("Vos sos un gran pendejo")



# # No recibir valores negativos
# while True:
#     try:
#         edad = int(input("Ingrese su edad : "))
#         if edad < 0:
#             raise ValueError("No se permiten valores negativos")
#         else:
#             print(edad)
#             break
#     except ValueError:
#         print("Repita")
    



"""
Realizar una operacion de division de division, omitiendo los errores de 
el denominador de 0.

"""

print(10/0)

