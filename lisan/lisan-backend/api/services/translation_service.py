from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from langdetect import detect
from fastapi import HTTPException
from sqlalchemy.orm import Session
from db.crud import save_translation  # New
from db.schemas import TranslationSchema  # New

model_name = "facebook/nllb-200-distilled-600M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

LANGUAGE_CODE_MAP = {
    "en": "eng_Latn",
    "ur": "urd_Arab",
    "hi": "hin_Deva",
    "ar": "arb_Arab",
    "fr": "fra_Latn",
    "es": "spa_Latn",
    "de": "deu_Latn",
    "zh": "cmn_Hans",
    "ru": "rus_Cyrl",
    "ja": "jpn_Jpan",
}

def translate_text(text: str, target_lang: str = "en", db: Session = None) -> str:
    try:
        detected_iso = detect(text)
        src = LANGUAGE_CODE_MAP.get(detected_iso, "eng_Latn")
        tgt = LANGUAGE_CODE_MAP.get(target_lang, "eng_Latn")

        tokenizer.src_lang = src
        inputs = tokenizer(text, return_tensors="pt")
        generated_tokens = model.generate(
            **inputs,
            forced_bos_token_id=tokenizer.convert_tokens_to_ids(tgt),
            max_length=512
        )
        translated = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]

        if db:
            data = TranslationSchema(
                source_text=text,
                translated_text=translated,
                source_lang=detected_iso,
                target_lang=target_lang
            )
            save_translation(db, data)

        return translated
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation failed: {e}")
