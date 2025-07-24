from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

model_name = "facebook/mbart-large-50-many-to-many-mmt"
tokenizer = MBart50TokenizerFast.from_pretrained(model_name)
model = MBartForConditionalGeneration.from_pretrained(model_name)

def translate(text, src_lang="ur_PK", tgt_lang="en_XX"):
    tokenizer.src_lang = src_lang
    encoded = tokenizer(text, return_tensors="pt")
    generated = model.generate(**encoded, forced_bos_token_id=tokenizer.lang_code_to_id[tgt_lang])
    return tokenizer.decode(generated[0], skip_special_tokens=True)

def test_translation():
    sample_text = "یہ ایک ٹیسٹ جملہ ہے۔"
    translated = translate(sample_text)
    print(f"Translation:\n{translated}")

if __name__ == "__main__":
    test_translation()
