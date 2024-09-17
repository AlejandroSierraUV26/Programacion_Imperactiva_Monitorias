# for i in range(0,10,1):
#     print(f" {i} - Alejandro")
# i = 0
# while (i<10):
#     print(f"{i} Alejandro Sierra")
#     i+=1

# Break -> romper
# Continue  -> continuar
    
    
    
    
# print(2 in [1,2,3,4,5,6,7])






# Mostrar los numeros divisibles del 220 excluya el {5, 10, 20} 

# for i in range(1,100000000):
#     if i == 5 or i == 10 or i == 20:
#         continue
#     elif i == 220+1:
#         break
#     elif 220 % i == 0:
#         print(i) 
    

# Determinar que numeros son divisibles por 2, 4 y 7
# Mostrar los primeros 100 numeros

# (10 % 2 == 0) -> Bool


num1 = 2
num2 = 4
num3 = 8
veces = 100
# For
for i in range(1,veces+1):
    if i % num1 == 0 and i % num2 == 0 and i % num3 == 0: 
        print(i)


# While 
i = 1
while i <= veces:
    if i % num1 == 0 and i % num2 == 0 and i % num3 == 0: 
        print(i)
    i+=1
    

    
    
# Ctrl + K + C comentar
# Ctrl + K + U descomentar