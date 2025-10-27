import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
from pathlib import Path

MODEL_PATH = "./models/t5-small-note"
SAVE_PATH = "./models/t5-small-note-quantized"

print("🔹 Loading model...")
model = T5ForConditionalGeneration.from_pretrained(MODEL_PATH)
tokenizer = T5Tokenizer.from_pretrained(MODEL_PATH)

print("🔹 Quantizing model (INT8 dynamic)...")
model_quantized = torch.quantization.quantize_dynamic(
    model, {torch.nn.Linear}, dtype=torch.qint8
)

Path(SAVE_PATH).mkdir(parents=True, exist_ok=True)

print("💾 Saving quantized model object (entire)...")
torch.save(model_quantized, f"{SAVE_PATH}/quantized_model.pt")

tokenizer.save_pretrained(SAVE_PATH)

print("✅ Quantized model saved successfully at:", SAVE_PATH)
