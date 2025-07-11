from transformers import pipeline
from langdetect import detect
import sys

# Map language codes to Hugging Face MarianMT models
model_map = {
    ("en", "ur"): "Helsinki-NLP/opus-mt-en-ur",
    ("ur", "en"): "Helsinki-NLP/opus-mt-ur-en",
    ("en", "fr"): "Helsinki-NLP/opus-mt-en-fr",
    ("fr", "en"): "Helsinki-NLP/opus-mt-fr-en",
    # Add more pairs if needed
}

# Language display names
lang_names = {
    "en": "English",
    "ur": "Urdu",
    "fr": "French",
}

# Prompt user input
input_text = input("Enter the text you want to translate:\n")

# Auto-detect source language
try:
    src_lang = detect(input_text)
except Exception as e:
    print(f"Could not detect language. Error: {e}")
    sys.exit()

print(f"\nDetected language: {lang_names.get(src_lang, src_lang)}")

# Ask for target language
print("\nSelect target language:")
for code, name in lang_names.items():
    if code != src_lang:
        print(f"- {name} ({code})")

tgt_lang = input("\nEnter target language code (e.g., 'en' for English): ").strip()

# Validate model existence
if (src_lang, tgt_lang) not in model_map:
    print(f"Sorry! Translation from {src_lang} to {tgt_lang} is not supported.")
    sys.exit()

# Load the appropriate model
model_name = model_map[(src_lang, tgt_lang)]
translator = pipeline("translation", model=model_name)

# Translate and display output
translated = translator(input_text)[0]['translation_text']
print(f"\nTranslated text ({lang_names.get(tgt_lang, tgt_lang)}):")
print(translated)
