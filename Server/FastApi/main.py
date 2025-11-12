from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
from pathlib import Path

app = FastAPI(title="T5 Note Generator API")

MODEL_PATH = "./models/t5-small-note"

class NoteGenerator:
    def __init__(self, model_path=MODEL_PATH):
        self.model_path = Path(model_path)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = None
        self.tokenizer = None

    def load_model(self):
        """Loads the model only once, when needed."""
        if self.model is None or self.tokenizer is None:
            if self.model_path.exists():
                print("✅ Loading fine-tuned model from:", self.model_path)
                self.tokenizer = T5Tokenizer.from_pretrained(self.model_path)
                self.model = T5ForConditionalGeneration.from_pretrained(self.model_path).to(self.device)
            else:
                raise RuntimeError(f"Model path '{self.model_path}' not found.")
        else:
            print("⚡ Model already loaded in memory.")

    def generate_notes(self, text: str, max_length=256, min_length=50):
        """Generates notes using the model (loads it if not already loaded)."""
        self.load_model()  # Lazy load

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
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)


# ---------- Initialize lazy generator (no load yet) ----------
generator = NoteGenerator()

class NoteRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "T5 Note Generator API is running!"}

@app.post("/generate-notes")
def generate_notes(request: NoteRequest):
    try:
        print(f"🟢 Incoming text length: {len(request.text)}")
        result = generator.generate_notes(request.text)
        print("✅ Notes generated successfully")
        return {"notes": result}
    except Exception as e:
        import traceback
        print("❌ Error generating notes:", e)
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
