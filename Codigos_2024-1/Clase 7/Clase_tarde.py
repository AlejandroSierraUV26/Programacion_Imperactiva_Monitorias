"""
Realizar un algortimo que cuente cuantas vocales tiene una palabra: 

Ejemplo:

adacadabra --> a => 5

abecedario --> a => 2, e => 2, i => 1, o => 1
"""
def contador_no_vacio(contador, letra):
    if contador != 0:
        return f"{letra} =  {contador}"
    else:
        return " "
palabra = "abecedario"
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
contador5 = 0 
for i in palabra:
    if i == "a":
        contador1+=1
    elif i == "e":
        contador2+=1
    elif i == "i":
        contador3+=1
    elif i == "o":
        contador4+=1
    elif i == "u":
        contador5+=1

print(f"""La palabra {palabra} tiene 
      {contador_no_vacio(contador1,"a")}
      {contador_no_vacio(contador2,"e")}
      {contador_no_vacio(contador3,"i")}
      {contador_no_vacio(contador4,"o")}
      {contador_no_vacio(contador5,"u")}
      
      """)
        


"""
Determinar si una oracion es palindromo:


ejemplo:

reconocer --> Es palindromo

casa --> No es palindromo

oso --> Es palindromo

anita lava la tina --> Es palindromo



"""
def ispalindromo(palabra):
    palabrainvetrida = palabra[::-1].lower().replace(" ","")
    print(palabrainvetrida)
    if palabra.lower().replace(" ","") == palabrainvetrida:
        print("Es un palindromo")
    else:
        print("No es un palindromo")

ispalindromo("anita lava la tina")