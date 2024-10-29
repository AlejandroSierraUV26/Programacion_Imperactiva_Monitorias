# tuplas = (1,2,3,4,5)
# diccionario = {"nombre":"Juan","nombre":22}
# conjuntos = {1,2,3,4,1}


lista = [1,1,1,1,1,1,1,1,1,1,1,2,3,4,1,2]



def eliminar_mejorado(lista, elem):
    n = len(lista)
    global lista_resu
    lista_resu = []
    for i in range(n):
        if lista[i] != elem:
            lista_resu.append(lista[i])

    
eliminar_mejorado(lista,1)
lista = lista_resu
print(lista)
