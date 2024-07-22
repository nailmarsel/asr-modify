import json
import torch
from os import listdir
from os.path import isfile, join

def load_whisper_model(model_path, device):
    model = torch.load(model_path, map_location=device)
    model.to(device)
    return model

def transcribe_audio(input_file, output_file):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model_path = "/app/models/whisper/model.pt"
    model = load_whisper_model(model_path, device)

    result = model.transcribe(input_file)
    result.pop("segments")

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
    print(f"Transcription saved to {output_file}")
