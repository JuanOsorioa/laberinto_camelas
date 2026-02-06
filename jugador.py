"""
Clase del jugador
"""
import pygame

class Jugador:
    def __init__(self, username):
        self.username = username
        self.posicion = (0, 0)  # Empezar en la esquina superior izquierda
        self.puntos = 0
        self.vidas = 3
        self.color = (0, 0, 255)  # Azul
        
    def mover(self, tecla, laberinto):
        """Mueve al jugador según la tecla presionada"""
        x, y = self.posicion
        nueva_x, nueva_y = x, y
        
        if tecla == pygame.K_UP or tecla == pygame.K_w:
            nueva_y -= 1
        elif tecla == pygame.K_DOWN or tecla == pygame.K_s:
            nueva_y += 1
        elif tecla == pygame.K_LEFT or tecla == pygame.K_a:
            nueva_x -= 1
        elif tecla == pygame.K_RIGHT or tecla == pygame.K_d:
            nueva_x += 1
        
        # Verificar si el movimiento es válido
        if not laberinto.es_pared(nueva_x, nueva_y):
            self.posicion = (nueva_x, nueva_y)
            self.puntos += 1
    
    def dibujar(self, screen):
        """Dibuja al jugador en la pantalla"""
        tamanho_celda = min(screen.get_width() // 20, 
                           screen.get_height() // 20)
        
        pygame.draw.circle(screen, self.color,
                          (self.posicion[0] * tamanho_celda + tamanho_celda // 2,
                           self.posicion[1] * tamanho_celda + tamanho_celda // 2),
                          tamanho_celda // 3)
    
    def perder_vida(self):
        """El jugador pierde una vida"""
        self.vidas -= 1
        return self.vidas > 0
