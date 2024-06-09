
"""
    Autor : Alejandro Sierra
    Fecha : 2024/05/20
    Codigo : 2259559-3743
    Version: 1.0
    Descripcion: Este programa recibe una matriz de adyacencia de un grafo no dirigido y
                devuelve una lista de colores asignados a los nodos y una matriz de selección de villas.
                Cada fila de la matriz de selección de villas representa una villa y cada columna
                representa un nodo. Si un nodo está en la fila de una villa, entonces esa villa
                ha sido asignada a ese nodo.
                

"""

def obtener_datos_txt(archivo):
    matrix = []
    with open(archivo, 'r') as file:
        lines = file.read()
        lines = lines.split("\n")
        for line in lines:
            line = line.split(",")
            matrix.append([int(i) for i in line])
    return matrix
def organizar_datos(graph):
    colors, current_color = coloreo(graph)
    villa_matrix = generar_matrix(colors, current_color)
    return villa_matrix

def coloreo(graph):
    n = len(graph)
    colors = [-1] * n
    degree = [(i, sum(graph[i])) for i in range(n)]
    degree.sort(key=lambda x: x[1], reverse=True)
    neighbor_colors = [set() for _ in range(n)]
    
    current_color = 0
    for node, _ in degree:
        if colors[node] == -1:
            colors[node] = current_color
            for neighbor in range(n):
                if graph[node][neighbor] == 0 and colors[neighbor] == -1 and current_color not in neighbor_colors[neighbor]:
                    colors[neighbor] = current_color
                    for k in range(n):
                        if graph[neighbor][k] == 1:
                            neighbor_colors[k].add(current_color)
            current_color += 1
    return colors, current_color

def generar_matrix(colors, num_villas):
    num_selections = len(colors)
    villa_matrix = [[int(villa == colors[selection]) for selection in range(num_selections)] for villa in range(num_villas)]
    return villa_matrix


def main():
    graph = obtener_datos_txt(fr"Pruebas\archivo.txt")
    villa_matrix = organizar_datos(graph)
    print(villa_matrix)
    

if __name__ == '__main__':
    main()
    