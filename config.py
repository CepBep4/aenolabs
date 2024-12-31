import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'  # Подключение к базе данных SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Отключение предупреждений о модификациях

class DevelopmentConfig(Config):
    HOST = 'http://127.0.0.1:5000'
    DEBUG = True
    BOTLINK = "https://t.me/severrr_72_bot"

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False