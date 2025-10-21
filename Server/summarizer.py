"""
Lightweight T5-small summarizer
--------------------------------
- Summarizes text up to 200 words
- Works offline after first download
- Automatically uses GPU if available
- Ready for deployment (no FastAPI needed)
"""

import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
from pathlib import Path


class T5Summarizer:
    def __init__(self, model_dir: str = "./models/t5-small", model_name: str = "t5-small"):
        """
        Initialize the summarizer.
        If `model_dir` exists, load the model locally to avoid redownloading.
        """
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        local_path = Path(model_dir)
        if local_path.exists():
            print(f"✅ Loading model locally from: {local_path.resolve()}")
            self.tokenizer = T5Tokenizer.from_pretrained(local_path)
            self.model = T5ForConditionalGeneration.from_pretrained(local_path).to(self.device)
        else:
            print(f"⬇️ Downloading model '{model_name}' from Hugging Face (first-time only)...")
            self.tokenizer = T5Tokenizer.from_pretrained(model_name)
            self.model = T5ForConditionalGeneration.from_pretrained(model_name).to(self.device)

            # Save for future offline use
            local_path.mkdir(parents=True, exist_ok=True)
            self.tokenizer.save_pretrained(local_path)
            self.model.save_pretrained(local_path)
            print(f"💾 Model saved locally to: {local_path.resolve()}")

    def summarize(self, text: str, max_length: int = 100, min_length: int = 30) -> str:
        """
        Summarize a given text (up to 200 words).
        """
        text = text.strip().replace("\n", " ")
        words = text.split()
        if len(words) > 200:
            text = " ".join(words[:200])

        input_text = f"summarize: {text}"
        inputs = self.tokenizer.encode(input_text, return_tensors="pt", truncation=True).to(self.device)

        summary_ids = self.model.generate(
            inputs,
            max_length=max_length,
            min_length=min_length,
            num_beams=4,
            length_penalty=2.0,
            early_stopping=True,
        )
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary


if __name__ == "__main__":
    summarizer = T5Summarizer()

    # Example text (you can replace this with your own input)
    text = """
    Artificial intelligence (AI) is revolutionizing industries across the world.
    From healthcare to finance, AI-driven tools automate tasks, optimize decisions,
    and uncover insights hidden in massive datasets. The rise of machine learning,
    natural language processing, and computer vision continues to accelerate
    innovation and productivity at unprecedented rates.
    """

    print("\n--- Summary ---\n")
    print(summarizer.summarize(text))
