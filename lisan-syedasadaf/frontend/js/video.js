const videoInput = document.getElementById("videoInput");
const langSelect = document.getElementById("videoLang");
const videoBtn = document.getElementById("videoBtn");
const videoStatus = document.getElementById("videoStatus");
const videoPlayer = document.getElementById("videoPlayer");
const videoSource = document.getElementById("videoSource");

videoBtn.addEventListener("click", async () => {
  const file = videoInput.files[0];
  const lang = langSelect.value.trim();

  if (!file || !lang) {
    alert("Select a video and target language.");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);
  formData.append("target_lang", lang);

  videoStatus.textContent = "🎬 Processing video...";
  videoPlayer.hidden = true;

  try {
    const response = await fetch("http://localhost:8000/vvvideo/process-video", {
      method: "POST",
      body: formData
    });

    if (!response.ok) throw new Error(`Video processing failed: ${response.status}`);

    const data = await response.json();
    const videoUrl = `http://localhost:8000/static/${data.processed_video_path}?t=${Date.now()}`;

    // Properly update the source tag and reload video
    videoPlayer.src = videoUrl;  // 🔥 set video URL directly on <video>
    videoPlayer.hidden = false;
    videoPlayer.load();
    videoPlayer.play();


    videoStatus.textContent = "✅ Translated video ready!";
  } catch (err) {
    console.error("Video Error:", err);
    videoStatus.textContent = `❌ Video Error: ${err.message}`;
  }
});
