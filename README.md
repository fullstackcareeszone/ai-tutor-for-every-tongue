#  AI Tutor for Every Tongue

An intelligent multilingual tutor that listens to your spoken input, transcribes it using speech-to-text, translates it into the desired language, answers your questions using NLP models, and reads responses out loud using text-to-speech.

---

## 🚀 Features

- 🎤 **Speech-to-Text (STT)**: Converts spoken audio into text using OpenAI Whisper.
- 🌐 **Translation**: Translates English text into multiple languages using Hugging Face models (MBART, MarianMT).
- ❓ **Question Answering (Q&A)**: Answers user questions using pre-trained Transformer models.
- 🔊 **Text-to-Speech (TTS)**: Speaks answers out loud using Coqui TTS or Tacotron.

---

## 🛠️ Tech Stack

| Component           | Library/Model                          |
|--------------------|----------------------------------------|
| Speech-to-Text     | `openai-whisper`                       |
| Translation        | `transformers` (MBART / MarianMT)      |
| Question Answering | `transformers` (e.g., BERT-based QA)   |
| Text-to-Speech     | `TTS` (by Coqui) or `pyttsx3`          |

##  🐍 Install Dependencies
pip install openai-whisper
pip install transformers
pip install sentencepiece
pip install soundfile
pip install TTS   # For Coqui TTS
pip install pyttsx3

## 🧠 Models Used
openai/whisper-base

facebook/mbart-large-50-many-to-many-mmt

Helsinki-NLP/opus-mt-en-ur and other MarianMT variants

deepset/bert-base-cased-squad2 for Q&A

tts_models/en/ljspeech/tacotron2-DDC (for TTS)






> **Branch:** `khansauro0j`  
> **Contributor:** Khansa Urooj  
> **Date:** July 11, 2025 (Day 01)
> ** email:** khansaurooj912@example.com
