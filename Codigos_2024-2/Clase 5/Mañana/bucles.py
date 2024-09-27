# Iterativos
# for i in range(0,10,1): # for control y versatibilidad 
#     print(i)

# for i in "Alejandro":
#     print(i)



# i = 0 #Inicio
# while i<= 10: # Hasta donde
#     print(f"{i} Hola Alejandro")
#     i+=3 # Incremento
    
# print("Se estabilizo")

    

# Secuenciales





# lista = []
# def guardar_valor(a,b):
#     if not (a+b) in lista:
#         lista.append((a+b))
#         print("Okay yo lo guardo")
#     else:
#         print(f"Ya esa respueta la sé {(a+b)}")

# def sumar(a,b):
#     return a+b

# guardar_valor(2,2)
# guardar_valor(2,2)


# ! Realizar una calculadora para un numero ingresado por pantalla
# la calculadora debe ir desde 0 hasta 20
# Como las tablas con las que les peganban de niños

# Realizar las multiplicaciones en una funcion

# 2 * 0 = 0
# 2 * 1 = 1 
# 2 * 2 = 2 
# 2 * 3 = 6
# 2 * 4 = 8


def multiplicar(a,b):
    return a*b
def multiplicar_numeros():
    print("TABLA DE MULTIPLICAR EPICA!")
    valor = int(input("Ingrese el valor a multiplicar : "))
    limite = int(input("Ingrese el valor a llegar : "))
    for i in range(0,limite+1):
        print(f"{valor} * {i} = {multiplicar(valor,i)}")
        print("- - - - - - ")
        
if __name__ == "__main__":
    multiplicar_numeros()