# 📍 GPS Tracker Simple

Sistema de tracking GPS en tiempo real con múltiples usuarios conectados simultáneamente.

## Instalación

```bash
git clone https://github.com/benyhi/efi_redes.git
cd efi_redes
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python database.py
python server.py
```

Acceder a: `http://localhost:5000`

## Usuarios por defecto

- **admin** / admin123
- **user** / 123456  
- **demo** / demo

## Endpoints

### HTTP
- `GET /` - Dashboard principal
- `POST /login` - Autenticación de usuario
- `POST /register` - Registro de nuevo usuario
- `GET /users` - Lista de usuarios
- `GET /status` - Estado del servidor

### WebSocket
- `location_update` - Cliente envía ubicación GPS
- `coordinates_update` - Servidor envía ubicaciones a todos los clientes