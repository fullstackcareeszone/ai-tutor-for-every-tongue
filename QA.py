import sys
print(sys.executable)
print(sys.version)

from transformers import pipeline
#Try Hugging Face’s pipeline(“question-answering”).
qa_pipeline = pipeline("question-answering")

paragraphs = [
    "Machine learning allows computers to learn from data without explicit programming.",
    "Deep learning is a subfield using neural networks with many layers.",
    "BERT is a transformer-based model designed for language understanding."
]
question = "What is BERT?"

best_answer = ""
best_score = 0

for para in paragraphs:
    result = qa_pipeline(question=question, context=para)
    if result["score"] > best_score:
        best_answer = result["answer"]
        best_score = result["score"]

print("Answer:", best_answer)