from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from api.services.tts_service import generate_speech
from db.database import get_db  # Assuming you have this
from pydantic import BaseModel
import os
from fastapi.responses import FileResponse

router = APIRouter()


class TTSRequest(BaseModel):
    text: str

@router.post("/generate-tts")
async def tts_endpoint(
    request_data: TTSRequest,
    request: Request,
    db: Session = Depends(get_db)
):
    response = generate_speech(request_data.text, request=request, db=db)
    return response


@router.get("/download-audio/{filename}")
async def download_audio(filename: str):
    file_path = os.path.join("output", "audios", filename)
    if not os.path.isfile(file_path):
        return {"error": "File not found"}
    return FileResponse(
        path=file_path,
        filename=filename,
        media_type='audio/mpeg',
        headers={"Content-Disposition": f'attachment; filename="{filename}"'}
    )
