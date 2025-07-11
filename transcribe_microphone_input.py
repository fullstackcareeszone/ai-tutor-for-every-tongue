import os
import sounddevice as sd
from scipy.io.wavfile import write
import whisper
os.environ["PATH"] += os.pathsep + r"C:\Users\HP\Downloads\ffmpeg-7.1.1-full_build\ffmpeg-7.1.1-full_build\bin"
fs = 16000  # Sample rate

seconds = int(input("Enter duration of recording in seconds: "))
print("Recording... Speak now!")
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()  # Wait until recording is finished

write("input.wav", fs, recording)
print("Recording saved as input.wav")
model = whisper.load_model("base")

result = model.transcribe("input.wav")
original_text = result["text"]
print("Transcription:", original_text)
with open("microphone.txt", "w", encoding="utf-8") as f:
    f.write(original_text)
print("Transcription saved to transcription.txt")

