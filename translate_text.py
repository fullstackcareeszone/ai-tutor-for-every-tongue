from googletrans import Translator

translator = Translator()
result = translator.translate('Hello, how are you?', dest='ur')  # Translate to Urdu
print(result.text)
