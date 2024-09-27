def imc(peso, altura):
    if (altura < 1.0 or altura > 2.5) or (peso < 20 or peso > 200): 
        return None
    return peso/ altura **2

print(imc(352.5,1.65))

# -> None
