def primo(numero):
    contador = 0
    for i in range(1,numero):
        if i == 1 or numero == i:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else: 
        return False
    
def compuesto(numero,lista):
    for i in range(2,numero):
        if numero % i == 0:
            lista.append(i)
    return lista

def divisores(numero):
    lista = []
    if primo(numero):
        return f"El numero {numero} es primo"
    else:
        return compuesto(numero,lista)

if __name__ == "__main__":
    numero = int(input("Ingrese un numero : "))
    print(divisores(numero))