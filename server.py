from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit
import json
from datetime import datetime
import os

# Importar funciones de base de datos
from database import init_database, verify_user, create_user, get_all_users, delete_user

# Crear aplicación Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'gps_tracker_secret_key'

# Configurar Socket.IO
socketio = SocketIO(app, cors_allowed_origins="*", logger=True, engineio_logger=True)

# Inicializar base de datos al arrancar
init_database()

# Usuarios conectados
connected_users = {}
# Coordenadas en tiempo real    
live_coordinates = {}

# Rutas HTTP
@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({"error": "Usuario y contraseña requeridos"}), 400
        
        # Usar función de la base de datos
        user_info = verify_user(username, password)
        
        if user_info["success"]:
            return jsonify({
                "success": True, 
                "message": "Login exitoso",
                "user": {
                    "username": user_info["username"],
                    "email": user_info.get("email"),
                    "user_id": user_info["user_id"]
                }
            })
        else:
            return jsonify({"error": user_info["message"]}), 401
            
    except Exception as e:
        print(f"Error en login: {e}")
        return jsonify({"error": "Error en el servidor"}), 500

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        email = data.get('email', '')
        
        if not username or not password:
            return jsonify({"error": "Usuario y contraseña requeridos"}), 400
        
        # Crear usuario en la base de datos
        result = create_user(username, password, email)
        
        if result["success"]:
            return jsonify({
                "success": True,
                "message": result["message"],
                "user": {
                    "username": result["username"],
                    "user_id": result["user_id"]
                }
            })
        else:
            return jsonify({"error": result["message"]}), 400
            
    except Exception as e:
        print(f"Error en registro: {e}")
        return jsonify({"error": "Error en el servidor"}), 500

@app.route('/users', methods=['GET'])
def list_users():
    """Endpoint para administradores - listar usuarios"""
    try:
        users = get_all_users()
        return jsonify({"users": users})
    except Exception as e:
        print(f"Error obteniendo usuarios: {e}")
        return jsonify({"error": "Error en el servidor"}), 500

@app.route('/status')
def status():
    return jsonify({
        "connected_users": len(connected_users),
        "active_devices": len(live_coordinates),
        "coordinates": live_coordinates
    })

# Eventos Socket.IO
@socketio.on('connect')
def handle_connect():
    print(f"🔌 Cliente conectado: {request.sid}")

@socketio.on('disconnect')
def handle_disconnect():
    print(f"👋 Cliente desconectado: {request.sid}")
    if request.sid in connected_users:
        del connected_users[request.sid]

@socketio.on('location_update')
def handle_location_update(data):
    try:
        device_id = data.get('device_id')
        if device_id:
            live_coordinates[device_id] = data
            connected_users[request.sid] = device_id
            
            print(f"📍 Ubicación recibida de {device_id}: {data['latitude']:.6f}, {data['longitude']:.6f}")
            
            # Enviar a todos los clientes conectados
            socketio.emit('coordinates_update', live_coordinates)
            
    except Exception as e:
        print(f"❌ Error procesando ubicación: {e}")

if __name__ == '__main__':
    print("🚀 Iniciando GPS Tracker Simple con Flask")
    print("👤 Usuarios disponibles en la base de datos:")
    try:
        users = get_all_users()
        for user in users:
            print(f"   - {user['username']} (ID: {user['id']}, Email: {user.get('email', 'N/A')})")
    except Exception as e:
        print(f"   Error obteniendo usuarios: {e}")
    print("📍 Servidor listo para recibir coordenadas GPS")
    
    # Configuración para Railway
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    
    print(f"🌐 URL: http://{host}:{port}")
    print("📝 Endpoints disponibles:")
    print("   - POST /login - Iniciar sesión")
    print("   - POST /register - Registrar usuario")
    print("   - GET /users - Listar usuarios")
    print("   - GET /status - Estado del servidor")
    
    socketio.run(app, host=host, port=port, debug=False, allow_unsafe_werkzeug=True)