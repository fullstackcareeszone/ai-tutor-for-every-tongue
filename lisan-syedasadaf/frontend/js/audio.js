const uploadBtn = document.getElementById('uploadBtn');
const audioInput = document.getElementById('audioInput');
const asrOutput = document.getElementById('asrOutput');

uploadBtn.addEventListener('click', async () => {
  const file = audioInput.files[0];
  if (!file) {
    alert('Please select an audio file.');
    return;
  }

  const formData = new FormData();
  formData.append('file', file);

  asrOutput.textContent = "⏳ Transcribing audio...";

  try {
    const response = await fetch('http://localhost:8000/asr/transcribe', {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      throw new Error(`Server responded with ${response.status}`);
    }

    const data = await response.json();
    asrOutput.textContent = `📝 ${data.text} \n🌐 Detected language: ${data.language}`;
  } catch (err) {
    console.error('ASR Upload Error:', err);
    asrOutput.textContent = `❌ Error: ${err.message}`;
  }
});
