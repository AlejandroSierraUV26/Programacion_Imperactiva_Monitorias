i = 2 #! Se inicializa el contador en 2
numero = 7 #! Se define el numero a evaluar
contador = 0 #! Se inicializa el contador en 0
while i<numero:
    if numero % i == 0:
        contador+=1 #? Se incrementa el contador en 1 si es que el numero es divisible por i
    i+=1 #? Se incrementa el contador en 1
if contador == 0: #? Si el contador es 0, el numero es primo
    print("El numero es primo")
else:
    print("El numero no es primo")