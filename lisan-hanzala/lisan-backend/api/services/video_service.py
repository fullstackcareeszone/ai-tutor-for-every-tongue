import os
import uuid
import ffmpeg
from fastapi import HTTPException
from api.services.asr_service import transcribe_file_path
from api.services.translation_service import translate_text
from api.services.tts_service import generate_speech
from db.crud import save_video_processing
from sqlalchemy.orm import Session
from db.schemas import VideoProcessingSchema  # New

# Define paths for saving media
BASE_DIR = os.getcwd()
AUDIO_DIR = os.path.join(BASE_DIR, "static", "audio")
TRANSLATED_AUDIO_DIR = os.path.join(BASE_DIR, "static", "translated_audio")
VIDEO_DIR = os.path.join(BASE_DIR, "static", "video")

# Ensure directories exist
os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(TRANSLATED_AUDIO_DIR, exist_ok=True)
os.makedirs(VIDEO_DIR, exist_ok=True)

async def process_video(file, target_lang="urd_Arab", db: Session = None):
    try:
        # Step 1: Save uploaded video
        unique_id = str(uuid.uuid4())
        original_video_filename = f"{unique_id}_original.mp4"
        original_video_path = os.path.join(VIDEO_DIR, original_video_filename)

        with open(original_video_path, "wb") as f:
            f.write(await file.read())

        # Step 2: Extract audio
        extracted_audio_filename = f"{unique_id}_original.mp3"
        extracted_audio_path = os.path.join(AUDIO_DIR, extracted_audio_filename)

        (
            ffmpeg
            .input(original_video_path)
            .output(extracted_audio_path, **{'q:a': 0, 'map': 'a'})
            .run(overwrite_output=True)
        )

        # Step 3: Transcribe & Translate
        transcript = await transcribe_file_path(extracted_audio_path)
        translated_text = translate_text(transcript, target_lang)

        # Step 4: Generate translated speech
        translated_audio_filename = f"{unique_id}_translated.mp3"
        translated_audio_path = os.path.join(TRANSLATED_AUDIO_DIR, translated_audio_filename)

        # ✅ Now store generated speech audio to translated_audio_path
        generate_speech(
            text=translated_text,
            lang=target_lang,
            out_path=translated_audio_path,  # <-- Important
            request=None,
            db=db
        )

        # Step 5: Merge audio & video
        final_video_filename = f"{unique_id}_final.mp4"
        final_video_path = os.path.join(VIDEO_DIR, final_video_filename)

        (
            ffmpeg
            .output(
                ffmpeg.input(original_video_path).video,
                ffmpeg.input(translated_audio_path).audio,
                final_video_path,
                vcodec='copy',
                acodec='aac',
                shortest=None
            )
            .global_args('-map', '0:v:0', '-map', '1:a:0')
            .run(overwrite_output=True)
        )

        # Optional DB record
        if db:
            video_data = VideoProcessingSchema(
                original_file=file.filename,
                audio_path=extracted_audio_path,  # Fixed: correct variable
                transcript=transcript,
                processed_video_path=final_video_path  # Fixed: correct variable
            )
            save_video_processing(db, video_data)

        return {
            "message": "Video processed successfully",
            "output_file": final_video_path
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Video processing failed: {e}")
