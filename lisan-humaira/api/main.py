from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from api.routes import asr, translation, tts, qa, video
from api.database import SessionLocal, engine, Base
from api import models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Lisan Tutor",
    description="Audio ➔ Text ➔ Translation ➔ Audio pipeline with FastAPI",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse("frontend/index.html")

app.include_router(asr.router, prefix="/asr")
app.include_router(translation.router)
app.include_router(tts.router, prefix="/tts")
app.include_router(qa.router, prefix="/qa")
app.include_router(video.router, prefix="/video")

@app.get("/db-test")
def test_db():
    db = SessionLocal()
    try:
        db.execute("SELECT 1")
        return {"status": "Connected to DB!"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        db.close()

