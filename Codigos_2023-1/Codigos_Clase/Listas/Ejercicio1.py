
"""
Ejercicio 1.	
Realizar un algoritmo que genere un codigo de 4 digitos, 
dos alfabeticos y dos numericos.
"""
import random
#*Libreria Inicializada
codigo = []

#*Crear las palabras a usar
letras = ["A", "B", "C", "D", "E", "F", "G", 
          "H", "I", "J", "K", "L", "M", "N", 
          "Ñ", "O", "P", "Q", "R", "S", "T", 
          "U", "V", "W", "X", "Y", "Z"]


#*Ingresar las letras en la lista
for j in range(0,2):
    n  = random.randint(0,len(letras)+1)
    codigo.append(letras[n])
    
#*Crear los numeros a usar
for i in range(0,2):
    x = random.randint(0,10)
    codigo.append(x)
    


print(codigo)
