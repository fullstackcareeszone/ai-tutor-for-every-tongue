from api.database import SessionLocal
from api.models.transcript import Transcript
from api.models.qa_history import QAHistory
from sqlalchemy.orm import Session

def save_transcript(original_text: str):
    db = SessionLocal()
    transcript = Transcript(original_text=original_text)
    db.add(transcript)
    db.commit()
    db.refresh(transcript)
    db.close()
    return transcript.id  # ✅ Return ID to use later

def update_translated_text(transcript_id: int, translated_text: str):
    db = SessionLocal()
    transcript = db.query(Transcript).filter(Transcript.id == transcript_id).first()
    if transcript:
        transcript.translated_text = translated_text
        db.commit()
        db.refresh(transcript)
    db.close()
    return transcript

def save_qa(db: Session, question: str, answer: str) -> QAHistory:
    entry = QAHistory(question=question, answer=answer)
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry
