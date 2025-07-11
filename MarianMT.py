#MarainMT  #here we use model to translate en to french

from transformers import MarianMTModel, MarianTokenizer

model_name = 'Helsinki-NLP/opus-mt-fr-en'


tokenizer=MarianTokenizer.from_pretrained(model_name)
model=MarianMTModel.from_pretrained(model_name)

text="Bonjour, comment ça va ?"

tokens=tokenizer(text,return_tensors="pt",padding=True)
translated = model.generate(**tokens)

output = tokenizer.decode(translated[0],skip_special_tokens=True)
print(output)

