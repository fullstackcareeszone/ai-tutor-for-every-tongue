from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from .database import Base

class AudioToText(Base):
    __tablename__ = "audio_to_text"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    transcript = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Translation(Base):
    __tablename__ = "translations"
    id = Column(Integer, primary_key=True, index=True)
    source_text = Column(Text)
    translated_text = Column(Text)
    source_lang = Column(String)
    target_lang = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class TextToAudio(Base):
    __tablename__ = "text_to_audio"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    filename = Column(String)
    language = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class ChatQA(Base):
    __tablename__ = "chat_qa"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text)
    answer = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class VideoProcessing(Base):
    __tablename__ = "video_processing"
    id = Column(Integer, primary_key=True, index=True)
    original_file = Column(String)
    audio_path = Column(String, nullable=True)
    transcript = Column(Text, nullable=True)
    processed_video_path = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
