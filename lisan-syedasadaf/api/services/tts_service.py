from gtts import gTTS
from database.db_config import SessionLocal
from database.models import MediaLog
from datetime import datetime
import os

def synthesize_speech(text, lang='en'):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    filename = f"speech_{timestamp}.mp3"
    output_dir = "static/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, filename)

    tts = gTTS(text=text, lang=lang)
    tts.save(output_path)

    # ✅ Log to DB
    db = SessionLocal()
    log = MediaLog(
        input_type="tts",
        input_file=text,
        transcription="Generated speech",
        output_file=output_path,
        language=lang
    )
    db.add(log)
    db.commit()
    db.close()

    return output_path  # this will be like static/output/speech_20250719183412.mp3
