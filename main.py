#!/usr/bin/env python3
"""
Laberinto Camelas - Juego principal
"""
import pygame
import sys
from database import Database
from laberinto import Laberinto
from jugador import Jugador
from auth import Authentication

# Inicializar pygame
pygame.init()

# Constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Laberinto Camelas")
        self.clock = pygame.time.Clock()
        self.running = True
        self.db = Database()
        self.auth = Authentication(self.db)
        self.current_user = None
        self.laberinto = None
        self.jugador = None
        
    def mostrar_menu_principal(self):
        """Muestra el menú principal del juego"""
        print("=== LABERINTO CAMELAS ===")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")
        return opcion
    
    def iniciar_sesion(self):
        """Proceso de inicio de sesión"""
        username = input("Usuario: ")
        password = input("Contraseña: ")
        
        if self.auth.login(username, password):
            self.current_user = username
            print(f"¡Bienvenido {username}!")
            return True
        else:
            print("Credenciales incorrectas")
            return False
    
    def registrar_usuario(self):
        """Proceso de registro"""
        username = input("Usuario: ")
        password = input("Contraseña: ")
        email = input("Email: ")
        
        if self.auth.register(username, password, email):
            print("¡Registro exitoso!")
            return True
        else:
            print("Error en el registro")
            return False
    
    def iniciar_juego(self):
        """Inicia el juego principal"""
        self.laberinto = Laberinto()
        self.jugador = Jugador(self.current_user)
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.jugador.mover(event.key, self.laberinto)
            
            # Actualizar pantalla
            self.screen.fill((0, 0, 0))
            self.laberinto.dibujar(self.screen)
            self.jugador.dibujar(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)
            
            # Verificar si completó el laberinto
            if self.laberinto.verificar_victoria(self.jugador.posicion):
                print(f"¡Victoria! Puntuación: {self.jugador.puntos}")
                self.db.guardar_puntuacion(self.current_user, self.jugador.puntos)
                break
    
    def run(self):
        """Loop principal del juego"""
        while True:
            opcion = self.mostrar_menu_principal()
            
            if opcion == "1":
                if self.iniciar_sesion():
                    self.iniciar_juego()
            elif opcion == "2":
                self.registrar_usuario()
            elif opcion == "3":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida")
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
