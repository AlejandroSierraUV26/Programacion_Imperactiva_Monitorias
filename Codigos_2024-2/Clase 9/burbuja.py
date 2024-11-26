lista = [1,2,3,4,5]
lista.sort()
def burbuja(lista):
    for i in range(len(lista)):
        print("i:",i)
        for j in range(len(lista) - 1):
            print("j:",j)
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
            print(lista)
            
            if determinar_order(lista):
                return lista
    return lista
def determinar_order(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return False
    return True

print(burbuja(lista))

