"""
Crear un codigo que guarde los nombres de las personas ingresadas 
en un txt 
Y comprobar si ya se encuetra dentro del txt


"""
def comprobar_Correo_arroba(correo):
    if '@' in correo:
        return True
    else:
        return False
def comprobar_Correo_punto(correo):
    if '.com' or '.co' or '.edu.co' in correo:
        return True
    else:
        return False
def verificar_dominio(correo):
    if '@' in correo:
        correo = correo.split('@')
        if correo[1] == 'correounivalle.edu.co':
            return True
        elif correo[1] == 'gmail.com':
            return True
        elif correo[1] == 'hotmail.com':
            return True
        elif correo[1] == 'yahoo.com':
            return True
        elif correo[1] == 'outlook.com':
            return True
        else:
            return False
    else:
        return False
    
def guardar_persona(persona):
    with open("personas.txt", "a") as archivo:
        archivo.write(persona + '\n')

if __name__ == "__main__":
    correo = str(input("Ingrese su correo : "))
    print(comprobar_Correo_punto(correo) and comprobar_Correo_arroba(correo) and verificar_dominio(correo))

    
    
    