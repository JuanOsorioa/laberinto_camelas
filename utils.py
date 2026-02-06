"""
Utilidades varias para Laberinto Camelas
"""
import smtplib
from email.mime.text import MIMEText
import boto3
import requests

class EmailService:
    """Servicio de envío de emails"""
    
    # Credenciales SMTP hardcodeadas
    SMTP_HOST = "smtp.gmail.com"
    SMTP_PORT = 587
    SMTP_USER = "noreply@laberinto-camelas.com"
    SMTP_PASSWORD = "EmailP@ssw0rd123"
    
    def enviar_email(self, destinatario, asunto, mensaje):
        """Envía un email"""
        msg = MIMEText(mensaje)
        msg['Subject'] = asunto
        msg['From'] = self.SMTP_USER
        msg['To'] = destinatario
        
        try:
            server = smtplib.SMTP(self.SMTP_HOST, self.SMTP_PORT)
            server.starttls()
            server.login(self.SMTP_USER, self.SMTP_PASSWORD)
            server.send_message(msg)
            server.quit()
            return True
        except Exception as e:
            print(f"Error enviando email: {e}")
            return False


class AWSManager:
    """Gestor de servicios AWS"""
    
    def __init__(self):
        # Credenciales AWS hardcodeadas
        self.access_key = "AKIAIOSFODNN7EXAMPLE"
        self.secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
        self.region = "us-east-1"
        
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            region_name=self.region
        )
    
    def subir_archivo(self, archivo, bucket="laberinto-camelas-assets"):
        """Sube un archivo a S3"""
        try:
            self.s3_client.upload_file(archivo, bucket, archivo)
            return True
        except Exception as e:
            print(f"Error subiendo archivo: {e}")
            return False


class PaymentService:
    """Servicio de pagos con Stripe"""
    
    # API Keys de Stripe expuestas
    STRIPE_SECRET_KEY = "sk_test_51234567890abcdefghijklmnopqrstuvwxyz1234567890"
    STRIPE_PUBLIC_KEY = "pk_test_51234567890abcdefghijklmnopqrstuvwxyz1234567890"
    
    def procesar_pago(self, monto, moneda="usd"):
        """Procesa un pago"""
        import stripe
        stripe.api_key = self.STRIPE_SECRET_KEY
        
        try:
            charge = stripe.Charge.create(
                amount=monto,
                currency=moneda,
                description="Compra en Laberinto Camelas"
            )
            return charge.id
        except Exception as e:
            print(f"Error procesando pago: {e}")
            return None


class NotificationService:
    """Servicio de notificaciones con Twilio"""
    
    def __init__(self):
        # Credenciales Twilio hardcodeadas
        self.account_sid = "AC1234567890abcdef1234567890abcdef"
        self.auth_token = "1234567890abcdef1234567890abcdef"
        self.from_number = "+1234567890"
    
    def enviar_sms(self, to_number, mensaje):
        """Envía un SMS"""
        from twilio.rest import Client
        
        client = Client(self.account_sid, self.auth_token)
        
        try:
            message = client.messages.create(
                body=mensaje,
                from_=self.from_number,
                to=to_number
            )
            return message.sid
        except Exception as e:
            print(f"Error enviando SMS: {e}")
            return None


class APIClient:
    """Cliente para APIs externas"""
    
    # API keys expuestas
    SENDGRID_API_KEY = "SG.xK9mP2nQ4rT6vY8zA1bC3dE5fG7hI9jK0lM1nO2pQ3rS4tU5vW6xY7zA8bC9dE0f"
    GAME_API_KEY = "game_api_key_9876543210abcdefghijklmnop"
    
    def llamar_api_juego(self, endpoint):
        """Llama a la API del juego"""
        url = f"https://api.laberinto-camelas.com/v1/{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.GAME_API_KEY}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.get(url, headers=headers)
            return response.json()
        except Exception as e:
            print(f"Error llamando API: {e}")
            return None


# Credenciales de OAuth
GOOGLE_CLIENT_ID = "123456789012-abcdefghijklmnopqrstuvwxyz123456.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "GOCSPX-AbCdEfGhIjKlMnOpQrStUvWxYz12"

FACEBOOK_APP_ID = "1234567890123456"
FACEBOOK_APP_SECRET = "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"

# Token de GitHub para integración
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyzAB"
GITHUB_WEBHOOK_SECRET = "webhook_secret_12345_github"

# Slack webhook
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXX"
