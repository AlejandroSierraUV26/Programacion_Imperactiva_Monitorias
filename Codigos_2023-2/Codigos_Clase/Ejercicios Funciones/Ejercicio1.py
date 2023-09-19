"""
1. Diseñe una función que reciba 3 números x,y,z, la función retorne el resultado de:

            1) (x^2+6y-3z)/x----->x>0
            
f(x,y,z) =  2) 2y-3 ------------->x=0

            3) x^3-7x+8y--------->x<0
    
"""

def f(x,y,z):
    if x>0:
        return (x**2+6*y-3*z)/x
    elif x==0:
        return 2*y-3
    else:
        return x**3-7*x+8*y

print(f"El resultado para la primera funcion es : {f(1,2,3)}")

print(f"El resultado para la segunda funcion es : {f(0,1,1)}")

print(f"El resultado para la tercera funcion es : {f(-1,0,1)}")


