const translateBtn = document.getElementById('translateBtn');
const translationOutput = document.getElementById('translationOutput');

translateBtn.addEventListener('click', async () => {
  const transcript = document.getElementById('asrOutput').textContent;
  const targetLang = document.getElementById('targetLang').value.trim();

  if (!transcript || transcript.startsWith("❌") || transcript.trim() === "") {
    alert("No valid transcription available to translate.");
    return;
  }

  if (!targetLang) {
    alert("Please enter a target language code (e.g. en, ur, ps).");
    return;
  }

  try {
    const response = await fetch('http://localhost:8000/translation/translate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: new URLSearchParams({
        text: transcript,
        target_lang: targetLang
      })
    });

    if (!response.ok) {
      throw new Error(`Translation failed: ${response.status}`);
    }

    const data = await response.json();
    translationOutput.textContent = `🌍 Translated (${targetLang}): ${data.translated_text}`;
  } catch (err) {
    console.error('Translation Error:', err);
    translationOutput.textContent = `❌ Translation Error: ${err.message}`;
  }
});
