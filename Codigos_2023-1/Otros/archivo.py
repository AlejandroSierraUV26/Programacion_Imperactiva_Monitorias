def separar(n):
    n = str(n)
    separados = []
    for i in n:
        separados.append(i) 
    sumatotal = int(0)
    for i in range(0,len(separados)):
        separados[i] = int(separados[i])
        sumatotal+= separados[i]
    return sumatotal 


numero_original = 132189
numero = separar(numero_original) 
if(numero > 9):
    numero = separar(numero)
print(numero)
    