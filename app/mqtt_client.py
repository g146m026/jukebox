import logging
import paho.mqtt.client as mqtt
from app.config import Config

logger = logging.getLogger("mqtt")

class MQTTClient:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.username_pw_set(Config.MQTT_USERNAME, Config.MQTT_PASSWORD)
        self.client.connect_async(Config.MQTT_BROKER, Config.MQTT_PORT)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        logger.info(f"MQTT connecté avec code {rc}")

    def on_disconnect(self, client, userdata, rc):
        logger.warning(f"MQTT déconnecté avec code {rc}")
        if rc != 0:
            logger.info("Tentative de reconnexion MQTT...")
            self.client.reconnect()

    def publish(self, topic, payload):
        logger.info(f"MQTT publish: {topic} {payload}")
        self.client.publish(topic, payload)
