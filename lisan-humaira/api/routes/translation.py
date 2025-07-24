from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from api.services.translation_service import translate_text_pipeline

router = APIRouter(prefix="/translate")

class TranslationRequest(BaseModel):
    text: str
    src_lang: str
    tgt_lang: str

@router.post("/")
async def translate_endpoint(req: TranslationRequest):
    try:
        translated = translate_text_pipeline(req.text, req.src_lang, req.tgt_lang)
        return {
            "original_text": req.text,
            "translated_text": translated
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Translation failed: " + str(e))
