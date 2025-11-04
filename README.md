# GPS Tracker Simple 📍# 🌍 GPS Tracker - Sistema de Monitoreo en Tiempo Real# 🌍 GPS Tracker - Sistema de Monitoreo en Tiempo Real# 🌍 GPS Tracker - Sistema de Monitoreo en Tiempo Real# 🌍 GPS Tracker - Sistema de Monitoreo en Tiempo Real# 🗺️ Sistema WebSocket de Ubicaciones en Tiempo Real



Sistema de tracking GPS en tiempo real con autenticación de usuarios y visualización en mapa.



## CaracterísticasSistema simplificado de tracking GPS con autenticación y visualización en tiempo real usando Socket.IO y OpenStreetMap.



- 🔐 **Autenticación de usuarios** (registro/login)

- 📍 **Tracking GPS en tiempo real**

- 🗺️ **Visualización en mapa con Leaflet**## 📋 CaracterísticasSistema simplificado de tracking GPS con autenticación y visualización en tiempo real usando Socket.IO y OpenStreetMap.

- 👥 **Multi-usuario** (todos los usuarios conectados se ven en el mapa)

- 📝 **Sistema de logs en tiempo real**

- ⚡ **WebSocket para comunicación instantánea**

- 🎯 **Panel de administración simple**- ✅ **Autenticación segura** con SQLite y bcrypt



## Tecnologías- ✅ **Coordenadas en tiempo real** via Socket.IO



- **Backend**: Flask + Flask-SocketIO- ✅ **Mapa interactivo** con OpenStreetMap (sin API key necesaria)## 📋 CaracterísticasSistema simplificado de tracking GPS con autenticación y visualización en tiempo real usando Socket.IO y Google Maps.

- **Frontend**: HTML5 + CSS3 + JavaScript vanilla

- **Base de datos**: SQLite- ✅ **Vista dual** (mapa interactivo + tarjetas)

- **Mapas**: Leaflet.js

- **Tiempo real**: WebSocket/Socket.IO- ✅ **Interfaz web moderna** y responsive



## Instalación Local- ✅ **Envío de coordenadas reales** desde dispositivos



```bash- ✅ **Sin datos simulados** - solo coordenadas reales- ✅ **Autenticación segura** con SQLite y bcrypt

# Clonar repositorio

git clone <tu-repo>

cd efi_redes

## 🚀 Instalación y Uso- ✅ **Coordenadas en tiempo real** via Socket.IO

# Crear entorno virtual

python -m venv env

source env/bin/activate  # Linux/Mac

# o### Ejecutar con script automático:- ✅ **Mapa interactivo** con OpenStreetMap (sin API key necesaria)## 📋 CaracterísticasSistema simplificado de tracking GPS con autenticación y visualización en tiempo real usando Socket.IO.Sistema para recibir y distribuir información de posición de dispositivos en tiempo real usando WebSockets.

env\Scripts\activate     # Windows



# Instalar dependencias

pip install -r requirements.txt```bash- ✅ **Vista dual** (mapa interactivo + tarjetas)



# Inicializar base de datos# Windows

python database.py

start.bat- ✅ **Interfaz web moderna** y responsive

# Ejecutar servidor

python server.py

```

# Linux/Mac- ✅ **Simulación de dispositivos GPS** para desarrollo

## Despliegue en Railway

chmod +x start.sh && ./start.sh

Este proyecto está configurado para desplegarse automáticamente en Railway:

```- ✅ **Actualizaciones automáticas** cada 3 segundos- ✅ **Autenticación segura** con SQLite y bcrypt

1. Conecta tu repositorio de GitHub a Railway

2. Railway detectará automáticamente la configuración

3. El despliegue se iniciará automáticamente

### O manualmente:

### Archivos de configuración incluidos:



- `Procfile` - Comando de inicio

