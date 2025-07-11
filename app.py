import os
import time
import speech_recognition as sr
from openai import OpenAI
from dotenv import load_dotenv
from gtts import gTTS
from playsound import playsound
import pyttsx3

# Load API Key
load_dotenv()
client = OpenAI()  # Auth via .env

# Init recognizer and TTS
recognizer = sr.Recognizer()
engine_en = pyttsx3.init()

def speak_urdu(text):
    try:
        tts = gTTS(text=text, lang='ur')
        filename = "urdu_response.mp3"
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        print("❌ Urdu TTS error:", e)

def speak_english(text):
    try:
        engine_en.say(text)
        engine_en.runAndWait()
    except Exception as e:
        print("❌ English TTS error:", e)

def listen(lang='en-US'):
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)
    try:
        text = recognizer.recognize_google(audio, language=lang)
        print(f"📝 You said: {text}")
        return text
    except Exception as e:
        print("❌ Speech recognition error:", e)
        return ""

def translate_with_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("❌ GPT error:", e)
        return "Error from GPT"

# ----- Main bilingual loop -----
if __name__ == "__main__":
    print("👂 Waiting for English question from user...")
    eng_text = listen(lang="en-US")

    if eng_text:
        # Step 1: Translate English to Urdu
        prompt_translate = f"Translate this to Urdu: {eng_text}"
        urdu_translated = translate_with_gpt(prompt_translate)
        print("🟢 Urdu Translation:", urdu_translated)
        speak_urdu(urdu_translated)

        # Step 2: User replies in Urdu
        print("\n🎙️ Now, reply in Urdu:")
        urdu_response = listen(lang="ur-PK")

        if urdu_response:
            # Step 3: Translate Urdu to English
            prompt_translate_back = f"Translate this to English: {urdu_response}"
            eng_for_gpt = translate_with_gpt(prompt_translate_back)
            print("🔁 Translated back to English:", eng_for_gpt)
            speak_english(eng_for_gpt)  # ✅ Speak translation before sending to GPT

            # Step 4: Ask GPT
            gpt_reply = translate_with_gpt(eng_for_gpt)
            print("🤖 GPT:", gpt_reply)

            # Step 5: Speak GPT's reply (in English)
            speak_english(gpt_reply)

