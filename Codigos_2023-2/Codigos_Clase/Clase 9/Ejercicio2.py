"""
Pedir al usuario que ingrese dos numeros, uno entero y uno decimal, 
verificar que no tengan errores de ningun tipo y mostrar la 
division de ambos. 

Decimal numerador y entero denominador.


"""
while(True):
    try: 
        a = int(input("Ingrese  un numero : "))
        b = int(input("Ingrese  un numero : "))
        print(a/b)
        break
    except Exception as e: 
        print("Invalid",e)