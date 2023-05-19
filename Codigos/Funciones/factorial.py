def factorial(n):
    if n < 1:
        return 1
    else:
        return factorial(n - 1) * n
    
print(factorial(5))
#?Imprime 120 = 1*2*3*4*5
