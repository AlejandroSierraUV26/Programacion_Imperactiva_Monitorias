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
    return numero[::-1]

def farenheit_a_celcuis(grados):
    c = (grados-32) * 5/9
    return c

def capicua(numero):
    return numero == invertir(numero)
def entero_binario(numero):
    return bin(numero)
#Celcius = (Farenheit - 32) * 5/9

