import math     # se importa la libreeria math para realizar la operacion de raiz cuadrada de forma exacta

def discriminante_cuadratica(a, b, c):   # se realiza la discriminante para saber si tiene 1 o 2 soluciones o no tiene solucion en los reales
    discriminante = (b**2) - 4*a*c   
    if discriminante < 0:  
        return "No tiene soluciones en los reales"
    elif discriminante > 0:               
        primera_solucion = (-b + math.sqrt(discriminante)) / (2*a)  
        segunda_solucion = (-b - math.sqrt(discriminante)) / (2*a)  
        return primera_solucion, segunda_solucion 
    elif discriminante == 0: 
        solucion = -b / (2*a)
        return solucion


def factorizado(a, b, c):
    discriminante = (b**2) - 4*a*c    
    if discriminante == 0 :
        return(f"(x - {solucion})")
    if discriminante < 0:
        return "No tiene solucion en los reales"
    
    primera_solucion = (-b + math.sqrt(discriminante)) / (2*a)  
    segunda_solucion = (-b - math.sqrt(discriminante)) / (2*a)
    solucion = -b / (2*a)
    if discriminante > 0 :
        return(f"{a}(x - {primera_solucion })(x - {segunda_solucion})")

if __name__ == '__main__':
    
    print("RESOLVER ECUACIONES CUADRÁTICAS ")
    print("ingrese los valores de a, b y c de la ecuacion cuadratica")
    
    # pide al usuario los valores de a, b y c de la ecuacion cuadratica
    
    a = int(input("ingrese el valor de a: "))
    b = int(input("ingrese el valor de b: "))
    c = int(input("ingrese el valor de c: "))
    print(discriminante_cuadratica(a, b, c))
    print(factorizado(a, b, c))