from TTS.api import TTS

tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_model_here", progress_bar=True, gpu=False)

def tts_to_file(text, output_path):
    tts.tts_to_file(text=text, file_path=output_path)

def test_tts():
    sample_text = "This is a test of text to speech."
    output_path = "test_output.wav"
    tts_to_file(sample_text, output_path)
    print(f"Audio saved to {output_path}")

if __name__ == "__main__":
    test_tts()
