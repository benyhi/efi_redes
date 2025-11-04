import sqlite3
import os
from datetime import datetime

def init_database():
    """Inicializa la base de datos y crea las tablas necesarias"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Crear tabla de usuarios
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_login TIMESTAMP
        )
    ''')
    
    # Crear usuarios por defecto si no existen
    default_users = [
        ("admin", "admin123", "admin@gps.local"),
        ("user", "123456", "user@gps.local"),
        ("demo", "demo", "demo@gps.local")
    ]
    
    for username, password, email in default_users:
        try:
            cursor.execute(
                "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                (username, password, email)
            )
            print(f"✅ Usuario '{username}' creado (password: {password})")
        except sqlite3.IntegrityError:
            print(f"ℹ️ Usuario '{username}' ya existe")
    
    conn.commit()
    conn.close()
    print("✅ Base de datos inicializada")

def verify_user(username: str, password: str) -> dict:
    """Verifica las credenciales del usuario y retorna información"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT id, username, email, created_at FROM users WHERE username = ? AND password = ?", 
        (username, password)
    )
    result = cursor.fetchone()
    
    if result:
        # Actualizar último login
        cursor.execute(
            "UPDATE users SET last_login = ? WHERE username = ?",
            (datetime.now().isoformat(), username)
        )
        conn.commit()
        conn.close()
        
        return {
            "success": True,
            "user_id": result[0],
            "username": result[1],
            "email": result[2],
            "created_at": result[3]
        }
    
    conn.close()
    return {"success": False, "message": "Credenciales inválidas"}

def create_user(username: str, password: str, email: str = None) -> dict:
    """Crea un nuevo usuario"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Validaciones básicas
    if len(username) < 3:
        return {"success": False, "message": "El usuario debe tener al menos 3 caracteres"}
    
    if len(password) < 3:
        return {"success": False, "message": "La contraseña debe tener al menos 3 caracteres"}
    
    try:
        cursor.execute(
            "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
            (username, password, email)
        )
        user_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return {
            "success": True,
            "message": "Usuario creado exitosamente",
            "user_id": user_id,
            "username": username
        }
        
    except sqlite3.IntegrityError:
        conn.close()
        return {"success": False, "message": "El usuario ya existe"}

def get_all_users() -> list:
    """Obtiene lista de todos los usuarios (para administración)"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT id, username, email, created_at, last_login FROM users ORDER BY created_at DESC"
    )
    users = []
    for row in cursor.fetchall():
        users.append({
            "id": row[0],
            "username": row[1],
            "email": row[2],
            "created_at": row[3],
            "last_login": row[4]
        })
    
    conn.close()
    return users

def delete_user(username: str) -> dict:
    """Elimina un usuario"""
    if username in ["admin"]:  # Proteger usuario admin
        return {"success": False, "message": "No se puede eliminar el usuario admin"}
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM users WHERE username = ?", (username,))
    if cursor.rowcount > 0:
        conn.commit()
        conn.close()
        return {"success": True, "message": f"Usuario '{username}' eliminado"}
    else:
        conn.close()
        return {"success": False, "message": "Usuario no encontrado"}

if __name__ == "__main__":
    init_database()