- `railway.json` - Configuración específica de Railway```bash## 🚀 Instalación y Uso- ✅ **Coordenadas en tiempo real** via Socket.IO

- `runtime.txt` - Versión de Python

- `requirements.txt` - Dependencias# Activar entorno virtual



## Usoenv\Scripts\activate



1. **Registro/Login**: Crea una cuenta o inicia sesión

2. **Activar GPS**: Permite el acceso a la ubicación

3. **Ver mapa**: Tu ubicación aparecerá en el mapa# Instalar dependencias### Ejecutar con script automático:- ✅ **Google Maps integrado** con marcadores dinámicos## 📋 Características## 🏗️ Arquitectura

4. **Multi-usuario**: Otros usuarios conectados aparecerán como marcadores diferentes

5. **Logs**: Panel en tiempo real con información de conexiones y ubicacionespip install -r requirements.txt



## Usuarios por defecto



- **admin** / admin123# Inicializar base de datos

- **user** / user123  

- **demo** / demo123python database.py```bash- ✅ **Vista dual** (mapa interactivo + tarjetas)



## Endpoints API



- `GET /` - Dashboard principal# Ejecutar servidor# Windows

- `POST /login` - Autenticación

- `POST /register` - Registro de usuariospython server.py

- `GET /users` - Listar usuarios

- `GET /status` - Estado del servidor```start.bat- ✅ **Interfaz web moderna** y responsive



## WebSocket Events



- `connect` - Conexión establecida## 🌐 Acceso

- `disconnect` - Desconexión

- `location_update` - Actualización de ubicación

- `coordinates_update` - Distribución de coordenadas

Abrir navegador en: `http://localhost:8001`# Linux/Mac- ✅ **Simulación de dispositivos GPS** para desarrollo

## Licencia



MIT License
**Credenciales:**chmod +x start.sh && ./start.sh

- Usuario: `admin`

- Contraseña: `admin123````- ✅ **Actualizaciones automáticas** cada 3 segundos- ✅ **Autenticación segura** con SQLite y bcrypt```



## 📍 Enviar Coordenadas GPS



### Método 1: Desde la consola del navegador### O manualmente:



1. Abre el cliente web y haz login

2. Abre las herramientas de desarrollador (F12)

3. Ve a la pestaña "Console"```bash## 🏗️ Estructura del Proyecto- ✅ **Coordenadas en tiempo real** via Socket.IODispositivos (GPS) → WebSocket Server → Dashboards (Web)

4. Ejecuta este código:

# Activar entorno virtual

```javascript

// Enviar coordenadas de ejemploenv\Scripts\activate

socket.emit('send_coordinates', {

    device_id: 'mi_dispositivo',

    latitude: -34.6037,

    longitude: -58.3816,# Instalar dependencias```- ✅ **Interfaz web moderna** y responsive                           ↓

    name: 'Buenos Aires'

});pip install -r requirements.txt

```

efi_redes/

### Método 2: Usando el simulador GPS

# Inicializar base de datos

```bash

# Ejecutar simulador en otra terminalpython database.py├── server.py           # Servidor FastAPI + Socket.IO- ✅ **Simulación de dispositivos GPS** para desarrollo                      Base de Datos

python gps_simulator.py

```



### Método 3: Desde otra aplicación# Ejecutar servidor├── client.html         # Cliente web con Google Maps



```pythonpython server.py

import socketio

```├── database.py         # Gestión de base de datos SQLite- ✅ **Actualizaciones automáticas** cada 3 segundos                    (por implementar)

sio = socketio.Client()

sio.connect('http://localhost:8001')



# Autenticarse## 🌐 Acceso├── users.db           # Base de datos SQLite

sio.emit('authenticate', {

    'username': 'admin',

    'password': 'admin123'

})Abrir navegador en: `http://localhost:8001`├── requirements.txt   # Dependencias Python```



# Enviar coordenadas

sio.emit('send_coordinates', {

    'device_id': 'gps_001',**Credenciales:**├── README.md         # Documentación

    'latitude': -34.6037,

    'longitude': -58.3816,- Usuario: `admin`

    'name': 'Mi Ubicación'

})- Contraseña: `admin123`└── env/              # Entorno virtual Python## 🏗️ Estructura del Proyecto

```



## 🗺️ Funcionalidades

## 🗺️ Funcionalidades```

- **Mapa OpenStreetMap** (gratuito, sin API key)

- **Marcadores dinámicos** en tiempo real

- **Vista dual** (mapa + tarjetas)

- **Popups informativos** al hacer clic- **Mapa OpenStreetMap** (gratuito, sin API key)## 📁 Archivos del Proyecto

- **Auto-zoom** inteligente

