import os
from dotenv import load_dotenv
import google.generativeai as genai
from fastapi import HTTPException
from sqlalchemy.orm import Session
from functools import lru_cache
from db.crud import save_chat_qa  # New
from db.schemas import ChatQASchema  # New


load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

@lru_cache()
def get_gemini_model():
    return genai.GenerativeModel("gemini-1.5-flash")

def ask_question(question: str, db: Session) -> str:
    try:
        model = get_gemini_model()
        response = model.generate_content(question)
        answer = response.text if hasattr(response, "text") else str(response)

        # Save to DB using a valid schema object
        save_chat_qa(db, data=ChatQASchema(question=question, answer=answer))

        return answer
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Gemini Q/A failed: {e}")
