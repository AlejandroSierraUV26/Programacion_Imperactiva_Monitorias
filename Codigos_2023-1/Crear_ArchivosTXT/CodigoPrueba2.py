def guardar_mensaje(mensaje, carpeta, nombre_archivo,numero):
    numero = str(numero)
    ruta = carpeta + '/' + nombre_archivo + "_" + numero + '.txt'
    
    with open(ruta, 'w') as archivo:
        archivo.write(mensaje)
    print("El mensaje se ha guardado en el archivo", nombre_archivo + "." + numero  + '.txt')
    print()

def leer_archivo(direccion,nombre,numero):
    numero = str(numero)
    ruta = direccion + "/" + nombre + "_" + numero + '.txt'
    with open(ruta, 'r') as archivo:
        contenido = archivo.read()
    return contenido

def enviar_mensaje():
    for i in range(0,10):
        mensaje = f"Este es mi mensaje de prueba. {i+1}"
        guardar_mensaje(mensaje, carpeta_destino, nombre_archivo,i+1)
    
def mostrar_mensaje():
    print("Contenido del archivo:")
    for i in range(0,10):
        try:
            contenido_archivo = leer_archivo(carpeta_destino,nombre_archivo,i+1)
            print(f"Archivo {i+1}")
            print(contenido_archivo)
            print()
        except FileNotFoundError:
            print("El archivo no se encontró en la ruta especificada.")


carpeta_destino = "C:/Users/Alejandro/Desktop/Carpeta_Prueba"  
nombre_archivo = "mensaje_guardado"
enviar_mensaje()
mostrar_mensaje()



# #? Crear y guardar los archivos

# for i in range(0, 10):
#     numero = str(i+1)
#     nombre_archivo = "archivo"
#     mensaje = "Alejandro Sierra"
#     carpeta = "C:/Users/Alejandro/Desktop/Carpeta_Prueba"  
#     ruta = carpeta + '/' + nombre_archivo +'_'+ numero + '.txt'

#     with open(ruta, 'w') as archivo:
#         archivo.write(mensaje)
#     print("El mensaje se ha guardado en el archivo", nombre_archivo + '.txt')
#     print()

# #* Recolectar informacion de los archivos

# for j in range(0,10): 
#     numero = str(j+1)
#     print(f"Archivo {j+1}")
#     ruta_leer = carpeta + "/" + nombre_archivo + "_" + numero + '.txt'
#     with open(ruta_leer, 'r') as archivo:
#         contenido = archivo.read()
#         print(contenido)
        















