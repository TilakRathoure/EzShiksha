"""
Use fine-tuned T5-small model for note generation (offline ready)
---------------------------------------------------------------
"""

import sys
import json
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration
from pathlib import Path

MODEL_PATH = "./models/t5-small-note"

class NoteGenerator:
    def __init__(self, model_path=MODEL_PATH):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        local_path = Path(model_path)
        if local_path.exists():
            self.tokenizer = T5Tokenizer.from_pretrained(local_path)
            self.model = T5ForConditionalGeneration.from_pretrained(local_path).to(self.device)
        else:
            print(f"⬇️ Model path '{model_path}' not found. Please ensure the model exists.", file=sys.stderr)
            sys.exit(1)

    def generate_notes(self, text: str, max_length=256, min_length=50):
        text = " ".join(text.strip().split()[:200])  # limit to 200 words
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

if __name__ == "__main__":
    try:
        # Get input text from command-line argument
        input_text = sys.argv[1] if len(sys.argv) > 1 else ""
        if not input_text.strip():
            raise ValueError("No input text provided")

        generator = NoteGenerator()
        result = generator.generate_notes(input_text)
        print("Notes: \n",result)
        sys.exit(0)

    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)
