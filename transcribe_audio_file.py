import os
# Add your actual FFmpeg bin path here
os.environ["PATH"] += os.pathsep + r"C:\Users\HP\Downloads\ffmpeg-7.1.1-full_build\ffmpeg-7.1.1-full_build\bin"
import whisper
model = whisper.load_model("base")

# Transcribe file
result = model.transcribe("harvard.wav")
original_text = result["text"]
print("Transcription:", original_text)

# Save to file
with open("transcription.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])
print("Transcription saved to transcription.txt")
