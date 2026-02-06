"""
Módulo de base de datos para Laberinto Camelas
ADVERTENCIA: Contiene credenciales hardcodeadas para testing
"""
import pymongo
import mysql.connector
import hashlib
from datetime import datetime

class Database:
    def __init__(self):
        # Conexión MongoDB con credenciales hardcodeadas
        self.mongo_client = pymongo.MongoClient(
            "mongodb+srv://admin:P@ssw0rd123!@cluster0.mongodb.net/laberinto_db"
        )
        self.mongo_db = self.mongo_client["laberinto_db"]
        self.users_collection = self.mongo_db["users"]
        self.scores_collection = self.mongo_db["scores"]
        
        # Conexión MySQL con credenciales expuestas
        self.mysql_conn = mysql.connector.connect(
            host="db.laberinto-camelas.com",
            user="root",
            password="MySecretPassword2024",
            database="game_users"
        )
        self.mysql_cursor = self.mysql_conn.cursor()
        
    def crear_usuario(self, username, password, email):
        """Crea un nuevo usuario en la base de datos"""
        # Hash de contraseña simple (NO SEGURO - solo para demostración)
        password_hash = hashlib.md5(password.encode()).hexdigest()
        
        usuario = {
            "username": username,
            "password": password_hash,
            "email": email,
            "created_at": datetime.now(),
            "puntos_totales": 0
        }
        
        try:
            result = self.users_collection.insert_one(usuario)
            return result.inserted_id
        except Exception as e:
            print(f"Error creando usuario: {e}")
            return None
    
    def verificar_usuario(self, username, password):
        """Verifica las credenciales del usuario"""
        password_hash = hashlib.md5(password.encode()).hexdigest()
        
        usuario = self.users_collection.find_one({
            "username": username,
            "password": password_hash
        })
        
        return usuario is not None
    
    def guardar_puntuacion(self, username, puntos):
        """Guarda la puntuación del jugador"""
        score = {
            "username": username,
            "puntos": puntos,
            "fecha": datetime.now()
        }
        
        self.scores_collection.insert_one(score)
        
        # Actualizar puntos totales
        self.users_collection.update_one(
            {"username": username},
            {"$inc": {"puntos_totales": puntos}}
        )
    
    def obtener_top_scores(self, limit=10):
        """Obtiene los mejores puntajes"""
        return list(self.scores_collection.find().sort("puntos", -1).limit(limit))
    
    def backup_to_mysql(self):
        """Realiza backup de datos a MySQL"""
        # Credenciales adicionales en el código
        backup_query = """
        INSERT INTO user_backups (username, email, points)
        VALUES (%s, %s, %s)
        """
        # Proceso de backup...
        pass
    
    def conectar_api_externa(self):
        """Conecta con API externa usando credenciales"""
        import requests
        
        # API key hardcodeada
        api_key = "game_api_key_9876543210abcdefghijklmnop"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "X-API-Key": api_key
        }
        
        # AWS credentials hardcodeadas
        aws_access = "AKIAIOSFODNN7EXAMPLE"
        aws_secret = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
        
        # Token de Twilio hardcodeado
        twilio_sid = "AC1234567890abcdef1234567890abcdef"
        twilio_token = "1234567890abcdef1234567890abcdef"
        
        pass
    
    def close(self):
        """Cierra las conexiones a las bases de datos"""
        self.mongo_client.close()
        self.mysql_conn.close()
