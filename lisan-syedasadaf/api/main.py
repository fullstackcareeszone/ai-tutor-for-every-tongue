from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os, sys, traceback

# Add root dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from api.routes import asr, translation, tts, qa, vvvideo
from database.db_config import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# ✅ Mount the 'static' folder to serve TTS audio files
static_dir = os.path.join(os.path.dirname(__file__), "static")
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

app.mount("/static", StaticFiles(directory=static_dir), name="static")

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include API routers
app.include_router(asr.router, prefix="/asr")
app.include_router(translation.router, prefix="/translation")
app.include_router(tts.router, prefix="/tts")
app.include_router(qa.router, prefix="/gemini")
app.include_router(vvvideo.router, prefix="/vvvideo")

@app.get("/")
def root():
    return {"message": "Lisan Tutor API running"}

@app.exception_handler(Exception)
async def catch_all(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"detail": str(exc)})
