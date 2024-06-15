def es_primo(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
    
def organizar_lista(lista):
    for i in range(0,len(lista)):
        for j in range(0,len(lista)):
            if lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

def entero_a_binario(n):
    if n == 0:
        return '0'
    binario = ''
    for i in range(0,n):
        binario = str(n % 2) + binario 
        n//=2
    # eliminar 0 a la izquierda
    binario = binario.lstrip('0')
    return binario

def convertir_tiempos(horas, minutos, segundos):
    if segundos >= 60:
        minutos += segundos // 60
        segundos = segundos % 60
    if minutos >= 60:
        horas += minutos // 60
        minutos = minutos % 60
    return (horas, minutos, segundos)


def conjetura_collatz(n):
    def collatz(n):
        if n % 2 == 0:
            return n // 2
        else:
            return 3*n + 1
    secuencia = [n]
    while n != 1:
        n = collatz(n)
        secuencia.append(n)
    return secuencia

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    secuencia = []
    for i in range(0,n):
        secuencia.append(fib(i))
    return secuencia
    
def multiplicacion(n,m):
    # Este ejercicio se debe realizar de manera donde no se use, el operador (*) ni (/)
    resultado = 0
    for i in range(0,m):
        resultado += n
    return resultado

def potencia(base, exponente):
    resultado = 1
    for i in range(0,exponente):
        resultado *= base
    return resultado

def numero_perfecto(n):
    suma = 0
    for i in range(1,n):
        if n % i == 0:
            suma += i
    if suma == n:
        return True
    else:
        return False

def numero_narcisista(n):
    suma = 0
    for i in range(0,len(str(n))):
        suma += int(str(n)[i])**len(str(n))
    if suma == n:
        return True
    else:
        return False

def verificar_datos_txt(archivo, elemento):
    # Verificar si un elemento se encuentra dentro de un archivo de texto
    with open(archivo, 'r') as file:
        datos = file.read()
        datos = datos.split(',')
        if elemento in datos:
            return True
        else:
            return False
            






