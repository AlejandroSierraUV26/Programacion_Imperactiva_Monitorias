def obtener_datos(ruta):
    with open(ruta, "r") as archivo:
        nombres = archivo.read()
        nombres = nombres.split(",")
        
        nombres = [nombre.strip().strip('"') for nombre in nombres]
    return nombres

def escribir_nuevo_nombre(nombre_nuevo, ruta):
    nombres = obtener_datos(ruta)
    with open(ruta, "w") as archivo:
        for i in nombres:
            archivo.write(i)
            archivo.write(", ")
        archivo.write(nombre_nuevo)

def actualizar_nombres(nombres,ruta):
    with open(ruta, "w") as archivo:
        for i in range(len(nombres)):
            archivo.write(nombres[i])
            if i == len(nombres)-1:
                break
            else:
                archivo.write(", ")    
def buscar_modificar(nombre_buscar,nombre_nuevo,ruta):
    nombres = obtener_datos(ruta)
    
    for i in range(0,len(nombres)):
        if nombres[i] == nombre_buscar:
            nombres.remove(nombres[i])
            nombres.insert(i,nombre_nuevo)
    actualizar_nombres(nombres, ruta)
    
            
    
if __name__ == "__main__":
    ruta = fr"Clase 9\archivos\mensaje.txt"
    buscar_modificar("Alejandro","Pepe",ruta)
    
    
    # for i in range(10):
    #     nombres = input("Ingrese el nuevo nombre : ")
    #     escribir_nuevo_nombre(nombres, ruta)
    
