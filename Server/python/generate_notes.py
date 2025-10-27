import sys
import json
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration
from pathlib import Path

MODEL_PATH = "./models/t5-small-note-quantized"

def main():
    try:
        # 1️⃣ Get input text from Node process
        if len(sys.argv) < 2:
            print(json.dumps({"error": "No input text provided"}))
            sys.exit(1)
        input_text = sys.argv[1].strip()

        # 2️⃣ Load model and tokenizer (lazy load)
        print("🔹 Loading tokenizer...", file=sys.stderr)
        tokenizer = T5Tokenizer.from_pretrained(MODEL_PATH)

        print("💾 Loading quantized model object...", file=sys.stderr)
        quantized_model_path = Path(MODEL_PATH) / "quantized_model.pt"
        if not quantized_model_path.exists():
            raise FileNotFoundError(f"Quantized model not found at {quantized_model_path}")

        # Allowlist T5 class (safe for local model)
        torch.serialization.add_safe_globals([T5ForConditionalGeneration])

        # Load model
        model = torch.load(quantized_model_path, map_location="cpu", weights_only=False)
        model.eval()

        # 3️⃣ Generate notes
        processed_input = f"generate notes: {input_text}"
        inputs = tokenizer.encode(processed_input, return_tensors="pt", truncation=True)

        with torch.no_grad():
            outputs = model.generate(
                inputs,
                max_length=256,
                min_length=50,
                num_beams=5,
                length_penalty=2.0,
                early_stopping=True,
            )

        result = tokenizer.decode(outputs[0], skip_special_tokens=True)

        # 4️⃣ Print to stdout (Node reads this)
        print(result)
        sys.exit(0)

    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
