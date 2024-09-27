# Determinar que numeros son divisibles por 3 y por 5 a la vez
# Mostrar los primeros 150 numeros
# 15, 30, 45, 60 

def determinar_multiplo(num):
    if (num % 3 == 0) and (num % 5 == 0) : 
        print(f"El numero {num} es multiplo del 3 y 5")


for var_incrementable in range(1,150+1):
    determinar_multiplo(var_incrementable)
