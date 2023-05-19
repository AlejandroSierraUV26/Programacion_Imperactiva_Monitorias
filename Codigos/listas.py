#conjunto = {1,1,2,3,4,5,6,6}
#print(conjunto)
#diccionario = {2:"Hola"}
#print(diccionario[2])


#lista = [1,1,2,3,4,5,6,6]
#print(lista)

#!Metodos 

#*append()

lista = []
lista.append(10)
print(lista)
lista.append(20)
print(lista)

#*clear()

lista.clear()
print(lista)




""""
Ejercicio 1. 

Realizar un codigo que pregunte al usuario 10 numeros enteros positos y los almacene en una lista, 
que se debe mostrar.

Ejercicio 2. 

Realizar la suma de todos los numeros que estan dentro de esa lista


"""

#*Inicializar la lista
lista = []


#!Entredad de datos hacia la lista
def entreda_datos():
    for i in range(10):
        numero = int(input(f"Ingrese el numero {i+1} : "))
        lista.append(numero)
    return lista
def suma_numeros():
    suma = 0
    for i in range(len(lista)):
        suma += lista[i] 
    return(f"La suma es {suma}")
print(entreda_datos())
print(suma_numeros())
    
