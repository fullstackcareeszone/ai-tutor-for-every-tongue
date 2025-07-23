from sqlalchemy.orm import Session
import db.models as models
import db.schemas as schemas

def save_audio_to_text(db: Session, data: schemas.AudioToTextSchema):  # ✅ CORRECT
    record = models.AudioToText(**data.dict())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def save_translation(db: Session, data: schemas.TranslationSchema):
    record = models.Translation(**data.dict())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

def save_text_to_audio(db: Session, data: schemas.TextToAudioSchema):
    record = models.TextToAudio(**data.dict())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

def save_chat_qa(db: Session, data: schemas.ChatQASchema):
    record = models.ChatQA(**data.dict())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

def save_video_processing(db: Session, data: schemas.VideoProcessingSchema):
    record = models.VideoProcessing(**data.dict())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record
