import ffmpeg

def convert_to_wav(input_path, output_path):
    ffmpeg.input(input_path).output(output_path, format='wav').run(overwrite_output=True)
