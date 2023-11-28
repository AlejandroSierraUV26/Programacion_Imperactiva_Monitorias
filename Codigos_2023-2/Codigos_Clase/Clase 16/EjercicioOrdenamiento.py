"""
Ejercicio de ordenamiento: 

    Dada una lista de numeros enteros, ordenarlos de menor a mayor.
    
    Sin metodos de ordenamiento, solo con ciclos y condicionales.
    
    Ejemplo:
    
    Entrada: [5, 2, 3, 1, 4]
    
    Salida: [1, 2, 3, 4, 5]
 
# """
# lista = [5,2,3,1,4]


# for i in range(0,len(lista)):
#     for j in range(i+1,len(lista)):
#         if lista[i] > lista[j]:
#             acc = lista[i]
#             lista[i] =lista[j]
#             lista[j] = acc
            
# print(lista)



















"""

Ejercicio de conteo de personas: 

    Dada una lista de personas, contar cuantas personas hay de cada edad.
    
    Sin metodos de ordenamiento, solo con ciclos y condicionales.
    
    Ejemplo:
    
    Entrada: [["Juan",19], ["Maria",20], ["Juan",21], ["Pablo",19], ["Maria",20], ["Pablo",19]]
    
    Salida: Juan 19: 1
            Maria 20: 2
            Juan 21: 1 
            Pablo 19: 2

"""

cantidad_personas = []
personas =  [["Juan",19], ["Maria",20], ["Juan",21], ["Pablo",19], ["Maria",20], ["Pablo",19]]

for i in range(0,len(personas)):
    if i == 0:
        cantidad_personas.append([personas[i][0],personas[i][1],1])
    else:
        for j in range(0,len(cantidad_personas)):
            if personas[i][0] == cantidad_personas[j][0] and personas[i][1] == cantidad_personas[j][1]:
                cantidad_personas[j][2] += 1
                break
            elif j == len(cantidad_personas)-1:
                cantidad_personas.append([personas[i][0],personas[i][1],1])
                break
            
print(cantidad_personas)
        















