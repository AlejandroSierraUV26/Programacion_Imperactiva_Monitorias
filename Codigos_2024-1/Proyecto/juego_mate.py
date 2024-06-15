import numpy as np

import matplotlib.pyplot as plt

# Generar la función lineal aleatoria
def lineal():
    a = int(np.random.uniform(-10, 10))
    b = int(np.random.uniform(-10, 10))

    # Generar puntos x en el rango [-10, 10]
    x = np.linspace(-10, 10, 100)


    y = a * x + b


    # Graficar la función lineal 
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Función Lineal Aleatoria \n y = {a}x + {b}')
    # Establecer los límites de los ejes x e y
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    # Agregar los ejes x e y
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    plt.grid(True)
    plt.show()
def cuadratica():
    # Generar coeficientes aleatorios para la función cuadrática
    a = int(np.random.uniform(-10, 10))
    b = int(np.random.uniform(-10, 10))
    c = int(np.random.uniform(-10, 10))

    # Generar puntos x en el rango [-10, 10]
    x = np.linspace(-10, 10, 100)

    # Calcular los valores y correspondientes a los puntos x
    y = a * x ** 2 + b * x + c

    # Graficar la función cuadrática
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Función Cuadrática Aleatoria \n y = {a}x^2 + {b}x + {c}')
    # Establecer los límites de los ejes x e y
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    # Agregar los ejes x e y
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    plt.grid(True)
    plt.show()
    
def exponencial():
    # Generar coeficientes aleatorios para la función exponencial
    a = int(np.random.uniform(-10, 10))
    b = int(np.random.uniform(-10, 10))

    # Generar puntos x en el rango [-10, 10]
    x = np.linspace(-10, 10, 100)

    # Calcular los valores y correspondientes a los puntos x
    y = a * np.exp(b * x)

    # Graficar la función exponencial
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Función Exponencial Aleatoria \n y = {a} * exp({b} * x)')
    # Establecer los límites de los ejes x e y
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    # Agregar los ejes x e y
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    plt.grid(True)
    plt.show()
    
def logaritmica():
    # Generar coeficientes aleatorios para la función logarítmica
    a = int(np.random.uniform(-10, 10))
    b = int(np.random.uniform(-10, 10))

    # Generar puntos x en el rango [0.1, 10]
    x = np.linspace(0.1, 10, 100)

    # Calcular los valores y correspondientes a los puntos x
    y = a * np.log(b * x)

    # Graficar la función logarítmica
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Función Logarítmica Aleatoria \n y = {a} * log({b} * x)')
    # Establecer los límites de los ejes x e y
    plt.xlim(0, 10)
    plt.ylim(-10, 10)

    # Agregar los ejes x e y
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    plt.grid(True)
    plt.show()
def ventana_respuesta():
    ventana = tk.Tk()
    ventana.geometry("400x400")
    label = tk.Label(ventana, text="Respuesta")
    punto = tk.Label(ventana, text="Punto de corte: ")
    entrada = tk.Entry(ventana)
    punto.pack()
    entrada.pack()
    punto2 = tk.Label(ventana, text="Punto de corte: ")
    entrada2 = tk.Entry(ventana)
    punto2.pack()
    entrada.pack()
    label.pack()
    ventana.mainloop()
def verificar_punto_corte_lineal():
    punto = int(punto.get())
    punto2 = int(punto2.get())
    
    return punto, punto2
def main():
    while True:
        print("Seleccione una opción:")
        print("1. Función Lineal")
        print("2. Función Cuadrática")
        print("3. Función Exponencial")
        print("4. Función Logarítmica")
        print("5. Salir")

        opcion = int(input("Opción: "))

        if opcion == 1:
            lineal()
        elif opcion == 2:
            cuadratica()
        elif opcion == 3:
            exponencial()
        elif opcion == 4:
            logaritmica()
        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print("Opción inválida")
        
if __name__ == '__main__':
    main()