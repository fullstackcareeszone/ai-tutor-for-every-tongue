import whisper
from transformers import MarianMTModel, MarianTokenizer, pipeline
import os

# 🌐 Define available local translation models
language_models = {
    "ur": "huggingface_model_ur",
    "fr": "huggingface_model_fr",
    "ps": "huggingface_model_ps"
}

# 📥 Ask user which language they want
print("Available language codes:")
for code in language_models:
    print(f"  ➤ {code}")
target_lang = input("Enter language code (e.g., ur, fr, ps): ").strip().lower()

# 📁 Paths
base_dir = os.path.dirname(__file__)
audio_path = os.path.join(base_dir, "sample.opus")

# ✅ Check if audio file exists
if not os.path.exists(audio_path):
    raise FileNotFoundError("sample.opus not found in this folder.")

# ✅ Check if language model is available
if target_lang not in language_models:
    raise ValueError(f"Model for '{target_lang}' not found. Available: {', '.join(language_models.keys())}")

model_path = os.path.join(base_dir, language_models[target_lang])
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Local model folder not found at: {model_path}")

# 🎙️ Step 1: Transcribe
print("🎙️ Transcribing to English...")
whisper_model = whisper.load_model("base")
result = whisper_model.transcribe(audio_path)
original_text = result["text"]
print("🗣️ Transcribed Text:", original_text)

# 🌍 Step 2: Translate
print(f"🔄 Translating to {target_lang}...")
tokenizer = MarianTokenizer.from_pretrained(model_path)
translation_model = MarianMTModel.from_pretrained(model_path)
translator = pipeline("translation", model=translation_model, tokenizer=tokenizer)
translated = translator(original_text)[0]["translation_text"]
print(f"🌐 Translated Text ({target_lang}):", translated)

# 💾 Step 3: Save translation
output_path = os.path.join(base_dir, f"translated_{target_lang}.txt")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(translated)
print(f"✅ Translation saved to: {output_path}")
