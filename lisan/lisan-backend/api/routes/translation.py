from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.database import get_db
from api.services.translation_service import translate_text

router = APIRouter()

class TranslationRequest(BaseModel):
    text: str
    target_lang: str 

@router.post("/translate")
async def translate(request: TranslationRequest, db: Session = Depends(get_db)):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text must not be empty.")

    translated = translate_text(
        text=request.text,
        target_lang=request.target_lang,  # 👈 Pass this properly
        db=db
    )
    return {"translated_text": translated}

