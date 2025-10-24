import re
from pathlib import Path

import torch
from datasets import load_dataset
from transformers import (
    T5Tokenizer,
    T5ForConditionalGeneration,
    Trainer,
    TrainingArguments,
    DataCollatorForSeq2Seq,
    EarlyStoppingCallback
)

# -------------------- Config --------------------
MODEL_NAME = "t5-small"
MODEL_DIR = "./models/t5-small-note"
DATA_DIR = "./data"
TRAIN_FILE = f"{DATA_DIR}/train.jsonl"
VAL_FILE = f"{DATA_DIR}/val.jsonl"

MAX_INPUT_LENGTH = 512
MAX_TARGET_LENGTH = 150
BATCH_SIZE = 4
EPOCHS = 10
LEARNING_RATE = 1e-4

# ----------------- Preprocessing -----------------
def remove_duplicate_sentences(text: str) -> str:
    sentences = re.split(r'(?<=[.!?]) +', text.strip())
    seen = set()
    unique_sentences = []
    for s in sentences:
        if s not in seen:
            seen.add(s)
            unique_sentences.append(s)
    return " ".join(unique_sentences)

def preprocess_function(examples, tokenizer):
    cleaned_inputs = [
        "generate notes: " + remove_duplicate_sentences(text)
        for text in examples["text"]
    ]
    model_inputs = tokenizer(
        cleaned_inputs,
        max_length=MAX_INPUT_LENGTH,
        truncation=True,
        padding="max_length"
    )

    labels = tokenizer(
        examples["notes"],
        max_length=MAX_TARGET_LENGTH,
        truncation=True,
        padding=False
    )
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

# ------------------- Main ------------------------
def main():
    # Device setup
    device = "cuda" if torch.cuda.is_available() else "cpu"
    if device == "cuda":
        print(f"✅ Using GPU: {torch.cuda.get_device_name(0)}")
    else:
        print("⚠️ GPU not detected. Training will be slow on CPU.")

    # Load tokenizer and model
    tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME)
    model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME).to(device)

    # Load datasets
    dataset = load_dataset("json", data_files={
        "train": TRAIN_FILE,
        "validation": VAL_FILE
    })

    # Preprocess dataset
    tokenized_datasets = dataset.map(
        lambda batch: preprocess_function(batch, tokenizer),
        batched=True,
        remove_columns=dataset["train"].column_names
    )

    # Data collator
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
        logging_steps=50,
        report_to="none",
    )

    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
        eval_dataset=tokenized_datasets["validation"],
        tokenizer=tokenizer,
        data_collator=data_collator,
        callbacks=[EarlyStoppingCallback(early_stopping_patience=3)]
    )

    # Train
    trainer.train()

    # Save model
    Path(MODEL_DIR).mkdir(parents=True, exist_ok=True)
    tokenizer.save_pretrained(MODEL_DIR)
    model.save_pretrained(MODEL_DIR)
    print(f"✅ Fine-tuned model saved to {MODEL_DIR}")

if __name__ == "__main__":
    main()
