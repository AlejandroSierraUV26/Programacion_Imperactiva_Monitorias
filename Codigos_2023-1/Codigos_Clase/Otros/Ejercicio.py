"""
Apartir de una lista de string separar cada elemento que 
contenga la palabra seleccionada

Ejemplo :

    Lista = ["Palabra en ingles", "Palabra en español", "Palabra en Programacion",
             "Python en Programacion", "Hola mundo, es una Palabra"]

    
    Output : Lista[0],Lista[1],Lista[2],Lista[4]

"""


lista = [] 
for i in range(0,len(lista)):
    for j in range(0,len(lista[i])):
        lista.append([])
        lista[i].append([2,3,4,5,6,7,8,9,10])
        print(lista[i][j])
        
    