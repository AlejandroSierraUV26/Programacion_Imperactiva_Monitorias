def calcular_altura(cantidad_bloques):
    altura = 0
    bloques_necesarios = 0
    while cantidad_bloques >= bloques_necesarios:
        altura += 1
        bloques_necesarios += altura

    if cantidad_bloques < bloques_necesarios:
        altura -= 1
    return altura


if __name__ == "__main__":
    cantidad_bloques = int(input("Ingrese la cantidad de bloques a apilar :"))
    altura = calcular_altura(cantidad_bloques)
    print(f"La altura de la pirámide es: {altura}")