- **Botón ubicar** desde tarjetas- **Marcadores dinámicos** en tiempo real



## 🔧 API Socket.IO- **Vista dual** (mapa + tarjetas)## 🚀 Instalación y Uso



### Eventos que puedes enviar:- **Popups informativos** al hacer clic



- `authenticate` - Autenticarse con usuario/contraseña- **Auto-zoom** inteligente```

- `send_coordinates` - Enviar coordenadas GPS

- **Botón ubicar** desde tarjetas

### Eventos que recibes:

### 1. Configurar Google Maps API

- `auth_success` - Autenticación exitosa

- `auth_error` - Error de autenticación  ## 📄 Licencia

- `coordinates_update` - Nuevas coordenadas disponibles

- `error` - Error generalefi_redes/- **`main.py`** - Servidor WebSocket con FastAPI



## 📄 LicenciaProyecto educativo - EFI Redes 2025

1. Ve a [Google Cloud Console](https://console.cloud.google.com/)

Proyecto educativo - EFI Redes 2025
2. Crea un nuevo proyecto o selecciona uno existente├── server.py           # Servidor FastAPI + Socket.IO- **`client.py`** - Cliente Python simulando dispositivo GPS

3. Habilita la **Maps JavaScript API**

4. Crea una clave API├── client.html         # Cliente web completo- **`client.js`** - Cliente JavaScript para dashboard web

5. Edita `client.html` y reemplaza `YOUR_API_KEY` con tu clave:

├── database.py         # Gestión de base de datos SQLite- **`dashboard.html`** - Interfaz web del dashboard

```html

<script async defer src="https://maps.googleapis.com/maps/api/js?key=TU_CLAVE_API&callback=initMap"></script>├── users.db           # Base de datos SQLite- **`test_websocket.py`** - Suite de pruebas del sistema

```

├── requirements.txt   # Dependencias Python- **`websocket_debug.log`** - Log de debugging del servidor

### 2. Instalar dependencias

├── README.md         # Documentación

```bash

# Crear entorno virtual (si no existe)└── env/              # Entorno virtual Python## 🚀 Cómo Ejecutar

python -m venv env

```

# Activar entorno virtual

# Windows:### 1. Instalar Dependencias

env\Scripts\activate

# Linux/Mac:## 🚀 Instalación y Uso

source env/bin/activate

```bash

# Instalar dependencias

pip install -r requirements.txt### 1. Instalar dependencias# Activar entorno virtual (si no está activado)

```

D:/itex/efi_redes/env/Scripts/activate

### 3. Inicializar base de datos

```bash

```bash

python database.py# Crear entorno virtual (si no existe)# Las dependencias ya están instaladas en el entorno

```

python -m venv env```

### 4. Ejecutar servidor



```bash

python server.py# Activar entorno virtual### 2. Iniciar el Servidor

```

# Windows:

### 5. Abrir aplicación

env\Scripts\activate```bash

Abrir navegador en: `http://localhost:8000`

# Linux/Mac:D:/itex/efi_redes/env/Scripts/python.exe main.py

## 🔐 Credenciales por Defecto

source env/bin/activate```

- **Usuario:** `admin`

- **Contraseña:** `admin123`



## 🗺️ Funcionalidades del Mapa# Instalar dependenciasEl servidor estará disponible en:



### Vista de Mapa:pip install -r requirements.txt- WebSocket: `ws://localhost:8000/ws`

- **Marcadores dinámicos** para cada dispositivo

- **InfoWindows** con información detallada```- Estadísticas: `http://localhost:8000/stats`

- **Auto-zoom** para mostrar todos los dispositivos

- **Marcadores personalizados** con iconos de dispositivos



### Vista de Tarjetas:### 2. Inicializar base de datos### 3. Conectar Dispositivos

- **Información detallada** en formato de tarjetas

- **Botón "Ubicar"** para enfocar en el mapa

- **Diseño responsive** para diferentes pantallas

```bashEn otra terminal:

### Controles:

- **Alternar vistas** entre mapa y tarjetaspython database.py```bash

- **Clic en marcador** para ver información

- **Zoom automático** y centrado inteligente```D:/itex/efi_redes/env/Scripts/python.exe client.py



## 🌐 Endpoints Disponibles```



