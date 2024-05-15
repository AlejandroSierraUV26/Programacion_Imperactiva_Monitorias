# with open(fr"Clase 9\archivos\mensaje_tarde.txt","r") as archivo:
#     contenido = archivo.read()
#     nombres = []
#     edad = []
#     contenido = contenido.split("\n")
#     nombres = contenido[0].split(",")
#     edades = contenido[1].split(",")
#     nombres = [nombre.strip() for nombre in nombres]
#     edades = [edad.strip() for edad in edades]
#     print(nombres)
#     print(edades)
    
#     for i in range(0,len(nombres)):
#         print(f"Nombre : {nombres[i]} \n Edad : {edades[i]}")
    

def agregar_persona():
    nombres = leer_archivo()
    with open(fr"Clase 9\archivos\mensaje_tarde.txt","a") as archivo:
        for i in range(0,len(nombres)):
            archivo.write("Martha")
            if i == len(nombres)-1:     
                break
            else:
                archivo.write(",")
def leer_archivo():
    with open(fr"Clase 9\archivos\mensaje_tarde.txt","r") as archivo:
        contenido = archivo.read()
        contenido = contenido.split(",")
        contenido = [nombre.strip() for nombre in contenido]
        
    return contenido