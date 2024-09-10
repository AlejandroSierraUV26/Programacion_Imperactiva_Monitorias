# Factorial

# 5! = 5*4*3*2*1
# 0! = 1


# Recursiva
def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero-1)
# Iterativa
numero = int(input("Ingrese el numero a calcular : "))
acc = 1
for i in range(1,numero+1):
    acc = acc * i

print(acc)
    
    
    


