# """
# Realizar una funcion que indique la posicion de un 
# elemento de una lista, si el elemento no se encuentra
# retornar vacio, si hay mas de un elemento retornar una tupla o una lista.

# Ejemplo : 

# Lista = [1,2,3,4,5,5,6,1,2]

# Elemento a buscar = 5

# Resultado = (4,5)


# """
# def encontrar_numero(lista,elem):
#     encontrados = []
#     for i in range(0,len(lista)):
#         if lista[i] == elem:
#             encontrados.append(i)
#     if len(encontrados) == 0:
#         return "No se encontro el elemento en la lista, no existe"
#     if len(encontrados) == 1:
#         return encontrados[0]
        
#     return encontrados

# lista = [1,2,3,4,5,5,6,1,2,5,3423423,5,64,656,6,5]


# print(encontrar_numero(lista,3423423))


def union(conj1,conj2):
    conj1 = list(conj1)
    conj2 = list(conj2)
    conjunto_resultante = []
    for i in range(len(conj1)):
        conjunto_resultante.append(conj1[i])
        conjunto_resultante.append(conj2[i])
    return set(conjunto_resultante)
        
conjunto1 = {1,2,"Alejandro"}
conjunto2 = {3,4,5}

print(union(conjunto1, conjunto2))