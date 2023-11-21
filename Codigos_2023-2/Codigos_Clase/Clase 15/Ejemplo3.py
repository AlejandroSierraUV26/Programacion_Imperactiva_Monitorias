matrix = [
]

def agregar_materia():
    global matrix
    nombre = str(input("Ingrese el nombre de la materia : "))
    matrix.append([])
    matrix[-1].append(nombre)
    for i in range(0,3):
        nota = float(input(f"Ingrese la nota {i+1} : "))
        matrix[-1].append(nota)
    print("Materia agregada con exito")
    
def promedio(matrix, i):
    return(matrix[i][1] * 0.4) +(matrix[i][2] * 0.3) + (matrix[i][3] * 0.3)

def mostrar_Datos():    
    for i in range(0,3):
        agregar_materia()
    for i in range(0,3):
        print(f"{matrix[i][0]} {i+1}: ")
        print(promedio(matrix,i))
        
if __name__ == "__main__":
    mostrar_Datos()
    print(matrix)

    
    