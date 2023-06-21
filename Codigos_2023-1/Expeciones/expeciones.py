while(True):
    try:    
        x = int(input("Ingrese un numero : "))
        print(x)
        break
    except ValueError:
        print("Por favor ingrese un valor numerico")
        print("Ingrese nuevamente")
    except SyntaxError:
        print("Error por sintaxis")
print("Hola")