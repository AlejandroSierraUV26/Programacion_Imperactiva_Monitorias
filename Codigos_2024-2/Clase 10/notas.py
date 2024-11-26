# generar 10 mil notas aleatorias de 10 mil estudiantes, para guardarlos en un txt


import random

nombres = ['Juan', 'Pedro', 'Maria', 'Jose', 'Ana', 'Luis', 'Carlos', 'Sofia', 'Laura', 'Fernando', 'Ricardo', 'Roberto', 'Raul', 'Rosa', 'Luisa']

apellido = ['Perez', 'Gomez', 'Gonzalez', 'Rodriguez', 'Fernandez', 'Lopez', 'Martinez', 'Sanchez', 'Torres', 'Ramirez', 'Diaz', 'Vargas', 'Mendoza', 'Castro', 'Gutierrez']    


def generar_nombre():
    return random.choice(nombres) + ' ' + random.choice(apellido)

def generar_nota(nombre):
    # Notas desde el 0.0 a 5.0
    return random.randint(0, 50) / 10

def generar_estudiantes(n):
    with open('notas.txt', 'w') as archivo:
        for i in range(n):
            nombre = generar_nombre()
            nota = generar_nota(nombre)
            archivo.write(f'{nombre}, {nota}\n')
            
    
if __name__ == '__main__':
    generar_estudiantes(10000)
    print('Archivo generado exitosamente')

    