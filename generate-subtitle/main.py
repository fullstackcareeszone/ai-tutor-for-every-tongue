import os
import ffmpeg
import math
from faster_whisper import WhisperModel

# CONFIG
input_video = r"D:\Full Stack Zone\BootCamp\Day 7\generate-subtitle\input.mp4"
input_video_name = os.path.splitext(os.path.basename(input_video))[0]  # e.g., "input"
ffmpeg_bin_path = r"C:\ffmpeg\bin"  # Update if different
soft_subtitle = False  # Set to True for soft subtitle embedding

# Ensure ffmpeg.exe is found inside virtual environment
os.environ["PATH"] += os.pathsep + ffmpeg_bin_path

def extract_audio():
    """Extracts audio from the input video file as .wav"""
    extracted_audio = f"{input_video_name}.wav"
    stream = ffmpeg.input(input_video)
    stream = ffmpeg.output(stream, extracted_audio)
    ffmpeg.run(stream, overwrite_output=True)
    return extracted_audio

def transcribe(audio):
    """Transcribes the extracted audio and returns language + segments"""
    model = WhisperModel("small")
    segments, info = model.transcribe(audio)
    language = info.language  # ✅ FIXED here
    print(f"\n📘 Detected language: {language}\n")
    segments = list(segments)
    for segment in segments:
        print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
    return language, segments

def format_time(seconds):
    """Formats time in SRT format"""
    hours = math.floor(seconds / 3600)
    seconds %= 3600
    minutes = math.floor(seconds / 60)
    seconds %= 60
    milliseconds = round((seconds - math.floor(seconds)) * 1000)
    seconds = math.floor(seconds)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

def generate_subtitle_file(language, segments):
    """Generates .srt subtitle file from transcription segments"""
    subtitle_file = f"sub-{input_video_name}.{language}.srt"
    text = ""
    for index, segment in enumerate(segments):
        segment_start = format_time(segment.start)
        segment_end = format_time(segment.end)
        text += f"{index+1}\n"
        text += f"{segment_start} --> {segment_end}\n"
        text += f"{segment.text}\n\n"

    with open(subtitle_file, "w", encoding="utf-8") as f:
        f.write(text)

    return subtitle_file

def add_subtitle_to_video(soft_subtitle, subtitle_file, subtitle_language):
    """Embeds subtitles into video (soft or hard) and saves final video"""
    output_video = f"output-{input_video_name}.mp4"

    if soft_subtitle:
        video_input_stream = ffmpeg.input(input_video)
        subtitle_input_stream = ffmpeg.input(subtitle_file)
        stream = ffmpeg.output(
            video_input_stream,
            subtitle_input_stream,
            output_video,
            **{"c": "copy", "c:s": "mov_text"},
            **{
                "metadata:s:s:0": f"language={subtitle_language}",
                "metadata:s:s:1": f"title=Subtitles"
            }
        )
    else:
        # Hardcoded subtitles (burned into video)
        stream = ffmpeg.output(
            ffmpeg.input(input_video),
            output_video,
            vf=f"subtitles={subtitle_file}"
        )

    ffmpeg.run(stream, overwrite_output=True)
    print(f"\n✅ Final video with subtitles saved as: {output_video}")

def run():
    print("🎬 Extracting audio...")
    extracted_audio = extract_audio()

    print("🧠 Transcribing audio...")
    language, segments = transcribe(extracted_audio)

    print("📄 Generating subtitle file...")
    subtitle_file = generate_subtitle_file(language, segments)

    print("🎞️ Embedding subtitles into video...")
    add_subtitle_to_video(soft_subtitle, subtitle_file, language)

    print("\n✅ All done!")

if __name__ == "__main__":
    run()
