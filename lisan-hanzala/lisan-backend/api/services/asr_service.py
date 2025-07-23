import whisper
import tempfile
from fastapi import HTTPException, UploadFile, File, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db.crud import save_audio_to_text  # New
from db import schemas
from functools import lru_cache

@lru_cache()
def get_whisper_model():
    return whisper.load_model("base")
 

async def transcribe_audio(file: UploadFile, db: Session):
    try:
        model = get_whisper_model()
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            tmp.write(await file.read())
            tmp.flush()
            result = model.transcribe(tmp.name)

        transcript = result["text"]

        # Save to DB using schema
        data = schemas.AudioToTextSchema(filename=file.filename, transcript=transcript)
        save_audio_to_text(db, data)

        return transcript
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"ASR transcription failed: {e}")



async def transcribe_file_path(path: str):
    try:
        model = get_whisper_model()
        result = model.transcribe(path)
        return result["text"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"ASR transcription failed: {e}")