- **`/`** - Cliente web principal### 3. Ejecutar servidor

- **`/docs`** - Documentación API (Swagger)

- **`/api/login`** - Endpoint de autenticación REST### 4. Abrir Dashboard

- **`/socket.io/`** - Conexión Socket.IO

```bash

## 🔧 Configuración para Producción

python server.pyAbrir `dashboard.html` en un navegador web o servir con un servidor local.

### Variables de entorno recomendadas:

```

```env

HOST=0.0.0.0## 🔧 Debugging y Monitoreo

PORT=8000

DATABASE_URL=sqlite:///users.db### 4. Abrir aplicación

SECRET_KEY=your-secret-key-here

GOOGLE_MAPS_API_KEY=your-google-maps-api-key### Ver Estadísticas en Tiempo Real

```

Abrir navegador en: `http://localhost:8000`

### Modificaciones sugeridas para producción:

```bash

1. **Cambiar credenciales por defecto**

2. **Usar PostgreSQL** en lugar de SQLite## 🔐 Credenciales por Defecto# Desde PowerShell o CMD

3. **Implementar JWT tokens** para sesiones

4. **Agregar HTTPS** y certificados SSLcurl http://localhost:8000/stats

5. **Configurar proxy reverso** (nginx)

6. **Implementar logging** estructurado- **Usuario:** `admin`

7. **Restricciones de API de Google Maps** por dominio

- **Contraseña:** `admin123`# O abrir en navegador: http://localhost:8000/stats

## 📡 Protocolo Socket.IO

```

### Eventos del cliente:

## 🌐 Endpoints Disponibles

- `authenticate` - Autenticación con credenciales

- `connect` - Conexión establecida### Logs del Servidor

- `disconnect` - Desconexión

- **`/`** - Cliente web principal

### Eventos del servidor:

- **`/docs`** - Documentación API (Swagger)El servidor genera logs en:

- `auth_success` - Autenticación exitosa

- `auth_error` - Error de autenticación- **`/api/login`** - Endpoint de autenticación REST- **Consola**: Para debugging inmediato

- `coordinates_update` - Actualización de coordenadas

- **`/socket.io/`** - Conexión Socket.IO- **`websocket_debug.log`**: Para análisis posterior

### Formato de coordenadas:



```json

[## 🔧 Configuración para Producción### Ejecutar Pruebas

  {

    "device_id": "device_1",

    "latitude": -34.6037,

    "longitude": -58.3816,### Variables de entorno recomendadas:```bash

    "name": "Buenos Aires",

    "timestamp": "2025-11-04T12:30:45.123456"D:/itex/efi_redes/env/Scripts/python.exe test_websocket.py

  }

]```env```

```

HOST=0.0.0.0

## 🔧 Desarrollo

PORT=8000## 🔍 Herramientas de Debugging

### Agregar nuevos usuarios:

DATABASE_URL=sqlite:///users.db

```python

from database import create_userSECRET_KEY=your-secret-key-here### 1. Verificar Conexiones Activas

create_user("nuevo_usuario", "contraseña123")

``````



### Modificar dispositivos simulados:```bash



Editar el diccionario `mock_devices` en `server.py`:### Modificaciones sugeridas para producción:# Ver estadísticas



```pythoncurl http://localhost:8000/stats

mock_devices = {

    "device_1": {"lat": -34.6037, "lng": -58.3816, "name": "Buenos Aires"},1. **Cambiar credenciales por defecto**```

    "device_2": {"lat": -31.4201, "lng": -64.1888, "name": "Córdoba"},

    # Agregar más dispositivos...2. **Usar PostgreSQL** en lugar de SQLite

}

```3. **Implementar JWT tokens** para sesionesRespuesta esperada:



### Personalizar el mapa:4. **Agregar HTTPS** y certificados SSL```json



