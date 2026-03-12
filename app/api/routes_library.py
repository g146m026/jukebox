from fastapi import APIRouter, Query
from app.services.library_service import LibraryService

router = APIRouter()
library_service = LibraryService()

@router.get("")
def get_library():
    return library_service.get_all_discs()

@router.get("/search")
def search_library(q: str = Query(...)):
    return library_service.search_discs(q)

@router.get("/disc/{slot}")
def get_disc(slot: int):
    disc = library_service.get_disc(slot)
    if not disc:
        return {"error": "Slot non trouvé"}
    tracks = library_service.get_tracks(slot)
    return {"disc": disc, "tracks": tracks}
