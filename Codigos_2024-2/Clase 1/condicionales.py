
# print("¡REQUERIMOS SU EDAD PARA ENTRAR A LA DISCOTECA!")
# edad = int(input("Ingrese su edad (SIN MENTIR):  "))


# if edad >= 18:
#     print("Puede entrar :)")
#     bebida = str(input("Que bebida quiere tomar ?"))
#     print("Son $20.000")
# else:
#     print("No puede entrar por que esta chiquito")


import time
import math

numero1 = float(input("Ingrese el numero: "))
numero2 = float(input("Ingrese el numero: "))
print("""
      Opciones de mi calculadora:
    
        1. SUMAR (+)
        2. RESTAR (-)
        3. MULTIPLICAR (*)
        4. DIVIDIR (/)
        5. POTENCIA (**)
        6. RAIZ CUADRADA
        7. SALIR      
      
      """)
opcion = int(input("Ingrese la opcion que requiere : "))

if opcion >= 1 and opcion <= 7:
    print("OPCION CORRECTA")
    print("CALCULANDO..........")
    time.sleep(3)
    if opcion == 1: 
        resultado = numero1 + numero2
    elif opcion == 2:
        resultado = numero1 - numero2
    elif opcion == 3:
        resultado = numero1 * numero2
    elif opcion == 4:
        resultado = numero1 / numero2
    elif opcion == 5:
        resultado = numero1 ** numero2
    elif opcion == 6:
        numero_raiz = float(input("Ingrese el numero a sacar raiz cuadrada : "))
        resultado = math.sqrt(numero_raiz)
    else:
        print("Saliendo de la calculadora....")
        time.sleep(3)
        exit()
    print(f"""
          La operacion dio como resultado :
                    {resultado}
          
          
          
          
          """)
else:
    print("Aprenda a leer tonto")
        
    