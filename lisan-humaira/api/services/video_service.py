import os
import uuid
import moviepy.editor as mp
from fastapi import UploadFile

from api.services.db_service import save_transcript, update_translated_text
from api.services.asr_service import transcribe_audio
from api.services.translation_service import translate_text_pipeline
from api.services.tts_service import text_to_speech

# Compute absolute path to frontend static folder dynamically
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FRONTEND_STATIC_DIR = os.path.join(BASE_DIR, "frontend", "static")

async def process_video(file: UploadFile, target_lang: str) -> str:
    # Ensure static directory exists
    os.makedirs(FRONTEND_STATIC_DIR, exist_ok=True)

    # Step 1-3: Save video + extract audio
    input_video_path = os.path.join(FRONTEND_STATIC_DIR, f"{uuid.uuid4()}.mp4")
    with open(input_video_path, "wb") as f:
        f.write(await file.read())

    video = mp.VideoFileClip(input_video_path)
    audio_path = input_video_path.replace(".mp4", ".mp3")
    video.audio.write_audiofile(audio_path)

    # Step 4: Transcribe
    with open(audio_path, "rb") as audio_file:
        class DummyFile: file = audio_file
        original_text = transcribe_audio(DummyFile())

    # Step 5: Translate
    translated_text = translate_text_pipeline(original_text, src_lang="en", tgt_lang=target_lang)

    # Step 6: Save to DB
    transcript_id = save_transcript(original_text=original_text)
    update_translated_text(transcript_id=transcript_id, translated_text=translated_text)

    # Step 7: Text-to-speech and combine with video...
    tts_audio_path = text_to_speech(translated_text, lang=target_lang)

    # Convert tts_audio_path (likely a URL or relative path) to absolute file path
    if tts_audio_path.startswith("/static/"):
        tts_audio_path = os.path.join(FRONTEND_STATIC_DIR, os.path.relpath(tts_audio_path, "/static/"))

    new_audio = mp.AudioFileClip(tts_audio_path)
    video = video.set_audio(new_audio)

    # ✅ Step 8: Write final video to disk and return path
    output_video_path = os.path.join(FRONTEND_STATIC_DIR, f"{uuid.uuid4()}.mp4")
    video.write_videofile(output_video_path, codec="libx264", audio_codec="aac")

    return output_video_path
