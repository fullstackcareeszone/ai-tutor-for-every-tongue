from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.database import get_db
from api.services.qa_service import ask_question

router = APIRouter()

class QARequest(BaseModel):
    question: str

@router.post("/ask")
async def qa(request: QARequest, db: Session = Depends(get_db)):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question must not be empty.")
    answer = ask_question(request.question, db=db)
    return {"answer": answer}
