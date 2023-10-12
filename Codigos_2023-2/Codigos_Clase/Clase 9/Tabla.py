def funcion(numero):
    if numero == 5:
        return 1
    else:
        return 20 + funcion(numero-1)

print(funcion(20))


