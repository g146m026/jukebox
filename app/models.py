from pydantic import BaseModel
from typing import Optional

class Disc(BaseModel):
    slot_number: int
    artist: str
    album: str
    year: Optional[int]
    genre: Optional[str]
    notes: Optional[str]

class Track(BaseModel):
    id: int
    slot_number: int
    track_number: int
    title: str
    duration: Optional[str]

class History(BaseModel):
    id: int
    timestamp: str
    slot_number: int
    track_number: int

class PlayerState(BaseModel):
    slot: int
    status: str
    track: Optional[int] = None
