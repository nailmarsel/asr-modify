import whisper
import os
import torch


model = whisper.load_model("small")

model_dir = "/app/models/whisper"
os.makedirs(model_dir, exist_ok=True)

model_path = os.path.join(model_dir, "model.pt")
torch.save(model, model_path)

print(f"Model saved to {model_path}")
