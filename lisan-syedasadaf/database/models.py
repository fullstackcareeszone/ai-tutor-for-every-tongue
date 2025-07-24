from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from .db_config import Base

class MediaLog(Base):
    __tablename__ = "media_logs"

    id = Column(Integer, primary_key=True, index=True)
    input_type = Column(String(255))  # "audio" or "video"
    input_file = Column(String)
    transcription = Column(Text)
    translation = Column(Text)
    answer = Column(Text, nullable=True)  # for audio Q&A
    output_file = Column(String)
    language = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
