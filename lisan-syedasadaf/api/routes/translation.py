from fastapi import APIRouter, Body
from pydantic import BaseModel
from api.services.translation_service import translate_text

router = APIRouter()

class TranslationRequest(BaseModel):
    text: str
    target_lang: str

@router.post("/translate")
async def translate(payload: TranslationRequest):
    translated = translate_text(payload.text, target_lang=payload.target_lang)
    return {"translated_text": translated}
