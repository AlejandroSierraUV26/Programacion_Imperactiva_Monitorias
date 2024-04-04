# def Es_primo(numero):
#     contador = 0
#     for i in range(2,numero):
#         if numero % i == 0:
#             contador += 1
#     if contador > 0:
#         return False
#     return True

# for i in range(0,10):
#     if(not(Es_primo(i))):
#         print(i)



# numero = 5
# acomulador = 1
# for i in range(numero,1,-1):
#     acomulador *= i
    
# print(acomulador)
    
personas = []
for i in range(0,2):
        nombre = input("Ingrese su nombre :")
        edad = int(input("Ingrese su edad :"))
        personas.append([nombre, edad])
print(personas)


print(personas[0][0])
    