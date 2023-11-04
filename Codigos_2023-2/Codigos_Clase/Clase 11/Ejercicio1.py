def pedirDatos(lista):
    materia = str(input("Ingrese la materia : "))
    lista.append(materia)
    
    return lista
def pedirDatos2(lista2):
    nota = float(input("Ingrese su nota : "))
    lista2.append(nota)
    
    return lista2

if __name__ == '__main__':
    lista = []
    lista2 = []
    for i in range(3):
        pedirDatos(lista)
        pedirDatos2(lista2)
    
    for i in range(3):
        print("La materia : ", lista[i], "Nota : ", lista2[i])
        
    