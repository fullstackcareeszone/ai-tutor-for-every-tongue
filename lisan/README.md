# 📚 Lisan: The AI Tutor for Every Tongue

**Lisan** is a full-stack AI-powered tutor designed to help users translate, subtitle, and learn languages using state-of-the-art machine learning models. This project combines a beautiful frontend interface with a robust backend built using FastAPI.

---

## 🚀 Features

- 🌍 Translate audio to any target language.
- 🧠 AI-based speech recognition and language detection.
- 🌐 AI assitant to ask questions about anything.
- 🎥 Upload and process videos for translation/subtitling.
- ⚙️ Real-time feedback and progress visualization.
- 🔒 Secure and optimized backend communication.


---

## 🧰 Tech Stack

**Frontend:**
- HTML5  
- CSS3 (Tailwind CSS)
- JavaScript (Vanilla JS, Alpin.js, Recorder.js)

**Backend:**
- FastAPI (Python)
- SQLAlchemy & PostgreSQL
- OpenAI Whisper for transcription
- Huggging Face Transformers (NLLB) for translation
- gTTS and langdetect for Text-to-Speech
- Google Generative AI (Gemini) for QA Chat bot
- FFmpeg for video processing

---

## 📁 Project Structure

```bash
lisan/
├── lisan-frontend/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   ├── api.js
│   │   └── nav.js
│   ├── assistant.html
│   ├── index.html
│   ├── text-to-speech.html
│   ├── transcribe.html
│   ├── translate.html
│   └── video-translate.html
│
├── lisan-backend/
│   ├── api/
│   │   ├── __pycache__/
│   │   ├── routes/
│   │   │   ├── __pycache__/
│   │   │   ├── __init__.py
│   │   │   ├── asr.py
│   │   │   ├── qa.py
│   │   │   ├── translation_service.py
│   │   │   ├── tts.py
│   │   │   └── video.py
│   │   └── services/
│   │       ├── __pycache__/
│   │       ├── __init__.py
│   │       ├── asr_service.py
│   │       ├── qa_service.py
│   │       ├── translation_service.py
│   │       ├── tts_service.py
│   │       └── video_service.py
│   │
│   ├── db/
│   │   ├── __pycache__/
│   │   ├── crud.py
│   │   ├── database.py
│   │   ├── models.py
│   │   └── schemas.py
│   │
│   ├── output/
│   │   └── audios/
│   │
│   ├── static/
│   │   ├── audio/
│   │   ├── translated_audio/
│   │   └── video/
│   │
│   ├── main.py
│   ├── .env
│   └── venv/
│
├── README.md         # 📄 Project documentation (you are here)
```

---

## 🛠️ Setup Instructions

### ⚙️ Backend (FastAPI)

```bash
cd lisan-backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

### 🌐 Frontend

Just open `index.html` in your browser, or serve via Live Server (VS Code extension).

---

## 📝 License

MIT License

Copyright (c) 2025 Hanzala Salaheen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

... *(rest of license included in the file)*

---

## 🤝 Credits

Crafted with ❤️ by **Hanzala Salaheen**  
www.linkedin.com/in/hanzala-salaheen-2a3944224 | [github.com/hanzi448](https://github.com/Hanzi448)

---

## 🌟 Styling Suggestions (for frontend)

To improve UI:

- Use **TailwindCSS** or **Bootstrap** for rapid UI design.
- Add **AOS.js** or **GSAP** for entry animations.
- Add animated loaders during processing.

---

## 📬 Contribution

Pull requests are welcome. For major changes, open an issue first to discuss what you would like to change.
