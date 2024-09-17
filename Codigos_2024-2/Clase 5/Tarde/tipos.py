# Globales 
num = 1
pal = "Hola"


# Locales
def sumar(a,b):
    global resultado
    resultado = num # 1
    resultado += a+b # 1 + a + b
    return resultado

def obtener_datos():
    ruta = fr"Clase 5\Tarde\mensaje.txt"
    with open(ruta, "r") as archivo:
        datos = archivo.read()
    return datos

        
print(obtener_datos())