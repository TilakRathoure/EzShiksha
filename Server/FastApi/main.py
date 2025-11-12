from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
from pathlib import Path

app = FastAPI(title="T5 Note Generator API")

MODEL_PATH = "./models/t5-small-note"

# ---------- Load model once at startup ----------
class NoteGenerator:
    def __init__(self, model_path=MODEL_PATH):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        local_path = Path(model_path)
        if local_path.exists():
            print("✅ Loading fine-tuned model from:", model_path)
            self.tokenizer = T5Tokenizer.from_pretrained(local_path)
            self.model = T5ForConditionalGeneration.from_pretrained(local_path).to(self.device)
        else:
            raise RuntimeError(f"Model path '{model_path}' not found.")

    def generate_notes(self, text: str, max_length=256, min_length=50):
        text = " ".join(text.strip().split()[:200])
        input_text = f"generate notes: {text}"

        inputs = self.tokenizer.encode(input_text, return_tensors="pt", truncation=True).to(self.device)
        outputs = self.model.generate(
            inputs,
            max_length=max_length,
            min_length=min_length,
            num_beams=5,
            length_penalty=2.0,
            early_stopping=True,
        )
        result = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return result


# ---------- Initialize model ----------
generator = NoteGenerator()

# ---------- Request Body ----------
class NoteRequest(BaseModel):
    text: str

# ---------- Routes ----------
@app.get("/")
def home():
    return {"message": "T5 Note Generator API is running!"}

@app.post("/generate-notes")
def generate_notes(request: NoteRequest):
    try:
        result = generator.generate_notes(request.text)
        return {"notes": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
