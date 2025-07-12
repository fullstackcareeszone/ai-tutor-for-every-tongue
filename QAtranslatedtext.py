from transformers import MBartForConditionalGeneration, MBart50TokenizerFast, pipeline

# ==== mBART model for Urdu → English ====
model_name = "facebook/mbart-large-50-many-to-many-mmt"
tokenizer = MBart50TokenizerFast.from_pretrained(model_name)
model = MBartForConditionalGeneration.from_pretrained(model_name)

# Your Urdu question
urdu_question = "ہیری پوٹر کی کتاب کس نے لکھی؟"

# Set source language as Urdu
tokenizer.src_lang = "ur_PK"
encoded_input = tokenizer(urdu_question, return_tensors="pt")

# Translate Urdu → English
generated_tokens = model.generate(
    **encoded_input,
    forced_bos_token_id=tokenizer.lang_code_to_id["en_XX"]
)
translated_question = tokenizer.decode(generated_tokens[0], skip_special_tokens=True)
print(" Translated Question:", translated_question)

# ==== Context / Text Corpus ====
context = "J.K. Rowling is a British author. She wrote the Harry Potter series which became very popular worldwide."

# ==== QA Pipeline ====
qa = pipeline("question-answering")

# Get answer
result = qa(question=translated_question, context=context)
answer = result['answer']
print(" English Answer:", answer)

# ==== Translate Answer Back to Urdu ====
# Now translate the answer back from English to Urdu using mBART
tokenizer.src_lang = "en_XX"
answer_tokens = tokenizer(answer, return_tensors="pt")
translated_back_tokens = model.generate(
    **answer_tokens,
    forced_bos_token_id=tokenizer.lang_code_to_id["ur_PK"]
)
final_urdu_answer = tokenizer.decode(translated_back_tokens[0], skip_special_tokens=True)

print("Final Answer in Urdu:", final_urdu_answer)
       