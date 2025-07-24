import tempfile
import os
from api.utils.video_utils import extract_audio_from_video, merge_audio_with_video, add_subtitles_to_video
from api.services.asr_service import model  # Reuse loaded whisper model
from api.services.translation_service import translate_text
from api.services.tts_service import synthesize_speech
from database.db_config import SessionLocal
from database.models import MediaLog

async def process_video(file, target_lang):
    # Save uploaded video to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
        contents = await file.read()
        tmp.write(contents)
        tmp_path = tmp.name

    # Step 1: Extract audio from video
    audio_path = "static/output/extracted_audio.wav"
    extract_audio_from_video(tmp_path, audio_path)

    # Step 2: Transcribe audio
    result = model.transcribe(audio_path)
    transcribed_text = result.get("text")
    src_lang = result.get("language")

    # Step 3: Translate to target language
    translated_text = translate_text(transcribed_text, target_lang) or ""

    # Step 4: Synthesize translated audio
    translated_audio_path = synthesize_speech(translated_text, lang=target_lang)

    # Step 5: Merge translated audio into video
    translated_video_path = "static/output/video_with_translated_audio.mp4"
    merge_audio_with_video(tmp_path, translated_audio_path, translated_video_path)

    # Step 6: Add subtitles
    final_video_path = "static/output/final_video.mp4"
    add_subtitles_to_video(translated_video_path, translated_text, final_video_path)

    # Step 7: Log into DB
    db = SessionLocal()
    log = MediaLog(
        input_type="video",
        input_file=tmp_path,
        transcription=transcribed_text,
        translation=translated_text,
        output_file=final_video_path,
        language=src_lang
    )
    db.add(log)
    db.commit()
    db.close()

    # Return both final video path and TTS audio path (relative for frontend)
    return {
        "processed_video_path": final_video_path.replace("static/", ""),
        "translated_audio_path": translated_audio_path.replace("static/", "")
    }
