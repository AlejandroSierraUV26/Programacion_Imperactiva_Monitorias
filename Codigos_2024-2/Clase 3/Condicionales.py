# Condicionales -> Estructura de Control


# Estructura de Control

# Condicionales

edad = int(input("Ingrese su edad : "))

if edad >= 18 and edad <= 30: # [18,30]
    print("Puede entrar a la discoteca")
    if edad >=18 and edad<25:
        print("Puede entrar a la economica")
    elif edad >=25 and edad < 28:
        print("Puede entrar a palcos")
    elif edad == 29:
        print("Usted no puede entrar hoy")
    else:
        print("Usted tiene 30 años y puede entrar a VIP")
else:
    if edad < 18:
        print("Usted es un niño")
    else:
        print("Usted es un viejo verde")

# Hola Mundo
# Hola Alejandro
# 