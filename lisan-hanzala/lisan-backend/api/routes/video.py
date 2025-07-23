from fastapi import APIRouter, UploadFile, Form, HTTPException, Depends
from fastapi.responses import FileResponse
from api.services.video_service import process_video
from db.database import get_db  # ✅ Make sure this exists
from sqlalchemy.orm import Session
import os

router = APIRouter()

@router.post("/process-video")
async def process_uploaded_video(
    file: UploadFile,
    target_lang: str = Form(...),
    db: Session = Depends(get_db)  # ✅ Inject database session
):
    if not file:
        raise HTTPException(status_code=400, detail="No video file provided.")
    
    if not target_lang.strip():
        raise HTTPException(status_code=400, detail="Target language must not be empty.")
    
    # ✅ Pass DB to service
    result = await process_video(file, target_lang, db)

    output_path = result.get("output_file")
    if not output_path or not os.path.exists(output_path):
        raise HTTPException(status_code=500, detail="Processed video not found.")
    
    return FileResponse(
        path=output_path,
        media_type="video/mp4",
        filename=os.path.basename(output_path)
    )
