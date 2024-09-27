
menu = """
    -------------------MENU--------------------- 
    INGRESE UN NUMERO DEL QUE ESTA DISPONIBLE
    
    
    
    1. Calcular el factorial
    2. Imprimir su tabla de multiplicar
    3. Especificar si es Par o Impar
    4. Primo o no
    5. Imprimir el proximo primo

"""


print(menu)
numero = int(input("Ingrese el numero a calcular : "))
def factoriao(numero):
    # 5 * 4 * 3 * 2 * 1 
    acc = 1
    for i in range(1,numero+1):
        acc = acc * i
    return acc

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}")
    for i in range(1,10+1):
        print(f"{numero} x {i} = {numero * i}")
    

def par_impar(numero):
    if numero % 2 == 0:
        print(f"El numero : {numero} es par")
    else:
        print(f"El numero : {numero} no es par")
        

def Es_primo(numero):
    acc = 0
    for i in range(2,numero):
        if numero % i == 0:
            acc = acc + 1
    
    if acc == 0:
        return True
    else:
        return False
            

def siguiente_primo(numero):
    num = numero
    acc = 1
    while not Es_primo(numero+acc):
        num = num + 1
        acc = acc + 1
    return num + 1


            