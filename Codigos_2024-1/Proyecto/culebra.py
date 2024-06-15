# Crear un juego de la culebra con python y con objetos en pygame

import pygame
import time
import random

pygame.init()

# Colores
blanco = (255, 255, 255)

# Tamaño de la pantalla
ancho = 800
alto = 600

# Tamaño de la celda
tamano_celda = 20

# Velocidad de la culebra
velocidad = 20

# Cargar la fuente
fuente = pygame.font.Font(None, 36)

# Crear la pantalla
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Culebra")

# Reloj
reloj = pygame.time.Clock()


class Celda:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dibujar(self):
        pygame.draw.rect(pantalla, blanco, (self.x, self.y, tamano_celda, tamano_celda))
    
    def colision(self, celda):
        return self.x == celda.x and self.y == celda.y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __eq__(self, celda):
        return self.x == celda.x and self.y == celda.y
    
    def __ne__(self, celda):
        return self.x != celda.x or self.y != celda.y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __add__(self, celda):
        return Celda(self.x + celda.x, self.y + celda.y)
    
    def __sub__(self, celda):
        return Celda(self.x - celda.x, self.y - celda.y)
    
    def __mul__(self, celda):
        return Celda(self.x * celda.x, self.y * celda.y)
    
    def __truediv__(self, celda):
        return Celda(self.x // celda.x, self.y // celda.y)
    

class Culebra:
    def __init__(self, celda):
        self.cuerpo = [celda]
        self.direccion = Celda(1, 0)
        self.crecer = False
    
    def mover(self):
        cabeza = self.cuerpo[0] + self.direccion
        self.cuerpo.insert(0, cabeza)
        if not self.crecer:
            self.cuerpo.pop()
        else:
            self.crecer = False
    
    def crecer(self):
        self.crecer = True
    
    def colision(self):
        cabeza = self.cuerpo[0]
        return cabeza in self.cuerpo[1:]
    
    def dibujar(self):
        for celda in self.cuerpo:
            celda.dibujar()


class Comida:
    def __init__(self):
        self.celda = Celda(random.randint(0, ancho // tamano_celda - 1) * tamano_celda, random.randint(0, alto // tamano_celda - 1) * tamano_celda)
    
    def dibujar(self):
        self.celda.dibujar()
    
    def colision(self, celda):
        return self.celda == celda
    
    def mover(self):
        self.celda = Celda(random.randint(0, ancho // tamano_celda - 1) * tamano_celda, random.randint(0, alto // tamano_celda - 1) * tamano_celda)
    

def juego():
    culebra = Culebra(Celda(ancho // 2, alto // 2))
    comida = Comida()
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    culebra.direccion = Celda(0, -1)
                if evento.key == pygame.K_DOWN:
                    culebra.direccion = Celda(0, 1)
                if evento.key == pygame.K_LEFT:
                    culebra.direccion = Celda(-1, 0)
                if evento.key == pygame.K_RIGHT:
                    culebra.direccion = Celda(1, 0)
        
        culebra.mover()
        if culebra.colision():
            break
        if comida.colision(culebra.cuerpo[0]):
            culebra.crecer()
            comida.mover()
        
        pantalla.fill((0, 0, 0))
        culebra.dibujar()
        comida.dibujar()
        pygame.display.update()
        reloj.tick(velocidad)
        

juego()

    
    