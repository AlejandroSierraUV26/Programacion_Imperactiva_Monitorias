"""
Entrada: 2 numeros enteros
         Opcion : Entero
         
Salida: Operacion float 

Proceso: 

Si opcion es 1, sumar los numeros
Si opcion es 2, restar los numeros
Si opcion es 3, multiplicar los numeros
Si opcion es 4, dividir los numeros
Sino es ninguno deberia decir error de parametros
"""
#!Entrada 
num1 = int(input("Ingrese un numero : "))
num2 = int(input("Ingrese un numero : "))

opcion = int(input("Ingrese un numero \n 1. Sumar \n 2. Restar \n 3. Multiplicar \n 4. Dividir\n"))

#!Proceso

if opcion == 1:
    operacion = num1 + num2
elif opcion == 2:
    operacion = num1 - num2
elif opcion == 3:
    operacion = num1 * num2
elif opcion == 4:
    operacion = num1 / num2
else:
    operacion = 0
    print("Error de parametros")
    
#*Salida
print(f"El resultado es : {operacion}")





""""

if(operacion):
    print("Un procedimiento")
    if(operacion3):
        print("Un procedimiento en caso de 3")
    else:
        print("Un procedimiento en caso de que no se cumpla 3")
elif(operacion2):
    print("Un procedimiento en caso de 2")
else:
    print("Un procedimiento en caso de que no se cumpla ninguna de las anteriores")




-10<=n<=30










"""
