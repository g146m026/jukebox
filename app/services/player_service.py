import logging
from app.mqtt_client import MQTTClient
from app.models import PlayerState

logger = logging.getLogger("player_service")
mqtt = MQTTClient()

class PlayerService:
    def __init__(self):
        self.state = PlayerState(slot=0, status="stopped")

    def play_slot(self, slot: int):
        mqtt.publish("jukebox/cmd/play_slot", f'{{"slot": {slot}}}')
        self.state.slot = slot
        self.state.status = "playing"
        mqtt.publish("jukebox/state/player", self.state.json())

    def play(self):
        mqtt.publish("jukebox/cmd/play", "{}")
        self.state.status = "playing"
        mqtt.publish("jukebox/state/player", self.state.json())

    def stop(self):
        mqtt.publish("jukebox/cmd/stop", "{}")
        self.state.status = "stopped"
        mqtt.publish("jukebox/state/player", self.state.json())

    def next(self):
        mqtt.publish("jukebox/cmd/next", "{}")
        self.state.status = "playing"
        mqtt.publish("jukebox/state/player", self.state.json())

    def get_state(self):
        return self.state
