import os
# Add your actual FFmpeg bin path here
os.environ["PATH"] += os.pathsep + r"C:\Users\PMYLS\Downloads\ffmpeg-7.1.1-full_build\ffmpeg-7.1.1-full_build\bin"

import whisper
model = whisper.load_model("base")

# Transcribe file
result = model.transcribe("harvard.wav")
text = result["text"]
print("Transcription:", text)

from transformers import MarianMTModel, MarianTokenizer

model_name = 'Helsinki-NLP/opus-mt-en-ur'

tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

tokens = tokenizer(text, return_tensors="pt", padding=True)
translated = model.generate(**tokens)

output = tokenizer.decode(translated[0], skip_special_tokens=True)
print("After translation:\n", output)

with open("translationnur.txt", "w", encoding="utf-8") as f:
    f.write(output)

print("Translation saved to translationnur.txt")