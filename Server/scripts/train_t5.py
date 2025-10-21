"""
Fine-tune T5-small for note generation (1–10 bullet points)
-----------------------------------------------------------
- Lightweight, CPU/GPU compatible
- Handles texts up to 200 words
- Proper padding/truncation for stable batching
- Saves model locally for offline deployment
"""

from transformers import (
    T5Tokenizer,
    T5ForConditionalGeneration,
    Trainer,
    TrainingArguments,
    DataCollatorForSeq2Seq
)
from datasets import load_dataset
import torch
from pathlib import Path

# -------------------- Config --------------------
MODEL_NAME = "t5-small"
MODEL_DIR = "./models/t5-small-note"
DATA_DIR = "./data"
MAX_INPUT_LENGTH = 512
MAX_TARGET_LENGTH = 256
BATCH_SIZE = 4
EPOCHS = 3
LEARNING_RATE = 3e-4

# ----------------- Preprocessing -----------------
def preprocess_function(examples, tokenizer):
    # Limit input text to 200 words
    inputs = ["generate notes: " + " ".join(text.strip().split()[:200]) for text in examples["text"]]
    model_inputs = tokenizer(
        inputs,
        max_length=MAX_INPUT_LENGTH,
        truncation=True,
        padding="max_length"
    )

    labels = tokenizer(
        examples["notes"],
        max_length=MAX_TARGET_LENGTH,
        truncation=True,
        padding="max_length"
    )

    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

# ------------------- Main ------------------------
def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")

    tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME)
    model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME).to(device)

    # Load JSONL dataset
    dataset = load_dataset("json", data_files={
        "train": f"{DATA_DIR}/train.jsonl",
        "validation": f"{DATA_DIR}/val.jsonl"
    })

    # Preprocess dataset
    tokenized_datasets = dataset.map(
        lambda batch: preprocess_function(batch, tokenizer),
        batched=True,
        remove_columns=dataset["train"].column_names
    )

    # Data collator to handle dynamic padding
    data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

    # Training arguments
    training_args = TrainingArguments(
        output_dir=MODEL_DIR,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        learning_rate=LEARNING_RATE,
        per_device_train_batch_size=BATCH_SIZE,
        per_device_eval_batch_size=BATCH_SIZE,
        num_train_epochs=EPOCHS,
        weight_decay=0.01,
        logging_dir="./logs",
        save_total_limit=2,
        load_best_model_at_end=True,
        fp16=torch.cuda.is_available(),
    )

    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
        eval_dataset=tokenized_datasets["validation"],
        tokenizer=tokenizer,
        data_collator=data_collator
    )

    # Train
    trainer.train()

    # Save fine-tuned model locally
    Path(MODEL_DIR).mkdir(parents=True, exist_ok=True)
    tokenizer.save_pretrained(MODEL_DIR)
    model.save_pretrained(MODEL_DIR)
    print(f"✅ Fine-tuned model saved to {MODEL_DIR}")


if __name__ == "__main__":
    main()
