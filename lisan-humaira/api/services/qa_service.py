# D:\lisan-tutor\api\services\qa_service.py

import os
import google.generativeai as genai

# Load Gemini API key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])


# Initialize Gemini 1.5 Flash model
model = genai.GenerativeModel("gemini-1.5-flash-latest")

def answer_question(question: str) -> str:
    """
    Uses Gemini 1.5 Flash to answer a given question accurately and concisely.
    """
    try:
        response = model.generate_content(f"Answer this question precisely and concisely: {question}")
        return response.text.strip()
    except Exception as e:
        print(f"❌ Gemini error: {e}")
        return "Error generating answer."
