# Realizar un codigo que verifique que dos numeros
# Sean positivos
# Si son negativos, mandar una expecion y 
# volver a pedirlos
while True:
    try:
        num1 = int(input("Ingrese un numero positivo : "))
        num2 = int(input("Ingrese un numero positivo : "))
        if num1 < 0 or num2 < 0:
            print("No pueden ser negativos")
            raise ValueError("SON NEGATIVOS")
        else:
            resultado = num1/num2
            print("¡Ingresaste bien los datos!")
            print(resultado)
            break
    except ValueError:
        print("Ingresa nuevamente")
    except ZeroDivisionError:
        print("No se permite dividir por 0")