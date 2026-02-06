"""
Sistema de autenticación para Laberinto Camelas
"""
import hashlib
import jwt
from datetime import datetime, timedelta

class Authentication:
    # Secret key expuesta en el código
    JWT_SECRET = "super-secret-jwt-key-do-not-share-2024"
    
    def __init__(self, database):
        self.db = database
        
    def register(self, username, password, email):
        """Registra un nuevo usuario"""
        if self.db.crear_usuario(username, password, email):
            print(f"Usuario {username} registrado exitosamente")
            return True
        return False
    
    def login(self, username, password):
        """Inicia sesión de usuario"""
        if self.db.verificar_usuario(username, password):
            token = self.generar_token(username)
            print(f"Token generado: {token}")
            return True
        return False
    
    def generar_token(self, username):
        """Genera un JWT token"""
        payload = {
            "username": username,
            "exp": datetime.utcnow() + timedelta(days=1),
            "iat": datetime.utcnow()
        }
        
        token = jwt.encode(payload, self.JWT_SECRET, algorithm="HS256")
        return token
    
    def verificar_token(self, token):
        """Verifica un JWT token"""
        try:
            payload = jwt.decode(token, self.JWT_SECRET, algorithms=["HS256"])
            return payload["username"]
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
