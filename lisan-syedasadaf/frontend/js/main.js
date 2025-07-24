const speakBtn = document.getElementById('speakBtn');
const ttsInput = document.getElementById('ttsInput');
const ttsAudio = document.getElementById('ttsPlayer');
const ttsStatus = document.getElementById('ttsStatus');

speakBtn.addEventListener('click', async () => {
  const text = ttsInput.value.trim();
  if (!text) {
    alert('Please enter some text to synthesize.');
    return;
  }

  try {
    ttsStatus.textContent = "🔊 Generating speech...";
    
    const response = await fetch('http://localhost:8000/tts/speak', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ text })
    });

    if (!response.ok) {
      throw new Error(`TTS failed: ${response.status}`);
    }

    const data = await response.json();
    ttsAudio.src = `http://localhost:8000/static/${data.audio_file}?t=${Date.now()}`;
    ttsAudio.hidden = false;
    ttsAudio.play();
    ttsStatus.textContent = "✅ Speech generated.";
  } catch (err) {
    console.error("TTS Error:", err);
    ttsStatus.textContent = `❌ TTS Error: ${err.message}`;
  }
});
