from pydub import AudioSegment
import os
import subprocess

def modify_audio(input_file, output_file, speed=1.0, volume=1.0):
    # Adjust speed and volume using ffmpeg
    subprocess.run([
        "ffmpeg", "-y", "-i", input_file, 
        "-filter:a", f"atempo={speed},volume={volume}",
        output_file
    ], check=True)
    
    print(f"Audio file saved to {output_file}")