import argparse
import json
import whisper

def transcribe_audio(input_file, output_file):
    # Load Whisper model
    model = whisper.load_model("large")

    # Transcribe the audio file
    result = model.transcribe(input_file)
    result.pop("segments")
    # Write results to file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
    print(f"Transcription saved to {output_file}")