from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from api.routes import asr, translation, tts, qa, video
from db.database import Base, engine

# Create tables automatically at startup if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to ["http://localhost:5500"] to restrict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(asr.router)
app.include_router(translation.router)
app.include_router(tts.router)
app.include_router(qa.router)
app.include_router(video.router)

# Mount static directories
app.mount("/video", StaticFiles(directory="static/video"), name="video")
app.mount("/audio", StaticFiles(directory="static/audio"), name="audio")
app.mount("/translated_audio", StaticFiles(directory="static/translated_audio"), name="translated_audio")
app.mount("/audios", StaticFiles(directory="output/audios"), name="audios")

# Optional: only if you want to run directly with `python main.py`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
