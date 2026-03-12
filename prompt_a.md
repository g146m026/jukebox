Je veux développer un système jukebox local pour contrôler un Sony MegaStorage CD changer (300 CD) depuis Home Assistant.
Le système doit être entièrement local, sans accès Internet.

Contexte technique :

* Backend : Python FastAPI
* Messaging : MQTT (Mosquitto)
* Domotique : Home Assistant
* Bridge matériel : ESP32 avec IR transmitter et IR receiver
* Base de données : SQLite
* UI minimale : endpoints API + intégration Home Assistant
* OS cible : Linux (serveur local / Docker possible)

Objectif :

Créer un backend FastAPI qui agit comme "cerveau jukebox" et qui :

1. Maintient une base de données des CD stockés dans le Sony MegaStorage (300 slots)
2. Permet de rechercher par artiste, album ou numéro de slot
3. Envoie les commandes nécessaires au lecteur via MQTT
4. Maintient un état logiciel du lecteur (slot courant, track, état play/stop)
5. Publie les états sur MQTT pour Home Assistant

Architecture :

Home Assistant
|
MQTT (Mosquitto)
|
FastAPI jukebox service
|
MQTT
|
ESP32 IR bridge
|
Infrared
|
Sony MegaStorage CD changer

Topics MQTT à utiliser :

jukebox/cmd/play_slot
jukebox/cmd/play
jukebox/cmd/stop
jukebox/cmd/next
jukebox/state/player
jukebox/state/now_playing

Exemple message :

topic: jukebox/cmd/play_slot

payload JSON :
{
"slot": 123
}

Structure du projet souhaitée :

jukebox/
app/
main.py
config.py
mqtt_client.py
models.py
database.py
services/
player_service.py
library_service.py
api/
routes_player.py
routes_library.py
data/
jukebox.db

Base de données :

Table discs

* slot_number INTEGER PRIMARY KEY
* artist TEXT
* album TEXT
* year INTEGER
* genre TEXT
* notes TEXT

Table tracks

* id INTEGER PRIMARY KEY
* slot_number INTEGER
* track_number INTEGER
* title TEXT
* duration TEXT

Table history

* id INTEGER
* timestamp
* slot_number
* track_number

Endpoints FastAPI :

GET /library
GET /library/search?q=
GET /disc/{slot}

POST /player/play_slot/{slot}
POST /player/play
POST /player/stop
POST /player/next

Fonctionnement attendu :

Quand POST /player/play_slot/{slot} est appelé :

1. Publier sur MQTT :

topic : jukebox/cmd/play_slot

payload :
{
"slot": slot
}

2. Mettre à jour l'état logiciel

3. Publier l'état :

topic : jukebox/state/player

payload :
{
"slot": slot,
"status": "playing"
}

Contraintes :

* code Python clair et modulaire
* utiliser Pydantic pour les modèles
* gestion propre MQTT reconnect
* logging structuré
* compatible Docker
* pas de dépendance cloud

Demande :

1. Générer la structure complète du projet
2. Écrire le code principal FastAPI
3. Écrire le client MQTT
4. Implémenter les routes API
5. Ajouter un exemple de configuration Home Assistant MQTT
6. Ajouter un exemple de docker-compose
