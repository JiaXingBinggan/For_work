import os

import torch
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, Trainer, TrainingArguments, DataCollatorForSeq2Seq

os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"

# 加载并预处理数据
def preprocess_data(examples):
    dialogues = []
    for dialogue in examples['dialog']:
        for i in range(len(dialogue) - 1):
            dialogues.append((dialogue[i], dialogue[i+1]))
    input_texts = [d[0] for d in dialogues]
    target_texts = [d[1] for d in dialogues]
    return {'input_text': input_texts, 'target_text': target_texts}

def load_and_preprocess_data():
    dataset = load_dataset("daily_dialog")
    train_data = dataset['train'].map(preprocess_data, batched=True, remove_columns=['dialog', 'act', 'emotion'])
    return train_data

# Tokenize数据
def tokenize_function(examples, tokenizer):
    model_inputs = tokenizer(examples["input_text"], max_length=128, truncation=True, padding="max_length")
    labels = tokenizer(examples["target_text"], max_length=128, truncation=True, padding="max_length")
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

# 模型微调
def fine_tune_model(train_data, model_name="t5-small"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    tokenized_train_data = train_data.map(lambda x: tokenize_function(x, tokenizer), batched=True)
    data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

    training_args = TrainingArguments(
        output_dir="./results",
        evaluation_strategy="no",
        learning_rate=2e-5,
        per_device_train_batch_size=8,
        num_train_epochs=3,
        weight_decay=0.01,
        save_total_limit=2,
        remove_unused_columns=False,
        push_to_hub=False,
        logging_dir='./logs',
        logging_steps=10,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_train_data,
        tokenizer=tokenizer,
        data_collator=data_collator,
    )

    trainer.train()
    return model, tokenizer

# 实时对话
def chat_with_model(model, tokenizer, prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def start_chat(model, tokenizer):
    print("Chatbot is ready! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        response = chat_with_model(model, tokenizer, user_input)
        print(f"Bot: {response}")

# 主函数
def main():
    train_data = load_and_preprocess_data()
    model, tokenizer = fine_tune_model(train_data)
    start_chat(model, tokenizer)

if __name__ == "__main__":
    main()