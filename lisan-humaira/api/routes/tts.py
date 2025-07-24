from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from api.services.tts_service import text_to_speech

router = APIRouter()

class TTSRequest(BaseModel):
    text: str
    lang: str = "en"

@router.post("/")
async def tts_route(request: TTSRequest):
    try:
        audio_path = text_to_speech(request.text, request.lang)
        return {"audio_path": audio_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
