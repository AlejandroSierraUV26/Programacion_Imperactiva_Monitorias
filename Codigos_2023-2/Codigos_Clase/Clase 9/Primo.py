def primo(numero):
    contador = 0
    for i in range(1,numero+1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False

n = int(input("Ingrese un numero a validar: "))
contador = 0
numero = 1
while contador < n:
    if primo(numero):
        print(numero)
        contador += 1
    numero += 1