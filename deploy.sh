#!/bin/bash

# Script de deployment para Laberinto Camelas
# ADVERTENCIA: Contiene credenciales expuestas

echo "Iniciando deployment de Laberinto Camelas..."

# Variables de configuración
DEPLOY_USER="deployer"
DEPLOY_PASSWORD="Deployer123!"
DEPLOY_SERVER="deploy.laberinto-camelas.com"

# Credenciales de base de datos
DB_HOST="db.laberinto-camelas.com"
DB_USER="root"
DB_PASSWORD="MySecretPassword2024"
DB_NAME="game_users"

# Credenciales AWS
export AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
export AWS_SECRET_ACCESS_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
export AWS_DEFAULT_REGION="us-east-1"

# API Keys
SENDGRID_KEY="SG.xK9mP2nQ4rT6vY8zA1bC3dE5fG7hI9jK0lM1nO2pQ3rS4tU5vW6xY7zA8bC9dE0f"
STRIPE_KEY="sk_test_51234567890abcdefghijklmnopqrstuvwxyz1234567890"

# Conectar al servidor
echo "Conectando a $DEPLOY_SERVER..."
sshpass -p "$DEPLOY_PASSWORD" ssh $DEPLOY_USER@$DEPLOY_SERVER << 'ENDSSH'

# Actualizar código
cd /var/www/laberinto_camelas
git pull origin main

# Configurar variables de entorno
cat > .env << EOF
DATABASE_URL=postgresql://dbuser:DbP@ssw0rd2024@localhost:5432/gamedb
MONGO_URI=mongodb://admin:P@ssw0rd123!@localhost:27017/laberinto_db
SECRET_KEY=django-insecure-k8%h@n#j$7x9m2w!p5q&r*t4v6y8z0a1c3e5g7i9k1m3o5q7s9
JWT_SECRET=super-secret-jwt-key-do-not-share-2024
EOF

# Reiniciar servicios
sudo systemctl restart laberinto-game
sudo systemctl restart nginx

echo "Deployment completado!"

ENDSSH

# Backup de base de datos
echo "Realizando backup de base de datos..."
mysqldump -h $DB_HOST -u $DB_USER -p$DB_PASSWORD $DB_NAME > backup_$(date +%Y%m%d).sql

# Subir backup a S3
aws s3 cp backup_$(date +%Y%m%d).sql s3://laberinto-backups/

# Limpiar archivo de backup local
rm backup_$(date +%Y%m%d).sql

echo "Deployment completado exitosamente!"
