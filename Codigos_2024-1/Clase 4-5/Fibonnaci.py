# a,b = 0,1

# while b<55:
#     a,b = b,a+b
#     print(b)
    
    
a,b = 0,1
while b<55:
    aux = a
    a = b
    b = aux + a
    print(b)
    
    