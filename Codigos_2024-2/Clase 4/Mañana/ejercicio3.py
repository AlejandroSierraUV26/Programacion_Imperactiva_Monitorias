# Elabore un algoritmo que descomponga un numero entero de tres cifras en sus digitos y
# luego imprima cada uno de ellos en letras

# n => 123
# c = 1 d = 2 u = 3


# n = 123

# c = n // 100
# print(f"C : {c}")

# n = n % 100
# print(f"N = {n}")

# d = n // 10
# print(f"D {d}")
# n = n % 10
# print(f"N = {n}")

# u = n
# print(f"U = {u}")






# Realizar una funcion para determinar si un numero o palabra es capicua = palindromo

# reconocer = reconocer
# oso
# ala 

# 123 = F
# 121 = V
# 101 = V


# nombre = "Alejandro"
# nombre_rev = nombre[::-1] # Invertir una cadena Slices
# print(nombre_rev)


def int_binario(numero):
    result = ""
    while numero > 0:
        result = str(numero % 2) + result
        numero = numero // 2
    return result
    
    
print(int_binario(10))


 