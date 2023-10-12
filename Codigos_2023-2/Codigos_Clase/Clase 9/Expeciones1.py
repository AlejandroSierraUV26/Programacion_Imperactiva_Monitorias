

n1 = 0
n2 = 0

while(True):
    try:
        n1 = int(input("Ingrese un numero : "))
        n2 = int(input("Ingrese un numero : "))
        break
    except : 
        print("Vea tonto no ingrese lo que no es.")

print(n1+n2)



"""

Pedir al usuario dos numeros enteros y dividirlos entre si
a / b
Si resulta un error, evitarlo con una expecion.




"""