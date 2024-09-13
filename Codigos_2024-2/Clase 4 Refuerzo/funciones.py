# Multiplos del 2 -> Pares
# No Multiplos del 2 -> Impares

numero1 = 7 # Impar
numero2 = 8 # Par 

# Modulo (%)

result1 = numero1 % 2 # Si es 0 quiere decir divisible por 2, sino pues que no es divisible 
result2 = numero2 % 2 

print(f"Residuo de : {numero1} % 2 = {result1}")
print(f"Residuo de : {numero2} % 2 = {result2}")            

if result1 == 0:
    print(f"El numero {numero1} es par")
else:
    print(f"El numero {numero1} es impar")
    
if result2 == 0:
    print(f"El numero {numero2} es par")
else:
    print(f"El numero {numero2} es impar")
    