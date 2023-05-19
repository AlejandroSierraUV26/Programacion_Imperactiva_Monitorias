"""
Autores: Alejandro Sierra Betancourt / Tina Maria Torres Tascon
Codigo Estudiante: 2259559-3743      / 2259729-3743
Fecha: 07/04/2022
Laboratorio 2
Descripcion: Fundamentos de programación. Punto 3 
"""

#Función que calcula el IMC
def imc(peso,altura):
    return peso/altura**2
#Función que indica el estado de obseidad
def obesidad(peso,altura):
    imc = peso/altura**2
    if imc <18.5:
        return "Bajo Peso"
    elif imc >=18.5 and imc<25.0:
        return "Peso normal"
    elif imc >=25.0 and imc<30:
        return "Sobre Peso"
    elif imc >=30:
        return "Obesidad Tipo I"
#Recoleccion de variables por parte del usuario
nombre = str(input("Ingrese su nombre: "))
peso = float(input("Ingrese su peso en kilos: "))
altura = float(input("Ingrese su altura en metros: "))
#Salida de los datos
print(f"Nombre . . . . . . . : {nombre} \n Peso . . . . . . . :{peso} kg\n Estatura . . . . . . . :{altura} m\n IMC . . . . . . . :{round(imc(peso,altura),2)}\n Estado de obesidad . . . . . . . :{obesidad(peso,altura)}")