def f(x,y):
    if x == 0:
        return y
    else:
        return f(x-1,y+1)
    
def g(x):
    if x == 0:
        return 1
    else:
        return f(x-1,1)

print(g(3))

# What is the output of this code?

# A) 1
# B) 2
# C) 3

# Realizar el mapeo de cada recursión para entender el flujo de la función.