#  Lisan: AI Tutor for Every Tongue – Syeda Sadaf's Version

This project is part of the **AI Tutor for Every Tongue** initiative. It enables multilingual learning through speech-based question-answering powered by AI.

This specific implementation (`lisan-syedasadaf`) includes a **FastAPI backend** and a **vanilla JavaScript + Tailwind frontend**, focused on voice-based interaction for students in regional languages like Urdu, Pashto, Sindhi, and Balochi.

---

##  Features

-  **Speech Recognition (ASR)**: Transcribe audio using OpenAI Whisper.
-  **Language Translation**: Translate speech to and from English using Hugging Face models.
-  **Question Answering**: Use AI to answer user questions from transcribed input.
-  **Text-to-Speech (TTS)**: Convert AI-generated answers to speech, including Urdu voice support.
-  **Video Support**: Extract and process audio from videos (under development).

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/fullstackcareeszone/ai-tutor-for-every-tongue.git
cd ai-tutor-for-every-tongue/lisan-syedasadaf
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install fastapi uvicorn python-multipart
pip install torch torchaudio
pip install openai-whisper ffmpeg-python
pip install transformers sentencepiece
pip install gtts pydub
```

>  Also install **FFmpeg** and ensure it's in your system PATH.

---

##  Run the Project

### Start the Backend Server

```bash
uvicorn api.main:app --reload
```

- Access the API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Launch the Frontend

Open `frontend/index.html` in your browser  
or  
use a live server (e.g., VS Code Live Server extension).

---

##  Folder Structure

```
lisan-syedasadaf/
├── api/             # FastAPI backend (ASR, TTS, QA, Translation, Video)
├── frontend/        # HTML, TailwindCSS, JavaScript UI
├── static/          # Stores TTS audio output
├── requirements.txt # Python dependencies
└── README.md        # This file
```

---

##  About This Folder

This is **Syeda Sadaf's personal implementation** under the collaborative repo.  
Each team member contributes their own version in a separate folder.

Main Repository: [fullstackcareeszone/ai-tutor-for-every-tongue](https://github.com/fullstackcareeszone/ai-tutor-for-every-tongue)

---

##  Contact

Feel free to open issues or reach out via GitHub if you'd like to collaborate or provide feedback.

