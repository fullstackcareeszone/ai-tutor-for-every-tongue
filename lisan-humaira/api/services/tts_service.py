from gtts import gTTS
import os
import uuid

def text_to_speech(text, lang="en"):
    if not text.strip():
        raise ValueError("TTS received empty text")

    filename = f"{uuid.uuid4()}.mp3"
    output_dir = os.path.join("frontend", "static", "output")
    os.makedirs(output_dir, exist_ok=True)

    filepath = os.path.join(output_dir, filename)

    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(filepath)

    return f"/static/output/{filename}"
