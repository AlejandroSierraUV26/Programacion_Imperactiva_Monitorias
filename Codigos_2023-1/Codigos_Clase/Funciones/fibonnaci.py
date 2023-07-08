def fibonnaci(n):
    if n <= 2:
        return 1
    return fibonnaci(n-1) + fibonnaci(n-2)

#* Muestra los primeros 10 numeros de la recurrencia

for i in range(10):
    print(fibonnaci(i))