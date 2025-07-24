from fastapi import APIRouter, UploadFile, File
import tempfile
from api.services.asr_service import transcribe_audio

router = APIRouter()

@router.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    # Save upload to temp path
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        contents = await file.read()
        tmp.write(contents)
        tmp_path = tmp.name

    # Call universal transcribe
    text, language = await transcribe_audio(tmp_path)
    return {"text": text, "language": language}

