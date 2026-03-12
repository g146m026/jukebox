import os

class Config:
    MQTT_BROKER = os.getenv("MQTT_BROKER", "localhost")
    MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
    MQTT_USERNAME = os.getenv("MQTT_USERNAME", "")
    MQTT_PASSWORD = os.getenv("MQTT_PASSWORD", "")
    DB_PATH = os.getenv("DB_PATH", "app/data/jukebox.db")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
