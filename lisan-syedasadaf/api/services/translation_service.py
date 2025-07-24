from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from langdetect import detect

# Load the NLLB model and tokenizer
model_name = "facebook/nllb-200-distilled-600M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Mapping between ISO language codes and NLLB language codes
LANGUAGE_CODE_MAP = {
    "en": "eng_Latn",
    "ur": "urd_Arab",
    "fr": "fra_Latn",
    "es": "spa_Latn",
    "hi": "hin_Deva",
    # Add more as needed
}


def translate_text(text: str, target_lang: str = "en") -> str:
    """
    Translate given text to target language using NLLB.
    Returns translated text as a string, or None if an error occurs.
    """
    try:
        # Detect the source language
        detected_lang = detect(text)
        print(f"🔍 Detected language: {detected_lang}")

        # Get the language codes for NLLB
        src = LANGUAGE_CODE_MAP.get(detected_lang, "eng_Latn")
        tgt = LANGUAGE_CODE_MAP.get(target_lang, "eng_Latn")
        print(f"🌐 Translating from {src} to {tgt}")

        # Tokenize and generate translation
        tokenizer.src_lang = src
        inputs = tokenizer(text, return_tensors="pt")
        generated_tokens = model.generate(
            **inputs,
            forced_bos_token_id=tokenizer.convert_tokens_to_ids(tgt)
        )

        # Decode and return the result
        translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
        print("✅ Translated text:", translated_text)
        return translated_text

    except Exception as e:
        print("❌ TRANSLATION FAILED:", str(e))
        return None
