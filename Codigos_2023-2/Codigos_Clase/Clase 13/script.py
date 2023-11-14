    import pygame
    import random

    # Inicializar pygame
    pygame.init()

    # Configuración de la ventana
    ancho = 800
    alto = 600
    ventana = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Fuegos Artificiales")

    # Colores
    NEGRO = (0, 0, 0)
    BLANCO = (255, 255, 255)

    # Clase para representar una partícula
    class Particula:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.color = BLANCO
            self.velocidad_y = random.uniform(-3, -1)  # Velocidad vertical hacia arriba

        def mover(self):
            self.y += self.velocidad_y

        def dibujar(self, superficie):
            pygame.draw.circle(superficie, self.color, (int(self.x), int(self.y)), 2)

    # Lista de partículas
    particulas = []

    # Bucle principal
    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

        ventana.fill(NEGRO)

        # Crear nuevas partículas cuando se hace clic
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            for _ in range(10):
                particula = Particula(x, y)
                particulas.append(particula)

        # Mover y dibujar las partículas
        for particula in particulas:
            particula.mover()
            particula.dibujar(ventana)

        # Eliminar partículas que salen de la pantalla
        particulas = [particula for particula in particulas if 0 <= particula.y <= alto]

        pygame.display.update()

    pygame.quit()
