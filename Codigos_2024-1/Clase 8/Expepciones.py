





# while True:
#     try:
#         edad = int(input("Ingrese su edad : "))
#         print(edad)
#         break
#     except ValueError:
#         print("SOLO SE PERMITE NUMEROS ENTEROS, NO DECIMALES NI LETRAS")
    

# for i in range(10):
#     print(i)



a = int(input("Ingrese un numero a :"))
while True:
    try:
        b = int(input("Ingrese un numero b:"))
        if b == 0:
            raise ZeroDivisionError("No se permite division por 0")
        else:
            break
    except Exception:
        print("Ingrese el valor nuevamente")
    
print(a/b)