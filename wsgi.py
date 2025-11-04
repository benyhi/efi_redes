#!/usr/bin/env python3
"""
WSGI entry point for Railway deployment
"""
from server import socketio, app

if __name__ == "__main__":
    socketio.run(app)