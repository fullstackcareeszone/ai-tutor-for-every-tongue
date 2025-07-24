import ffmpeg
import os
import subprocess

def extract_audio_from_video(video_path, audio_output_path):
    (
        ffmpeg
        .input(video_path)
        .output(audio_output_path, ac=1, ar='16k')  # mono, 16kHz
        .overwrite_output()
        .run()
    )

def merge_audio_with_video(video_path, audio_path, output_path):
    (
        ffmpeg
        .output(
            ffmpeg.input(video_path).video,
            ffmpeg.input(audio_path).audio,
            output_path,
            vcodec='copy',
            acodec='aac',
            strict='experimental',
            shortest=None  # Ensures video doesn't exceed audio
        )
        .run(overwrite_output=True)
    )

def add_subtitles_to_video(video_path, subtitle_text, output_path):
    subtitle_file = "static/output/subtitles.srt"
    with open(subtitle_file, "w", encoding="utf-8") as f:
        f.write("1\n")
        f.write("00:00:00,000 --> 00:00:10,000\n")
        f.write(f"{subtitle_text}\n")

    (
        ffmpeg
        .input(video_path)
        .output(output_path, vf=f"subtitles={subtitle_file}")
        .overwrite_output()
        .run()
    )
