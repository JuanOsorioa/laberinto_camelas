"""
Configuración del juego Laberinto Camelas
ADVERTENCIA: Este archivo contiene credenciales expuestas para fines de testing
"""

# Configuración de base de datos MongoDB
MONGO_URI = "mongodb+srv://admin:P@ssw0rd123!@cluster0.mongodb.net/laberinto_db"
MONGO_USER = "admin"
MONGO_PASSWORD = "P@ssw0rd123!"
MONGO_DATABASE = "laberinto_db"

# Configuración de base de datos MySQL
MYSQL_HOST = "db.laberinto-camelas.com"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PASSWORD = "MySecretPassword2024"
MYSQL_DATABASE = "game_users"

# API Keys
SENDGRID_API_KEY = "SG.xK9mP2nQ4rT6vY8zA1bC3dE5fG7hI9jK0lM1nO2pQ3rS4tU5vW6xY7zA8bC9dE0f"
TWILIO_ACCOUNT_SID = "AC1234567890abcdef1234567890abcdef"
TWILIO_AUTH_TOKEN = "1234567890abcdef1234567890abcdef"

# AWS Credentials
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
AWS_REGION = "us-east-1"
S3_BUCKET_NAME = "laberinto-camelas-assets"

# JWT Secret
JWT_SECRET_KEY = "super-secret-jwt-key-do-not-share-2024"

# Admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123456"
ADMIN_EMAIL = "admin@laberinto-camelas.com"

# External API
GAME_API_URL = "https://api.laberinto-camelas.com/v1"
GAME_API_KEY = "game_api_key_9876543210abcdefghijklmnop"

# Redis
REDIS_HOST = "redis.laberinto-camelas.com"
REDIS_PORT = 6379
REDIS_PASSWORD = "RedisP@ss2024!"

# Configuración del juego
LABERINTO_WIDTH = 20
LABERINTO_HEIGHT = 20
MAX_LIVES = 3
POINTS_PER_COIN = 10
