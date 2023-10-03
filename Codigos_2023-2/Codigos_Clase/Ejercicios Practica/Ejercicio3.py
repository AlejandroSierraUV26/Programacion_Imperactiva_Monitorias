def imc(peso,altura):
    if altura <1.0 or altura >2.5 or peso < 20 or peso >200:
        return None
    return peso/altura ** 2

print(imc(325.5,1.8))



"""
>>> a. 24.691358024691358
>>> b. 11.358024691351238
>>> c. 12.123242341358023
>>> d. None


"""