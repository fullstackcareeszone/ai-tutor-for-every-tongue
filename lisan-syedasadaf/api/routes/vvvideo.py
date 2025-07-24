from api.services.video_service import process_video
from fastapi import APIRouter, UploadFile, File, Form

router = APIRouter()

# vvvideo.py
@router.post("/process-video")
async def process_uploaded_video(file: UploadFile = File(...), target_lang: str = Form(...)):
    result = await process_video(file, target_lang)
    return result  # ✅ Just return what the service gives you
