import whisper
from googletrans import Translator
import os

# === Step 0: Get current script directory ===
current_dir = os.path.dirname(os.path.abspath(__file__))

# === Step 1: Ask user for audio file name (must be in the same folder) ===
print("📂 Audio files found in this folder:")
print([f for f in os.listdir(current_dir) if f.endswith((".mp3", ".opus", ".wav"))])
audio_name = input("🎵 Enter audio file name (e.g., sample.opus): ")

audio_path = os.path.join(current_dir, audio_name)

if not os.path.exists(audio_path):
    print("❌ File not found! Please check the name.")
    exit()

# === Step 2: Transcribe to English ===
print("\n🎙️ Transcribing audio to English using Whisper...")
model = whisper.load_model("base")
try:
    result = model.transcribe(audio_path, task="translate")  # Always outputs English
except Exception as e:
    print("❌ Whisper failed to process audio:", e)
    exit()

english_text = result["text"]
print("\n🔊 English Transcription:")
print(english_text)

# === Step 3: Ask user for target language ===
print("\n🌐 Language Codes (examples): ur=Urdu, pa=Punjabi, ps=Pashto, fr=French, hi=Hindi, ko=Korean, ar=Arabic")
target_lang = input("✏️ Enter the language code to translate to: ")

# === Step 4: Translate ===
translator = Translator()
try:
    translated = translator.translate(english_text, dest=target_lang)
    translated_text = translated.text
    print(f"\n🌍 Translated Text ({target_lang}):")
    print(translated_text)
except Exception as e:
    print("❌ Translation error:", e)
    exit()

# === Step 5: Save to current folder ===
file_name = f"translated_{target_lang}.txt"
file_path = os.path.join(current_dir, file_name)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(translated_text)

print(f"\n✅ Translated text saved to: {file_path}")
