import os
import google.generativeai as genai
from database.db_config import SessionLocal
from database.models import MediaLog

os.environ["GOOGLE_API_KEY"] = "AIzaSyAJ9J2dk-H17mqM5DQfjVmfTtVUMlJj5jA"
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-flash")

def ask_question(question: str, context: str = "") -> str:
    try:
        prompt = f"{context}\n\nQuestion: {question}" if context else question
        response = model.generate_content(prompt)
        answer = response.text

        # ✅ Log into DB
        db = SessionLocal()
        log = MediaLog(
            input_type="qa",
            input_file=question,
            transcription=answer,
            language="und"
        )
        db.add(log)
        db.commit()
        db.close()

        return answer
    except Exception as e:
        print("❌ Gemini API Error:", str(e))
        return f"[ERROR] {str(e)}"
