from langdetect import detect
from gtts import gTTS
import os
import uuid
from fastapi import Request
from sqlalchemy.orm import Session
from db.crud import save_text_to_audio  # New
from db.schemas import TextToAudioSchema  # New

def generate_speech(text: str, lang: str = None, request: Request = None, db: Session = None, out_path: str = None):
    detected_lang = lang or detect(text)

    if out_path:
        filepath = out_path
        filename = os.path.basename(filepath)
    else:
        filename = f"{uuid.uuid4()}.mp3"
        output_dir = os.path.join("output", "audios")
        filepath = os.path.join(output_dir, filename)
        os.makedirs(output_dir, exist_ok=True)

    tts = gTTS(text=text, lang=detected_lang)
    tts.save(filepath)

    if db:
        data = TextToAudioSchema(text=text, filename=filename, language=detected_lang)
        save_text_to_audio(db, data)

    base_url = str(request.base_url).rstrip('/') if request else ""
    return {
        "message": "TTS generated successfully.",
        "language": detected_lang,
        "download_url": f"{base_url}/audios/{filename}" if request else filepath
    }


