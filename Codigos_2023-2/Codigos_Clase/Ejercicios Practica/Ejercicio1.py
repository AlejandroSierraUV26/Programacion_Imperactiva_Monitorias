def factorial(n):
    # # Caso base
    if n == 1:
        return 1
    # Caso recursivo
    return n * factorial(n-1)
print(factorial(5))

"""
>>> A. 120
>>> B. 20
>>> C. RecursionError: maximum recursion depth exceeded
>>> D. 10 

"""
