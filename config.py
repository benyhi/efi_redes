# Configuración para Railway
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'gps_tracker_secret_key_production'
    DATABASE_URL = os.environ.get('DATABASE_URL') or 'sqlite:///users.db'
    
class DevelopmentConfig(Config):
    DEBUG = True
    
class ProductionConfig(Config):
    DEBUG = False
    
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': ProductionConfig
}