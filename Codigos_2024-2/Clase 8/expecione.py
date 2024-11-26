# while True:
#     try:
#         edad = int(input("Ingrese su edad :"))
#         print(f"Su edad es {edad}")
#         break
#     except Exception:
#         print("NO SE ALGO FALLO PERO NO SE QUE ES")
        
    
# print("Termino con exito!!!")



# Realizar una division de dos numeros, evitando todo tipo de errores.


while True:    
    try:    
        num1 = int(input("Ingrese el primer numero: "))
        while True:
            num2 = int(input("Ingrese el segundo numero : "))
            if num2 == 0:
                print("Ingresa nuevamente otro numero")
                continue
            else:
                break
        print(num1/num2)    
        break # Opcion 1
    except ValueError:
            print("NO SEA TAN TONTO, INGRESE UN NUMERO!!!! 😒")
    except NameError:
            print("No fue posible mostrar la edad 😢")
    except ZeroDivisionError:
        print("El numero2 no puede ser 0")




