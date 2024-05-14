"""
En su hogar se tiene el problema que est´a llegando el recibo de la energ´ıa por un
valor muy elevado. Para analizar este problema, usted debe construir un programa que permita
calcular el costo total del recibo de energ´ıa.
El gobierno maneja las siguientes tarifas para el cobro del servicio de energ´ıa
Los primeros 300kw se cobran a 50 cada kw
Los siguientes 200kw se cobran a 100 cada kw
Los siguientes 500kw se cobran a 150 cada kw
De all´ı en adelante se cobra 200 cada kw
Dise˜ne la funci´on calcular-costo-energia la cual recibe el total de consumo realizado durante
el mes retornando el valor total a pagar.


"""



def calcular_costo_energia(consumo):
    if consumo <= 300:
        return consumo*50
    elif consumo <= 500:
        return 300*50 + (consumo-300)*100
    elif consumo <= 1000:
        return 300*50 + 200*100 + (consumo-500)*150
    else:
        return 300*50 + 200*100 + 500*150 + (consumo-1000)*200
    

consumo = float(input("Ingrese el consumo total de energia: "))
print(f"El costo total del recibo de energia es: {calcular_costo_energia(consumo)}")



