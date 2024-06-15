
"""
    Autor : Grupo 2
    Fecha : 2024/05/20
    Version: 1.0
    Descripcion: Este programa recibe una matriz de adyacencia de un grafo no dirigido y
                devuelve una lista de colores asignados a los nodos y una matriz de selección de villas.
                Cada fila de la matriz de selección de villas representa una villa y cada columna
                representa un nodo. Si un nodo está en la fila de una villa, entonces esa villa
                ha sido asignada a ese nodo.
                

"""
# Funcion para leer la matriz de adyacencia de un archivo de texto
def obtener_datos_txt(archivo): 
    matrix = []
    with open(archivo, 'r') as file:
        lines = file.read()
        lines = lines.split("\n")
        for line in lines:
            line = line.split(",")
            matrix.append([int(i) for i in line])
    return matrix

# Union de las funciones coloreo y generar_matrix
def organizar_datos(graph):
    colors, current_color = coloreo(graph)
    villa_matrix = generar_matrix(colors, current_color)
    return villa_matrix


# La funcion coloreo se encarga de asignar un color a cada nodo del grafo
# de manera que nodos adyacentes no tengan el mismo color.
def coloreo(graph):
    n = len(graph) # Numero de nodos
    colors = [-1] * n # Lista de colores
    degree = [(i, sum(graph[i])) for i in range(n)] # Lista de nodos y su grado
    degree.sort(key=lambda x: x[1], reverse=True) # Ordenar nodos por grado
    neighbor_colors = [set() for _ in range(n)] # Colores de los nodos adyacentes
    
    current_color = 0 # Color actual
    for node, _ in degree: # Iterar nodos por grado
        if colors[node] == -1: # Si el nodo no tiene color
            colors[node] = current_color # Asignar color
            for neighbor in range(n): # Iterar nodos adyacentes
                if graph[node][neighbor] == 0 and colors[neighbor] == -1 and current_color not in neighbor_colors[neighbor]: # Si el nodo adyacente no tiene color y no tiene el color actual
                    colors[neighbor] = current_color # Asignar color
                    for k in range(n): # Iterar nodos adyacentes
                        if graph[neighbor][k] == 1: # Si el nodo adyacente tiene un nodo adyacente
                            neighbor_colors[k].add(current_color) # Agregar color a los nodos adyacentes
            current_color += 1 # Siguiente color
    return colors, current_color # Retornar colores y numero de colores
    

# La funcion generar_matrix se encarga de generar una matriz de selección de villas
def generar_matrix(colors, num_villas): # Generar matriz de selección de villas
    num_selections = len(colors)  # Numero de selecciones
    villa_matrix = [[int(villa == colors[selection]) for selection in range(num_selections)] for villa in range(num_villas)] # Matriz de selección de villas
    return villa_matrix # Retornar matriz de selección de villas


def main():
    graph = obtener_datos_txt(fr"Pruebas\archivo.txt")
    villa_matrix = organizar_datos(graph)
    print(villa_matrix)
    

if __name__ == '__main__':
    main()
    