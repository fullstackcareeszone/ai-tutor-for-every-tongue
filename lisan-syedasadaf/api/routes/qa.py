from fastapi import APIRouter
from api.services.qa_service import ask_question

router = APIRouter()

@router.post("/qa")
async def qa_endpoint(payload: dict):
    question = payload.get("question")
    if not question:
        return {"answer": "No question provided."}
    
    answer = ask_question(question)
    return {"answer": answer}
