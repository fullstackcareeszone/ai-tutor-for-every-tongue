from TTS.api import TTS
import sounddevice as sd
import soundfile as sf

# 1️⃣ Input text
text = "Hello! This is a test of text to speech using Coqui TTS in VS Code."

# 2️⃣ Load TTS model
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=True, gpu=False)

# 3️⃣ Convert text to speech & save as audio file
output_file = "output.wav"
tts.tts_to_file(text=text, file_path=output_file)

# 4️⃣ Read audio file
data, samplerate = sf.read(output_file)

# 5️⃣ Play audio
sd.play(data, samplerate)
sd.wait()  # Wait until audio playback is finished

print("✅ Done! Audio played successfully.")
