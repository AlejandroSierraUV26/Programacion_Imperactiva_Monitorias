"""
Se nos da un tiempo y debemos expresarlo de manera correcta.


Ejemplo:


Entrada: 5 minutos 30 segundos
Salida: 00:5:30

Ejemplo: 129 minutos 1290 segundos
Salida: 02:30:30

Ejemplo: 1 hora 120 minutos 120 segundos
Salida: 03:02:00


"""

def convertir_tiempos(horas, minutos, segundos):
    minutos += segundos // 60
    segundos = segundos % 60
    horas += minutos // 60
    minutos = minutos % 60
    return horas, minutos, segundos

if __name__ == "__main__":
    hora = 16
    minutos = 300
    segundos = 10002
    hora, minutos, segundos = convertir_tiempos(hora, minutos, segundos)
    print(f"{hora:02d}:{minutos:02d}:{segundos:02d}")

