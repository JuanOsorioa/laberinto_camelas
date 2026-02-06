"""
Generador y lógica del laberinto
"""
import random
import pygame

class Laberinto:
    def __init__(self, ancho=20, alto=20):
        self.ancho = ancho
        self.alto = alto
        self.grid = self.generar_laberinto()
        self.salida = (ancho - 1, alto - 1)
        
    def generar_laberinto(self):
        """Genera un laberinto aleatorio"""
        grid = [[1 for _ in range(self.ancho)] for _ in range(self.alto)]
        
        # Algoritmo simple de generación de caminos
        def crear_camino(x, y):
            direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            random.shuffle(direcciones)
            
            for dx, dy in direcciones:
                nx, ny = x + dx * 2, y + dy * 2
                
                if 0 <= nx < self.ancho and 0 <= ny < self.alto and grid[ny][nx] == 1:
                    grid[y + dy][x + dx] = 0
                    grid[ny][nx] = 0
                    crear_camino(nx, ny)
        
        # Empezar desde la esquina superior izquierda
        grid[0][0] = 0
        crear_camino(0, 0)
        
        # Asegurar que la salida esté abierta
        grid[self.alto - 1][self.ancho - 1] = 0
        
        return grid
    
    def es_pared(self, x, y):
        """Verifica si una posición es una pared"""
        if 0 <= x < self.ancho and 0 <= y < self.alto:
            return self.grid[y][x] == 1
        return True
    
    def dibujar(self, screen):
        """Dibuja el laberinto en la pantalla"""
        tamanho_celda = min(screen.get_width() // self.ancho, 
                           screen.get_height() // self.alto)
        
        for y in range(self.alto):
            for x in range(self.ancho):
                color = (50, 50, 50) if self.grid[y][x] == 1 else (200, 200, 200)
                pygame.draw.rect(screen, color, 
                               (x * tamanho_celda, y * tamanho_celda, 
                                tamanho_celda, tamanho_celda))
        
        # Dibujar la salida
        pygame.draw.rect(screen, (0, 255, 0),
                        (self.salida[0] * tamanho_celda, 
                         self.salida[1] * tamanho_celda,
                         tamanho_celda, tamanho_celda))
    
    def verificar_victoria(self, posicion):
        """Verifica si el jugador llegó a la salida"""
        return posicion == self.salida
