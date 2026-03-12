# Jukebox Backend

Ce projet permet de contrôler un Sony MegaStorage CD changer (300 CD) depuis Home Assistant via MQTT.

## Structure du projet

- `app/` : code source principal
  - `main.py` : point d'entrée FastAPI
  - `config.py` : configuration
  - `mqtt_client.py` : client MQTT
  - `models.py` : modèles Pydantic
  - `database.py` : gestion SQLite
  - `services/` : logique métier
    - `player_service.py` : gestion du lecteur
    - `library_service.py` : gestion de la bibliothèque
  - `api/` : routes FastAPI
    - `routes_player.py` : endpoints lecteur
    - `routes_library.py` : endpoints bibliothèque
  - `data/` : données
    - `jukebox.db` : base SQLite

## Endpoints FastAPI

- `GET /library` : liste des CD
- `GET /library/search?q=` : recherche
- `GET /disc/{slot}` : infos CD + pistes
- `POST /player/play_slot/{slot}` : jouer un slot
- `POST /player/play` : play
- `POST /player/stop` : stop
- `POST /player/next` : piste suivante

## Topics MQTT

- `jukebox/cmd/play_slot`
- `jukebox/cmd/play`
- `jukebox/cmd/stop`
- `jukebox/cmd/next`
- `jukebox/state/player`
- `jukebox/state/now_playing`

## Exemple configuration Home Assistant

```yaml
mqtt:
  sensor:
    - name: "Jukebox Player State"
      state_topic: "jukebox/state/player"
      value_template: "{{ value_json.status }}"
      json_attributes_topic: "jukebox/state/player"
  switch:
    - name: "Jukebox Play Slot"
      command_topic: "jukebox/cmd/play_slot"
      payload_on: '{"slot": 123}'
      payload_off: '{"slot": 0}'
```

## Exemple docker-compose

```yaml
version: '3.8'
services:
  mosquitto:
    image: eclipse-mosquitto
    ports:
      - "1883:1883"
    volumes:
      - ./mosquitto.conf:/mosquitto/config/mosquitto.conf
  jukebox:
    build: ./app
    environment:
      - MQTT_BROKER=mosquitto
      - DB_PATH=app/data/jukebox.db
    ports:
      - "8000:8000"
    depends_on:
      - mosquitto
```