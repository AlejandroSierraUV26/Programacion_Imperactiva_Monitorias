
def leer_archivo():
    with open(fr"Clase 9\archivos\mensaje.txt", "r") as archivo:
        contenido = archivo.read()
        nombres = contenido.split(",")

        print(nombres[0])
        nombres = [nombre.strip() for nombre in nombres] 
        
        return nombres
    
    

def escribir_archivo(nombres):
    with open(fr"Clase 9\archivos\mensaje.txt", "w") as archivo:
        nombre_nuevo = input("Ingresa un nuevo nombre: ")
        for nombre in nombres:
            archivo.write(f"{nombre}, ")
        archivo.write(f"{nombre_nuevo}")
        archivo.write("\n")
    

if __name__ == "__main__":
    nombres = leer_archivo()
    escribir_archivo(nombres)
    print(leer_archivo())
    print("Se ha escrito el archivo exitosamente.")
    
    
    