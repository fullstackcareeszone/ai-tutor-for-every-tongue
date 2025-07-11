import os
# Add your actual FFmpefromg bin path here
os.environ["PATH"] += os.pathsep + r"C:\Users\PMYLS\Downloads\ffmpeg-7.1.1-full_build\ffmpeg-7.1.1-full_build\bin"
import whisper

model = whisper.load_model("base")
result = model.transcribe("harvard.wav")  # Make sure harvard.wav exists in the same folder
text=result["text"]
print("Transcription:", result["text"])
