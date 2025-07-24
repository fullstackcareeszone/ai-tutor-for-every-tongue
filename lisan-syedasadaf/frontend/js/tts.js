const speakBtn = document.getElementById("speakBtn");
const ttsInput = document.getElementById("ttsInput");
const ttsPlayer = document.getElementById("ttsPlayer");
const ttsStatus = document.getElementById("ttsStatus");

speakBtn.addEventListener("click", async () => {
  const text = ttsInput.value.trim();
  if (!text) {
    alert("Please enter text for speech.");
    return;
  }

  try {
    ttsStatus.textContent = "⏳ Generating speech...";
    
    const response = await fetch("http://localhost:8000/tts/speak", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    });

    if (!response.ok) throw new Error(`TTS failed: ${response.status}`);

    const data = await response.json();
    const audioUrl = `http://localhost:8000/static/${data.audio_file}?v=${Date.now()}`;

    // Set audio source and show player without autoplay
    ttsPlayer.src = audioUrl;
    ttsPlayer.hidden = false;
    ttsStatus.textContent = "✅ Ready to play speech below.";
  } catch (err) {
    console.error("TTS Error:", err);
    ttsStatus.textContent = `❌ TTS Error: ${err.message}`;
  }
});
