"""

1. Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
    calcule el índice de masa corporal y lo almacene en una variable, y muestre por 
    pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice 
    de masa corporal calculado redondeado con dos decimales.

2. Escribir un programa que pida al usuario dos números enteros y muestre por pantalla 
    la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números 
    introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división 
    entera respectivamente. 

3. Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
    y el número de años, y muestre por pantalla el capital obtenido en la inversión.
    
"""
"""
Entrada : 
    peso -> float
    estatura -> float
    
Proceso : 
    imc = peso / estatura ** 2
Salida :
    imprimir(imc)
    

"""

# peso = float(input("Ingrese su peso, en kg: "))

# estatura = float(input("Ingrese su estatura, en m: "))


# imc = peso / estatura ** 2

# imc = round(imc,2)
# mensaje = f"Tu índice de masa corporal es {imc} donde {imc} es el índice de masa corporal \n calculado redondeado con dos decimales"

# print(mensaje)



"""
Entrada : 
    numerador -> int
    divisor -> int
    
Proceso : 
    cociente = numerador // divisor
    resto = numerador % divisor
Salida :
    imprimir(numerador, divisor, cociente, resto)
    

"""
numero = int(input("Ingrese el numerador : "))
divisor = int(input("Ingrese el divisor : "))


cociente = numero / divisor

resto = numero % divisor


print(f"La division de {numero} entre {divisor} es {cociente} con un residuo : {resto}")


