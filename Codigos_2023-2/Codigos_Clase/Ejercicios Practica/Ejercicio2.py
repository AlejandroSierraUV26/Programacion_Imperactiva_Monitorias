a = 1
b = 10
def fun():
    a = 2
    global b
    print(a+b)
fun()
print(a)

"""
>>> a. 1 2
>>> b. 2 2
>>> c. 2 1
>>> d. 1 1


"""