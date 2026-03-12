from fastapi import APIRouter
from app.services.player_service import PlayerService

router = APIRouter()
player_service = PlayerService()

@router.post("/play_slot/{slot}")
def play_slot(slot: int):
    player_service.play_slot(slot)
    return player_service.get_state()

@router.post("/play")
def play():
    player_service.play()
    return player_service.get_state()

@router.post("/stop")
def stop():
    player_service.stop()
    return player_service.get_state()

@router.post("/next")
def next():
    player_service.next()
    return player_service.get_state()

@router.get("/state")
def get_state():
    return player_service.get_state()
