import numpy as np 
def obtener_datos(ciudad,temperatura):
    menor = 100
    mayor = 0
    for i in range(0,len(temperatura)):
        if(menor > temperatura[i]):
            menor = temperatura[i]
            posicion1 = i
        if(mayor < temperatura[i]):
            mayor = temperatura[i]
            posicion2 = i
    print(f"Menor -> {ciudad[posicion1]} : {temperatura[posicion1]}")
    print(f"Mayor -> {ciudad[posicion2]} : {temperatura[posicion2]}")
    
ciudad = np.array(["Cartagena", "Manizales", "Cali", "Tulua"])
temperatura = np.array([30.2,15.3,40.3,32.2])
obtener_datos(ciudad,temperatura)

    