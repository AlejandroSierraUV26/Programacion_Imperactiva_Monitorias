# # def saludo(nombre):
# #     print("Hola " + nombre)


# # saludo("Alejandro")
# # saludo("Juan")

# def f(x):
#     return x**2 + 2*x + 1

# x = 1
# y = f(x)

# print(y)
# print(f(x))

def operacion(a,b):
    global x
    x = 3
    a = 3
    if a == b:
        return "Son iguales"
    elif a>b:
        return "A es mayor que B"
    else:
        return "B es mayor que A"
a = 2
print(operacion(a,2))
print(x)

















