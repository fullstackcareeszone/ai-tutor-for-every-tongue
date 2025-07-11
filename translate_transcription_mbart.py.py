import os
# Add your actual FFmpeg bin path here
os.environ["PATH"] += os.pathsep + r"C:\Users\HP\Downloads\ffmpeg-7.1.1-full_build\ffmpeg-7.1.1-full_build\bin"

import whisper
model = whisper.load_model("base")

# Transcribe file
result = model.transcribe("Television.wav")
text = result["text"]
print("Transcription:", text)

from transformers import MBart50TokenizerFast

model_name = "facebook/mbart-large-50-many-to-many-mmt"
tokenizer = MBartTokenizer.from_pretrained(model_name)

model = MBartForConditionalGeneration.from_pretrained(model_name)

# Set source language
tokenizer.src_lang = "en_XX"

text = "Hello, how are you?"

# Tokenize
tokens = tokenizer(text, return_tensors="pt")

# Generate
generated_tokens = model.generate(**tokens, forced_bos_token_id=tokenizer.lang_code_to_id["ur_PK"])

# Decode
output = tokenizer.decode(generated_tokens[0], skip_special_tokens=True)
print(output)
