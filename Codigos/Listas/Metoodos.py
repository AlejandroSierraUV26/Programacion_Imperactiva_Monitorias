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


index()

#* Indica el posicionamiento de un elemento en la lista, el primero en ser encontrado

insert(indice,elemento)

#* Inserta un elemento en la lista, en una posicion definida 

pop()

#* Elimina el ultimo elemento de la lista

remove()

#* Elimina el elemento buscado en una lista, elimina el primero que encuentra.

reverse()

#* Da la vuelta a una lista, el primer elemento hacia el ultimo.


sort()

#* Ordena los elementos de una lista, de menor a mayor.

#? sort(reverse = True)

#* Hace lo mismo pero de mayor a menor.

"""





#TODO: Realizar un algoritmo que cuente cuantos elementos hay en una lista, segun el numero
def buscar_numero(numero,numero2):
    contador = 0 
    contador2 = 0
    for i in range(len(lista)):
        if lista[i] == numero :
            contador+=1
        if lista[i] == numero2 :
            contador2+=1
    return contador,contador2
lista = [1,1,1,1,2]
numero = int(input("Ingrese el numero que desea buscar : "))
numero2 = int(input("Ingrese el numero que desea buscar : "))
print(buscar_numero(numero,numero2))
    
    
    
    
    
    
    
    
    
    
    
    