# # # Genere los 50 numeros pares



# # for i in range(0,25):
# #     print(i*2)
    
# # for i in range(0,50):
# #     # Condicional de una sola linea
# #     print(i) if i%2 == 0 else print("No es par")
    
# i = 0
# acc = 0
# while acc<100:
#     if i%7 == 0:
#         print(i)
#         acc+=1
#     i+=1
    
    
    
def Es_primo(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
i = 0
contador = 0
while contador < 100:
    if Es_primo(i) == True:
        contador+=1
        print(i)
    i+=1
print(contador)
print(i)
        
             
    