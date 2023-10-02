def f(x,y):
    x = y +2 
    return x, y 
def g(x,y):
    x,y = f(x,y)
    x = x + 10
    y = y - 10 * x
    return x, y 

print(g(-10,-10))
    
"""
Que imprimiria este codigo?

>>> A. (-188)
>>> B. (2, -30)
>>> C. (22,-210)
>>> D. (-28)

"""