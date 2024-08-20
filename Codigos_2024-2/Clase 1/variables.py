# nombre_completo = "Alejandro Sierra"
# edad = int(18)

# altura = float(1.80)

# print(nombre_completo,"\n", edad,"\n", altura)



# # Calculadora en python

# # numero1 = 0
# # numero2 = 0

# # SUMA (+)
# # RESTA (-)
# # MULT (*)
# # DIVISION (/) FLOAT
# # DIVISION (//) INT 
# # POTENCIA (**) 2**10
# # RAIZ (math.sqrt(9) = 3)



# numero1 = int(input("Ingrese el primer numero : "))
# numero2 = int(input("Ingrese el segundo numero : "))

# # Proceso 
# suma = numero1 + numero2
# resta = numero1 - numero2
# mult = numero1 * numero2
# div = numero1 / numero2
# div_int = numero1 // numero2
# potencia = numero1 ** numero2

# print("La suma es : ", suma)
# print("La resta es : ", resta)
# print("La multiplicacion es : ", mult)
# print("La division es : ", div)
# print("La division entera es : ", div_int)
# print("La potencia es : ", potencia)



# # # Entrada datos: 


# # nombre = input("Ingrese su nombre : ")


# # # Salida datos: 

# # print(nombre)










# Se requiere pedir la informacion de una persona 
# para despues mostrarla por pantalla

# *Nombre
# *Altura
# *Peso
# *Direccion
# *Telefono
# *IMC
# Formula IMC = peso / altura^2
# *Fecha de nacimiento
# Edad = 2024 - fecha_nacimiento
# *Calcular la edad 
# *Mostrar la informacion por pantalla

# ENTRADA DE DATOS
nombre = str(input("Ingrese su nombre  : "))
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
direccion = str(input("Ingrese su direccion : "))
telefono = str(input("Ingrese su numero : "))
fecha_nacimiento = int(input("Ingrese el año de nacimiento : "))


# PROCESO
imc = altura / peso**2
edad = 2024 - fecha_nacimiento

# SALIDA 

print("Su nombre es ", nombre)
print("Su direccion es " + direccion)

print(f"Altura : {altura}")
print(f"Peso : {peso}")
print(f"Telefono : {telefono}")
print(f"Edad : {edad}")
print(f"IMC : {imc} ")















