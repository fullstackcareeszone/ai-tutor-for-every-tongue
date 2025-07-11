# ai-tutor-for-every-tongue
An AI-powered language tutoring system designed to teach and converse in multiple languages using natural language processing and translation models.

# Audio Transcription & Translation Scripts

This module contains Python scripts for transcribing audio to text using OpenAI's Whisper model and translating the text using HuggingFace models. These scripts are part of the AI Tutor for Every Tongue project.

## 📁 Scripts Overview

| Script | Description |
|--------|-------------|
| `transcribe_audio_file.py` | Transcribes a pre-recorded `.wav` file using Whisper and saves the output text. |
| `transcribe_microphone_input.py` | Records live audio from the microphone, transcribes it, and saves the result. |
| `translate_transcription_marian.py` | Translates English text (from audio) into Urdu using MarianMT model. |
| `translate_transcription_mbart.py` | Translates English text into Urdu using mBART multilingual model. |

---

## ⚙️ Dependencies

Install required libraries:

```bash
pip install openai-whisper
pip install sounddevice
pip install scipy
pip install transformers
pip install torch
```

> ⚠️ Also make sure [FFmpeg](https://ffmpeg.org/download.html) is installed and its `/bin` path is added to your system PATH variable.

---

## 🚀 How to Run

### 1. Transcribe a pre-recorded file:
```bash
python transcribe_audio_file.py
```

### 2. Record mic input and transcribe:
```bash
python transcribe_microphone_input.py
```

### 3. Translate using MarianMT:
```bash
python translate_transcription_marian.py
```

### 4. Translate using mBART:
```bash
python translate_transcription_mbart.py
```

---

## 📌 Notes

- Models are loaded directly from HuggingFace and OpenAI Whisper.
- Whisper is best used with 16kHz `.wav` audio.
- All output text is saved to `.txt` files automatically.

---

## 👤 Author

Branch: `syedasadaf`  
Contributor: **Syedsadaf**
