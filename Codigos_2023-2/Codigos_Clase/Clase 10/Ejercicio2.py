import random
def generar_numeros():
    n1 = random.randint(1,10)
    return n1

def resultado(n1,n2,n3):
    operacion = round((n1 + n2 * (n1-n3))/n2,1)
    return operacion

def comprobar():
    for i in range(0,5):
        n1 = generar_numeros()
        n2 = generar_numeros()
        n3 = generar_numeros()


        operacion =resultado(n1, n2, n3)
        print("Ingrese el resultado : ")
        print(f" {n1} + {n2} * ({n1} - {n3}) / {n2} =" , end= " ")

        numero = float(input(""))
        if resultado == numero:
            print("Correcto")
            break
        else:
            print("Incorrecto","El resultado era :", operacion)

if __name__ == "__main__":
    comprobar()
