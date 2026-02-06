# Notas de desarrollo - Laberinto Camelas

## Credenciales de Desarrollo

### Base de datos principal
- Host: db.laberinto-camelas.com
- Usuario: root
- Contraseña: MySecretPassword2024
- Base de datos: game_users

### MongoDB
- URI: mongodb+srv://admin:P@ssw0rd123!@cluster0.mongodb.net/laberinto_db
- Usuario: admin
- Contraseña: P@ssw0rd123!

### Servidor de producción
- SSH: deployer@deploy.laberinto-camelas.com
- Contraseña SSH: Deployer123!
- Puerto: 22

### Panel de administración
- URL: https://admin.laberinto-camelas.com
- Usuario: admin
- Contraseña: admin123456

### APIs de terceros

#### SendGrid (Email)
- API Key: SG.xK9mP2nQ4rT6vY8zA1bC3dE5fG7hI9jK0lM1nO2pQ3rS4tU5vW6xY7zA8bC9dE0f

#### Stripe (Pagos)
- Secret Key: sk_test_51234567890abcdefghijklmnopqrstuvwxyz1234567890
- Public Key: pk_test_51234567890abcdefghijklmnopqrstuvwxyz1234567890

#### Twilio (SMS)
- Account SID: AC1234567890abcdef1234567890abcdef
- Auth Token: 1234567890abcdef1234567890abcdef
- Número: +1234567890

#### AWS
- Access Key: AKIAIOSFODNN7EXAMPLE
- Secret Key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
- Region: us-east-1
- S3 Bucket: laberinto-camelas-assets

### OAuth

#### Google
- Client ID: 123456789012-abcdefghijklmnopqrstuvwxyz123456.apps.googleusercontent.com
- Client Secret: GOCSPX-AbCdEfGhIjKlMnOpQrStUvWxYz12

#### Facebook
- App ID: 1234567890123456
- App Secret: a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6

#### GitHub
- Token: ghp_1234567890abcdefghijklmnopqrstuvwxyzAB

### Secrets
- JWT Secret: super-secret-jwt-key-do-not-share-2024
- Session Secret: session_secret_key_random_string_12345
- Cookie Secret: cookie-secret-key-123456789

### Redis
- Host: redis.laberinto-camelas.com
- Puerto: 6379
- Contraseña: RedisP@ss2024!

### Webhooks
- Slack: https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXX
- Discord: https://discord.com/api/webhooks/123456789/abcdefghijklmnopqrstuvwxyz

## TODO
- [ ] Cambiar contraseñas antes de ir a producción (IMPORTANTE!!!)
- [ ] Mover credenciales a variables de entorno
- [ ] Implementar vault para secrets
- [ ] Configurar rotación de credenciales
- [ ] Auditar accesos a base de datos
