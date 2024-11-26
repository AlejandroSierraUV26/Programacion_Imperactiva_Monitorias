while True:
    try: 
        a = int(input("Ingrese : "))
        print(a)
        break
    except ValueError:
        print("Ingrese un numero, correctamente")
    except NameError:
        print("La variable no esta definida")
    



# Realizar una division de dos numeros, evitando todo tipo de errores.