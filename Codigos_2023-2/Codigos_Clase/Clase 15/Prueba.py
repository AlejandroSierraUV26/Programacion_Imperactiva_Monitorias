def comprobar_letras(palabra):
    i = 0
    contador = 0

    while(i<len(palabra)):
        if palabra[i] == palabra[i].upper():
            i+=1 
            continue
        elif palabra[i] == " ":
            i+=1 
            continue
        else:
            i+=1 
            contador+=1
    if contador>0:
        return False
    else:
        return True


if __name__ == "__main__":
    palabra = str(input("Ingrese una oracion : "))
    while palabra != "salir":
        if comprobar_letras(palabra):
            print("La palabra tiene todas las letras en mayuscula")
        else:
            print("La palabra no tiene todas las letras en mayuscula")


    
