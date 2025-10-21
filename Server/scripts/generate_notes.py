"""
Use fine-tuned T5-small model for note generation (offline ready)
---------------------------------------------------------------
"""

import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

MODEL_PATH = "./models/t5-small-note"

class NoteGenerator:
    def __init__(self, model_path=MODEL_PATH):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = T5Tokenizer.from_pretrained(model_path)
        self.model = T5ForConditionalGeneration.from_pretrained(model_path).to(self.device)

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
    generator = NoteGenerator()
    sample_text = """
    Machine learning is a subset of artificial intelligence that focuses on enabling
    systems to learn from data and improve their performance without being explicitly
    programmed. It involves algorithms that analyze data, detect patterns, and make
    decisions with minimal human intervention.
    """

    print("\n--- Generated Notes ---\n")
    print(generator.generate_notes(sample_text))
