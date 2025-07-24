const qaBtn = document.getElementById('qaBtn');
const questionInput = document.getElementById('questionInput');
const qaOutput = document.getElementById('qaOutput');

qaBtn.addEventListener('click', async () => {
  const question = questionInput.value.trim();
  if (!question) {
    alert('Please enter a question.');
    return;
  }

  try {
    const res = await fetch('http://localhost:8000/gemini/qa', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ question })
    });

    if (!res.ok) {
      throw new Error(`QA failed: ${res.status}`);
    }

    const data = await res.json();
    qaOutput.textContent = `💡 Answer: ${data.answer}`;
  } catch (err) {
    console.error('QA Error:', err);
    qaOutput.textContent = `❌ QA Error: ${err.message}`;
  }
});
