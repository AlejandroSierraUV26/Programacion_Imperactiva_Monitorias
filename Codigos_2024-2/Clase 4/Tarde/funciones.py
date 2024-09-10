def Esprimo(numero):
    contador = 0
    for i in range(2,numero):
        if numero % i == 0:
            contador += 1

    if contador == 0:
        return True
    else:
        return False
    
# for i in range(2,100):
#     if not Esprimo(i):
#         print(i, end=",")
        
        
        
        
# 0 1 1 2 3 5 8 13 21 34 55 89 144 ... ... ... 

# a,b = 0,1

# for i in range(20):
#     print(a, end=", ")
#     a,b = b,a+b



numero = 123

c = numero // 100
print(c)
numero = numero % 100
print(numero)