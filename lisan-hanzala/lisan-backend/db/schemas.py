from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AudioToTextSchema(BaseModel):
    filename: str
    transcript: str

class TranslationSchema(BaseModel):
    source_text: str
    translated_text: str
    source_lang: str
    target_lang: str

class TextToAudioSchema(BaseModel):
    text: str
    filename: str
    language: str

class ChatQASchema(BaseModel):
    question: str
    answer: str

class VideoProcessingSchema(BaseModel):
    original_file: str
    audio_path: Optional[str]
    transcript: Optional[str]
    processed_video_path: Optional[str]
