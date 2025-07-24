// ASR (Speech to Text)
async function handleASR() {
    const fileInput = document.getElementById("asr-audio");
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch("/asr/", {
            method: "POST",
            body: formData
        });

        const result = await response.json();

        if (response.ok) {
            document.getElementById("asr-output-display").innerText = result.transcription;
            // Save transcription text globally for Translation
            window.currentTranscriptionText = result.transcription;
            console.log("Transcription Saved:", window.currentTranscriptionText);
        } else {
            alert("ASR Error: " + result.detail);
        }
    } catch (error) {
        alert("ASR Failed: " + error);
    }
}

// Translation (Text to Text)
async function handleTranslate() {
    if (!window.currentTranscriptionText) {
        alert("Please transcribe an audio first.");
        return;
    }

    const langSelect = document.getElementById("translate-lang");
    const langPair = langSelect.value.split("-");
    const srcLang = langPair[0];
    const tgtLang = langPair[1];

    try {
        const response = await fetch("/translate/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: window.currentTranscriptionText,
                src_lang: srcLang,
                tgt_lang: tgtLang
            })
        });

        const result = await response.json();

        if (response.ok) {
            document.getElementById("translate-output-display").innerText = result.translated_text;
        } else {
            alert("Translation Error: " + result.detail);
        }
    } catch (error) {
        alert("Translation Failed: " + error);
    }
}

// TTS (Text to Speech)
async function handleTTS() {
    const text = document.getElementById("tts-text").value.trim();
    if (!text) {
        alert("Please enter text for TTS.");
        return;
    }

    try {
        const response = await fetch("/tts/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: text, lang: "en" })
        });

        const result = await response.json();

        if (response.ok) {
            const audioElement = document.getElementById("tts-audio");
            audioElement.src = result.audio_path;
            audioElement.load();
            audioElement.play();
        } else {
            alert("TTS Error: " + result.detail);
        }
    } catch (error) {
        alert("TTS Request Failed: " + error);
    }
}

// Video Processing
async function handleVideo() {
    const videoInput = document.getElementById("video-file");
    const langSelect = document.getElementById("video-lang");
    const file = videoInput.files[0];
    const targetLang = langSelect.value;

    if (!file) {
        alert("Please upload a video file.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("target_lang", targetLang);

    try {
        const response = await fetch("/video/", {
            method: "POST",
            body: formData
        });

        if (response.ok) {
            const videoBlob = await response.blob();
            const videoURL = URL.createObjectURL(videoBlob);

            const videoElement = document.getElementById("output-video");
            videoElement.src = videoURL;
            videoElement.style.display = "block";

        } else {
            const result = await response.json();
            alert("Video Processing Error: " + result.detail);
        }
    } catch (error) {
        alert("Video Processing Failed: " + error);
    }
}


// Question Answering (QA)
async function handleQA() {
    const question = document.getElementById("qa-question").value.trim();
    if (!question) {
        alert("Please enter a question.");
        return;
    }

    try {
        const response = await fetch("/qa/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question: question })
        });

        const result = await response.json();

        if (response.ok) {
            document.getElementById("qa-output-display").innerText = result.answer;
        } else {
            alert("QA Error: " + result.detail);
        }
    } catch (error) {
        alert("QA Request Failed: " + error);
    }
}