En `client.html`, puedes modificar:5. **Configurar proxy reverso** (nginx){



```javascript6. **Implementar logging** estructurado  "total_connections": 2,

// Estilos del mapa

map = new google.maps.Map(document.getElementById('map'), {  "active_devices": 1,

    zoom: 6,

    center: argentina,## 📡 Protocolo Socket.IO  "active_dashboards": 1,

    styles: [

        // Personalizar colores y estilos  "messages_received": 150,

    ]

});### Eventos del cliente:  "messages_forwarded": 150,



// Iconos de marcadores  "errors": 0,

icon: {

    url: 'data:image/svg+xml;charset=UTF-8,' + encodeURIComponent(`- `authenticate` - Autenticación con credenciales  "device_list": ["device-123"]

        <svg><!-- Tu SVG personalizado --></svg>

    `),- `connect` - Conexión establecida}

    scaledSize: new google.maps.Size(30, 30)

}- `disconnect` - Desconexión```

```



## 📝 API REST

### Eventos del servidor:### 2. Monitorear Logs en Tiempo Real

### POST /api/login



Autenticación alternativa via REST API:

- `auth_success` - Autenticación exitosa```bash

```bash

curl -X POST "http://localhost:8000/api/login" \- `auth_error` - Error de autenticación# En PowerShell

     -H "Content-Type: application/json" \

     -d '{"username": "admin", "password": "admin123"}'- `coordinates_update` - Actualización de coordenadasGet-Content -Path "websocket_debug.log" -Wait

```



## 🐛 Troubleshooting

### Formato de coordenadas:# En CMD

### Google Maps no carga:

- Verificar que la clave API esté configuradatype websocket_debug.log

- Comprobar que la Maps JavaScript API esté habilitada

- Revisar restricciones de dominio en Google Cloud Console```json```



### Puerto ocupado:[

```bash

# Cambiar puerto en server.py línea final:  {### 3. Probar Manualmente con curl

uvicorn.run(socket_app, host="0.0.0.0", port=8001)

```    "device_id": "device_1",



### Error de base de datos:    "latitude": -34.6037,```bash

```bash

# Eliminar y recrear base de datos:    "longitude": -58.3816,# Prueba básica del servidor HTTP

rm users.db

python database.py    "name": "Buenos Aires",curl -i http://localhost:8000/stats

```

    "timestamp": "2025-11-04T12:30:45.123456"

### Problemas de conexión Socket.IO:

- Verificar que el servidor esté ejecutándose  }# Debería retornar 200 OK con estadísticas JSON

- Comprobar puertos en firewall

- Revisar consola del navegador para errores JavaScript]```



### Marcadores no aparecen:```

- Verificar coordenadas válidas en `mock_devices`

- Comprobar la consola del navegador para errores de Maps API## 🐛 Problemas Comunes y Soluciones

- Asegurar que `initMap` se ejecute correctamente

## 🔧 Desarrollo

## 🎯 Características Avanzadas

### 1. "Connection refused"

### Para implementar en futuras versiones:

### Agregar nuevos usuarios:

1. **Historial de rutas** con polylines

2. **Geofencing** y alertas**Problema**: El servidor no está corriendo

3. **Clusters de marcadores** para muchos dispositivos

4. **Mapa de calor** para densidad de ubicaciones```python**Solución**: 

5. **Controles de tiempo** para ver datos históricos

6. **Exportar datos** a KML/GPXfrom database import create_user```bash



## 📄 Licenciacreate_user("nuevo_usuario", "contraseña123")D:/itex/efi_redes/env/Scripts/python.exe main.py



Proyecto educativo - EFI Redes 2025``````



---



## 🚀 Inicio Rápido### Modificar dispositivos simulados:### 2. "Authentication failed"



```bash

# Windows

start.batEditar el diccionario `mock_devices` en `server.py`:**Problema**: Credenciales incorrectas



# Linux/Mac**Tokens válidos**:

chmod +x start.sh && ./start.sh

``````python- `device-123` → `TOKEN_ABC_123`



¡Disfruta del tracking GPS en tiempo real con Google Maps! 🌍📍mock_devices = {- `dashboard-1` → `TOKEN_DASH_999`

    "device_1": {"lat": -34.6037, "lng": -58.3816, "name": "Buenos Aires"},

    "device_2": {"lat": -31.4201, "lng": -64.1888, "name": "Córdoba"},### 3. "Invalid JSON"

    # Agregar más dispositivos...

}**Problema**: Formato de mensaje incorrecto

```**Formato válido para dispositivos**:

```json

## 📝 API REST{

  "lat": -31.4167,

### POST /api/login  "lon": -64.1833,

  "timestamp": "2025-11-03T10:30:00.000Z"

Autenticación alternativa via REST API:}

```

