# D:\lisan-tutor\api\routes\video.py

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse
from api.services.video_service import process_video
import traceback

router = APIRouter()

@router.post("/")
async def video_pipeline(
    file: UploadFile = File(...),
    target_lang: str = Form(...)
):
    """
    Full Video Translation Pipeline Endpoint

    Uploads a video file, transcribes it, translates it to target_lang,
    generates translated audio, and overlays it back to return the translated video.
    """

    try:
        print(f"✅ Received video upload: {file.filename}")
        print(f"✅ Target language received: {target_lang}")

        result_video_path = await process_video(file, target_lang)

        print(f"✅ Translated video generated at: {result_video_path}")

        return FileResponse(
            result_video_path,
            media_type="video/mp4",
            filename="translated_video.mp4"
        )

    except Exception as e:
        print("❌ Error in /video/ endpoint:", e)
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))
