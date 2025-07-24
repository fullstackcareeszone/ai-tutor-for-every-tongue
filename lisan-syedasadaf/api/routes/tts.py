from fastapi import APIRouter
from pydantic import BaseModel
from api.services.tts_service import synthesize_speech

router = APIRouter()

class TTSRequest(BaseModel):
    text: str

@router.post("/speak")
async def speak(payload: TTSRequest):
    file_path = synthesize_speech(payload.text)  # static/output/speech_xyz.mp3
    # Remove "static/" so frontend gets just output/speech_xyz.mp3
    relative_path = file_path.replace("static/", "")
    return {"audio_file": relative_path}
