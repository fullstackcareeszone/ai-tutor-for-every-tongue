 ############################        DAY:02   ###########################

# mBART = Multilingual + BART(Many-to-Many Translation)

# model:facebook/mbart-large-50-many-to-many-mmt(To translate the transcribed text into another language)
# transformers library (by Hugging Face)
# protobuf (dependency)



from transformers import pipeline, MBartForConditionalGeneration, MBart50TokenizerFast
import os
print("Current Directory:", os.getcwd())


# Set correct path using raw string or forward slashes
audio_path = r"D:\whisper_transcriber\day02-project\sample.opus"


# Load ASR model
asr = pipeline("automatic-speech-recognition", model="openai/whisper-small")
asr_text = asr(audio_path)["text"]
print("Transcribed Text:", asr_text)


# Load mBART model
model_name = "facebook/mbart-large-50-many-to-many-mmt"
tokenizer = MBart50TokenizerFast.from_pretrained(model_name)
model = MBartForConditionalGeneration.from_pretrained(model_name)

# Set source and target languages
src_lang = "en_XX"
tgt_lang = "ur_PK"

# Prepare input for translation
tokenizer.src_lang = src_lang
encoded = tokenizer(asr_text, return_tensors="pt")

# Generate translated output
generated_tokens = model.generate(
    **encoded,
    forced_bos_token_id=tokenizer.lang_code_to_id[tgt_lang]
)

# Decode and print translation
translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
print("Translated Text:", translated_text)
