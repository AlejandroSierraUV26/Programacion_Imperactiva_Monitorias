# Fibonnaci 
#! 0 1 2 3 4 5 6
#* 0 1 1 2 3 5 8

# def fibonnaci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonnaci(n-1) + fibonnaci(n-2)

# for i in range(6,0-1,-1):
#     print(fibonnaci(i))
    
# Mostrar los primeros 



#TODO: Sacar los n primeros numeros primos

# n = 10

# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29

def Es_primo(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    else:
        return True
    
n = int(input("Ingrese el valor a calcular : "))
acc = 0
i = 2
while acc<10:
    if Es_primo(i):
        acc+=1
        print(acc,i)
    i+=1
    
    