```bash

curl -X POST "http://localhost:8000/api/login" \### 4. Dispositivo no envía ubicaciones

     -H "Content-Type: application/json" \

     -d '{"username": "admin", "password": "admin123"}'**Debugging**:

```1. Verificar logs del cliente

2. Comprobar conexión de red

## 🐛 Troubleshooting3. Validar formato de datos



### Puerto ocupado:### 5. Dashboard no recibe actualizaciones

```bash

# Cambiar puerto en server.py línea final:**Debugging**:

uvicorn.run(socket_app, host="0.0.0.0", port=8001)1. Verificar conexión WebSocket en consola del navegador

```2. Comprobar que hay dispositivos conectados

3. Revisar logs del servidor

### Error de base de datos:

```bash## 📊 Formato de Datos

# Eliminar y recrear base de datos:

rm users.db### Ubicación de Dispositivo (Entrada)

python database.py

``````json

{

### Problemas de conexión Socket.IO:  "lat": -31.4167,          // Latitud (-90 a 90)

- Verificar que el servidor esté ejecutándose  "lon": -64.1833,          // Longitud (-180 a 180)

- Comprobar puertos en firewall  "timestamp": "2025-11-03T10:30:00.000Z",  // ISO 8601

- Revisar consola del navegador para errores JavaScript  "accuracy": 5.2,          // Opcional: precisión en metros

  "speed": 25.5,            // Opcional: velocidad en km/h

## 📄 Licencia  "heading": 180.0          // Opcional: dirección en grados

}

Proyecto educativo - EFI Redes 2025```

### Respuesta del Servidor

```json
{
  "status": "received",
  "forwarded_to": 2,
  "timestamp": "2025-11-03T10:30:01.000Z"
}
```

### Datos para Dashboard (Salida)

```json
{
  "deviceId": "device-123",
  "lat": -31.4167,
  "lon": -64.1833,
  "timestamp": "2025-11-03T10:30:00.000Z",
  "server_received": "2025-11-03T10:30:01.000Z",
  "accuracy": 5.2,
  "speed": 25.5,
  "heading": 180.0
}
```

## 🔒 Autenticación

El sistema usa tokens simples en query parameters:

```
ws://localhost:8000/ws?id=DEVICE_ID&token=TOKEN
```

**Tokens de prueba**:
- Dispositivos: `id=device-123&token=TOKEN_ABC_123`
- Dashboards: `id=dashboard-1&token=TOKEN_DASH_999`

## 📈 Métricas y Monitoreo

### Estadísticas Disponibles

- `total_connections`: Total de conexiones desde inicio
- `active_devices`: Dispositivos conectados actualmente
- `active_dashboards`: Dashboards conectados actualmente
- `messages_received`: Total de mensajes recibidos
- `messages_forwarded`: Total de mensajes reenviados
- `errors`: Total de errores registrados
- `device_list`: Lista de IDs de dispositivos activos

### Archivos de Log

- **Consola**: Información inmediata
- **websocket_debug.log**: Historial completo con timestamps

## 🚧 Próximas Mejoras

1. **Base de Datos**: Persistir ubicaciones
2. **Autenticación JWT**: Sistema más seguro
3. **Rate Limiting**: Prevenir abuso
4. **Geofencing**: Alertas por zonas
5. **Mapa Visual**: Dashboard con mapa interactivo
6. **Clustering**: Escalar horizontalmente

## 🆘 Obtener Ayuda

Si hay problemas:

1. **Revisar logs**: `websocket_debug.log`
2. **Ejecutar tests**: `python test_websocket.py`
3. **Verificar stats**: `curl http://localhost:8000/stats`
4. **Comprobar puertos**: Asegurar que puerto 8000 esté libre

## 📱 Ejemplo de Uso Completo

```bash
# Terminal 1: Servidor
D:/itex/efi_redes/env/Scripts/python.exe main.py

# Terminal 2: Dispositivo simulado
D:/itex/efi_redes/env/Scripts/python.exe client.py

# Terminal 3: Verificar estadísticas
curl http://localhost:8000/stats

# Navegador: Abrir dashboard.html
```

¡Listo para rastrear ubicaciones en tiempo real! 🎯