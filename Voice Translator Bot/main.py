import whisper
import speech_recognition as sr
from langdetect import detect
from transformers import pipeline
import pyttsx3
import time

# Load Whisper ASR model
asr_model = whisper.load_model("base")

# Language options
lang_map = {
    "en": "English",
    "ur": "Urdu",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
    "it": "Italian",
    "hi": "Hindi",
    "ar": "Arabic",
    "ru": "Russian",
    "zh": "Chinese (Simplified)",
    "ja": "Japanese",
    "pt": "Portuguese",
    "bn": "Bengali",
    "tr": "Turkish"
}

# Supported translation pairs (check Hugging Face model hub for more)
translation_models = {
    ("en", "ur"): "Helsinki-NLP/opus-mt-en-ur",
    ("ur", "en"): "Helsinki-NLP/opus-mt-ur-en",

    ("en", "fr"): "Helsinki-NLP/opus-mt-en-fr",
    ("fr", "en"): "Helsinki-NLP/opus-mt-fr-en",

    ("en", "de"): "Helsinki-NLP/opus-mt-en-de",
    ("de", "en"): "Helsinki-NLP/opus-mt-de-en",

    ("en", "es"): "Helsinki-NLP/opus-mt-en-es",
    ("es", "en"): "Helsinki-NLP/opus-mt-es-en",

    ("en", "it"): "Helsinki-NLP/opus-mt-en-it",
    ("it", "en"): "Helsinki-NLP/opus-mt-it-en",

    ("en", "hi"): "Helsinki-NLP/opus-mt-en-hi",
    ("hi", "en"): "Helsinki-NLP/opus-mt-hi-en",

    ("en", "ar"): "Helsinki-NLP/opus-mt-en-ar",
    ("ar", "en"): "Helsinki-NLP/opus-mt-ar-en",

    ("en", "ru"): "Helsinki-NLP/opus-mt-en-ru",
    ("ru", "en"): "Helsinki-NLP/opus-mt-ru-en",

    ("en", "zh"): "Helsinki-NLP/opus-mt-en-zh",
    ("zh", "en"): "Helsinki-NLP/opus-mt-zh-en",

    ("en", "ja"): "Helsinki-NLP/opus-mt-en-jap",
    ("ja", "en"): "Helsinki-NLP/opus-mt-jap-en",

    ("en", "pt"): "Helsinki-NLP/opus-mt-en-pt",
    ("pt", "en"): "Helsinki-NLP/opus-mt-pt-en",

    ("en", "bn"): "Helsinki-NLP/opus-mt-en-bn",
    ("bn", "en"): "Helsinki-NLP/opus-mt-bn-en",

    ("en", "tr"): "Helsinki-NLP/opus-mt-en-tr",
    ("tr", "en"): "Helsinki-NLP/opus-mt-tr-en",
}

# Ask user for desired output language
print("🌐 Available languages for translation output:")
for code, name in lang_map.items():
    print(f" - {name} ({code})")

target_lang = input("\nEnter the target language code you want replies in (e.g., 'en' for English): ").strip().lower()

if target_lang not in lang_map:
    print("❌ Unsupported language code.")
    exit()

# Set up microphone & recognizer
r = sr.Recognizer()
mic = sr.Microphone()

print("\n🎤 Prepare to speak. Recording starts in 2 seconds...")
time.sleep(2)

print("🎙️ Now recording for 8 seconds... Speak clearly!")
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source, duration=8)

# Save audio to file
with open("speech.wav", "wb") as f:
    f.write(audio.get_wav_data())

# Transcribe using Whisper
print("\n🧠 Transcribing speech...")
result = asr_model.transcribe("speech.wav")
original_text = result["text"]
print("🗣️ You said:", original_text)

# Detect spoken language
try:
    detected_lang = detect(original_text)
except Exception:
    print("❌ Could not detect language.")
    exit()

print("🌍 Detected Language:", lang_map.get(detected_lang, detected_lang))

# Check if translation model is available
model_key = (detected_lang, target_lang)
if model_key not in translation_models:
    print(f"❌ Translation from {detected_lang} to {target_lang} not supported.")
    exit()

# Translate using Hugging Face pipeline
print(f"🔄 Translating to {lang_map[target_lang]}...")
translator = pipeline("translation", model=translation_models[model_key])
translated = translator(original_text)[0]['translation_text']
print(f"💬 Translated Text ({lang_map[target_lang]}):", translated)

# Speak the translated text
engine = pyttsx3.init()
engine.setProperty("rate", 150)

try:
    engine.say(translated)
    engine.runAndWait()
except Exception as e:
    print("⚠️ TTS error:", e)
