import uvicorn
from fastapi import FastAPI
from app.api.routes_player import router as player_router
from app.api.routes_library import router as library_router

app = FastAPI(title="Jukebox Backend")

app.include_router(player_router, prefix="/player")
app.include_router(library_router, prefix="/library")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
