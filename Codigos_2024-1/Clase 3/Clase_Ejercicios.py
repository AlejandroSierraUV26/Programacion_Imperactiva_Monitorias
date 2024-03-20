def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero-1)
    
def Es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
def aplicar_iva(precio_neto,iva):
    return precio_neto + precio_neto*iva

def invertir(numero):
    numero = str(numero)
    numero_invertido = numero[::-1]
    return int(numero_invertido)

def farenheit_a_celsius(grados):
    #Celcius = (Farenheit - 32) * 5/9
    c = (grados-32) * 5/9
    return c
        
def capicua(numero):
    return numero == invertir(numero)

def entero_binario(numero):
    if numero == 0:
        return '0'
    binario = ''
    for i in range(0,numero):
        binario = str(numero % 2) + binario 
        numero//=2
    return binario
print(entero_binario(10))