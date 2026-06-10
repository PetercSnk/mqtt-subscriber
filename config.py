import os
import secrets

baseDir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Configuration settings for Flask.
    """
    SECRET_KEY = secrets.token_urlsafe(16)
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(baseDir, "app.db")
    MQTT_BROKER_URL = ""
    MQTT_BROKER_PORT = 0
    MQTT_USERNAME = ""
    MQTT_PASSWORD = ""
    MQTT_KEEPALIVE = 5
    MQTT_TLS_ENABLED = False
