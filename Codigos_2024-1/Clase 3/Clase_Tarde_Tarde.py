def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
    
def es_par(num):
    if num % 2 == 0:
        return True
    else:
        return False
def aplicar_IVA(precio_neto,iva):
    return precio_neto + precio_neto * iva

def inverso(num):
    num = str(num)
    num_inverso = num[::-1]
    return num_inverso


def capicua(num):
    if num == inverso(num):
        return True
    else:
        return False
    
def farenheit_a_celcius(grados):
    return (grados - 32) * 5/9

def celcius_a_farenheit(grados):
    return (grados * 9/5) + 32



def entero_binario(num):
    return bin(num)

print(entero_binario(10))
