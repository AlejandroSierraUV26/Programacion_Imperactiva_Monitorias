"""
2. En una empresa dedicada a la preparación de bebidas se tiene un recipiente 
rectangular en el que se almacena el líquido. Este recipiente tiene como 
dimensiones 5 metros de altura, 2 de anchura y 3 de profundidad. En el recipiente 
hay un medidor que indica la altura actual que alcanza el líquido.
Usted debe desarrollar una función que retorne la cantidad de litros almacenados 
en el recipiente dada una altura específica.
La función recibe como argumento la altura actual del líquido, el cual es solicitado 
por fuera de ella. Luego, se debe calcular el volumen usando la fórmula.

volumen=altura_actual x anchura x profundidad


Para conocer la cantidad de litros utilice la relación entre volumen y capacidad 
según la cual 1m3 = 1000 litros. Finalmente, la función muestra solamente la 
cantidad de litros.


Tener en cuenta que la altura no puede superar la altura actual. 


Realizar 3 llamados: 
2 permitidos y 1 que exceda la altura actual.

"""
#Definicion de la funcion CalcularVolumen
def CalcularVolumen(altura):
    volumen=altura*2*3
    litros=volumen*1000
    return litros

if __name__ == "__main__":

    altura_actual = float(input("Ingrese la altura actual del liquido: "))

    if altura_actual<=0 or altura_actual >5:
        print("La altura no puede ser mayor a 5 metros")
    else:
        print(f"La cantidad de litros almacenados en el recipiente es: {CalcularVolumen(altura_actual)}")

