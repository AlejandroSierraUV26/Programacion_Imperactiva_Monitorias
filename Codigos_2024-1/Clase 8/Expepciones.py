
while True:
    try:
        numero = int(input("Ingrese un numero : "))
        print(numero)
        break
    except ValueError:
        print("NO SE PERMITEN LETRAS, NI NUMEROS DECIMALES")




