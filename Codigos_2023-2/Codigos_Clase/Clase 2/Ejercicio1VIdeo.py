num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))
operacion = int(input("Ingrese la operacion \n 1. Suma \n 2. Resta \n 3. Multiplicacion \n 4. Division \n "))
resultado = 0

if operacion == 1:
    resultado = num1 + num2
else: 
    if operacion == 2:
        resultado = num1 - num2
    else: 
        if operacion == 3:
            resultado = num1 * num2
        else: 
            if operacion == 4:
                resultado = num1 / num2
            else:
                print("Operacion no valida")
    
print("El resultado es ",resultado)
