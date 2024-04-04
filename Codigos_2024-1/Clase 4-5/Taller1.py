"""
Elaborar un algoritmo que permita determinar cuál es el ganador de la beca de entre
cuatro estudiantes. El algoritmo deberáhallar la nota definitiva de cada uno de ellos (4
materias) Si es mayor que 4.5 el alumno podráaspirar a la beca, de lo contrario no.

"""

# def comprobar_beca(nota_estudiante):
#     if nota_estudiante >= 4.5:
#         return("Se aprobó para la beca")
#     else:
#         return("YUCA")
    
    
# def pedir_notas():
#     nota1= float(input("Nota 1: "))
#     nota2= float(input("Nota 2: "))
#     nota3= float(input("Nota 3: "))
#     nota4= float(input("Nota 4: "))
#     return (nota1,nota2,nota3,nota4)    

# def sacar_promedio():
#     n1,n2,n3,n4 = pedir_notas()
#     return (n1+n2+n3+n4)/4
    
# # Estudiante 1
# nota_promedio = sacar_promedio()
# print(comprobar_beca(nota_promedio))

# # Estudiante 2
# nota_promedio = sacar_promedio()
# print(comprobar_beca(nota_promedio))

# # Estudiante 3
# nota_promedio = sacar_promedio()
# print(comprobar_beca(nota_promedio))

# # Estudiante 4
# nota_promedio = sacar_promedio()
# print(comprobar_beca(nota_promedio))



"""
Elaborar un algoritmo que determine si un año ingresado por teclado es o no bisiesto.


"""

# def determinar_bisiesto(año):
#     if año % 4 == 0:
#         return "Es bisiesto"
#     return "No es bisiesto"

# print(determinar_bisiesto(2018))

"""
Elabore un algoritmo que descomponga un número entero de tres cifras en sus dígitos y
luego imprima cada uno de ellos en letras.


"""

# def descomponer_numero(numero):
#     if numero >=100 and numero < 1000:
#         a = numero // 100 
#         numero = numero % 100
#         b = numero //10
#         numero = numero % 10
#         c = numero % 10
#         return a,b,c
#     return "No es posible"
    
# print(descomponer_numero(123))
# print(descomponer_numero(1))
# print(descomponer_numero(12345))
# print(descomponer_numero(222))



"""
Elaborar un algoritmo que lea dos números ingresados por el usuario, si la suma de los dos
números es negativa, mostrar su promedio , de lo contrario mostrar si el resultado es par o
impar.


"""



def algortimo(num1,num2):
    if num1+num2 < 0: 
        return (num1+num2)/2
    if num1+num2 % 2 == 0:
        return "Es par"
    return "Es impar"


# # <Verdadero> if <Condicion> else <Falso>
# numero = 50
# print("Es divisible entre 5" if numero % 5 == 0 else "No es  divisible entre 5")


print(algortimo(1,2))
print(algortimo(1,-2))

print(algortimo(0,0))



"""
Diseñe el algorimtmo que imprima la serie

1/2 - 3/4 + 5/6 - 7/8 + 9/10 - 11/12 + ... + 99/100



"""

for i in range(1,100,2):
    print(f"{i}/{i+1}")