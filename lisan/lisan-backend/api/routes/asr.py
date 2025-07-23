from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from api.services.asr_service import transcribe_audio
from db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/transcribe")
async def transcribe(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    if not file:
        raise HTTPException(status_code=400, detail="No audio file provided.")
    text = await transcribe_audio(file, db)
    return {"transcribed_text": text}
