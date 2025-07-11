import os
import wave
import uuid
import pyaudio
import keyboard
from faster_whisper import WhisperModel

# === CONFIG ===
MODEL_SIZE = "small"
FFMPEG_BIN_PATH = r"C:\ffmpeg\bin"  # Update if different on your system

# === ENVIRONMENT SETUP ===
os.environ["PATH"] += os.pathsep + FFMPEG_BIN_PATH
os.environ["CTRANSLATE2_LOG_LEVEL"] = "ERROR"  # Suppress model warnings

# === AUDIO RECORDING FUNCTION ===
def record_audio():
    filename = f"mic-recording-{uuid.uuid4().hex[:6]}.wav"

    chunk = 1024
    format = pyaudio.paInt16
    channels = 1
    rate = 16000

    p = pyaudio.PyAudio()
    stream = p.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)

    print("🎙️ Recording... Press ESC to stop.")

    frames = []
    while True:
        if keyboard.is_pressed('esc'):
            break
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))

    return filename

# === TRANSCRIPTION FUNCTION ===
def transcribe(audio_path):
    model = WhisperModel(MODEL_SIZE)
    segments, info = model.transcribe(audio_path)  # Auto language detection

    segments = list(segments)
    transcription = ""
    for segment in segments:
        transcription += f"{segment.text.strip()}\n"

    return transcription.strip()

# === MAIN FUNCTION ===
def run():
    audio_file = record_audio()
    text = transcribe(audio_file)

    output_txt = os.path.splitext(audio_file)[0] + ".txt"
    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(text)

    os.remove(audio_file)

if __name__ == "__main__":
    run()
