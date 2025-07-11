from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

# Load the mBART50 model and tokenizer
model_name = "facebook/mbart-large-50-many-to-many-mmt"
tokenizer = MBart50TokenizerFast.from_pretrained(model_name)
model = MBartForConditionalGeneration.from_pretrained(model_name)

# Input text and language codes
text = "Hello, how are you?"

# Set source and target languages
tokenizer.src_lang = "en_XX"  # English
encoded = tokenizer(text, return_tensors="pt")

# Generate translation
generated_tokens = model.generate(
    **encoded,
    forced_bos_token_id=tokenizer.lang_code_to_id["ur_PK"]  # Urdu
)

# Decode the output
output = tokenizer.decode(generated_tokens[0], skip_special_tokens=True)
print(output)
