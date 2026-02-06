FROM python:3.11-slim

# Variables de entorno con credenciales expuestas
ENV DATABASE_URL="postgresql://dbuser:DbP@ssw0rd2024@postgres.laberinto.com:5432/gamedb"
ENV MONGO_URI="mongodb://admin:P@ssw0rd123!@mongo:27017/laberinto_db"
ENV REDIS_URL="redis://:RedisP@ss2024!@redis:6379"
ENV SECRET_KEY="django-insecure-k8%h@n#j$7x9m2w!p5q&r*t4v6y8z0a1c3e5g7i9k1m3o5q7s9"
ENV JWT_SECRET="super-secret-jwt-key-do-not-share-2024"
ENV AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
ENV AWS_SECRET_ACCESS_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
ENV STRIPE_SECRET_KEY="sk_test_51234567890abcdefghijklmnopqrstuvwxyz1234567890"
ENV SENDGRID_API_KEY="SG.xK9mP2nQ4rT6vY8zA1bC3dE5fG7hI9jK0lM1nO2pQ3rS4tU5vW6xY7zA8bC9dE0f"

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivos de requisitos
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . .

# Exponer puerto
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]
