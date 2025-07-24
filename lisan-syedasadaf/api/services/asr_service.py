# import whisper
# import tempfile
# import os
# from fastapi import UploadFile
# from database.db_config import SessionLocal
# from database.models import MediaLog

# model = whisper.load_model("base")

# async def transcribe_audio(file: UploadFile):
#     # Step 1: Save UploadFile to a temporary file
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
#         contents = await file.read()
#         tmp.write(contents)
#         tmp_path = tmp.name

#     try:
#         # Step 2: Transcribe the audio file
#         result = model.transcribe(tmp_path)
#         text = result["text"]
#         language = result["language"]

#         # Step 3: Log to the database
#         db = SessionLocal()
#         log = MediaLog(
#             input_type="audio",
#             input_file=tmp_path,
#             transcription=text,
#             language=language
#         )
#         db.add(log)
#         db.commit()
#         db.close()

#         return text, language

#     finally:
#         # Step 4: Clean up temporary file
#         os.remove(tmp_path)
# asr.py
# asr_service.py
import whisper
from database.db_config import SessionLocal
from database.models import MediaLog

model = whisper.load_model("base")

async def transcribe_audio(audio_path: str):
    result = model.transcribe(audio_path)
    text = result["text"]
    language = result["language"]

    # Log to DB
    db = SessionLocal()
    log = MediaLog(
        input_type="audio",
        input_file=audio_path,
        transcription=text,
        language=language
    )
    db.add(log)
    db.commit()
    db.close()

    return text, language
