
# ai-tutor-for-every-tongue
An AI-powered language tutoring system designed to teach and converse in multiple languages using natural language processing and translation models.

# Audio Transcription, Translation & Text-to-Speech Scripts

This module contains Python scripts for transcribing audio to text using OpenAI's Whisper model, translating the text using HuggingFace models, and generating speech using Coqui TTS.

## 📁 Scripts Overview

| Script | Description |
|--------|-------------|
| `transcribe_audio_file.py` | Transcribes a pre-recorded `.wav` file using Whisper and saves the output text. |
| `transcribe_microphone_input.py` | Records live audio from the microphone, transcribes it, and saves the result. |
| `translate_transcription_marian.py` | Translates English text (from audio) into Urdu using MarianMT model. |
| `translate_transcription_mbart.py` | Translates English text into Urdu using mBART multilingual model. |
| `qa_translate_urdu_to_english_and_back.py` | Translates a question in Urdu to English, answers it using a QA model, and translates the answer back to Urdu. |
| `text_to_speech_coqui.py` | Converts English text to speech using the Coqui TTS model and plays the output audio. |

---

## ⚙️ Dependencies

Install required libraries:

```bash
pip install openai-whisper
pip install sounddevice
pip install scipy
pip install transformers
pip install torch
pip install TTS
pip install soundfile
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

### 5. Urdu Question Answering with Translation:
```bash
python qa_translate_urdu_to_english_and_back.py
```

### 6. Text to Speech using Coqui TTS:
```bash
python text_to_speech_coqui.py
```

---

## 📌 Notes

- Models are loaded directly from HuggingFace and OpenAI Whisper.
- Whisper is best used with 16kHz `.wav` audio.
- HuggingFace’s QA and translation models handle multilingual interactions.
- Coqui TTS is used for text-to-speech synthesis.
- All output text and audio are saved where applicable.

---

## 👤 Author

Branch: `syedasadaf`  
Contributor: **Syedsadaf**
