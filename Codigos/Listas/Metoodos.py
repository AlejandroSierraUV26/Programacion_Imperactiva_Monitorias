"""
Metodos para lista.

append()
6
lista = [1,2,3,4,5]
lista.append(0)
lista = [1,2,3,4,5,0]

#* Agregar un elemento en el ultimo posicionamiento

?clear()

lista = [1,2,4,5,6,6]
lista.clear()
lista = []

#* Limpia la lista, dejando la lista vacia

extend()

lista = [1,2,3,4,5]
lista3 = []

lista3.extend(lista)

lista2 = [5,6,7]

lista.extend(lista2)

lista = [1,2,3,4,5,5,6,7]



#* Une una lista

count()

TODO: Realizar un algoritmo que cuente cuantos elementos hay en una lista, segun el numero
lista = [1,1,1,1,2]
lista.count(1)
> 4
lista.count(2)
> 1



#* Cuenta cuantas veces existe un elemento en una lista
lista = [1,1,1,1,2]
lista.index(1)
>(0,1,2,3)

index()

#* Indica el posicionamiento de un elemento en la lista, el primero en ser encontrado

insert(indice,elemento)

#* Inserta un elemento en la lista, en una posicion definida 

lista = [1,2,3,4,5]

lista.insert(0,0)

lista = [0,1,2,3,4,5]


pop()

#* Elimina el ultimo elemento de la lista

remove()

#* Elimina el elemento buscado en una lista, elimina el primero que encuentra.
TODO:  el primero en ser encontrado se elimina 

reverse()

[1,2,3,4,5]
[5,4,3,2,1]

#* Da la vuelta a una lista, el primer elemento hacia el ultimo.


sort()
lista = [2,3123,123,123,123,,232313]
lista.sort()

#* Ordena los elementos de una lista, de menor a mayor.

# #? sort(reverse = True)

# #* Hace lo mismo pero de mayor a menor.

# """





# # # #TODO: Realizar un algoritmo que cuente cuantos elementos hay en una lista, segun el numero
# # # def buscar_numero(numero,numero2):
# # #     contador = 0 
# # #     contador2 = 0
# # #     for i in range(len(lista)):
# # #         if lista[i] == numero :
# # #             contador+=1
# # #         if lista[i] == numero2 :
# # #             contador2+=1
# # #     return contador,contador2
# # # lista = [1,1,1,1,2]
# # # numero = int(input("Ingrese el numero que desea buscar : "))
# # # numero2 = int(input("Ingrese el numero que desea buscar : "))
# # # print(buscar_numero(numero,numero2))
    
    
        
# # lista = [1,1,1,0,2,0,0,0,0,0,0,0,0,1]
# # lista_guardar = []
# # numero = 1
# # for i in range(len(lista)):
# #     #?Condicional
# #     if numero == lista[i]:
# #         lista_guardar.append(i)
# # print(lista_guardar)
# # print(lista.index(1))
        
# # lista.remove(1)
# # print(lista)



# def obtener_indice(numero):
#     lista_guardar = []
#     for i in range(len(lista)):
#         if numero == lista[i]:
#             lista_guardar.append(i)
#     return lista_guardar


# lista = [1,2,0,1,2,1]
# print(obtener_indice(1))
#! (0,3,5)

# def contador_numeros(a,b):
#     contador = 0
#     contador2 = 0
#     for i in range(len(lista)):
#         if lista[i] == a:
#             contador +=1
#         elif lista[i] == b:
#             contador2 +=1
#     return contador,contador2
# lista = [1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,1]
# print(contador_numeros(1,2))




#? Escribir un programa que almacene el abecedario en una lista, 
#? elimine de la lista las letras que ocupen posiciones múltiplos de 3, 
#? y muestre por pantalla la lista resultante.







